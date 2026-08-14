#!/usr/bin/env python3
from pathlib import Path
import sys

MARKER = '/* SIMPLE STACK STYLE UI */'

SAFE_UI = r'''/* SIMPLE STACK STYLE UI */
(function(){
  var old=document.getElementById('simpleStackUi');if(old)old.remove();
  var st=document.createElement('style');st.id='simpleStackUi';
  st.textContent='body.menu-start .top,body.menu-over .top{opacity:0!important;transform:none!important}#start,#gameover{width:100%!important;max-width:none!important;padding:0!important;background:none!important;border:0!important;border-radius:0!important;box-shadow:none!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;overflow:visible!important}#start:before,#start:after,#gameover:before,#gameover:after{display:none!important;content:none!important}#start .simple-title{font-family:Arial,Helvetica,sans-serif;font-size:clamp(38px,9.6vw,72px);font-weight:300;line-height:1;letter-spacing:.035em;color:#fff;white-space:nowrap;text-shadow:0 0 18px rgba(255,255,255,.13)}#start .simple-tap{position:fixed;left:50%;top:min(76vh,calc(100vh - 150px));transform:translateX(-50%);margin:0!important;width:max-content;font-family:Arial,Helvetica,sans-serif;font-size:clamp(20px,5.5vw,31px);font-weight:300;letter-spacing:.055em;color:rgba(255,255,255,.94);animation:simpleTapPulse 1.55s ease-in-out infinite;z-index:20}#gameover{position:fixed!important;left:50%!important;top:max(88px,9vh)!important;transform:translateX(-50%)!important;text-align:center!important;z-index:30!important}#gameover .simple-over-title{font-family:Arial,Helvetica,sans-serif;font-size:clamp(38px,9vw,64px);font-weight:300;line-height:1;letter-spacing:.04em;color:#fff;white-space:nowrap;text-shadow:0 0 18px rgba(255,255,255,.12)}#gameover .simple-score{margin-top:20px;color:#fff}#gameover .simple-score span{display:block;font:300 13px/1 Arial,Helvetica,sans-serif;letter-spacing:.22em;opacity:.55}#gameover .simple-score b{display:block;margin-top:8px;font:300 clamp(54px,15vw,86px)/.9 Arial,Helvetica,sans-serif;letter-spacing:.02em}#gameover .simple-meta{margin-top:14px;font:300 clamp(14px,3.8vw,18px)/1.5 Arial,Helvetica,sans-serif;letter-spacing:.08em;color:rgba(255,255,255,.62)}#gameover .simple-meta b{font-weight:400;color:#fff}#gameover .hidden-combo{display:none!important}#gameover .simple-tap{position:fixed!important;left:50%!important;top:min(76vh,calc(100vh - 150px))!important;transform:translateX(-50%)!important;margin:0!important;width:max-content;font-family:Arial,Helvetica,sans-serif;font-size:clamp(20px,5.5vw,31px);font-weight:300;letter-spacing:.055em;color:rgba(255,255,255,.94);animation:simpleTapPulse 1.55s ease-in-out infinite;z-index:40}#orbitSettingsBtn{position:fixed;left:max(18px,env(safe-area-inset-left));top:max(18px,env(safe-area-inset-top));width:54px;height:54px;border:0;background:transparent;color:#fff;display:flex;align-items:center;justify-content:center;z-index:120;opacity:.92;filter:drop-shadow(0 0 10px rgba(255,255,255,.16));padding:0}#orbitSettingsBtn svg{width:42px;height:42px;stroke:currentColor;fill:none;stroke-width:2.3}body:not(.menu-start):not(.menu-over) #orbitSettingsBtn{display:none!important}.orbit-modal{position:fixed;inset:0;z-index:200;display:flex;align-items:center;justify-content:center;padding:22px;background:rgba(2,5,12,.60);backdrop-filter:blur(5px);-webkit-backdrop-filter:blur(5px)}.orbit-modal.hidden{display:none!important}.orbit-panel{position:relative;width:min(90vw,390px);padding:25px 22px 22px;border:2px solid rgba(255,255,255,.88);border-radius:18px;background:rgba(12,17,28,.94);box-shadow:0 28px 80px rgba(0,0,0,.52),0 0 28px rgba(91,233,255,.08);color:#fff;font-family:Arial,Helvetica,sans-serif}.orbit-panel h2{margin:0 0 18px;text-align:center;font-size:clamp(28px,7vw,38px);font-weight:300;letter-spacing:.04em}.orbit-close{position:absolute;right:10px;top:8px;width:40px;height:40px;border:0;background:transparent;color:rgba(255,255,255,.78);font-size:31px;font-weight:200;line-height:1}.orbit-setting-row{display:grid;grid-template-columns:52px 1fr auto;align-items:center;gap:12px;min-height:68px;padding:9px 0;border-top:1px solid rgba(255,255,255,.10)}.orbit-setting-row:first-of-type{border-top:1px solid rgba(255,255,255,.24)}.orbit-setting-icon{width:46px;height:46px;border:2px solid rgba(255,255,255,.78);border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:500}.orbit-setting-label{font-size:16px;font-weight:400;letter-spacing:.02em}.orbit-switch{width:58px;height:32px;border:1px solid rgba(255,255,255,.32);border-radius:999px;background:rgba(255,255,255,.13);padding:3px;transition:.2s}.orbit-switch:before{content:"";display:block;width:24px;height:24px;border-radius:50%;background:#fff;transition:.2s;box-shadow:0 2px 8px rgba(0,0,0,.35)}.orbit-switch.on{background:#4cbf7a}.orbit-switch.on:before{transform:translateX(26px)}.orbit-mini-btn{min-width:68px;height:36px;padding:0 12px;border:1px solid rgba(255,255,255,.55);border-radius:9px;background:rgba(255,255,255,.08);color:#fff;font:500 14px Arial,Helvetica,sans-serif;letter-spacing:.03em}.orbit-volume-wrap{display:flex;align-items:center;gap:9px}.orbit-volume{width:min(36vw,142px);accent-color:#63d88d}.orbit-volume-value{width:36px;text-align:right;font-size:13px;opacity:.72}.orbit-guide{position:fixed;inset:0;z-index:230;display:flex;align-items:center;justify-content:center;padding:22px;background:rgba(2,5,12,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}.orbit-guide.hidden{display:none!important}.orbit-guide-card{position:relative;width:min(90vw,390px);padding:26px 23px 24px;border:2px solid rgba(255,255,255,.88);border-radius:18px;background:rgba(11,16,28,.96);color:#fff;font-family:Arial,Helvetica,sans-serif;text-align:left}.orbit-guide-card h2{margin:0 0 20px;text-align:center;font-size:30px;font-weight:300}.orbit-guide-step{display:flex;gap:14px;align-items:flex-start;margin:16px 0;font-size:15px;line-height:1.45;color:rgba(255,255,255,.85)}.orbit-guide-num{flex:0 0 32px;width:32px;height:32px;border:1px solid rgba(255,255,255,.6);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff}.orbit-guide-ok{display:block;width:100%;height:46px;margin-top:22px;border:1px solid rgba(255,255,255,.78);border-radius:11px;background:rgba(255,255,255,.10);color:#fff;font:500 15px Arial,Helvetica,sans-serif}@keyframes simpleTapPulse{0%,100%{opacity:.45}50%{opacity:1}}@media(max-height:620px){#start .simple-tap,#gameover .simple-tap{top:min(74vh,calc(100vh - 90px))!important}#gameover{top:max(58px,7vh)!important}#gameover .simple-score{margin-top:12px}#gameover .simple-meta{margin-top:8px}#orbitSettingsBtn{width:48px;height:48px}.orbit-panel{padding-top:20px}.orbit-setting-row{min-height:58px}.orbit-setting-icon{width:40px;height:40px}}';
  document.head.appendChild(st);

  var start=document.getElementById('start');
  if(start)start.innerHTML='<div class="simple-title">ORBIT BREAK</div><div class="simple-tap" id="simpleStartTap">TAP TO START</div>';
  var over=document.getElementById('gameover');
  if(over){
    over.innerHTML='<div class="simple-over-title">ORBIT LOST</div><div class="simple-score"><span id="simpleScoreLabel">SCORE</span><b id="finalScore">0</b></div><div class="simple-meta"><span id="simpleBestLabel">BEST</span> <b id="highScore">0</b></div><b id="finalCombo" class="hidden-combo">x1</b><div class="simple-tap" id="simpleRetryTap">TAP TO RETRY</div>';
    el.final=document.getElementById('finalScore');el.high=document.getElementById('highScore');el.finalCombo=document.getElementById('finalCombo');
  }

  var gear=document.createElement('button');gear.id='orbitSettingsBtn';gear.setAttribute('aria-label','Settings');gear.innerHTML='<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="7"></circle><path d="M24 4v6M24 38v6M4 24h6M38 24h6M9.9 9.9l4.2 4.2M33.9 33.9l4.2 4.2M38.1 9.9l-4.2 4.2M14.1 33.9l-4.2 4.2"></path><circle cx="24" cy="24" r="15"></circle></svg>';document.body.appendChild(gear);

  var modal=document.createElement('div');modal.id='orbitSettingsModal';modal.className='orbit-modal hidden';
  modal.innerHTML='<div class="orbit-panel"><button class="orbit-close" id="orbitSettingsClose" aria-label="Close">×</button><h2 id="orbitSettingsTitle">SETTINGS</h2><div class="orbit-setting-row"><div class="orbit-setting-icon">▥</div><div class="orbit-setting-label" id="orbitVibrationLabel">Vibration</div><button class="orbit-switch" id="orbitVibrationToggle" aria-label="Toggle vibration"></button></div><div class="orbit-setting-row"><div class="orbit-setting-icon">文A</div><div class="orbit-setting-label" id="orbitLanguageLabel">Language</div><button class="orbit-mini-btn" id="orbitLanguageBtn">VI</button></div><div class="orbit-setting-row"><div class="orbit-setting-icon">?</div><div class="orbit-setting-label" id="orbitGuideLabel">How to play</div><button class="orbit-mini-btn" id="orbitGuideBtn">OPEN</button></div><div class="orbit-setting-row"><div class="orbit-setting-icon">◖))</div><div class="orbit-setting-label" id="orbitVolumeLabel">Volume</div><div class="orbit-volume-wrap"><input class="orbit-volume" id="orbitVolume" type="range" min="0" max="100" step="1"><span class="orbit-volume-value" id="orbitVolumeValue">100</span></div></div></div>';
  document.body.appendChild(modal);

  var guide=document.createElement('div');guide.id='orbitGuide';guide.className='orbit-guide hidden';
  guide.innerHTML='<div class="orbit-guide-card"><button class="orbit-close" id="orbitGuideClose" aria-label="Close">×</button><h2 id="orbitGuideTitle">HOW TO PLAY</h2><div class="orbit-guide-step"><div class="orbit-guide-num">1</div><div id="orbitGuideStep1">Tap when the moving orb reaches the target ring.</div></div><div class="orbit-guide-step"><div class="orbit-guide-num">2</div><div id="orbitGuideStep2">Every successful tap gives exactly 1 point.</div></div><div class="orbit-guide-step"><div class="orbit-guide-num">3</div><div id="orbitGuideStep3">Tap too early or too late and the run ends.</div></div><button class="orbit-guide-ok" id="orbitGuideOk">GOT IT</button></div>';
  document.body.appendChild(guide);

  function saveSettings(){try{localStorage.setItem('orbitBreakSettings',JSON.stringify(orbitSettings))}catch(e){}}
  function updateAudioVolume(){
    var v=Math.max(0,Math.min(1,Number(orbitSettings.volume)||0));
    try{if(rhythmSfx)rhythmSfx.gain.value=.9*v;if(rhythmGain&&audioCtx)rhythmGain.gain.setValueAtTime(rhythmStarted?Math.max(.0001,.62*v):.0001,audioCtx.currentTime)}catch(e){}
  }
  function applyLanguage(){
    var vi=orbitSettings.language==='vi';
    var tx={settings:vi?'CÀI ĐẶT':'SETTINGS',vibration:vi?'Rung':'Vibration',language:vi?'Ngôn ngữ':'Language',guide:vi?'Hướng dẫn cách chơi':'How to play',open:vi?'MỞ':'OPEN',volume:vi?'Âm lượng':'Volume',start:vi?'CHẠM ĐỂ BẮT ĐẦU':'TAP TO START',retry:vi?'CHẠM ĐỂ CHƠI LẠI':'TAP TO RETRY',score:vi?'ĐIỂM':'SCORE',best:vi?'KỶ LỤC':'BEST',guideTitle:vi?'CÁCH CHƠI':'HOW TO PLAY',s1:vi?'Chạm đúng lúc quả cầu đang xoay đi vào vòng mục tiêu.':'Tap when the moving orb reaches the target ring.',s2:vi?'Mỗi lần bấm trúng được cộng đúng 1 điểm.':'Every successful tap gives exactly 1 point.',s3:vi?'Bấm quá sớm hoặc quá muộn thì lượt chơi kết thúc.':'Tap too early or too late and the run ends.',ok:vi?'ĐÃ HIỂU':'GOT IT'};
    var set=function(id,val){var n=document.getElementById(id);if(n)n.textContent=val};
    set('orbitSettingsTitle',tx.settings);set('orbitVibrationLabel',tx.vibration);set('orbitLanguageLabel',tx.language);set('orbitGuideLabel',tx.guide);set('orbitGuideBtn',tx.open);set('orbitVolumeLabel',tx.volume);set('simpleStartTap',tx.start);set('simpleRetryTap',tx.retry);set('simpleScoreLabel',tx.score);set('simpleBestLabel',tx.best);set('orbitGuideTitle',tx.guideTitle);set('orbitGuideStep1',tx.s1);set('orbitGuideStep2',tx.s2);set('orbitGuideStep3',tx.s3);set('orbitGuideOk',tx.ok);set('orbitLanguageBtn',vi?'VI':'EN');
  }
  function syncSettingsUi(){
    var vib=document.getElementById('orbitVibrationToggle');if(vib)vib.classList.toggle('on',!!orbitSettings.vibration);
    var vol=document.getElementById('orbitVolume');if(vol)vol.value=Math.round(orbitSettings.volume*100);
    var vv=document.getElementById('orbitVolumeValue');if(vv)vv.textContent=Math.round(orbitSettings.volume*100);
    applyLanguage();updateAudioVolume();
  }
  function stop(e){if(e){e.preventDefault();e.stopPropagation()}}
  function openSettings(e){stop(e);modal.classList.remove('hidden');syncSettingsUi()}
  function closeSettings(e){stop(e);modal.classList.add('hidden')}
  function openGuide(e){stop(e);modal.classList.add('hidden');guide.classList.remove('hidden')}
  function closeGuide(e){stop(e);guide.classList.add('hidden');modal.classList.remove('hidden')}
  gear.addEventListener('pointerdown',stop);gear.addEventListener('click',openSettings);
  modal.addEventListener('pointerdown',function(e){e.stopPropagation();if(e.target===modal)closeSettings(e)});document.getElementById('orbitSettingsClose').addEventListener('click',closeSettings);
  guide.addEventListener('pointerdown',function(e){e.stopPropagation();if(e.target===guide)closeGuide(e)});document.getElementById('orbitGuideClose').addEventListener('click',closeGuide);document.getElementById('orbitGuideOk').addEventListener('click',closeGuide);
  document.getElementById('orbitGuideBtn').addEventListener('click',openGuide);
  document.getElementById('orbitVibrationToggle').addEventListener('click',function(e){stop(e);orbitSettings.vibration=!orbitSettings.vibration;saveSettings();syncSettingsUi();if(orbitSettings.vibration&&navigator.vibrate)navigator.vibrate(18)});
  document.getElementById('orbitLanguageBtn').addEventListener('click',function(e){stop(e);orbitSettings.language=orbitSettings.language==='vi'?'en':'vi';saveSettings();applyLanguage()});
  document.getElementById('orbitVolume').addEventListener('input',function(e){e.stopPropagation();orbitSettings.volume=Number(this.value)/100;saveSettings();var vv=document.getElementById('orbitVolumeValue');if(vv)vv.textContent=this.value;updateAudioVolume()});
  document.getElementById('orbitVolume').addEventListener('pointerdown',function(e){e.stopPropagation()});

  document.body.classList.add('menu-start');
  if(el.score)el.score.style.display='none';
  syncSettingsUi();
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
