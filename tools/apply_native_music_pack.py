#!/usr/bin/env python3
from pathlib import Path
import sys

MUSIC_MARKER = '/* NATIVE MULTI TRACK MUSIC PACK */'
UI_MARKER = '/* SIMPLE STACK STYLE UI */'

MUSIC_PACK = r'''
/* NATIVE MULTI TRACK MUSIC PACK */
const NATIVE_MUSIC_TRACKS=[
  {name:'NEON DRIVE',bass:[55,55,65.41,49,55,73.42,65.41,49],arp:[220,329.63,440,261.63,220,392,523.25,329.63],lead:[440,523.25,659.25,587.33],pad:[110,164.81,220],kick:[1,0,1,0],snare:[0,1,0,1],bassWave:'sawtooth',arpWave:'square',leadWave:'triangle',bassVol:.050,arpVol:.020,leadVol:.016,hatVol:.022,doubleKick:false},
  {name:'VOID PULSE',bass:[43.65,43.65,51.91,58.27,43.65,65.41,51.91,38.89],arp:[174.61,261.63,349.23,233.08,196,293.66,392,261.63],lead:[349.23,293.66,392,261.63],pad:[87.31,130.81,174.61],kick:[1,0,0,1],snare:[0,1,0,1],bassWave:'triangle',arpWave:'square',leadWave:'sawtooth',bassVol:.056,arpVol:.018,leadVol:.013,hatVol:.018,doubleKick:true},
  {name:'AURORA RUSH',bass:[65.41,73.42,82.41,73.42,65.41,98,87.31,73.42],arp:[261.63,392,523.25,329.63,293.66,440,587.33,392],lead:[523.25,659.25,783.99,698.46],pad:[130.81,196,261.63],kick:[1,0,1,0],snare:[0,1,0,1],bassWave:'sawtooth',arpWave:'triangle',leadWave:'square',bassVol:.047,arpVol:.022,leadVol:.015,hatVol:.025,doubleKick:false},
  {name:'DATA BREAK',bass:[49,0,61.74,49,73.42,0,61.74,55],arp:[196,293.66,392,246.94,220,329.63,440,293.66],lead:[392,493.88,587.33,440],pad:[98,146.83,196],kick:[1,0,1,1],snare:[0,1,0,1],bassWave:'square',arpWave:'sawtooth',leadWave:'triangle',bassVol:.044,arpVol:.018,leadVol:.017,hatVol:.026,doubleKick:true}
];
let nativeMusicTrackOffset=Math.floor(Math.random()*NATIVE_MUSIC_TRACKS.length);
function nativeMusicTrack(i){return NATIVE_MUSIC_TRACKS[(nativeMusicTrackOffset+Math.floor(i/32))%NATIVE_MUSIC_TRACKS.length]}
function nativeMusicPad(freqs,time,dur,vol){for(let j=0;j<freqs.length;j++)rhythmNote(freqs[j],time,dur,vol*(j===0?1:.72),'triangle')}
rhythmInit=function(){try{audioCtx=audioCtx||new (window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();if(!rhythmGain){const master=audioCtx.createGain();master.gain.value=.95;const comp=audioCtx.createDynamicsCompressor();comp.threshold.value=-14;comp.knee.value=16;comp.ratio.value=5;comp.attack.value=.002;comp.release.value=.18;master.connect(comp);comp.connect(audioCtx.destination);rhythmGain=audioCtx.createGain();rhythmGain.gain.value=.0001;rhythmGain.connect(master);rhythmSfx=audioCtx.createGain();rhythmSfx.gain.value=.88;rhythmSfx.connect(master);rhythmNoise=audioCtx.createBuffer(1,Math.floor(audioCtx.sampleRate*.25),audioCtx.sampleRate);const d=rhythmNoise.getChannelData(0);for(let i=0;i<d.length;i++)d[i]=Math.random()*2-1}return true}catch(e){return false}};
rhythmBeat=function(i,time){const tr=nativeMusicTrack(i),b=i%8,q=i%4,bar=i%32;if(tr.kick[q])rhythmKick(time);if(tr.doubleKick&&b===6)rhythmKick(time+RHYTHM_BEAT*.5);if(tr.snare[q]){rhythmNoiseHit(time,.075,1550,.13);rhythmNote(tr.name==='AURORA RUSH'?220:180,time,.10,.020,'triangle')}rhythmNoiseHit(time,tr.hatVol,6800,.032);rhythmNoiseHit(time+RHYTHM_BEAT*.5,tr.hatVol*.62,8200,.024);const bass=tr.bass[b];if(bass)rhythmNote(bass,time,RHYTHM_BEAT*.76,tr.bassVol,tr.bassWave);const arp=tr.arp[b];if(arp)rhythmNote(arp,time+.018,RHYTHM_BEAT*.34,tr.arpVol,tr.arpWave);if(i%2===0){const lead=tr.lead[(i/2)%tr.lead.length|0];rhythmNote(lead,time+.045,RHYTHM_BEAT*.42,tr.leadVol,tr.leadWave)}if(i%8===0)nativeMusicPad(tr.pad,time,RHYTHM_BEAT*7.2,.0115);if(bar===0){rhythmNoiseHit(time,.045,3600,.22);rhythmNote(tr.pad[0]*2,time,RHYTHM_BEAT*1.7,.018,'triangle')}};
rhythmStart=function(){if(!rhythmInit())return;if(rhythmTimer)clearInterval(rhythmTimer);nativeMusicTrackOffset=(nativeMusicTrackOffset+1)%NATIVE_MUSIC_TRACKS.length;const t=audioCtx.currentTime+.08;rhythmStarted=true;rhythmPhase=t;rhythmNextBeat=t;rhythmBeatIndex=0;rhythmGain.gain.cancelScheduledValues(audioCtx.currentTime);rhythmGain.gain.setValueAtTime(Math.max(.0001,rhythmGain.gain.value),audioCtx.currentTime);rhythmGain.gain.exponentialRampToValueAtTime(.86,audioCtx.currentTime+.20);rhythmSchedule();rhythmTimer=setInterval(rhythmSchedule,30)};
'''

UI_PACK = r'''
/* SIMPLE STACK STYLE UI */
(function(){
  const old=document.getElementById('simpleStackUi');if(old)old.remove();
  const st=document.createElement('style');st.id='simpleStackUi';
  st.textContent=`
    body.menu-start .top,body.menu-over .top{opacity:0!important;transform:none!important}
    #start,#gameover{width:100%!important;max-width:none!important;padding:0!important;background:none!important;border:0!important;border-radius:0!important;box-shadow:none!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;overflow:visible!important}
    #start:before,#start:after,#gameover:before,#gameover:after{display:none!important;content:none!important}
    #start .simple-title{font-family:Arial,Helvetica,sans-serif;font-size:clamp(50px,13vw,86px);font-weight:300;line-height:1;letter-spacing:.035em;color:#fff;white-space:nowrap;text-shadow:0 0 18px rgba(255,255,255,.13)}
    #start .simple-tap,#gameover .simple-tap{margin-top:62px;font-family:Arial,Helvetica,sans-serif;font-size:clamp(20px,5.5vw,31px);font-weight:300;letter-spacing:.055em;color:rgba(255,255,255,.94);animation:simpleTapPulse 1.55s ease-in-out infinite}
    #gameover .simple-over-title{font-family:Arial,Helvetica,sans-serif;font-size:clamp(42px,10vw,68px);font-weight:300;line-height:1;letter-spacing:.04em;color:#fff;white-space:nowrap;text-shadow:0 0 18px rgba(255,255,255,.12)}
    #gameover .simple-score{margin-top:42px;color:#fff}
    #gameover .simple-score span{display:block;font:300 14px/1 Arial,Helvetica,sans-serif;letter-spacing:.22em;opacity:.58}
    #gameover .simple-score b{display:block;margin-top:10px;font:300 clamp(56px,15vw,88px)/.9 Arial,Helvetica,sans-serif;letter-spacing:.02em}
    #gameover .simple-meta{margin-top:26px;font:300 clamp(14px,3.8vw,19px)/1.5 Arial,Helvetica,sans-serif;letter-spacing:.08em;color:rgba(255,255,255,.66)}
    #gameover .simple-meta b{font-weight:400;color:#fff}
    #gameover .simple-tap{margin-top:54px}
    @keyframes simpleTapPulse{0%,100%{opacity:.48}50%{opacity:1}}
    @media(max-height:620px){#start .simple-tap{margin-top:38px}#gameover .simple-score{margin-top:28px}#gameover .simple-meta{margin-top:18px}#gameover .simple-tap{margin-top:34px}}
  `;
  document.head.appendChild(st);
  const start=document.getElementById('start');
  if(start)start.innerHTML='<div class="simple-title">ORBIT BREAK</div><div class="simple-tap">TAP TO START</div>';
  const over=document.getElementById('gameover');
  if(over){
    over.innerHTML='<div class="simple-over-title">ORBIT LOST</div><div class="simple-score"><span>SCORE</span><b id="finalScore">0</b></div><div class="simple-meta">BEST <b id="highScore">0</b> &nbsp;·&nbsp; COMBO <b id="finalCombo">x1</b></div><div class="simple-tap">TAP TO RETRY</div>';
    el.final=document.getElementById('finalScore');el.high=document.getElementById('highScore');el.finalCombo=document.getElementById('finalCombo');
  }
})();
'''

def addon_bounds(text: str, path: Path):
    addon_start = text.find('const addon=String.raw`')
    if addon_start < 0:
        raise SystemExit(f'{path}: addon template not found')
    addon_end = text.find('\n`;', addon_start)
    if addon_end < 0:
        raise SystemExit(f'{path}: addon template end not found')
    return addon_start, addon_end

def patch(path: Path, music: bool = True, ui: bool = True) -> None:
    text = path.read_text(encoding='utf-8')
    _, addon_end = addon_bounds(text, path)
    inserts = []
    if music and MUSIC_MARKER not in text:
        inserts.append(MUSIC_PACK.strip())
    if ui and UI_MARKER not in text:
        inserts.append(UI_PACK.strip())
    if not inserts:
        print(f'{path}: requested patches already applied')
        return
    text = text[:addon_end] + '\n' + '\n'.join(inserts) + '\n' + text[addon_end:]
    path.write_text(text, encoding='utf-8')
    print(f'{path}: applied ' + ', '.join(('music' if MUSIC_MARKER in x else 'simple-ui') for x in inserts))

if __name__ == '__main__':
    args = sys.argv[1:]
    ui_only = False
    if '--ui-only' in args:
        ui_only = True
        args.remove('--ui-only')
    if not args:
        raise SystemExit('usage: apply_native_music_pack.py [--ui-only] <html> [<html> ...]')
    for item in args:
        patch(Path(item), music=not ui_only, ui=True)
