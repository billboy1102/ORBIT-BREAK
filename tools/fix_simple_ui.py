#!/usr/bin/env python3
from pathlib import Path
import sys

MARKER = '/* SIMPLE STACK STYLE UI */'

SAFE_UI = r'''/* SIMPLE STACK STYLE UI */
(function(){
  var old=document.getElementById('simpleStackUi');if(old)old.remove();
  var st=document.createElement('style');st.id='simpleStackUi';
  st.textContent='body.menu-start .top,body.menu-over .top{opacity:0!important;transform:none!important}#start,#gameover{width:100%!important;max-width:none!important;padding:0!important;background:none!important;border:0!important;border-radius:0!important;box-shadow:none!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;overflow:visible!important}#start:before,#start:after,#gameover:before,#gameover:after{display:none!important;content:none!important}#start .simple-title{font-family:Arial,Helvetica,sans-serif;font-size:clamp(38px,9.6vw,72px);font-weight:300;line-height:1;letter-spacing:.035em;color:#fff;white-space:nowrap;text-shadow:0 0 18px rgba(255,255,255,.13)}#start .simple-tap{position:fixed;left:50%;top:min(76vh,calc(100vh - 150px));transform:translateX(-50%);margin:0!important;width:max-content;font-family:Arial,Helvetica,sans-serif;font-size:clamp(20px,5.5vw,31px);font-weight:300;letter-spacing:.055em;color:rgba(255,255,255,.94);animation:simpleTapPulse 1.55s ease-in-out infinite;z-index:20}#gameover{position:fixed!important;left:50%!important;top:max(88px,9vh)!important;transform:translateX(-50%)!important;text-align:center!important;z-index:30!important}#gameover .simple-over-title{font-family:Arial,Helvetica,sans-serif;font-size:clamp(38px,9vw,64px);font-weight:300;line-height:1;letter-spacing:.04em;color:#fff;white-space:nowrap;text-shadow:0 0 18px rgba(255,255,255,.12)}#gameover .simple-score{margin-top:20px;color:#fff}#gameover .simple-score span{display:block;font:300 13px/1 Arial,Helvetica,sans-serif;letter-spacing:.22em;opacity:.55}#gameover .simple-score b{display:block;margin-top:8px;font:300 clamp(54px,15vw,86px)/.9 Arial,Helvetica,sans-serif;letter-spacing:.02em}#gameover .simple-meta{margin-top:14px;font:300 clamp(14px,3.8vw,18px)/1.5 Arial,Helvetica,sans-serif;letter-spacing:.08em;color:rgba(255,255,255,.62)}#gameover .simple-meta b{font-weight:400;color:#fff}#gameover .hidden-combo{display:none!important}#gameover .simple-tap{position:fixed!important;left:50%!important;top:min(76vh,calc(100vh - 150px))!important;transform:translateX(-50%)!important;margin:0!important;width:max-content;font-family:Arial,Helvetica,sans-serif;font-size:clamp(20px,5.5vw,31px);font-weight:300;letter-spacing:.055em;color:rgba(255,255,255,.94);animation:simpleTapPulse 1.55s ease-in-out infinite;z-index:40}@keyframes simpleTapPulse{0%,100%{opacity:.45}50%{opacity:1}}@media(max-height:620px){#start .simple-tap,#gameover .simple-tap{top:min(74vh,calc(100vh - 90px))!important}#gameover{top:max(58px,7vh)!important}#gameover .simple-score{margin-top:12px}#gameover .simple-meta{margin-top:8px}}';
  document.head.appendChild(st);
  var start=document.getElementById('start');
  if(start)start.innerHTML='<div class="simple-title">ORBIT BREAK</div><div class="simple-tap">TAP TO START</div>';
  var over=document.getElementById('gameover');
  if(over){
    over.innerHTML='<div class="simple-over-title">ORBIT LOST</div><div class="simple-score"><span>SCORE</span><b id="finalScore">0</b></div><div class="simple-meta">BEST <b id="highScore">0</b></div><b id="finalCombo" class="hidden-combo">x1</b><div class="simple-tap">TAP TO RETRY</div>';
    el.final=document.getElementById('finalScore');el.high=document.getElementById('highScore');el.finalCombo=document.getElementById('finalCombo');
  }
  document.body.classList.add('menu-start');
})();'''

def fix(path: Path):
    text=path.read_text(encoding='utf-8')
    start=text.find(MARKER)
    if start<0:
        raise SystemExit(f'{path}: simple UI marker not found')
    addon_end=text.find('\n`;',start)
    if addon_end<0:
        raise SystemExit(f'{path}: addon end not found')
    text=text[:start]+SAFE_UI+'\n'+text[addon_end:]
    path.write_text(text,encoding='utf-8')
    print(f'{path}: replaced unsafe simple UI with safe version')

if __name__=='__main__':
    if len(sys.argv)<2:
        raise SystemExit('usage: fix_simple_ui.py <html> [<html> ...]')
    for item in sys.argv[1:]:
        fix(Path(item))
