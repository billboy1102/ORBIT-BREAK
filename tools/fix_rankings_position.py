#!/usr/bin/env python3
from pathlib import Path
import sys

BROKEN = '#orbitRankingsModal{top:0!important;left:0!important;right:0!important;bottom:calc(84px + env(safe-area-inset-bottom))!important;inset:auto!important;'
FIXED = '#orbitRankingsModal{inset:0 0 calc(84px + env(safe-area-inset-bottom)) 0!important;'


def fix(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    if BROKEN in text:
        text = text.replace(BROKEN, FIXED, 1)
    if BROKEN in text:
        raise SystemExit(f'{path}: broken Rankings inset rule is still present')
    if FIXED not in text:
        raise SystemExit(f'{path}: fixed Rankings inset rule not found')
    path.write_text(text, encoding='utf-8')
    print(f'{path}: fixed Rankings viewport positioning')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: fix_rankings_position.py <html> [<html> ...]')
    for item in sys.argv[1:]:
        fix(Path(item))
