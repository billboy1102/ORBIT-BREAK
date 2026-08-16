#!/usr/bin/env python3
from pathlib import Path
import sys

from add_legal_docs import apply as apply_legal_docs

OLD_WEB = 'assets/bobbey-game-studio-splash.jpg'
NEW_WEB = 'assets/bobbey-game-studio-splash.webp'
OLD_DESKTOP = '../assets/bobbey-game-studio-splash.jpg'
NEW_DESKTOP = '../assets/bobbey-game-studio-splash.webp'


def patch(path: str) -> None:
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    before = text
    text = text.replace(OLD_DESKTOP, NEW_DESKTOP)
    text = text.replace(OLD_WEB, NEW_WEB)

    # Keep the supplied Bobbey artwork fully visible. Do not crop or restyle it.
    text = text.replace(
        '#boot img{width:100%;height:100%;object-fit:contain;display:block}',
        '#boot img{width:100%;height:100%;object-fit:contain;object-position:center;display:block}'
    )

    if NEW_WEB not in text and NEW_DESKTOP not in text:
        raise SystemExit(f'{path}: Bobbey splash reference was not found')
    p.write_text(text, encoding='utf-8')

    # Desktop wrapper has one fewer blank line before patchGame than web/android.
    # Normalize it so the same legal injector works for every target.
    normalized = p.read_text(encoding='utf-8')
    web_anchor = '\n`;\n\nfunction patchGame(){'
    desktop_anchor = '\n`;\nfunction patchGame(){'
    if web_anchor not in normalized and desktop_anchor in normalized:
        normalized = normalized.replace(desktop_anchor, web_anchor, 1)
        p.write_text(normalized, encoding='utf-8')

    # Legal documentation is applied here so Pages, Android and Windows all receive
    # exactly the same Settings > Legal documentation UI without separate build logic.
    apply_legal_docs(p)
    final = p.read_text(encoding='utf-8')

    # Avoid a MutationObserver feedback loop caused by rewriting localized labels from
    # inside the observer callback. Text is still refreshed every time Legal is opened.
    final = final.replace(
        "var mo=new MutationObserver(function(){ensureRow();syncText()});mo.observe(document.body,{childList:true,subtree:true});",
        "var mo=new MutationObserver(function(){ensureRow()});mo.observe(document.body,{childList:true,subtree:true});"
    )
    p.write_text(final, encoding='utf-8')

    required = ['ORBIT LEGAL DOCUMENTATION START', 'orbitLegalModal', 'orbitLegalDeleteData']
    missing = [item for item in required if item not in final]
    if missing:
        raise SystemExit(f'{path}: legal documentation injection failed: {missing}')
    if 'MutationObserver(function(){ensureRow();syncText()})' in final:
        raise SystemExit(f'{path}: unstable legal MutationObserver remained after patch')

    print(f'Branding + legal docs fixed: {path}' + (' (updated)' if final != before else ''))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: fix_branding.py <html> [html ...]')
    for arg in sys.argv[1:]:
        patch(arg)
