#!/usr/bin/env python3
from pathlib import Path
import sys

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
    print(f'Branding fixed: {path}' + (' (updated)' if text != before else ''))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: fix_branding.py <html> [html ...]')
    for arg in sys.argv[1:]:
        patch(arg)
