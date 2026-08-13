from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='const rhythmBaseDraw=draw;'
if marker not in s:
    raise SystemExit('draw marker not found')

block=r'''
/* DESKTOP PERFORMANCE + ADAPTIVE FX */
const PERF_DESKTOP=matchMedia('(pointer:fine)').matches&&!/Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
let perfQuality=PERF_DESKTOP?.82:1,perfFps=60,perfClock=0;
const perfOriginalResize=resize;
removeEventListener('resize',perfOriginalResize);
resize=function(){
  W=innerWidth;H=innerHeight;
  const nativeDpr=devicePixelRatio||1;
  const pixelBudget=PERF_DESKTOP?2100000:1550000;
  const budgetDpr=Math.sqrt(pixelBudget/Math.max(1,W*H));
  DPR=Math.min(nativeDpr,PERF_DESKTOP?1.15:1.7,Math.max(PERF_DESKTOP?.72:1,budgetDpr));
  canvas.width=Math.max(1,Math.round(W*DPR));canvas.height=Math.max(1,Math.round(H*DPR));ctx.setTransform(DPR,0,0,DPR,0,0);
  radius=clamp(Math.min(W,H)*.27,76,128);seedBackground();
  const maxStars=Math.round((PERF_DESKTOP?62:78)*perfQuality);if(stars.length>maxStars)stars=stars.slice(0,maxStars);
  const maxDust=Math.round((PERF_DESKTOP?20:28)*perfQuality);if(dust.length>maxDust)dust=dust.slice(0,maxDust);
  if(state!=='play'){anchor={x:0,y:0};camera={x:0,y:0};buildTarget()}
};
addEventListener('resize',resize,{passive:true});

if(PERF_DESKTOP){
  const perfStyle=document.createElement('style');
  perfStyle.textContent='.card,.pill{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}';
  document.head.appendChild(perfStyle);
  const startCta=document.querySelector('#start .cta');if(startCta)startCta.innerHTML='<span class="playtri"></span>SPACE';
  const overCta=document.querySelector('#gameover .cta');if(overCta)overCta.innerHTML='<span class="retry-icon"></span>SPACE';
  addEventListener('keydown',function(e){if(e.code==='Space'&&e.repeat){e.preventDefault();e.stopImmediatePropagation()}},true);
}

deepTunnel=function(t){
  let vX=W*.5-camera.x*.045,vY=H*.42-camera.y*.035,flow=clamp((speed-1.5)/3.8,0,1),rings=Math.max(12,Math.round(13+perfQuality*14));
  for(let i=rings-1;i>=0;i--){let d=((i+now*.003*(1.25+flow*2.2))%rings)/rings,e=d*d;ctx.strokeStyle=rgba(i%3?t.a:t.b,(1-d)*(.025+flow*.075));ctx.lineWidth=.8+d*3;ctx.beginPath();ctx.ellipse(vX,vY+e*H*.5,W*(.025+d*.86),H*(.012+d*.66),0,Math.PI*.07,Math.PI*.93);ctx.stroke()}
  const lanes=perfQuality<.68?5:8;for(let i=-lanes;i<=lanes;i++){ctx.strokeStyle=rgba(i%2?t.a:t.b,.028+flow*.055);ctx.beginPath();ctx.moveTo(vX+i*9,vY);ctx.lineTo(W*.5+i*W*.15-camera.x*.08,H+30);ctx.stroke()}
  if(perfQuality>.62){let g=ctx.createRadialGradient(vX,vY,0,vX,vY,Math.min(W,H)*.19);g.addColorStop(0,rgba(t.a,.14));g.addColorStop(1,rgba(t.a,0));ctx.fillStyle=g;ctx.fillRect(0,0,W,H)}
};

bossFx=function(t){
  let b=clamp((combo-5)/9,0,1);if(!b)return;let beat=typeof rhythmPulse==='function'?rhythmPulse():0,cx=W*.5-camera.x*.02,cy=H*.42-camera.y*.02,q=b*(.75+.25*Math.sin(now*.008)+beat*.3),rings=perfQuality<.68?4:6,rays=perfQuality<.68?7:10;
  ctx.save();ctx.globalCompositeOperation='screen';
  for(let i=0;i<rings;i++){let r=42+i*32+q*16;ctx.strokeStyle=rgba(i%2?t.b:t.a,.06+q*.11);ctx.lineWidth=1.1+i*.28;ctx.beginPath();ctx.arc(cx,cy,r,now*.0006*(i%2?1:-1),now*.0006*(i%2?1:-1)+Math.PI*1.42);ctx.stroke()}
  for(let i=0;i<rays;i++){let a=now*.0009+i*TAU/rays,r=50+q*22;ctx.strokeStyle=rgba(i%2?t.a:t.b,.04+q*.08);ctx.beginPath();ctx.moveTo(cx+Math.cos(a)*r,cy+Math.sin(a)*r*.55);ctx.lineTo(cx+Math.cos(a)*(r+62),cy+Math.sin(a)*(r+62)*.55);ctx.stroke()}
  if(perfQuality>.7){let g=ctx.createRadialGradient(cx,cy,0,cx,cy,88);g.addColorStop(0,rgba('#ffffff',.11*q));g.addColorStop(.22,rgba(t.b,.16*q));g.addColorStop(1,rgba(t.a,0));ctx.fillStyle=g;ctx.beginPath();ctx.arc(cx,cy,90,0,TAU);ctx.fill()}
  ctx.restore()
};

drawBackground=function(){
  let n=Math.floor(hits/3)%THEMES.length;if(n!==themeNow){themePrev=themeNow;themeNow=n;themeAt=now;updateHUD()}
  let m=clamp((now-themeAt)/(perfQuality<.68?420:720),0,1),e=m*m*(3-2*m);ctx.fillStyle='#010308';ctx.fillRect(0,0,W,H);
  if(themeNow!==themePrev&&perfQuality>.68){ctx.save();themeDraw(themePrev,THEMES[themePrev]);ctx.restore();ctx.save();ctx.globalAlpha=e;themeDraw(themeNow,THEMES[themeNow]);ctx.restore()}else{ctx.save();themeDraw(themeNow,THEMES[themeNow]);ctx.restore()}
  deepTunnel(THEMES[themeNow]);bossFx(THEMES[themeNow]);let flow=clamp((speed-1.8)/3.7,0,1),step=perfQuality<.68?2:1;
  for(let i=0;i<dust.length;i+=step){let d=dust[i],sh=now*.022*d.s*(.75+flow*1.25),x=((d.x-camera.x*.44-sh*Math.cos(d.a))%(W+180)+(W+180))%(W+180)-90,y=((d.y-camera.y*.44-sh*Math.sin(d.a))%(H+180)+(H+180))%(H+180)-90;ctx.strokeStyle=rgba(THEMES[themeNow].a,.045+flow*.14);ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+d.l*(1+flow*.35)*Math.cos(d.a),y+d.l*(1+flow*.35)*Math.sin(d.a));ctx.stroke()}
};

overlay=function(){
  let t=THEMES[themeNow],beat=typeof rhythmPulse==='function'?rhythmPulse():0,v=clamp(flash*2+beat*.28,0,1);
  if(v&&perfQuality>.58){let g=ctx.createRadialGradient(W*.5,H*.57,10,W*.5,H*.57,Math.max(W,H)*.45);g.addColorStop(0,rgba(t.a,.055*v));g.addColorStop(.65,rgba(t.b,.025*v));g.addColorStop(1,rgba(t.a,0));ctx.fillStyle=g;ctx.fillRect(0,0,W,H)}
  let boss=clamp((combo-5)/9,0,1),c=Math.max(flash*.4,boss*.24);if(c&&perfQuality>.62){ctx.globalCompositeOperation='screen';ctx.fillStyle='rgba(255,0,90,'+(c*.018)+')';ctx.fillRect(2,0,W,H);ctx.fillStyle='rgba(0,220,255,'+(c*.018)+')';ctx.fillRect(-2,0,W,H);ctx.globalCompositeOperation='source-over'}
  let vg=ctx.createRadialGradient(W*.5,H*.5,Math.min(W,H)*.2,W*.5,H*.5,Math.max(W,H)*.76);vg.addColorStop(0,'#00000000');vg.addColorStop(1,'#0000004d');ctx.fillStyle=vg;ctx.fillRect(0,0,W,H);
  if(perfQuality>.78){ctx.strokeStyle='#ffffff06';for(let y=0;y<H;y+=14){ctx.beginPath();ctx.moveTo(0,y+.5);ctx.lineTo(W,y+.5);ctx.stroke()}}
  if(flash){ctx.fillStyle='rgba(255,255,255,'+(flash*.09)+')';ctx.fillRect(0,0,W,H)}
};

const perfBaseBurst=burst;
burst=function(x,y,n){perfBaseBurst(x,y,Math.max(7,Math.round(n*(PERF_DESKTOP?.72:.9)*perfQuality)))};
const perfBaseUpdate=update;
update=function(dt){
  perfFps=perfFps*.92+(1/Math.max(.001,dt))*.08;perfClock+=dt;
  if(perfClock>1.25){if(perfFps<48)perfQuality=Math.max(.52,perfQuality-.14);else if(perfFps>57)perfQuality=Math.min(PERF_DESKTOP?.88:1,perfQuality+.07);perfClock=0}
  perfBaseUpdate(dt);const maxTrail=Math.max(16,Math.round(34*perfQuality));if(trail.length>maxTrail)trail.splice(0,trail.length-maxTrail)
};
'''

s=s.replace(marker,block+'\n'+marker,1)
s=s.replace("if(bp>.03){const g=ctx.createRadialGradient", "if(bp>.03&&perfQuality>.56){const g=ctx.createRadialGradient",1)
p.write_text(s,encoding='utf-8')
print('patched index.html')
