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

    new_css = """html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#02040b}\nbody{position:relative;isolation:isolate;background:radial-gradient(circle at 18% 22%,rgba(71,235,255,.18),transparent 30%),radial-gradient(circle at 82% 72%,rgba(255,70,205,.16),transparent 34%),linear-gradient(180deg,#07101f 0%,#030713 50%,#02040b 100%)}\nbody:before{content:\"\";position:fixed;inset:-25%;z-index:0;pointer-events:none;opacity:.48;background-image:linear-gradient(rgba(92,232,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,76,207,.07) 1px,transparent 1px);background-size:42px 42px;transform:perspective(700px) rotateX(63deg) translateY(28%);transform-origin:center bottom;filter:drop-shadow(0 0 10px rgba(67,225,255,.16))}\nbody:after{content:\"\";position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(ellipse at center,transparent 0 26%,rgba(27,220,255,.055) 38%,transparent 58%),linear-gradient(90deg,rgba(55,225,255,.035),transparent 28% 72%,rgba(255,69,204,.035))}\n#gameFrame{position:fixed;inset:0;width:100%;height:100%;border:0;background:#050711;opacity:0;pointer-events:none;transition:opacity .12s ease,filter .2s ease;z-index:2}\n#gameFrame.ready{opacity:1;pointer-events:auto}\nbody.orbit-fs-locked #gameFrame{pointer-events:none!important;filter:brightness(.55) saturate(.7)}\n#boot{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;background:#03111a;overflow:hidden}\n@media (min-aspect-ratio:9/16){#gameFrame,#boot{left:50%;top:50%;right:auto;bottom:auto;width:min(100vw,calc(100vh * .5625));height:min(100vh,calc(100vw * 1.7777778));aspect-ratio:9/16;transform:translate(-50%,-50%);box-shadow:0 0 0 1px rgba(95,235,255,.10),0 0 46px rgba(65,228,255,.11),0 0 90px rgba(255,69,204,.08)}}"""

    if old_css not in html:
        raise SystemExit('Expected outer wrapper CSS was not found')
    html = html.replace(old_css, new_css, 1)

    fullscreen_gate = r'''
<!-- ORBIT Y8 DESKTOP FULLSCREEN GATE -->
<style id="orbitY8FullscreenGateStyle">
#orbitY8FullscreenGate{position:fixed;inset:0;z-index:10001;display:none;align-items:center;justify-content:center;padding:24px;background:radial-gradient(circle at 50% 42%,rgba(18,48,74,.88),rgba(2,6,16,.97) 62%);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);font-family:Arial,Helvetica,sans-serif;color:#fff;text-align:center}
#orbitY8FullscreenGate.show{display:flex}
#orbitY8FullscreenGate:before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.42;background-image:linear-gradient(rgba(82,232,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,77,207,.07) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,transparent,#000 30%,#000)}
.orbit-fs-card{position:relative;width:min(88vw,430px);padding:32px 26px 28px;border:1px solid rgba(103,237,255,.4);border-radius:24px;background:linear-gradient(180deg,rgba(9,24,42,.96),rgba(5,10,24,.97));box-shadow:0 28px 90px rgba(0,0,0,.6),0 0 48px rgba(65,226,255,.12),0 0 74px rgba(255,72,206,.08)}
.orbit-fs-mark{width:72px;height:72px;margin:0 auto 18px;border:2px solid rgba(99,238,255,.9);border-radius:20px;display:grid;place-items:center;box-shadow:0 0 24px rgba(81,232,255,.25);font-size:32px}
.orbit-fs-title{margin:0;font-size:clamp(25px,4vw,36px);font-weight:700;letter-spacing:.05em}
.orbit-fs-copy{margin:13px auto 22px;max-width:330px;color:rgba(255,255,255,.72);font-size:14px;line-height:1.55}
#orbitY8EnterFullscreen{width:100%;height:54px;border:1px solid rgba(255,255,255,.55);border-radius:14px;background:linear-gradient(90deg,#28dff4,#717dff 52%,#ed4bc9);color:#fff;font:700 15px Arial,Helvetica,sans-serif;letter-spacing:.08em;cursor:pointer;box-shadow:0 12px 35px rgba(65,112,255,.3)}
#orbitY8EnterFullscreen:active{transform:scale(.985)}
#orbitY8FullscreenHint{min-height:18px;margin:13px 0 0;color:rgba(255,255,255,.52);font-size:12px;line-height:1.4}
</style>
<div id="orbitY8FullscreenGate" aria-hidden="true">
  <div class="orbit-fs-card">
    <div class="orbit-fs-mark">⛶</div>
    <h2 class="orbit-fs-title">FULLSCREEN REQUIRED</h2>
    <p class="orbit-fs-copy">ORBIT BREAK requires fullscreen on desktop. Enter fullscreen to start or continue playing.</p>
    <button id="orbitY8EnterFullscreen" type="button">ENTER FULLSCREEN</button>
    <p id="orbitY8FullscreenHint">Press Esc to exit fullscreen. The game will lock again until fullscreen is restored.</p>
  </div>
</div>
<script id="orbitY8FullscreenGateScript">
(() => {
  'use strict';
  const gate = document.getElementById('orbitY8FullscreenGate');
  const btn = document.getElementById('orbitY8EnterFullscreen');
  const hint = document.getElementById('orbitY8FullscreenHint');
  const frame = document.getElementById('gameFrame');
  const boot = document.getElementById('boot');

  const isMobile = () => /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile/i.test(navigator.userAgent || '');
  const isDesktop = () => !isMobile();
  const viewportLooksFullscreen = () => {
    const sw = Math.max(1, screen.availWidth || screen.width || 1);
    const sh = Math.max(1, screen.availHeight || screen.height || 1);
    return window.innerWidth >= sw * 0.94 && window.innerHeight >= sh * 0.88;
  };
  const isFullscreen = () => !!(document.fullscreenElement || document.webkitFullscreenElement) || viewportLooksFullscreen();
  const bootFinished = () => !boot || boot.classList.contains('hide');

  function setLocked(locked) {
    if (!isDesktop()) locked = false;
    document.body.classList.toggle('orbit-fs-locked', locked);
    gate.classList.toggle('show', locked);
    gate.setAttribute('aria-hidden', locked ? 'false' : 'true');
    if (!locked && frame) {
      try { frame.contentWindow.focus(); } catch (e) {}
    }
  }

  function refreshGate() {
    if (!isDesktop() || !bootFinished() || window.orbitY8AdBusy) {
      setLocked(false);
      return;
    }
    setLocked(!isFullscreen());
  }

  async function requestFullscreen() {
    hint.textContent = 'Opening fullscreen…';
    try {
      const root = document.documentElement;
      if (root.requestFullscreen) {
        await root.requestFullscreen({ navigationUI: 'hide' });
      } else if (root.webkitRequestFullscreen) {
        root.webkitRequestFullscreen();
      } else {
        throw new Error('Fullscreen API unavailable');
      }
      setTimeout(refreshGate, 120);
    } catch (e) {
      console.warn('ORBIT BREAK fullscreen request blocked:', e);
      hint.textContent = 'If the browser blocks this button, use Y8’s fullscreen icon. The game unlocks automatically once the player fills the screen.';
      setLocked(true);
    }
  }

  btn.addEventListener('click', requestFullscreen);
  document.addEventListener('fullscreenchange', refreshGate);
  document.addEventListener('webkitfullscreenchange', refreshGate);
  window.addEventListener('resize', () => setTimeout(refreshGate, 80));
  window.addEventListener('focus', refreshGate);
  document.addEventListener('visibilitychange', refreshGate);

  if (boot) {
    new MutationObserver(refreshGate).observe(boot, { attributes: true, attributeFilter: ['class'] });
  }
  setInterval(refreshGate, 900);
  refreshGate();
})();
</script>
'''

    if '</body>' not in html:
        raise SystemExit('Unable to insert desktop fullscreen gate')
    html = html.replace('</body>', fullscreen_gate + '\n</body>', 1)

    required = [
        "appId: '6a8af910b3a217f531663764'",
        "gameId: '281161'",
        'orbitBottomNav',
        'orbitSkinsModal',
        'orbitRankingsModal',
        'simpleStartTap',
        'orbitY8FullscreenGate',
        'ENTER FULLSCREEN',
        'orbit-fs-locked',
    ]
    missing = [x for x in required if x not in html]
    if missing:
        raise SystemExit('Y8 build is missing required UI/SDK/fullscreen markers: ' + ', '.join(missing))

    target.write_text(html, encoding='utf-8')

    ZIP.parent.mkdir(parents=True, exist_ok=True)
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(OUT.rglob('*')):
            if path.is_file():
                zf.write(path, path.relative_to(OUT).as_posix())

    print(f'Created {ZIP}')
    print('Y8 build includes Home / Skins / Ranking UI, portrait 9:16 gameplay, neon/grid sides, and mandatory desktop fullscreen gate.')


if __name__ == '__main__':
    main()
