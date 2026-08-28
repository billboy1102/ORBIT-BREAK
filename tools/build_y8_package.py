#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist' / 'y8-build'
ZIP = ROOT / 'dist' / 'ORBIT-BREAK-Y8.zip'


def run(*args):
    subprocess.run([str(a) for a in args], cwd=ROOT, check=True)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    shutil.copy2(ROOT / 'index.html', OUT / 'index.html')
    shutil.copy2(ROOT / 'game-base.html', OUT / 'game-base.html')
    shutil.copytree(ROOT / 'assets', OUT / 'assets')

    target = OUT / 'index.html'

    # Bake the same current web UI used by GitHub Pages into the Y8 package.
    run('python3', ROOT / 'tools' / 'apply_native_music_pack.py', '--ui-only', target)
    run('python3', ROOT / 'tools' / 'fix_simple_ui.py', target)
    run('python3', ROOT / 'tools' / 'fix_rankings_position.py', target)
    run('python3', ROOT / 'tools' / 'fix_branding.py', target)
    run('python3', ROOT / 'tools' / 'fix_first_tap_clock.py', target)

    html = target.read_text(encoding='utf-8')

    old_css = """html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#050711}\n#gameFrame{position:fixed;inset:0;width:100%;height:100%;border:0;background:#050711;opacity:0;pointer-events:none;transition:opacity .12s ease}\n#gameFrame.ready{opacity:1;pointer-events:auto}\n#boot{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;background:#03111a;overflow:hidden}"""

    new_css = """html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#02040b}\nbody{position:relative;isolation:isolate;background:radial-gradient(circle at 18% 22%,rgba(71,235,255,.18),transparent 30%),radial-gradient(circle at 82% 72%,rgba(255,70,205,.16),transparent 34%),linear-gradient(180deg,#07101f 0%,#030713 50%,#02040b 100%)}\nbody:before{content:\"\";position:fixed;inset:-25%;z-index:0;pointer-events:none;opacity:.48;background-image:linear-gradient(rgba(92,232,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,76,207,.07) 1px,transparent 1px);background-size:42px 42px;transform:perspective(700px) rotateX(63deg) translateY(28%);transform-origin:center bottom;filter:drop-shadow(0 0 10px rgba(67,225,255,.16))}\nbody:after{content:\"\";position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(ellipse at center,transparent 0 26%,rgba(27,220,255,.055) 38%,transparent 58%),linear-gradient(90deg,rgba(55,225,255,.035),transparent 28% 72%,rgba(255,69,204,.035))}\n#gameFrame{position:fixed;inset:0;width:100%;height:100%;border:0;background:#050711;opacity:0;pointer-events:none;transition:opacity .12s ease;z-index:2}\n#gameFrame.ready{opacity:1;pointer-events:auto}\n#boot{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;background:#03111a;overflow:hidden}\n@media (min-aspect-ratio:9/16){#gameFrame,#boot{left:50%;top:50%;right:auto;bottom:auto;width:min(100vw,calc(100vh * .5625));height:min(100vh,calc(100vw * 1.7777778));aspect-ratio:9/16;transform:translate(-50%,-50%);box-shadow:0 0 0 1px rgba(95,235,255,.10),0 0 46px rgba(65,228,255,.11),0 0 90px rgba(255,69,204,.08)}}"""

    if old_css not in html:
        raise SystemExit('Expected outer wrapper CSS was not found')
    html = html.replace(old_css, new_css, 1)

    required = [
        "appId: '6a8af910b3a217f531663764'",
        "gameId: '281161'",
        'orbitBottomNav',
        'orbitSkinsModal',
        'orbitRankingsModal',
        'simpleStartTap',
    ]
    missing = [x for x in required if x not in html]
    if missing:
        raise SystemExit('Y8 build is missing required UI/SDK markers: ' + ', '.join(missing))

    target.write_text(html, encoding='utf-8')

    ZIP.parent.mkdir(parents=True, exist_ok=True)
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(OUT.rglob('*')):
            if path.is_file():
                zf.write(path, path.relative_to(OUT).as_posix())

    print(f'Created {ZIP}')
    print('Y8 build includes full Home / Skins / Ranking UI and portrait 9:16 gameplay with neon/grid side background.')


if __name__ == '__main__':
    main()
