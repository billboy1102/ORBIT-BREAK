#!/usr/bin/env python3
from pathlib import Path
import sys

CHOOSE_OLD = "if(audioCtx&&rhythmStarted){\n    const t=audioCtx.currentTime;rhythmSegmentStart=t;"
CHOOSE_NEW = "if(audioCtx&&rhythmStarted&&audioCtx.state==='running'){\n    const t=audioCtx.currentTime;rhythmSegmentStart=t;"

UPDATE_OLD = "if(audioCtx&&rhythmStarted)progress=speed*Math.max(0,audioCtx.currentTime-rhythmSegmentStart);else progress+=speed*dt;"
UPDATE_NEW = "if(audioCtx&&rhythmStarted&&audioCtx.state==='running'&&rhythmSegmentStart>0)progress=speed*Math.max(0,audioCtx.currentTime-rhythmSegmentStart);else progress+=speed*dt;"

RESET_OLD = "reset=function(){\n  score=0;combo=1;bestCombo=1;hits=0;"
RESET_NEW = "reset=function(){\n  rhythmSegmentStart=0;\n  score=0;combo=1;bestCombo=1;hits=0;"


def patch(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    changed = False

    if CHOOSE_OLD in text:
        text = text.replace(CHOOSE_OLD, CHOOSE_NEW, 1)
        changed = True
    elif CHOOSE_NEW not in text:
        raise SystemExit(f'{path}: chooseGoal audio-clock marker not found')

    if UPDATE_OLD in text:
        text = text.replace(UPDATE_OLD, UPDATE_NEW, 1)
        changed = True
    elif UPDATE_NEW not in text:
        raise SystemExit(f'{path}: update audio-clock marker not found')

    if RESET_OLD in text:
        text = text.replace(RESET_OLD, RESET_NEW, 1)
        changed = True
    elif RESET_NEW not in text:
        raise SystemExit(f'{path}: reset marker not found')

    if changed:
        path.write_text(text, encoding='utf-8')
        print(f'{path}: fixed first-tap Safari clock fallback')
    else:
        print(f'{path}: first-tap clock fix already applied')


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        raise SystemExit('usage: fix_first_tap_clock.py <html> [<html> ...]')
    for item in args:
        patch(Path(item))
