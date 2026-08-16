#!/usr/bin/env python3
from pathlib import Path
import sys

OLD_ENSURE = "function ensureRow(){var panel=document.querySelector('#orbitSettingsModal .orbit-panel');if(!panel||document.getElementById('orbitLegalRow'))return;var row=document.createElement('div');row.className='orbit-setting-row';row.id='orbitLegalRow';row.innerHTML='<div class=\"orbit-setting-icon\">§</div><div class=\"orbit-setting-label\" id=\"orbitLegalLabel\">Legal documentation</div><button class=\"orbit-legal-open\" id=\"orbitLegalOpen\">OPEN</button>';panel.appendChild(row);document.getElementById('orbitLegalOpen').addEventListener('click',openLegal);syncText()}"

NEW_ENSURE = "function ensureRow(){var panel=document.querySelector('#orbitSettingsModal .orbit-panel');if(!panel||document.getElementById('orbitLegalRow'))return;var row=document.createElement('div');row.className='orbit-settings-actions';row.id='orbitLegalRow';row.innerHTML='<button class=\"orbit-settings-icon-action\" id=\"orbitLegalIconBtn\" type=\"button\" aria-label=\"Legal documentation\" title=\"Legal documentation\"><svg viewBox=\"0 0 48 48\" aria-hidden=\"true\"><path d=\"M24 5 39 11v11c0 10-6.4 17.1-15 21-8.6-3.9-15-11-15-21V11L24 5Z\"></path><path d=\"m16.5 23.5 5 5 10-11\"></path></svg></button><a class=\"orbit-settings-icon-action\" id=\"orbitContactEmail\" href=\"mailto:partnerships@bobbey.net?subject=ORBIT%20BREAK%20Support\" aria-label=\"Contact Bobbey Game Studio\" title=\"partnerships@bobbey.net\"><svg viewBox=\"0 0 48 48\" aria-hidden=\"true\"><rect x=\"6\" y=\"10\" width=\"36\" height=\"28\" rx=\"3\"></rect><path d=\"m8 13 16 13 16-13\"></path></svg></a>';panel.appendChild(row);document.getElementById('orbitLegalIconBtn').addEventListener('click',openLegal);var mail=document.getElementById('orbitContactEmail');if(mail)mail.addEventListener('click',function(e){e.stopPropagation()});syncText()}"

CSS_ANCHOR = ".orbit-legal-open{min-width:68px;height:36px;padding:0 12px;border:1px solid rgba(255,255,255,.55);border-radius:9px;background:rgba(255,255,255,.08);color:#fff;font:500 14px Arial,Helvetica,sans-serif;letter-spacing:.03em}"
CSS_EXTRA = ".orbit-settings-actions{display:flex;align-items:center;justify-content:center;gap:18px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,.10)}.orbit-settings-icon-action{width:76px;height:58px;display:flex;align-items:center;justify-content:center;padding:0;border:2px solid rgba(255,255,255,.74);border-radius:10px;background:rgba(255,255,255,.055);color:rgba(255,255,255,.94);text-decoration:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.05);touch-action:manipulation}.orbit-settings-icon-action svg{width:39px;height:39px;fill:none;stroke:currentColor;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}.orbit-settings-icon-action:active{transform:scale(.96);background:rgba(96,232,255,.10);border-color:rgba(111,239,255,.92);box-shadow:0 0 18px rgba(87,232,255,.14)}"


def apply(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    if 'ORBIT LEGAL DOCUMENTATION START' not in text:
        raise SystemExit(f'{path}: legal documentation must be injected before settings actions')

    if OLD_ENSURE in text:
        text = text.replace(OLD_ENSURE, NEW_ENSURE, 1)
    elif NEW_ENSURE not in text:
        raise SystemExit(f'{path}: could not find Legal settings row')

    if CSS_EXTRA not in text:
        if CSS_ANCHOR not in text:
            raise SystemExit(f'{path}: could not find Legal CSS anchor')
        text = text.replace(CSS_ANCHOR, CSS_ANCHOR + CSS_EXTRA, 1)

    path.write_text(text, encoding='utf-8')

    final = path.read_text(encoding='utf-8')
    required = [
        'orbitLegalIconBtn',
        'orbitContactEmail',
        'mailto:partnerships@bobbey.net',
        'orbit-settings-icon-action',
        'm16.5 23.5 5 5 10-11',
    ]
    missing = [x for x in required if x not in final]
    if missing:
        raise SystemExit(f'{path}: compact Settings actions missing: {missing}')
    if "row.className='orbit-setting-row';row.id='orbitLegalRow'" in final:
        raise SystemExit(f'{path}: old full-width Legal row still present')
    print(f'Compact Legal + contact buttons applied: {path}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: fix_settings_actions.py <html> [html ...]')
    for arg in sys.argv[1:]:
        apply(Path(arg))
