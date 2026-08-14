from pathlib import Path

p=Path('tools/fix_simple_ui.py')
s=p.read_text(encoding='utf-8')

css='''#orbitRankingsModal{position:fixed;inset:0;z-index:210;display:flex;align-items:center;justify-content:center;padding:18px;background:rgba(2,5,12,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}#orbitRankingsModal.hidden{display:none!important}.orbit-rank-panel{position:relative;width:min(94vw,430px);max-height:min(78vh,680px);display:flex;flex-direction:column;padding:22px 18px 18px;border:1px solid rgba(255,255,255,.28);border-radius:18px;background:rgba(9,14,26,.96);box-shadow:0 28px 80px rgba(0,0,0,.55);color:#fff;font-family:Arial,Helvetica,sans-serif}.orbit-rank-panel h2{margin:0 0 6px;text-align:center;font-size:clamp(28px,7vw,38px);font-weight:300;letter-spacing:.05em}.orbit-rank-sub{margin:0 0 14px;text-align:center;font-size:12px;letter-spacing:.08em;color:rgba(255,255,255,.52)}.orbit-rank-list{overflow:auto;border-top:1px solid rgba(255,255,255,.10);border-bottom:1px solid rgba(255,255,255,.10)}.orbit-rank-row{display:grid;grid-template-columns:42px 1fr auto;align-items:center;gap:10px;min-height:48px;padding:7px 5px;border-bottom:1px solid rgba(255,255,255,.07)}.orbit-rank-row:last-child{border-bottom:0}.orbit-rank-pos{font-size:15px;text-align:center;color:rgba(255,255,255,.56)}.orbit-rank-name{font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.orbit-rank-score{font-size:18px;font-weight:500}.orbit-rank-row.me{background:rgba(92,234,255,.09);box-shadow:inset 2px 0 0 rgba(92,234,255,.85)}.orbit-rank-empty{padding:30px 10px;text-align:center;color:rgba(255,255,255,.55);font-size:14px}.orbit-rank-me{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;margin-top:14px;padding:12px;border:1px solid rgba(255,255,255,.12);border-radius:12px;background:rgba(255,255,255,.045)}.orbit-rank-me-main{min-width:0}.orbit-rank-me-label{font-size:10px;letter-spacing:.14em;color:rgba(255,255,255,.45)}.orbit-rank-me-name{margin-top:4px;font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.orbit-rank-me-side{text-align:right}.orbit-rank-me-side b{display:block;font-size:19px}.orbit-rank-me-side span{display:block;margin-top:3px;font-size:11px;color:rgba(255,255,255,.5)}.orbit-rank-actions{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:10px}.orbit-rank-action{height:40px;border:1px solid rgba(255,255,255,.28);border-radius:10px;background:rgba(255,255,255,.06);color:#fff;font:400 13px Arial,Helvetica,sans-serif}.orbit-name-modal{position:fixed;inset:0;z-index:240;display:flex;align-items:center;justify-content:center;padding:22px;background:rgba(2,5,12,.76);backdrop-filter:blur(7px);-webkit-backdrop-filter:blur(7px)}.orbit-name-modal.hidden{display:none!important}.orbit-name-card{width:min(90vw,360px);padding:24px;border:1px solid rgba(255,255,255,.30);border-radius:18px;background:rgba(10,15,27,.98);color:#fff;font-family:Arial,Helvetica,sans-serif}.orbit-name-card h3{margin:0 0 7px;text-align:center;font-size:25px;font-weight:300}.orbit-name-card p{margin:0 0 15px;text-align:center;font-size:13px;color:rgba(255,255,255,.55)}#orbitPlayerNameInput{width:100%;height:46px;padding:0 13px;border:1px solid rgba(255,255,255,.28);border-radius:11px;outline:none;background:rgba(255,255,255,.07);color:#fff;font:400 16px Arial,Helvetica,sans-serif;text-align:center}#orbitPlayerNameInput:focus{border-color:rgba(91,235,255,.75)}.orbit-name-save{width:100%;height:44px;margin-top:11px;border:1px solid rgba(255,255,255,.62);border-radius:11px;background:rgba(255,255,255,.10);color:#fff;font:500 14px Arial,Helvetica,sans-serif}.orbit-rank-loading{padding:28px 10px;text-align:center;color:rgba(255,255,255,.55)}'''
if '#orbitRankingsModal{' not in s:
    m='@keyframes simpleTapPulse'
    if m not in s: raise SystemExit('CSS marker missing')
    s=s.replace(m,css+m,1)

dom='''\n  var rankings=document.createElement('div');rankings.id='orbitRankingsModal';rankings.className='hidden';rankings.innerHTML='<div class="orbit-rank-panel"><button class="orbit-close" id="orbitRankingsClose" aria-label="Close">×</button><h2 id="orbitRankingsTitle">RANKINGS</h2><div class="orbit-rank-sub" id="orbitRankingsSub">GLOBAL TOP PLAYERS</div><div class="orbit-rank-list" id="orbitRankingsList"><div class="orbit-rank-loading">Loading...</div></div><div class="orbit-rank-me"><div class="orbit-rank-me-main"><div class="orbit-rank-me-label" id="orbitRankYouLabel">YOU</div><div class="orbit-rank-me-name" id="orbitRankMyName">Player</div></div><div class="orbit-rank-me-side"><b id="orbitRankMyScore">0</b><span id="orbitRankMyPlace">#—</span></div></div><div class="orbit-rank-actions"><button class="orbit-rank-action" id="orbitRankRename">RENAME</button><button class="orbit-rank-action" id="orbitRankRefresh">REFRESH</button></div></div>';document.body.appendChild(rankings);\n  var nameModal=document.createElement('div');nameModal.id='orbitNameModal';nameModal.className='orbit-name-modal hidden';nameModal.innerHTML='<div class="orbit-name-card"><h3 id="orbitNameTitle">PLAYER NAME</h3><p id="orbitNameHelp">This name will appear on the global ranking.</p><input id="orbitPlayerNameInput" maxlength="20" autocomplete="off" spellcheck="false"><button class="orbit-name-save" id="orbitNameSave">SAVE</button></div>';document.body.appendChild(nameModal);\n'''
if "rankings.id='orbitRankingsModal'" not in s:
    m='document.body.appendChild(guide);'
    if m not in s: raise SystemExit('guide append marker missing')
    s=s.replace(m,m+dom,1)

code=r'''\n  var ORBIT_LB_URL='https://lmtcnbhdnryivjgupuct.supabase.co/functions/v1/orbit-leaderboard';
  var orbitIdentity=null;
  function orbitPlatform(){return /Android/i.test(navigator.userAgent)?'android':'web'}
  function orbitHex(bytes){return Array.from(bytes).map(function(b){return b.toString(16).padStart(2,'0')}).join('')}
  function orbitLoadIdentity(){
    try{var x=JSON.parse(localStorage.getItem('orbitBreakPlayer')||'null');if(x&&x.id&&x.secret&&x.name){orbitIdentity=x;return x}}catch(e){}
    var id=(crypto.randomUUID?crypto.randomUUID():('xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx').replace(/[xy]/g,function(c){var r=Math.random()*16|0,v=c==='x'?r:(r&3|8);return v.toString(16)}));
    var buf=new Uint8Array(32);crypto.getRandomValues(buf);var n='Player'+String(Math.floor(1000+Math.random()*9000));
    orbitIdentity={id:id,secret:orbitHex(buf),name:n};try{localStorage.setItem('orbitBreakPlayer',JSON.stringify(orbitIdentity))}catch(e){}return orbitIdentity;
  }
  function orbitSaveIdentity(){try{localStorage.setItem('orbitBreakPlayer',JSON.stringify(orbitIdentity))}catch(e){}}
  async function orbitLbCall(payload){
    var ctrl=new AbortController(),timer=setTimeout(function(){ctrl.abort()},8000);
    try{var r=await fetch(ORBIT_LB_URL,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),signal:ctrl.signal});var d=await r.json().catch(function(){return {}});if(!r.ok)throw new Error(d.error||('HTTP '+r.status));return d}finally{clearTimeout(timer)}
  }
  async function orbitEnsureRegistered(){
    var x=orbitLoadIdentity();
    try{await orbitLbCall({action:'register',playerId:x.id,playerSecret:x.secret,playerName:x.name,platform:orbitPlatform()});return true}catch(e){console.warn('Leaderboard register failed',e);return false}
  }
  async function orbitSubmitBest(value){
    var n=Math.max(0,Math.floor(Number(value)||0));if(!n)return;
    var x=orbitLoadIdentity();await orbitEnsureRegistered();
    try{await orbitLbCall({action:'submit',playerId:x.id,playerSecret:x.secret,playerName:x.name,score:n,platform:orbitPlatform()})}catch(e){console.warn('Leaderboard submit failed',e)}
  }
  function orbitEsc(v){return String(v==null?'':v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  async function orbitLoadRankings(){
    var list=document.getElementById('orbitRankingsList');if(list)list.innerHTML='<div class="orbit-rank-loading">Loading...</div>';
    var x=orbitLoadIdentity();await orbitEnsureRegistered();
    try{var d=await orbitLbCall({action:'rankings',limit:50,playerId:x.id}),rows=d.rankings||[],html='';for(var i=0;i<rows.length;i++){var r=rows[i],me=r.player_id===x.id;html+='<div class="orbit-rank-row'+(me?' me':'')+'"><div class="orbit-rank-pos">#'+(i+1)+'</div><div class="orbit-rank-name">'+orbitEsc(r.player_name)+'</div><div class="orbit-rank-score">'+Number(r.best_score||0)+'</div></div>'}if(list)list.innerHTML=html||'<div class="orbit-rank-empty">No scores yet</div>';var mine=d.me;var mn=document.getElementById('orbitRankMyName'),ms=document.getElementById('orbitRankMyScore'),mp=document.getElementById('orbitRankMyPlace');if(mn)mn.textContent=(mine&&mine.player_name)||x.name;if(ms)ms.textContent=String((mine&&mine.best_score)||0);if(mp)mp.textContent=mine&&mine.rank?'#'+mine.rank:'#—'}catch(e){if(list)list.innerHTML='<div class="orbit-rank-empty">Unable to load rankings</div>';console.warn(e)}
  }
  function orbitOpenRankings(e){stop(e);var m=document.getElementById('orbitRankingsModal');if(m)m.classList.remove('hidden');orbitLoadRankings()}
  function orbitCloseRankings(e){stop(e);var m=document.getElementById('orbitRankingsModal');if(m)m.classList.add('hidden');var h=document.getElementById('orbitHomeNav');document.querySelectorAll('.orbit-nav-btn').forEach(function(x){x.classList.remove('active')});if(h)h.classList.add('active')}
  function orbitOpenName(e){stop(e);var x=orbitLoadIdentity(),m=document.getElementById('orbitNameModal'),inp=document.getElementById('orbitPlayerNameInput');if(inp)inp.value=x.name;if(m)m.classList.remove('hidden');setTimeout(function(){if(inp){inp.focus();inp.select()}},60)}
  async function orbitSaveName(e){stop(e);var inp=document.getElementById('orbitPlayerNameInput'),v=(inp?inp.value:'').replace(/[\\u0000-\\u001f\\u007f]/g,'').trim().replace(/\\s+/g,' ').slice(0,20);if(v.length<2)return;var x=orbitLoadIdentity();x.name=v;orbitIdentity=x;orbitSaveIdentity();await orbitEnsureRegistered();var m=document.getElementById('orbitNameModal');if(m)m.classList.add('hidden');orbitLoadRankings()}
  orbitLoadIdentity();orbitEnsureRegistered();
  var rankBtn=document.getElementById('orbitRankingsNav');if(rankBtn)rankBtn.addEventListener('click',orbitOpenRankings);
  var rankClose=document.getElementById('orbitRankingsClose');if(rankClose)rankClose.addEventListener('click',orbitCloseRankings);
  var rankRefresh=document.getElementById('orbitRankRefresh');if(rankRefresh)rankRefresh.addEventListener('click',function(e){stop(e);orbitLoadRankings()});
  var rankRename=document.getElementById('orbitRankRename');if(rankRename)rankRename.addEventListener('click',orbitOpenName);
  var nameSave=document.getElementById('orbitNameSave');if(nameSave)nameSave.addEventListener('click',orbitSaveName);
  var nameInput=document.getElementById('orbitPlayerNameInput');if(nameInput)nameInput.addEventListener('keydown',function(e){if(e.key==='Enter')orbitSaveName(e)});
  rankings.addEventListener('pointerdown',function(e){e.stopPropagation();if(e.target===rankings)orbitCloseRankings(e)});nameModal.addEventListener('pointerdown',function(e){e.stopPropagation()});
  var lastSubmittedScore=-1;if(over){new MutationObserver(function(){if(!over.classList.contains('hidden')){var f=document.getElementById('finalScore'),v=f?Number(f.textContent):0;if(v>=0&&v!==lastSubmittedScore){lastSubmittedScore=v;orbitSubmitBest(v)}}}).observe(over,{attributes:true,attributeFilter:['class']})}
'''
if 'var ORBIT_LB_URL=' not in s:
    m="  gear.addEventListener('pointerdown',stop);gear.addEventListener('click',openSettings);"
    if m not in s: raise SystemExit('events marker missing')
    s=s.replace(m,code+'\n'+m,1)

old="set('orbitGuideOk',tx.ok);set('orbitLanguageBtn',vi?'VI':'EN');set('orbitHomeLabel',vi?'TRANG CHỦ':'HOME');set('orbitSkinsLabel',vi?'GIAO DIỆN':'SKINS');set('orbitRankingsLabel',vi?'XẾP HẠNG':'RANKINGS');"
new="set('orbitGuideOk',tx.ok);set('orbitLanguageBtn',vi?'VI':'EN');set('orbitHomeLabel',vi?'TRANG CHỦ':'HOME');set('orbitSkinsLabel',vi?'GIAO DIỆN':'SKINS');set('orbitRankingsLabel',vi?'XẾP HẠNG':'RANKINGS');set('orbitRankingsTitle',vi?'XẾP HẠNG':'RANKINGS');set('orbitRankingsSub',vi?'TOP NGƯỜI CHƠI TOÀN CẦU':'GLOBAL TOP PLAYERS');set('orbitRankYouLabel',vi?'BẠN':'YOU');set('orbitRankRename',vi?'ĐỔI TÊN':'RENAME');set('orbitRankRefresh',vi?'LÀM MỚI':'REFRESH');set('orbitNameTitle',vi?'TÊN NGƯỜI CHƠI':'PLAYER NAME');set('orbitNameHelp',vi?'Tên này sẽ hiển thị trên bảng xếp hạng toàn cầu.':'This name will appear on the global ranking.');set('orbitNameSave',vi?'LƯU':'SAVE');"
if old in s and "set('orbitRankingsTitle'" not in s:
    s=s.replace(old,new,1)

p.write_text(s,encoding='utf-8')
print('leaderboard patch applied')
