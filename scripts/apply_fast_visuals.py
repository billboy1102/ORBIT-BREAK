from pathlib import Path
p=Path('index.html')
s=p.read_text()
if 'MORE PROCEDURAL BACKGROUNDS v2' in s:
    raise SystemExit('already applied')

s=s.replace('const RHYTHM_BPM=124,RHYTHM_BEAT=60/RHYTHM_BPM;','const RHYTHM_BPM=138,RHYTHM_BEAT=60/RHYTHM_BPM;')
s=s.replace("speed=1.72;dir=1;progress=0;goal=2.65;","speed=2.15;dir=1;progress=0;goal=2.65;")
s=s.replace("speed=Math.min(4.15,1.72+hits*.055);","speed=Math.min(5.35,2.15+hits*.09);")
s=s.replace("const tol=clamp(.30-hits*.004,.18,.30);if(progress>goal+tol)die('MISS BEAT');","const tol=clamp(speed*.075,.26,.42);if(progress>goal+tol)die('MISS BEAT');")

marker="if(typeof billboards==='function')billboards=function(){};"
extra=r'''

/* MORE PROCEDURAL BACKGROUNDS v2 */
THEMES.push(
{name:'PLASMA RIFT',bg:'#180f35',bg2:'#03050d',a:'#ff58de',b:'#61efff',c:'#8d6dff'},
{name:'LASER VAULT',bg:'#091d29',bg2:'#02060a',a:'#7affd8',b:'#ff5f9d',c:'#58a5ff'},
{name:'CRYSTAL VOID',bg:'#161126',bg2:'#03040b',a:'#b989ff',b:'#59f5ff',c:'#ff80c8'},
{name:'SOLAR DRIVE',bg:'#2a1112',bg2:'#060505',a:'#ffd166',b:'#ff5b73',c:'#67e8ff'}
);
function plasmaRift(t){sky(t);ctx.save();ctx.globalCompositeOperation='screen';for(let k=0;k<7;k++){ctx.beginPath();for(let x=-20;x<=W+20;x+=16){let y=H*(.16+k*.105)+Math.sin(x*.014+now*.0015+k)*34+Math.cos(x*.007-now*.001+k)*20-camera.y*.035;x<0?ctx.moveTo(x,y):ctx.lineTo(x,y)}ctx.strokeStyle=rgba(k%2?t.a:t.b,.055+k*.007);ctx.lineWidth=8+k*1.5;ctx.shadowColor=k%2?t.a:t.b;ctx.shadowBlur=18;ctx.stroke()}ctx.shadowBlur=0;for(let i=0;i<12;i++){let a=now*.00035+i*TAU/12,r=70+i*20,cx=W*.5-camera.x*.035,cy=H*.47-camera.y*.03;ctx.strokeStyle=rgba(i%2?t.c:t.a,.045);ctx.lineWidth=1.4;ctx.beginPath();ctx.arc(cx,cy,r,a,a+Math.PI*1.3);ctx.stroke()}ctx.restore()}
function laserVault(t){sky(t);let vx=W*.5-camera.x*.04,vy=H*.39-camera.y*.03;ctx.save();ctx.globalCompositeOperation='screen';for(let i=-9;i<=9;i++){ctx.strokeStyle=rgba(i%2?t.a:t.b,.10);ctx.lineWidth=1.3;ctx.beginPath();ctx.moveTo(vx+i*7,vy);ctx.lineTo(W*.5+i*W*.13,H+35);ctx.stroke()}for(let j=0;j<18;j++){let d=((j+now*.0036)%18)/18,y=vy+d*d*(H-vy+40);ctx.strokeStyle=rgba(j%2?t.c:t.a,.04+(1-d)*.11);ctx.lineWidth=1+d*2;ctx.beginPath();ctx.moveTo(W*(.08*d),y);ctx.lineTo(W-W*(.08*d),y);ctx.stroke()}for(let i=0;i<10;i++){let x=((i*101-camera.x*.18)%(W+100)+(W+100))%(W+100)-50,h=H*(.18+(i%4)*.05),y=H-h;ctx.fillStyle=rgba(i%2?t.a:t.b,.035);ctx.fillRect(x,y,10+i%3*5,h);ctx.strokeStyle=rgba(i%2?t.a:t.b,.14);ctx.strokeRect(x,y,10+i%3*5,h)}ctx.restore()}
function crystalVoid(t){sky(t);ctx.save();ctx.globalCompositeOperation='screen';let cx=W*.5-camera.x*.035,cy=H*.48-camera.y*.035;for(let i=0;i<18;i++){let a=now*.00022*(i%2?1:-1)+i*TAU/18,r=55+(i%6)*42,x=cx+Math.cos(a)*r,y=cy+Math.sin(a)*r*.75,z=10+(i%5)*4;ctx.beginPath();ctx.moveTo(x,y-z*1.8);ctx.lineTo(x+z,y);ctx.lineTo(x,y+z*1.8);ctx.lineTo(x-z,y);ctx.closePath();ctx.fillStyle=rgba(i%3===0?t.a:i%3===1?t.b:t.c,.035+(i%4)*.012);ctx.strokeStyle=rgba(i%2?t.a:t.b,.16);ctx.lineWidth=1.2;ctx.fill();ctx.stroke()}for(let r=80;r<Math.max(W,H);r+=70){ctx.strokeStyle=rgba(t.c,.035);ctx.beginPath();ctx.arc(cx,cy,r,now*.0002,-now*.0002+Math.PI*1.4);ctx.stroke()}ctx.restore()}
function solarDrive(t){sky(t);let cx=W*.5-camera.x*.03,cy=H*.37-camera.y*.025,beat=typeof rhythmPulse==='function'?rhythmPulse():0;ctx.save();ctx.globalCompositeOperation='screen';let g=ctx.createRadialGradient(cx,cy,0,cx,cy,120+beat*18);g.addColorStop(0,rgba('#ffffff',.24));g.addColorStop(.18,rgba(t.a,.26));g.addColorStop(.55,rgba(t.b,.10));g.addColorStop(1,rgba(t.b,0));ctx.fillStyle=g;ctx.fillRect(0,0,W,H);for(let i=0;i<28;i++){let a=now*.00018+i*TAU/28,r0=42,r1=110+(i%5)*24+beat*12;ctx.strokeStyle=rgba(i%2?t.a:t.b,.045+(i%4)*.012);ctx.lineWidth=1.2;ctx.beginPath();ctx.moveTo(cx+Math.cos(a)*r0,cy+Math.sin(a)*r0);ctx.lineTo(cx+Math.cos(a)*r1,cy+Math.sin(a)*r1);ctx.stroke()}for(let i=0;i<10;i++){let r=50+i*28;ctx.strokeStyle=rgba(i%2?t.c:t.a,.05);ctx.beginPath();ctx.ellipse(cx,cy,r,r*.42,now*.00015,0,TAU);ctx.stroke()}ctx.restore()}
const originalThemeDraw=themeDraw;
themeDraw=function(i,t){if(i<4)return originalThemeDraw(i,t);if(i===4)return plasmaRift(t);if(i===5)return laserVault(t);if(i===6)return crystalVoid(t);return solarDrive(t)};
/* Keep boss energy FX but remove all boss text. */
bossFx=function(t){let b=clamp((combo-5)/9,0,1);if(!b)return;let beat=typeof rhythmPulse==='function'?rhythmPulse():0,cx=W*.5-camera.x*.02,cy=H*.42-camera.y*.02,q=b*(.75+.25*Math.sin(now*.008)+beat*.35);ctx.save();ctx.globalCompositeOperation='screen';for(let i=0;i<7;i++){let r=42+i*30+q*18;ctx.strokeStyle=rgba(i%2?t.b:t.a,.07+q*.13);ctx.lineWidth=1.2+i*.3;ctx.beginPath();ctx.arc(cx,cy,r,now*.0006*(i%2?1:-1),now*.0006*(i%2?1:-1)+Math.PI*1.45);ctx.stroke()}for(let i=0;i<12;i++){let a=now*.0009+i*TAU/12,r=50+q*24;ctx.strokeStyle=rgba(i%2?t.a:t.b,.05+q*.1);ctx.beginPath();ctx.moveTo(cx+Math.cos(a)*r,cy+Math.sin(a)*r*.55);ctx.lineTo(cx+Math.cos(a)*(r+70),cy+Math.sin(a)*(r+70)*.55);ctx.stroke()}let g=ctx.createRadialGradient(cx,cy,0,cx,cy,92);g.addColorStop(0,rgba('#ffffff',.14*q));g.addColorStop(.2,rgba(t.b,.2*q));g.addColorStop(1,rgba(t.a,0));ctx.fillStyle=g;ctx.beginPath();ctx.arc(cx,cy,94,0,TAU);ctx.fill();ctx.restore()};
/* Change theme every 3 hits instead of every 5. */
drawBackground=function(){let n=Math.floor(hits/3)%THEMES.length;if(n!==themeNow){themePrev=themeNow;themeNow=n;themeAt=now;updateHUD()}let m=clamp((now-themeAt)/850,0,1),e=m*m*(3-2*m);ctx.fillStyle='#010308';ctx.fillRect(0,0,W,H);ctx.save();themeDraw(themePrev,THEMES[themePrev]);ctx.restore();if(themeNow!==themePrev){ctx.save();ctx.globalAlpha=e;themeDraw(themeNow,THEMES[themeNow]);ctx.restore()}deepTunnel(THEMES[themeNow]);bossFx(THEMES[themeNow]);let flow=clamp((speed-1.8)/3.7,0,1);for(let d of dust){let sh=now*.022*d.s*(.75+flow*1.25),x=((d.x-camera.x*.44-sh*Math.cos(d.a))%(W+180)+(W+180))%(W+180)-90,y=((d.y-camera.y*.44-sh*Math.sin(d.a))%(H+180)+(H+180))%(H+180)-90;ctx.strokeStyle=rgba(THEMES[themeNow].a,.05+flow*.17);ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+d.l*(1+flow*.45)*Math.cos(d.a),y+d.l*(1+flow*.45)*Math.sin(d.a));ctx.stroke()}};
const fastBaseTap=tap;removeEventListener('pointerdown',fastBaseTap);
tap=function(e){if(e)e.preventDefault();if(state==='menu'||state==='over'){reset();return}if(state!=='play')return;let tol=clamp(speed*.075,.26,.42),d=Math.abs(progress-goal);d<=tol?success(d):die(progress<goal?'TOO EARLY':'MISS BEAT')};
addEventListener('pointerdown',tap,{passive:false});
'''
if marker not in s: raise SystemExit('billboard marker not found')
s=s.replace(marker,marker+extra)
p.write_text(s)
