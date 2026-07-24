<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#0c0a1a">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="차원 균열의 만물상">
  <title>차원 균열의 만물상</title>
  <link href="https://cdn.jsdelivr.net/npm/galmuri@latest/dist/galmuri.css" rel="stylesheet">
<style>
:root{
  --bg:#0c0a1a; --panel:#161231; --panel2:#1d1840; --line:#2e2560;
  --rift:#a06bff; --cyan:#43e6cf; --gold:#ffd23f; --red:#ff5470; --green:#8cff6b;
  --txt:#eae6ff; --mut:#948dc4;
}
*{box-sizing:border-box; margin:0; padding:0;}
body{
  background:var(--bg); color:var(--txt);
  font-family:'Galmuri11','Galmuri9',monospace; font-size:14px;
  min-height:100vh; padding:14px;
  background-image:
    radial-gradient(ellipse 60% 40% at 50% -10%, #1c1445 0%, transparent 60%);
}
h1{font-family:'Galmuri14','Galmuri11',monospace; font-size:20px; letter-spacing:1px;}
button{
  font-family:inherit; font-size:13px; color:var(--txt);
  background:var(--panel2); border:2px solid var(--line);
  padding:7px 10px; cursor:pointer; image-rendering:pixelated;
  box-shadow:0 3px 0 #0a0818;
}
button:hover:not(:disabled){border-color:var(--rift); color:#fff;}
button:active:not(:disabled){transform:translateY(2px); box-shadow:0 1px 0 #0a0818;}
button:disabled{opacity:.38; cursor:not-allowed;}
button.buy{border-color:#4a3a8a;}
button.danger{border-color:#6b2438;}
button.gold-btn{border-color:#7a611c; color:var(--gold);}

.wrap{max-width:1060px; margin:0 auto;}
header{
  display:flex; justify-content:space-between; align-items:center;
  border:2px solid var(--line); background:var(--panel);
  padding:10px 14px; margin-bottom:12px;
}
header .sub{color:var(--mut); font-size:12px;}
.hud{display:flex; gap:14px; align-items:center; font-size:13px;}
.hud b{color:var(--gold);}
.hud .shard{color:var(--rift);}

main{display:grid; grid-template-columns: 560px 1fr; gap:12px;}
@media (max-width:980px){ main{grid-template-columns:1fr;} }

.box{border:2px solid var(--line); background:var(--panel); padding:12px;}
.box h2{font-size:15px; color:var(--cyan); margin-bottom:8px;}

/* ---- 전투 화면 ---- */
#stageBar{display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;}
#stageName{font-size:15px;}
#stageName em{color:var(--rift); font-style:normal;}
.pips{display:flex; gap:4px;}
.pip{width:12px; height:12px; background:#241d4d; border:1px solid var(--line);}
.pip.on{background:var(--cyan); border-color:var(--cyan);}
.pip.boss{background:#241d4d; border-color:var(--red);}
.pip.boss.on{background:var(--red);}

canvas#game{
  width:100%; display:block; background:#0a0716;
  border:2px solid var(--line); image-rendering:pixelated;
}
#bossTimerWrap{height:14px; background:#241d4d; border:1px solid var(--line); margin-top:6px; position:relative; display:none;}
#bossTimer{height:100%; background:var(--red); width:100%;}
#bossTimerTxt{position:absolute; inset:0; text-align:center; font-size:11px; line-height:12px; color:#fff;}

.bars{display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:8px;}
.barbox{font-size:12px;}
.barbox .lb{display:flex; justify-content:space-between; color:var(--mut); margin-bottom:3px;}
.bar{height:14px; background:#241d4d; border:1px solid var(--line);}
.bar > div{height:100%; transition:width .15s;}
#pHpBar{background:var(--green);} #mHpBar{background:var(--red);}
#expBarWrap{margin-top:6px;}
#expBar{background:var(--rift); height:8px;}
#expOuter{height:8px; background:#241d4d; border:1px solid var(--line);}

#statLine{display:flex; flex-wrap:wrap; gap:10px; margin-top:8px; font-size:12px; color:var(--mut);}
#statLine b{color:var(--txt);}

#bossBtn{width:100%; margin-top:10px; border-color:var(--red); color:#ffb3c0; font-size:14px; padding:10px;}
#bossBtn.ready{animation:pulse 1s infinite; color:#fff; background:#3a1030;}
@keyframes pulse{0%,100%{box-shadow:0 3px 0 #0a0818,0 0 0 0 rgba(255,84,112,.5);}50%{box-shadow:0 3px 0 #0a0818,0 0 14px 2px rgba(255,84,112,.55);}}

#log{margin-top:10px; font-size:12px; color:var(--mut); height:64px; overflow:hidden; line-height:1.6; border-top:1px dashed var(--line); padding-top:6px;}
#log .g{color:var(--gold);} #log .p{color:var(--rift);} #log .r{color:var(--red);} #log .c{color:var(--cyan);}

/* ---- 우측 패널 ---- */
.tabs{display:flex; gap:6px; margin-bottom:10px; flex-wrap:wrap;}
.tabs button{padding:6px 12px;}
.tabs button.on{border-color:var(--cyan); color:var(--cyan);}
.tabpage{display:none;}
.tabpage.on{display:block;}

.row{display:flex; justify-content:space-between; align-items:center; gap:8px; padding:8px; border:1px solid var(--line); background:var(--panel2); margin-bottom:6px;}
.row .info{font-size:12px; line-height:1.5;}
.row .info small{color:var(--mut); display:block;}
.chips{display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px;}
.chip{font-size:11px; border:1px solid var(--line); background:var(--panel2); padding:4px 8px; color:var(--mut);}
.chip b{color:var(--txt);}

.gN{color:#cfc9f2;} .gR{color:#5ab0ff;} .gE{color:#c07bff;} .gL{color:var(--gold);}
.slot{border:1px dashed var(--line); padding:8px; margin-bottom:6px; font-size:12px;}
.slot span.empty{color:var(--mut);}

.art{display:flex; justify-content:space-between; padding:6px 8px; border:1px solid var(--line); margin-bottom:5px; font-size:12px; background:var(--panel2);}
.art b{color:var(--rift);}
.prob{font-size:11px; color:var(--mut); margin-top:6px; line-height:1.6;}

.dlc{border:2px solid #7a611c; background:#20183a; padding:10px; margin-bottom:8px;}
.dlc h3{color:var(--gold); font-size:13px; margin-bottom:4px;}
.dlc p{font-size:12px; color:var(--mut); line-height:1.5; margin-bottom:8px;}
.dlc .owned{color:var(--green); font-size:12px;}
.notice{font-size:11px; color:var(--mut); border:1px dashed var(--line); padding:8px; line-height:1.7; margin-top:10px;}

/* ---- 모달 ---- */
#modalBg{position:fixed; inset:0; background:rgba(5,3,15,.8); display:none; align-items:center; justify-content:center; z-index:10;}
#modal{background:var(--panel); border:2px solid var(--rift); padding:20px; max-width:380px; width:92%; text-align:center;}
#modal h3{color:var(--rift); margin-bottom:10px; font-size:16px;}
#modal .body{font-size:13px; line-height:1.9; margin-bottom:14px;}
#modal .body b{color:var(--gold);}
#modal .body .big{font-size:15px; color:var(--cyan);}

footer{margin-top:12px; text-align:center; font-size:11px; color:var(--mut);}

/* ===== 픽셀 UI 장식 ===== */
.box, header{position:relative;}
.box::before, header::before{
  content:''; position:absolute; inset:3px;
  border:1px solid #221a4d; pointer-events:none;
}
.box::after, header::after{
  content:''; position:absolute; top:-2px; left:-2px; width:12px; height:12px;
  border-top:4px solid var(--rift); border-left:4px solid var(--rift); pointer-events:none;
}
.box > .brCorner{position:absolute; bottom:-2px; right:-2px; width:12px; height:12px;
  border-bottom:4px solid var(--cyan); border-right:4px solid var(--cyan); pointer-events:none;}
header h1 em{animation:riftGlow 2.2s infinite;}
@keyframes riftGlow{0%,100%{text-shadow:0 0 4px rgba(160,107,255,.4);}50%{text-shadow:0 0 12px rgba(160,107,255,.95), 0 0 20px rgba(67,230,207,.35);}}
.tabs button.on{box-shadow:0 3px 0 #0a0818, inset 0 -3px 0 var(--cyan);}

#cvWrap{position:relative; border:2px solid var(--line); background:#0a0716;}
#cvWrap canvas{border:none; width:100%;}
#scanlines{position:absolute; inset:0; pointer-events:none;
  background:repeating-linear-gradient(0deg, rgba(0,0,0,.16) 0 2px, transparent 2px 4px);}
#vignette{position:absolute; inset:0; pointer-events:none;
  box-shadow:inset 0 0 46px 12px rgba(4,2,12,.75);}
.cvGem{position:absolute; width:8px; height:8px; background:var(--rift); animation:gemBlink 1.6s infinite;}
.cvGem.g1{top:-4px; left:-4px;} .cvGem.g2{top:-4px; right:-4px; animation-delay:.4s;}
.cvGem.g3{bottom:-4px; left:-4px; animation-delay:.8s;} .cvGem.g4{bottom:-4px; right:-4px; animation-delay:1.2s;}
@keyframes gemBlink{0%,100%{background:var(--rift);}50%{background:var(--cyan);}}

.bar{position:relative;}
.bar::after{content:''; position:absolute; inset:0; pointer-events:none;
  background:repeating-linear-gradient(90deg, transparent 0 12px, rgba(0,0,0,.3) 12px 14px);}
.bar > div{box-shadow:inset 0 -4px 0 rgba(0,0,0,.28);}
#pips .pip.on{box-shadow:0 0 5px rgba(67,230,207,.7);}
@media (prefers-reduced-motion: reduce){
  header h1 em, .cvGem, #bossBtn.ready{animation:none;}
}

.gN{color:#9aa0b0}.gR{color:#43a0e6}.gE{color:#a86bff}.gU{color:#ffd23f}
.gL{color:#ff8a3a}.gM{color:#ff5470;text-shadow:0 0 4px #ff5470}
.gC{color:#43e6cf;text-shadow:0 0 6px #43e6cf}
.gP{color:#fff;text-shadow:0 0 8px #fff,0 0 12px #a86bff}

.gDEV{color:#ff2d95;font-weight:bold;text-shadow:0 0 6px #ff2d95,0 0 12px #ffd23f,0 0 18px #43e6cf}
#devConsole input::placeholder{color:#666}
</style>


<body>

<div class="wrap">
<header>
  <div>
    <h1>차원 균열의 <em style="color:var(--rift); font-style:normal;">만물상</em></h1>
    <div class="sub">Dimensional Shopkeeper — 방치형 RPG</div>
    <div id="nickTag" style="font-size:11px; color:var(--green); margin-top:4px;">내 고유이름: …</div>
  </div>
  <div class="hud">
    <span>골드 <b id="goldTxt">0</b></span>
    <span>스탯PT <b id="statPtTxt" style="color:var(--green)">0</b></span>
    <span class="shard">균열의 조각 <b id="shardTxt" style="color:var(--rift)">0</b></span>
    <span>전투력 <b id="powerDisplay" style="color:var(--gold)">0</b></span>
    <button id="saveBtn" style="display:none;" style="font-size:11px; padding:4px 8px;">수동 저장<button onclick="openPoker()" class="buy" style="background:linear-gradient(135deg, #e94560, #ffd23f);">🃏 포커</button>
    <button onclick="openSlotMachine()" class="buy" style="grid-column:1/3;background:linear-gradient(135deg,#2d1b4e,#ffd23f);">🎰 슬롯머신 (LUCKY 777)</button></button>
  </div>
</header>

<main>
  <!-- ===== 좌: 전투 ===== -->
  <section class="box"><div class="brCorner"></div>
    <div id="questBox" style="border:1px dashed var(--cyan); padding:8px; margin-bottom:8px; background:rgba(67,230,207,.04);">
      <div style="font-size:11px; color:var(--cyan);">🎯 차원의 무한 퀘스트</div>
      <div id="questDesc" style="font-size:12px; margin:3px 0;"></div>
      <div class="bar" style="height:10px;"><div id="questBar" style="background:var(--cyan); width:0%; height:100%;"></div></div>
      <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--mut); margin-top:3px;">
        <span id="questCount"></span><span style="color:var(--gold);" id="questReward"></span>
      </div>
    </div>
    <div id="stageBar">
      <div id="stageName">스테이지 <em>1-1</em> · 슬라임 습지</div>
      <div class="pips" id="pips"></div>
    </div>
    <div id="skillButtons" style="margin:15px 0; display:grid; grid-template-columns:1fr 1fr; gap:8px;"></div>
  <div id="cvWrap">
      <canvas id="game" width="520" height="290"></canvas>
      <div id="scanlines"></div><div id="vignette"></div>
      <div class="cvGem g1"></div><div class="cvGem g2"></div><div class="cvGem g3"></div><div class="cvGem g4"></div>
    </div>
    <div style="font-size:11px; color:var(--mut); margin-top:5px;">🖱 <b style="color:var(--cyan)">수동 전투 모드</b> — 몬스터를 직접 클릭해서 공격하세요 (쿨타임 0.01초). 게임을 꺼두면 만물상이 자동으로 사냥합니다.</div>
    <div id="bossTimerWrap"><div id="bossTimer"></div><div id="bossTimerTxt">30.0s</div></div>

    <div class="bars">
      <div class="barbox">
        <div class="lb"><span id="pName">만물상 주인 LV.1</span><span id="pHpTxt"></span></div>
        <div class="bar"><div id="pHpBar" style="width:100%"></div></div>
        <div id="expBarWrap"><div id="expOuter"><div id="expBar" style="width:0%"></div></div></div>
      </div>
      <div class="barbox">
        <div class="lb"><span id="mName">슬라임</span><span id="mHpTxt"></span></div>
        <div class="bar"><div id="mHpBar" style="width:100%"></div></div>
      </div>
    </div>
    <div id="statLine"></div>
    <div style="margin-top:6px;">
      <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--mut);"><span>🔥 피버 게이지</span><span id="feverTxt">0%</span></div>
      <div class="bar" style="height:8px;"><div id="feverBar" style="background:linear-gradient(90deg,#ff8c42,#ffd23f); width:0%; height:100%;"></div></div>
    </div>
    <div id="dpsLine" style="font-size:11px; color:var(--mut); margin-top:5px;"></div>
    <button id="bossBtn" disabled>보스 도전 (일반 몬스터 10마리 처치 필요)</button>
    <div id="log"></div>
  </section>

  <!-- ===== 우: 관리 패널 ===== -->
  <section class="box"><div class="brCorner"></div>
    <div class="tabs">
      <button data-tab="up" class="on">강화</button>
      <button data-tab="eq">장비·인벤토리</button>
      <button data-tab="art">유물·환생</button>
      <button data-tab="shop">만물상 상점</button>
      <button data-tab="content">콘텐츠</button>
      <button data-tab="talent">특성·도감</button>
      <button data-tab="set">설정</button>
      <button data-tab="social">💬 소셜</button>
    </div>

    <div class="tabpage on" id="tab-up">
      <h2>스탯 영구 강화</h2>
      <div class="row">
        <div class="info">공격력 강화 <span id="atkLvTxt"></span><small id="atkGainTxt"></small></div>
        <button id="upAtk" class="gold-btn"></button>
      </div>
      <div class="row">
        <div class="info">방어력 강화 <span id="defLvTxt"></span><small id="defGainTxt"></small></div>
        <button id="upDef" class="gold-btn"></button>
      </div>
      <div class="row">
        <div class="info">치명타 대미지 강화 <span id="critLvTxt"></span><small id="critGainTxt"></small></div>
        <button id="upCrit" class="gold-btn"></button>
      </div>
      <h2 style="margin-top:12px;">스탯 포인트 분배 <span style="color:var(--mut); font-size:12px;">(레벨업마다 +4)</span></h2>
      <div class="row">
        <div class="info">한 번에 투자할 개수</div>
        <input type="number" id="statAmt" value="1" min="1" style="width:70px; background:var(--panel2); border:2px solid var(--line); color:var(--gold); text-align:center; font-family:inherit; padding:5px;">
      </div>
      <div class="row"><div class="info">💪 힘 <span id="stStr"></span><small>공격 대미지 +3/pt</small></div><button class="gold-btn" onclick="addStatMulti('str')">+</button></div>
      <div class="row"><div class="info">🏹 민첩 <span id="stDex"></span><small>치명타 확률 +1%/pt</small></div><button class="gold-btn" onclick="addStatMulti('dex')">+</button></div>
      <div class="row"><div class="info">❤️ 체력 <span id="stVit"></span><small>최대 생명력 +25/pt</small></div><button class="gold-btn" onclick="addStatMulti('vit')">+</button></div>
      <h2 style="margin-top:12px;">🔨 장착 무기 제련</h2>
      <div class="row"><div class="info"><span id="forgeName">무기 없음</span><small id="forgeChance"></small></div><button class="gold-btn" id="forgeBtn" onclick="forgeWeapon()">-</button></div>
      <div class="notice">💡 강화 비용은 1회당 <b>7%씩 복리</b>로 오르고, 효과는 5%씩 오릅니다. 골드만으로는 언젠가 벽에 부딪히도록 설계되어 있어요. 그때가 <span style="color:var(--rift)">환생</span> 타이밍입니다.</div>
    </div>

    <div class="tabpage" id="tab-eq">
      <h2>장착 중</h2>
      <div class="slot" id="slotW"><span class="empty">무기 없음</span></div>
      <div class="slot" id="slotA"><span class="empty">방어구 없음</span></div>
      <h2 style="margin-top:10px;">재료 주머니</h2>
      <div class="chips" id="matChips"></div>
      <h2>장비 인벤토리 <span id="invCount" style="color:var(--mut); font-size:12px;"></span></h2>
      <div style="font-size:11px; color:var(--mut); margin-bottom:6px;">같은 이름·등급 장비 3개 = 상위 등급 1개로 합성 · 강화는 강화석+골드 소모</div>
      <div id="eqList"></div>
    </div>

    <div class="tabpage" id="tab-art">
      <h2>유물 (환생해도 유지)</h2>
      <div id="artList"></div>
      <button id="gachaBtn" class="buy" style="width:100%; margin-top:6px;">유물 각인 — 균열의 조각 1개</button>
      <div class="prob">확률 공시: 공격의 유물 25% · 황금의 유물 25% · 시간의 유물 25% · 급소의 유물 25%<br>(동일 확률 · 중복 시 해당 유물 레벨 +1)</div>
      <h2 style="margin-top:14px;">환생 — 차원 붕괴</h2>
      <div class="row">
        <div class="info">레벨·골드·장비·스탯 강화가 초기화됩니다.<small id="rebirthGainTxt"></small></div>
        <button id="rebirthBtn" class="danger">차원 붕괴</button>
      </div>
    </div>

    <div class="tabpage" id="tab-shop">
      <h2>동료 영입 (재료 소모 · 영구)</h2>
            <div style="border:2px solid var(--rift); padding:10px; margin:10px 0; border-radius:4px;">
        <h3 style="color:var(--cyan);">🐾 나의 펫 보관함</h3>
        <div style="background:var(--panel2); padding:8px; margin:10px 0; border-radius:4px; min-height:50px;">
          <div id="petInventory" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(70px, 1fr)); gap:8px;">
            <!-- 펫 목록이 여기 나타남 -->
          </div>
        </div>
        <h3 style="color:var(--cyan); margin-top:15px;">⭐ 현재 장착 펫</h3>
        <div style="background:var(--panel); padding:10px; border:2px solid var(--gold); border-radius:4px; margin:10px 0; text-align:center;">
          <div id="equippedPet" style="font-size:24px; margin:10px 0;">펫을 선택하세요</div>
          <button onclick="unequipPet()" style="width:100%; margin-top:5px;" class="red-btn">장착 해제</button>
        </div>
      </div>
      <h2 style="margin-top:14px;">만물상 가챠 (골드 소모)</h2>
      <div class="row"><div class="info">⚔️ 무기 직거래 <small>[일반~영웅] 1회 300G</small></div>
        <div style="display:flex; gap:4px;"><button onclick="buyShopItemMulti('weapon_normal',1)">1회</button><button onclick="buyShopItemMulti('weapon_normal',10)">10회</button><button onclick="buyShopItemMulti('weapon_normal',50)">50회</button></div></div>
      <div class="row"><div class="info">🎲 프리미엄 무기 뽑기 <small>[희귀~전설] 1회 800G</small></div>
        <div style="display:flex; gap:4px;"><button class="gold-btn" onclick="buyShopItemMulti('weapon_gacha',1)">1회</button><button class="gold-btn" onclick="buyShopItemMulti('weapon_gacha',10)">10회</button><button class="gold-btn" onclick="buyShopItemMulti('weapon_gacha',50)">50회</button></div></div>
      <div class="row"><div class="info">🐥 펫 뽑기 <small>1회 1200G · 미보유 동료 랜덤 영입 (전부 보유 시 600G 환급)</small></div>
        <div style="display:flex; gap:4px;"><button class="buy" onclick="petGacha(1)">1회</button><button class="buy" onclick="petGacha(3)">3회</button></div></div>
      <div class="row"><div class="info">⚡ 최고 장착 <small>가장 강한 무기·방어구 자동 장착</small></div><button onclick="equipBestGear()">실행</button></div>
      <h2 style="margin-top:14px;">DLC (스팀 상점 데모)</h2>
      <div class="dlc" id="dlcSupporter">
        <h3>🌟 서포터 팩 — ₩5,500</h3>
        <p>골드 획득량 영구 2배 + 황금 로브 스킨. 소모성 아이템이 아닌 영구 효과 1회 구매입니다.</p>
        <button class="gold-btn" id="buySupporter">구매 시뮬레이션</button>
      </div>
      <div class="dlc" id="dlcOffline">
        <h3>⏰ 차원 시계 — ₩3,300</h3>
        <p>오프라인 보상 누적 한도 8시간 → 24시간 확장.</p>
        <button class="gold-btn" id="buyOffline">구매 시뮬레이션</button>
      </div>
      <div class="notice">⚠️ 실제 스팀 빌드에서는 이 버튼 대신 <b>Steamworks DLC 소유 확인</b>(SteamApps.BIsDlcInstalled)으로 대체하세요. 소모성 재화 판매·가챠는 스팀 리뷰와 국내 확률형 아이템 규제 측면에서 권장하지 않습니다. (게임 내 유물 각인은 무료 재화만 사용)</div>
    </div>
    <div class="tabpage" id="tab-content">
      <h2>🗼 무한의 탑 <span id="towerFloorTxt" style="color:var(--mut); font-size:12px;"></span></h2>
      <div class="row"><div class="info">한 층씩 오르는 도전 던전<small>5층마다 균열의 조각 +1 · 층수는 환생해도 유지</small></div><button id="towerBtn" onclick="toggleTower()">입장</button></div>
      <h2 style="margin-top:10px;">⛏ 미다스의 방 <span id="dgnUseTxt" style="color:var(--mut); font-size:12px;"></span></h2>
      <div class="row"><div class="info">60초 동안 때리는 만큼 골드 획득<small>하루 3회 입장</small></div><button onclick="enterGoldDgn()">입장</button></div>
      <h2 style="margin-top:10px;">⚒ 광산 방치</h2>
      <div class="row"><div class="info" id="mineInfo"></div><button id="mineBtn" onclick="toggleMine()">보내기</button></div>
      <h2 style="margin-top:10px;">🚪 차원의 문 탐험</h2>
      <div class="row"><div class="info" id="expInfo"></div><button id="expBtn" onclick="doExped()">출발</button></div>
      <h2 style="margin-top:10px;">📜 현상 수배 (일일)</h2>
      <div class="row"><div class="info" id="bountyInfo"></div></div>
      <h2 style="margin-top:10px;">🎲 만물상 주점 — 주사위</h2>
      <div class="row"><div class="info">골드를 걸고 딜러와 주사위 대결<small>승리 시 2배 · 무승부 환불</small></div>
        <div style="display:flex; gap:4px;"><input type="number" id="diceBet" value="100" min="1" style="width:80px; background:var(--panel2); border:2px solid var(--line); color:var(--gold); text-align:center; font-family:inherit; padding:5px;"><button onclick="playDice()">굴리기</button></div></div>
      <h2 style="margin-top:10px;">🎁 무료 보상</h2>
      <div class="row"><div class="info">5분마다 무료 골드<small id="freeInfo"></small></div><button id="freeBtn" onclick="claimFree()">받기</button></div>
      <h2 style="margin-top:10px;">🧪 공격 물약</h2>
      <div class="row"><div class="info">공격력 +50% (5분 지속)<small id="potionInfo"></small></div><button id="potionBtn" class="gold-btn" onclick="buyPotion()"></button></div>
      <h2 style="margin-top:10px;">🕐 암시장 <span style="color:var(--mut); font-size:12px;">(1시간마다 목록 갱신)</span></h2>
      <div id="bmList"></div>
    </div>

    <div class="tabpage" id="tab-talent">
      <h2>🌳 특성 트리 <span style="color:var(--mut); font-size:12px;">(균열의 조각 소모 · 환생 유지)</span></h2>
      <div id="talentList"></div>
      <h2 style="margin-top:10px;">📖 무기 도감 <span id="collCnt" style="color:var(--mut); font-size:12px;"></span></h2>
      <div class="notice">새로운 종류의 무기를 획득할 때마다 모든 공격력 +1% 영구 상승</div>
      <h2 style="margin-top:10px;">🎖 숙련도 · 명성</h2>
      <div id="masteryInfo" style="font-size:12px; margin-bottom:8px; line-height:1.8;"></div>
      <h2>🏆 업적 (달성 시 자동 보상)</h2>
      <div id="achList" style="max-height:210px; overflow-y:auto;"></div>
    </div>

    <div class="tabpage" id="tab-set">
      <h2>⚙️ 설정</h2>
      <div class="row"><div class="info">효과음 (SFX)</div><button id="sfxBtn" onclick="togSet('sfx')"></button></div>
      <div class="row"><div class="info">배경음 (BGM)</div><button id="bgmBtn" onclick="togSet('bgm')"></button></div>
      <div class="row"><div class="info">화면 흔들림</div><button id="shakeBtn" onclick="togSet('shake')"></button></div>
      <div class="row"><div class="info">자동 판매 필터 <small>일반 등급 드랍은 즉시 골드로 환전</small></div><button id="autoSellBtn" onclick="togAutoSell()"></button></div>
      <div class="row"><div class="info">대미지 숫자 크기</div><div style="display:flex; gap:4px;"><button onclick="setDmgSize(0.8)">작게</button><button onclick="setDmgSize(1)">보통</button><button onclick="setDmgSize(1.5)">크게</button></div></div>
      <div class="row"><div class="info">대미지 색상</div><div style="display:flex; gap:4px;"><button onclick="setDmgColor('default')">기본</button><button onclick="setDmgColor('gold')">골드</button><button onclick="setDmgColor('cyan')">시안</button><button onclick="setDmgColor('red')">레드</button></div></div>
      <div class="row"><div class="info">테마</div><div style="display:flex; gap:4px;"><button onclick="applyTheme('purple');saveGame(true)">보라</button><button onclick="applyTheme('blue');saveGame(true)">네온블루</button><button onclick="applyTheme('green');saveGame(true)">레트로그린</button></div></div>
      <h2 style="margin-top:10px;">🤖 스마트 자동 강화</h2>
      <div class="row"><div class="info">골드가 바닥날 때까지 연속 강화</div><div style="display:flex; gap:4px;"><button class="gold-btn" onclick="smartUp('atk')">공격</button><button class="gold-btn" onclick="smartUp('def')">방어</button><button class="gold-btn" onclick="smartUp('crit')">치명</button></div></div>
      <h2 style="margin-top:10px;">🎒 가방 확장 <span id="bagTxt" style="color:var(--mut); font-size:12px;"></span></h2>
      <div class="row"><div class="info">인벤토리 +10칸 (최대 100칸)</div><button id="bagBtn" class="gold-btn" onclick="expandBag()"></button></div>
      <h2 style="margin-top:10px;">💾 세이브 백업</h2>
      <div class="row"><div class="info">텍스트 코드로 내보내기 / 가져오기<small>다른 컴퓨터에서 이어하기</small></div><div style="display:flex; gap:4px;"><button onclick="exportSave()">내보내기</button><button onclick="importSave()">가져오기</button></div></div>
      <h2 style="margin-top:10px;">📊 전투 통계</h2>
      <div id="statsDash" style="font-size:12px; line-height:1.9; border:1px dashed var(--line); padding:8px;"></div>
    </div>

    <div class="tabpage" id="tab-social">
      <h2>🪪 내 정보</h2>
      <div class="row">
        <div class="info">고유이름<small id="rankDisplay" style="color:var(--mut);"></small></div>
        <div style="display:flex; gap:4px;">
          <input type="text" id="nickInput" placeholder="2~15글자" maxlength="15" style="width:120px; background:var(--panel2); border:2px solid var(--line); color:var(--txt); padding:6px; font-family:inherit;">
          <button onclick="setNickname()">변경</button>
        </div>
      </div>
      <div class="row">
  <div style="border:2px solid var(--rift); padding:10px; margin:10px 0;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
      <b style="color:var(--cyan)">🌐 온라인</b>
      <span id="netBadge" style="font-size:11px;cursor:pointer" onclick="setServerUrl()">📴 오프라인</span>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
      <button class="buy" style="font-size:12px" onclick="showRankings()">🏆 랭킹</button>
      <button class="buy" style="font-size:12px" onclick="showOnlineGUI()">👥 접속자</button>
      <button class="buy" style="font-size:12px" onclick="showBossGUI()">🐉 월드보스</button>
      <button class="buy" style="font-size:12px" onclick="showMarketGUI()">🏪 거래소</button>
      <button class="buy" style="font-size:12px" onclick="showMailGUI()">📬 우편함</button>
      <button class="buy" style="font-size:12px" onclick="showGuildGUI()">🏰 길드</button>
    </div>
    <div id="worldBossBox" style="border-top:1px solid var(--line);padding-top:8px;margin-top:8px"></div>
  </div>
  </div>
<div class="info">🏆 전투력 랭킹 <small>내 순위와 상위 20명 확인</small></div><button onclick="showRankings()">랭킹 보기</button></div>
      <h2 style="margin-top:14px;">🌍 글로벌 채팅</h2>
      <div style="border:1px solid var(--line); background:var(--panel2); height:160px; overflow-y:auto; padding:8px; margin-bottom:8px; font-size:11px; line-height:1.6;" id="gChatLog"></div>
      <div style="display:flex; gap:4px;"><input type="text" id="gChatInput" placeholder="메시지 입력" style="flex:1; background:var(--panel2); border:2px solid var(--line); color:var(--txt); padding:6px; font-family:inherit;"><button onclick="sendGlobalChat()">전송</button></div>
      <h2 style="margin-top:12px;">🏰 길드</h2>
      <div id="guildJoinUI"><div class="row"><div class="info">길드 생성/가입</div></div><div class="row"><input type="text" id="guildNameInput" placeholder="길드명" style="flex:1; background:var(--panel2); border:2px solid var(--line); color:var(--txt); padding:6px; font-family:inherit;"><button onclick="createOrJoinGuild()">생성</button></div><div class="row"><button onclick="toggleGuildList()" style="width:100%;">다른 길드</button></div><div id="guildList" style="display:none; max-height:180px; overflow-y:auto;"></div></div>
      <div id="guildMemberUI" style="display:none;"><div class="row"><div class="info">현재 길드: <b id="curGuildName"></b> <small id="guildMemberCount"></small></div><button onclick="leaveGuild()" class="danger">탈퇴</button></div><div id="guildMembers" style="border:1px solid var(--line); padding:6px; margin:6px 0; font-size:11px; max-height:80px; overflow-y:auto;"></div><div style="border:1px solid var(--line); background:var(--panel2); height:100px; overflow-y:auto; padding:6px; margin-bottom:6px; font-size:10px; line-height:1.5;" id="guildChatLog"></div><div style="display:flex; gap:4px;"><input type="text" id="guildChatInput" placeholder="길드 메시지" style="flex:1; background:var(--panel2); border:2px solid var(--line); color:var(--txt); padding:4px; font-family:inherit; font-size:11px;"><button onclick="sendGuildChat()" style="padding:4px 8px;">전송</button></div></div>
    </div>
  </section>
</main>

<footer>자동 저장: 15초마다 · 오프라인 보상: 마지막 접속 시점 기준 자동 계산</footer>
</div>

<div id="adminPanel" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); z-index:20000; background:#1c0505; border:2px dashed #ff4545; padding:14px; width:min(560px, 94vw); max-height:88vh; overflow-y:auto; box-shadow:0 0 40px rgba(255,69,69,.5);">
  <button onclick="toggleDevConsole(false)" style="position:absolute; top:8px; right:10px; background:none; border:none; color:#ff4545; font-size:20px; cursor:pointer; padding:0 4px;">×</button>
  <div style="color:#ff4545; font-size:12px; margin-bottom:8px;">⚡ 코어 개발자 콘솔 (Shift+F12+Del · 내 고유이름을 입력하면 작동)</div>
  <div style="display:flex; gap:8px; flex-wrap:wrap;">
    <input id="admTarget" type="text" placeholder="이름 입력" style="flex:1; min-width:140px; background:#2d0b0b; border:1px solid #ff4545; color:var(--txt); padding:6px; font-family:inherit;">
    <button class="danger" onclick="executeAdminGift('gold')">💰 골드 +50,000</button>
    <button class="danger" onclick="executeAdminGift('stat')">✨ 스탯 +100</button>
  </div>

  <div style="margin-top:10px; border-top:1px dashed #ff4545; padding-top:10px;">
    <div style="color:#ffd23f; font-size:11px; margin-bottom:6px;">📦 온라인 플레이어에게 아이템 전송</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
      <input id="admItemTarget" type="text" placeholder="받는 사람 이름" style="background:#2d0b0b; border:1px solid #ff8a3a; color:var(--txt); padding:6px; font-family:inherit; font-size:12px;">
      <input id="admItemName" type="text" placeholder="아이템 이름 (예: 전설의 검)" style="background:#2d0b0b; border:1px solid #ff8a3a; color:var(--txt); padding:6px; font-family:inherit; font-size:12px;">
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px; margin-top:6px;">
      <select id="admItemGrade" style="background:#2d0b0b; border:1px solid #ff8a3a; color:var(--txt); padding:6px; font-family:inherit; font-size:12px;">
        <option value="normal">일반</option><option value="rare">고급</option><option value="epic">희귀</option>
        <option value="unique">영웅</option><option value="legend">전설</option><option value="myth">신화</option>
      </select>
      <input id="admItemQty" type="number" value="1" min="1" max="999" style="background:#2d0b0b; border:1px solid #ff8a3a; color:var(--gold); padding:6px; font-family:inherit; font-size:12px; text-align:center;">
      <button class="danger" style="font-size:11px; padding:6px;" onclick="executeAdminSendItem()">📤 전송</button>
    </div>
    <div style="margin-top:6px; font-size:10px; color:var(--mut);">온라인 플레이어에게 우편으로 즉시 전송합니다. 같은 server.py 에 연결돼 있어야 받습니다.</div>
  </div>

  <div id="devConsole" style="margin-top:10px; border-top:1px dashed #ff4545; padding-top:10px;">
    <div style="color:#ff8a3a; font-size:11px; margin-bottom:6px;">👑 명령어 입력 (고유이름이 "개발자"여야 작동 · /help)</div>
    <div style="display:flex; gap:6px;">
      <input id="devCmd" type="text" placeholder="/help" autocomplete="off"
        style="flex:1; background:#2d0b0b; border:1px solid #ff8a3a; color:#ffd23f; padding:6px; font-family:inherit; font-size:12px;"
        onkeydown="if(event.key==='Enter'){ runDevCommand(this.value); this.value=''; }">
      <button class="danger" onclick="const i=document.getElementById('devCmd'); runDevCommand(i.value); i.value='';">실행</button>
    </div>
    <div style="display:flex; gap:5px; flex-wrap:wrap; margin-top:8px;">
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devGiveGear()">⚔️ 무한 장비</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devSkipStage(1)">⏭️ 스테이지 +1</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devSkipStage(10)">⏭️ +10</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devLevelUp(10)">⬆️ 레벨 +10</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devLevelUp(100)">⬆️ +100</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devMaxStats()">✨ 스탯 강화</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="devGiveAllPets()">🐾 전체 펫</button>
      <button class="danger" style="font-size:11px; padding:4px 7px;" onclick="runDevCommand('/god')">👑 GOD</button>
    </div>
  </div>
</div>
<div id="modalBg"><div id="modal">
  <h3 id="modalTitle">오프라인 보상</h3>
  <div class="body" id="modalBody"></div>
  <button id="modalOk" class="buy" style="width:100%;">받기</button>
</div></div>

<div id="difficultyModal" style="position:fixed; inset:0; background:rgba(5,3,15,.95); display:flex; align-items:center; justify-content:center; z-index:100;">
  <div style="background:var(--panel); border:3px solid var(--rift); padding:30px; max-width:500px; width:90%; text-align:center;">
    <h2 style="color:var(--rift); margin-bottom:20px; font-size:24px;">⚔️ 난이도 선택</h2>
    <p style="color:var(--txt); margin-bottom:20px; font-size:14px;">게임 시작 시에만 선택할 수 있습니다</p>
    
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-bottom:20px;">
      <button onclick="setDifficulty('easy')" style="background:#1a3a1a; border:2px solid var(--green); color:var(--green); padding:15px; font-size:14px; cursor:pointer;">
        <div style="font-size:20px; margin-bottom:5px;">🟢</div>
        <b>쉬움</b><br>
        <small style="color:var(--mut);">HP 1.15배<br>ATK 1.10배</small>
      </button>
      <button onclick="setDifficulty('normal')" style="background:#2a2a1a; border:2px solid var(--gold); color:var(--gold); padding:15px; font-size:14px; cursor:pointer;">
        <div style="font-size:20px; margin-bottom:5px;">🟡</div>
        <b>보통</b><br>
        <small style="color:var(--mut);">HP 1.25배<br>ATK 1.20배</small>
      </button>
      <button onclick="setDifficulty('hard')" style="background:#3a1a1a; border:2px solid var(--red); color:var(--red); padding:15px; font-size:14px; cursor:pointer;">
        <div style="font-size:20px; margin-bottom:5px;">🔴</div>
        <b>어려움</b><br>
        <small style="color:var(--mut);">HP 1.35배<br>ATK 1.30배</small>
      </button>
    </div>
    
    <div style="background:var(--panel2); border:1px dashed var(--line); padding:10px; border-radius:4px; margin-top:15px;">
      <small style="color:var(--mut); line-height:1.6;">
        💡 난이도는 게임 시작 후 설정 탭에서 변경할 수 있습니다.<br>
        난이도를 올릴수록 더 많은 보상을 얻을 수 있습니다!
      </small>
    </div>
  </div>
</div>

  <div style="border:2px solid var(--cyan); padding:10px; margin:10px 0;">
    <b style="color:var(--cyan)">🔊 사운드</b>
    <div style="margin-top:8px;font-size:12px">
      <div style="display:flex;align-items:center;gap:8px;margin:6px 0">
        <span style="width:60px">마스터</span>
        <input type="range" id="volMaster" min="0" max="100" value="100" style="flex:1"
          oninput="Audio8.setVol('master', this.value/100); document.getElementById('volMasterV').textContent=this.value+'%'">
        <span id="volMasterV" style="width:38px;text-align:right;color:var(--gold)">100%</span>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin:6px 0">
        <span style="width:60px">효과음</span>
        <input type="range" id="volSfx" min="0" max="100" value="90" style="flex:1"
          oninput="Audio8.setVol('sfx', this.value/100); document.getElementById('volSfxV').textContent=this.value+'%'">
        <span id="volSfxV" style="width:38px;text-align:right;color:var(--gold)">90%</span>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin:6px 0">
        <span style="width:60px">배경음</span>
        <input type="range" id="volBgm" min="0" max="100" value="50" style="flex:1"
          oninput="Audio8.setVol('bgm', this.value/100); document.getElementById('volBgmV').textContent=this.value+'%'">
        <span id="volBgmV" style="width:38px;text-align:right;color:var(--gold)">50%</span>
      </div>
      <div style="display:flex;gap:6px;margin-top:8px">
        <button class="buy" style="flex:1;font-size:11px" onclick="toggleBGM()">🎵 배경음 켜기/끄기</button>
        <button class="buy" style="flex:1;font-size:11px" onclick="sfx('legend')">🔔 소리 테스트</button>
      </div>
    </div>
  </div>
<div id="autoSellSection" style="display:none;"></div>
  <script>
// ============================================================================
// 🎰 슬롯머신 (고퀄 도트 스타일 + 애니메이션)
// ============================================================================

const SLOT_SYMBOLS = [
  {icon:'7', name:'세븐', color:'#ff4757', payout:50},
  {icon:'💎', name:'다이아', color:'#43e6cf', payout:20},
  {icon:'🔔', name:'벨', color:'#ffd23f', payout:10},
  {icon:'🍒', name:'체리', color:'#ff6b9d', payout:5},
  {icon:'🍋', name:'레몬', color:'#f9ca24', payout:3},
  {icon:'⭐', name:'별', color:'#a29bfe', payout:2},
];

let slotState = {
  spinning: false,
  reels: [0, 0, 0],
  bet: 100,
  spinTimers: []
};

function openSlotMachine(){
  let slotDiv = document.getElementById('slotMachineModal');
  if(!slotDiv){
    slotDiv = document.createElement('div');
    slotDiv.id = 'slotMachineModal';
    document.body.appendChild(slotDiv);
  }
  
  slotDiv.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:9999;display:flex;align-items:center;justify-content:center;overflow-y:auto;';
  
  slotDiv.innerHTML = `
    <div style="background:linear-gradient(180deg,#2d1b4e 0%,#1a1a2e 100%);border:4px solid #ffd23f;padding:0;max-width:420px;width:95%;font-family:monospace;box-shadow:0 0 40px rgba(255,210,63,0.4), inset 0 0 20px rgba(0,0,0,0.5);image-rendering:pixelated;">
      
      <!-- 머신 상단 (네온 사인) -->
      <div style="background:linear-gradient(90deg,#e94560,#ffd23f,#e94560);padding:3px;">
        <div style="background:#1a1a2e;padding:12px;text-align:center;">
          <div id="slotTitle" style="font-size:22px;font-weight:bold;color:#ffd23f;text-shadow:0 0 10px #ffd23f, 2px 2px 0 #000;letter-spacing:4px;">🎰 LUCKY 777 🎰</div>
          <div style="display:flex;justify-content:center;gap:6px;margin-top:6px;" id="slotLights">
            ${Array(9).fill(0).map((_,i)=>`<div class="slot-light" style="width:8px;height:8px;background:${i%2?'#e94560':'#ffd23f'};border:1px solid #000;"></div>`).join('')}
          </div>
        </div>
      </div>
      
      <!-- 릴 화면 -->
      <div style="background:#0a0a15;padding:20px;border-top:3px solid #000;border-bottom:3px solid #000;">
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:#000;padding:10px;border:3px solid #444;box-shadow:inset 0 4px 12px rgba(0,0,0,0.9);">
          ${[0,1,2].map(i=>`
            <div style="background:linear-gradient(180deg,#ddd 0%,#fff 20%,#fff 80%,#ddd 100%);border:3px solid #333;height:110px;overflow:hidden;position:relative;">
              <div id="reel${i}" style="position:absolute;width:100%;transition:none;">
                ${SLOT_SYMBOLS.concat(SLOT_SYMBOLS).concat(SLOT_SYMBOLS).map(s=>`
                  <div style="height:110px;display:flex;align-items:center;justify-content:center;font-size:52px;text-shadow:2px 2px 0 rgba(0,0,0,0.2);">${s.icon}</div>
                `).join('')}
              </div>
              <!-- 상하 그라데이션 -->
              <div style="position:absolute;top:0;left:0;right:0;height:25px;background:linear-gradient(180deg,rgba(0,0,0,0.4),transparent);pointer-events:none;"></div>
              <div style="position:absolute;bottom:0;left:0;right:0;height:25px;background:linear-gradient(0deg,rgba(0,0,0,0.4),transparent);pointer-events:none;"></div>
            </div>
          `).join('')}
        </div>
        
        <!-- 당첨 라인 표시 -->
        <div id="slotResult" style="text-align:center;margin-top:12px;min-height:28px;font-size:14px;font-weight:bold;color:#ffd23f;"></div>
      </div>
      
      <!-- 코인 트레이 (당첨 시 코인 떨어지는 곳) -->
      <div id="coinTray" style="position:relative;height:40px;background:linear-gradient(180deg,#1a1a2e,#0a0a15);border-bottom:3px solid #000;overflow:hidden;">
        <div style="position:absolute;bottom:0;left:20%;right:20%;height:12px;background:#333;border:2px solid #555;border-bottom:none;border-radius:4px 4px 0 0;"></div>
      </div>
      
      <!-- 조작부 -->
      <div style="padding:15px;background:linear-gradient(180deg,#2d1b4e,#1a1a2e);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;background:#0a0a15;border:2px solid #444;padding:10px;">
          <div style="color:#43e6cf;font-size:12px;">💰 골드<br><span id="slotGold" style="font-size:16px;font-weight:bold;color:#ffd23f;">${(S.gold||0).toLocaleString()}</span></div>
          <div style="color:#43e6cf;font-size:12px;text-align:right;">🎲 베팅<br><span id="slotBet" style="font-size:16px;font-weight:bold;color:#ff6b9d;">${slotState.bet.toLocaleString()}</span></div>
        </div>
        
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:12px;">
          <button onclick="setSlotBet(100)" style="padding:8px;background:#16213e;color:#ffd23f;border:2px solid #ffd23f;cursor:pointer;font-weight:bold;font-family:monospace;">100</button>
          <button onclick="setSlotBet(500)" style="padding:8px;background:#16213e;color:#ffd23f;border:2px solid #ffd23f;cursor:pointer;font-weight:bold;font-family:monospace;">500</button>
          <button onclick="setSlotBet(1000)" style="padding:8px;background:#16213e;color:#ffd23f;border:2px solid #ffd23f;cursor:pointer;font-weight:bold;font-family:monospace;">1K</button>
          <button onclick="setSlotBet(5000)" style="padding:8px;background:#16213e;color:#ff6b9d;border:2px solid #ff6b9d;cursor:pointer;font-weight:bold;font-family:monospace;">5K</button>
        </div>
        
        <button id="spinBtn" onclick="spinSlot()" style="width:100%;padding:16px;background:linear-gradient(180deg,#e94560,#c23152);color:white;border:4px solid #000;cursor:pointer;font-weight:bold;font-size:18px;font-family:monospace;letter-spacing:3px;box-shadow:0 4px 0 #7a1f33;text-shadow:2px 2px 0 #000;">
          ▶ SPIN ◀
        </button>
        
        <button onclick="closeSlotMachine()" style="width:100%;padding:10px;background:#666;color:white;border:3px solid #000;cursor:pointer;font-weight:bold;font-family:monospace;margin-top:8px;">◄ 나가기</button>
        
        <!-- 배당표 -->
        <div style="margin-top:12px;background:#0a0a15;border:2px solid #444;padding:10px;font-size:11px;color:#aaa;">
          <div style="color:#ffd23f;font-weight:bold;margin-bottom:5px;">💰 배당표 (3개 일치)</div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:3px;">
            ${SLOT_SYMBOLS.map(s=>`<div>${s.icon} ×3 = <span style="color:#ffd23f;">×${s.payout}</span></div>`).join('')}
            <div style="grid-column:1/3;color:#43e6cf;margin-top:4px;">아무거나 2개 일치 = ×1.5</div>
          </div>
        </div>
      </div>
    </div>
  `;
  
  // 초기 릴 위치 설정
  [0,1,2].forEach(i=>{
    const reel = document.getElementById('reel'+i);
    if(reel) reel.style.transform = 'translateY(-' + (slotState.reels[i] * 110) + 'px)';
  });
  
  // 네온 라이트 애니메이션
  startSlotLights();
}

let slotLightInterval = null;
function startSlotLights(){
  if(slotLightInterval) clearInterval(slotLightInterval);
  let phase = 0;
  slotLightInterval = setInterval(()=>{
    const lights = document.querySelectorAll('.slot-light');
    if(!lights.length){ clearInterval(slotLightInterval); return; }
    lights.forEach((light, i)=>{
      light.style.background = ((i + phase) % 2) ? '#e94560' : '#ffd23f';
      light.style.boxShadow = ((i + phase) % 2) ? '0 0 6px #e94560' : '0 0 6px #ffd23f';
    });
    phase++;
  }, 400);
}

function setSlotBet(amount){
  if(slotState.spinning) return;
  slotState.bet = amount;
  const betEl = document.getElementById('slotBet');
  if(betEl) betEl.textContent = amount.toLocaleString();
}

function spinSlot(){
  if(slotState.spinning) return;
  
  if((S.gold||0) < slotState.bet){
    alert('골드가 부족합니다!');
    return;
  }
  
  S.gold -= slotState.bet;
  slotState.spinning = true;
  
  const spinBtn = document.getElementById('spinBtn');
  if(spinBtn){ spinBtn.style.opacity = '0.5'; spinBtn.textContent = '● ● ●'; }
  
  const resultEl = document.getElementById('slotResult');
  if(resultEl) resultEl.textContent = '';
  
  updateSlotGold();
  
  // 결과 미리 결정
  const results = [
    Math.floor(Math.random() * SLOT_SYMBOLS.length),
    Math.floor(Math.random() * SLOT_SYMBOLS.length),
    Math.floor(Math.random() * SLOT_SYMBOLS.length)
  ];
  
  // 잭팟 확률 보정 (5% 확률로 777)
  if(Math.random() < 0.05){
    results[0] = 0; results[1] = 0; results[2] = 0;
  }
  // 2개 일치 확률 보정 (15%)
  else if(Math.random() < 0.15){
    const sym = Math.floor(Math.random() * SLOT_SYMBOLS.length);
    results[0] = sym; results[1] = sym;
  }
  
  // 각 릴을 순차적으로 회전
  [0,1,2].forEach(i=>{
    spinReel(i, results[i], 1200 + i * 700);
  });
  
  // 모든 릴이 멈춘 후 결과 판정
  setTimeout(()=>{
    slotState.reels = results;
    slotState.spinning = false;
    if(spinBtn){ spinBtn.style.opacity = '1'; spinBtn.textContent = '▶ SPIN ◀'; }
    checkSlotResult(results);
  }, 1200 + 2 * 700 + 400);
}

function spinReel(reelIndex, finalSymbol, duration){
  const reel = document.getElementById('reel' + reelIndex);
  if(!reel) return;
  
  const symbolHeight = 110;
  const totalSymbols = SLOT_SYMBOLS.length;
  const startTime = Date.now();
  let velocity = 40; // 시작 속도
  let position = slotState.reels[reelIndex] * symbolHeight;
  
  function animate(){
    const elapsed = Date.now() - startTime;
    const progress = elapsed / duration;
    
    if(progress < 1){
      // 감속 커브
      if(progress > 0.7){
        velocity = Math.max(5, velocity * 0.95);
      }
      position += velocity;
      
      // 릴 순환
      const maxPos = totalSymbols * symbolHeight;
      const wrappedPos = position % maxPos;
      reel.style.transform = 'translateY(-' + wrappedPos + 'px)';
      
      requestAnimationFrame(animate);
    } else {
      // 최종 위치로 부드럽게 정착 (바운스 효과)
      const finalPos = finalSymbol * symbolHeight;
      reel.style.transition = 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
      reel.style.transform = 'translateY(-' + finalPos + 'px)';
      
      setTimeout(()=>{
        reel.style.transition = 'none';
      }, 350);
      
      // 정지 사운드 효과 (화면 흔들림)
      const modal = document.getElementById('slotMachineModal');
      if(modal && modal.firstElementChild){
        modal.firstElementChild.style.transform = 'translateY(2px)';
        setTimeout(()=>{ modal.firstElementChild.style.transform = 'translateY(0)'; }, 80);
      }
    }
  }
  
  requestAnimationFrame(animate);
}

function checkSlotResult(results){
  const [a, b, c] = results;
  const resultEl = document.getElementById('slotResult');
  let winAmount = 0;
  let message = '';
  
  if(a === b && b === c){
    // 3개 일치!
    const symbol = SLOT_SYMBOLS[a];
    winAmount = slotState.bet * symbol.payout;
    
    if(a === 0){
      // 🎉 777 잭팟!!
      message = '🎊 JACKPOT!! 777 🎊';
      triggerJackpotAnimation(winAmount);
    } else {
      message = '🎉 ' + symbol.icon + ' × 3 당첨! +' + winAmount.toLocaleString() + 'G';
      triggerCoinAnimation(Math.min(30, 10 + symbol.payout));
    }
  } else if(a === b || b === c || a === c){
    // 2개 일치
    winAmount = Math.floor(slotState.bet * 1.5);
    message = '✨ 2개 일치! +' + winAmount.toLocaleString() + 'G';
    triggerCoinAnimation(8);
  } else {
    message = '💨 꽝... 다시 도전!';
  }
  
  if(winAmount > 0){
    S.gold += winAmount;
    if(typeof log === 'function'){
      log('<span class="gold">🎰 슬롯머신 당첨! +' + winAmount.toLocaleString() + 'G</span>');
    }
    saveGame(true);
  }
  
  if(resultEl){
    resultEl.textContent = message;
    resultEl.style.animation = 'none';
    void resultEl.offsetWidth;
    resultEl.style.animation = winAmount > 0 ? 'slotWinPulse 0.5s ease 3' : 'none';
  }
  
  updateSlotGold();
}

function updateSlotGold(){
  const goldEl = document.getElementById('slotGold');
  if(goldEl) goldEl.textContent = (S.gold||0).toLocaleString();
}

// 💰 코인 떨어지는 애니메이션
function triggerCoinAnimation(coinCount){
  const tray = document.getElementById('coinTray');
  if(!tray) return;
  
  for(let i = 0; i < coinCount; i++){
    setTimeout(()=>{
      const coin = document.createElement('div');
      const startX = 10 + Math.random() * 80;
      coin.textContent = '🪙';
      coin.style.cssText = 'position:absolute;top:-20px;left:' + startX + '%;font-size:' + (14 + Math.random() * 8) + 'px;pointer-events:none;z-index:10;';
      tray.appendChild(coin);
      
      // 떨어지는 애니메이션
      const fallDuration = 400 + Math.random() * 300;
      const bounceHeight = 5 + Math.random() * 10;
      
      coin.animate([
        { top: '-20px', transform: 'rotate(0deg)' },
        { top: '22px', transform: 'rotate(' + (Math.random() > 0.5 ? 360 : -360) + 'deg)', offset: 0.7 },
        { top: (22 - bounceHeight) + 'px', offset: 0.85 },
        { top: '22px' }
      ], {
        duration: fallDuration,
        easing: 'cubic-bezier(0.5, 0, 1, 1)',
        fill: 'forwards'
      });
      
      // 잠시 후 사라짐
      setTimeout(()=>{
        coin.animate([{opacity: 1}, {opacity: 0}], {duration: 500, fill: 'forwards'});
        setTimeout(()=>coin.remove(), 500);
      }, fallDuration + 800);
    }, i * 60);
  }
}

// 🎊 잭팟 대박 애니메이션 (777)
function triggerJackpotAnimation(winAmount){
  // 1. 화면 전체 플래시
  const flash = document.createElement('div');
  flash.style.cssText = 'position:fixed;inset:0;background:#ffd23f;z-index:10001;pointer-events:none;opacity:0.8;';
  document.body.appendChild(flash);
  flash.animate([{opacity: 0.8}, {opacity: 0}], {duration: 600, fill: 'forwards'});
  setTimeout(()=>flash.remove(), 600);
  
  // 2. 대량 코인 애니메이션
  triggerCoinAnimation(50);
  
  // 3. 화면 전체에 코인 비 내리기
  for(let i = 0; i < 40; i++){
    setTimeout(()=>{
      const coin = document.createElement('div');
      const symbols = ['🪙', '💰', '✨', '💎'];
      coin.textContent = symbols[Math.floor(Math.random() * symbols.length)];
      const startX = Math.random() * 100;
      coin.style.cssText = 'position:fixed;top:-40px;left:' + startX + 'vw;font-size:' + (20 + Math.random() * 20) + 'px;pointer-events:none;z-index:10000;';
      document.body.appendChild(coin);
      
      coin.animate([
        { top: '-40px', transform: 'rotate(0deg)' },
        { top: '105vh', transform: 'rotate(' + (Math.random() * 720 - 360) + 'deg)' }
      ], {
        duration: 1500 + Math.random() * 1500,
        easing: 'cubic-bezier(0.4, 0, 1, 1)',
        fill: 'forwards'
      });
      
      setTimeout(()=>coin.remove(), 3200);
    }, i * 50);
  }
  
  // 4. 잭팟 텍스트 팝업
  const jackpotText = document.createElement('div');
  jackpotText.innerHTML = '<div style="font-size:48px;font-weight:bold;color:#ffd23f;text-shadow:0 0 20px #ffd23f, 3px 3px 0 #e94560, 6px 6px 0 #000;font-family:monospace;letter-spacing:6px;">JACKPOT!</div><div style="font-size:28px;color:#fff;text-shadow:2px 2px 0 #000;font-family:monospace;margin-top:10px;">+' + winAmount.toLocaleString() + 'G</div>';
  jackpotText.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);z-index:10002;pointer-events:none;text-align:center;';
  document.body.appendChild(jackpotText);
  
  jackpotText.animate([
    { transform: 'translate(-50%,-50%) scale(0) rotate(-10deg)' },
    { transform: 'translate(-50%,-50%) scale(1.3) rotate(3deg)', offset: 0.5 },
    { transform: 'translate(-50%,-50%) scale(1) rotate(0deg)', offset: 0.7 },
    { transform: 'translate(-50%,-50%) scale(1)', offset: 0.9 },
    { transform: 'translate(-50%,-50%) scale(0)', opacity: 0 }
  ], {
    duration: 3000,
    easing: 'ease-out',
    fill: 'forwards'
  });
  
  setTimeout(()=>jackpotText.remove(), 3000);
  
  // 5. 타이틀 반짝임
  const title = document.getElementById('slotTitle');
  if(title){
    title.style.animation = 'slotWinPulse 0.3s ease 10';
  }
}

function closeSlotMachine(){
  if(slotState.spinning) return;
  if(slotLightInterval) clearInterval(slotLightInterval);
  const slotDiv = document.getElementById('slotMachineModal');
  if(slotDiv) slotDiv.remove();
  saveGame(true);
  renderAll();
}


function startPokerGame(){
  console.log('포커 시작');
  pokerGame.active = true;
  pokerGame.chips = Math.max(10, Math.floor(S.gold / 100));
  pokerGame.playerChips = pokerGame.chips;
  pokerGame.dealerChips = pokerGame.chips;
  pokerGame.pot = 0;
  pokerGame.playerBet = 0;
  pokerGame.deck = createDeck();
  
  pokerGame.playerHand = [dealCard(), dealCard()];
  pokerGame.dealerHand = [dealCard(), {rank:'?', suit:'?'}];
  
  renderPokerGame();
}

function renderPokerGame(){
  let pokerDiv = document.getElementById('pokerGameModal');
  if(!pokerDiv) {
    pokerDiv = document.createElement('div');
    pokerDiv.id = 'pokerGameModal';
    document.body.appendChild(pokerDiv);
  }
  
  const cardHTML = (hand) => {
    if(!hand) return '';
    return hand.map(card => {
      if(card.rank === '?') {
        return '<div style="width:50px;height:70px;background:#ff6b9d;border:2px solid #000;display:flex;align-items:center;justify-content:center;font-weight:bold;color:white;font-family:monospace;">?</div>';
      }
      return '<div style="width:50px;height:70px;background:#fff;border:2px solid #000;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:bold;font-family:monospace;font-size:11px;color:black;"><span>' + card.rank + '</span><span>' + card.suit + '</span></div>';
    }).join('');
  };
  
  pokerDiv.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.8);z-index:9999;display:flex;align-items:center;justify-content:center;';
  
  pokerDiv.innerHTML = `
    <div style="background:linear-gradient(135deg, #0f3460, #16213e);border:4px solid #ffd23f;border-radius:0;padding:30px;max-width:500px;width:90%;color:white;font-family:monospace;">
      <h1 style="text-align:center;color:#ffd23f;margin-bottom:20px;">▓▓▓ 포커 게임 ▓▓▓</h1>
      
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 0;">
        <div style="background:#0f3460;border:3px solid #e94560;padding:15px;border-radius:0;text-align:center;">
          <div style="color:#e94560;font-weight:bold;margin-bottom:10px;">🤖 딜러</div>
          <div style="display:flex;gap:8px;justify-content:center;margin-bottom:10px;">
            ${cardHTML(pokerGame.dealerHand)}
          </div>
          <div style="color:#e94560;font-family:monospace;font-weight:bold;">💰 ${pokerGame.dealerChips}</div>
        </div>
        
        <div style="background:#0f3460;border:3px solid #43e6cf;padding:15px;border-radius:0;text-align:center;">
          <div style="color:#43e6cf;font-weight:bold;margin-bottom:10px;">🎮 플레이어</div>
          <div style="display:flex;gap:8px;justify-content:center;margin-bottom:10px;">
            ${cardHTML(pokerGame.playerHand)}
          </div>
          <div style="color:#43e6cf;font-family:monospace;font-weight:bold;">💰 ${pokerGame.playerChips}</div>
        </div>
      </div>
      
      <div style="background:#1a3a52;border:2px solid #ffd23f;padding:12px;margin:15px 0;text-align:center;font-size:16px;font-weight:bold;color:#ffd23f;border-radius:0;">
        🍲 냄비: ${pokerGame.pot} 칩
      </div>
      
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:15px 0;">
        <button onclick="openBettingUI()" style="padding:12px;background:#43e6cf;color:black;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;font-family:monospace;grid-column:1/3;">▶ 베팅</button>
        <button onclick="pokerCheck()" style="padding:12px;background:#ffd23f;color:black;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;font-family:monospace;">○ 체크</button>
        <button onclick="pokerFold()" style="padding:12px;background:#e94560;color:white;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;font-family:monospace;">✕ 폴드</button>
      </div>
      
      <button onclick="closePokerGame()" style="width:100%;padding:12px;background:#666;color:white;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;font-family:monospace;">◄ 종료</button>
    </div>
  `;
  
  console.log('포커 화면 렌더링 완료');
}

function openBettingUI(){
  if(pokerGame.playerChips <= 0) {
    alert('칩이 부족합니다');
    return;
  }
  
  const maxBet = pokerGame.playerChips;
  let selectedBet = 10;
  
  let bettingDiv = document.getElementById('bettingModal');
  if(!bettingDiv) {
    bettingDiv = document.createElement('div');
    bettingDiv.id = 'bettingModal';
    document.body.appendChild(bettingDiv);
  }
  
  bettingDiv.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:10000;display:flex;align-items:center;justify-content:center;';
  
  bettingDiv.innerHTML = `
    <div style="background:linear-gradient(135deg, #0f3460, #16213e);border:4px solid #ffd23f;border-radius:0;padding:20px;max-width:350px;width:90%;color:white;font-family:monospace;">
      <h2 style="text-align:center;color:#ffd23f;margin-bottom:15px;">베팅 금액 선택</h2>
      
      <div style="background:#1a3a52;border:2px solid #ffd23f;padding:15px;margin:15px 0;text-align:center;border-radius:0;">
        <div style="font-size:12px;color:#aaa;margin-bottom:8px;">💰 현재 보유: ${maxBet} 칩</div>
        <div style="font-size:20px;font-weight:bold;color:#ffd23f;">선택: <span id="betAmount">10</span> 칩</div>
      </div>
      
      <div style="margin:15px 0;">
        <input type="range" id="betSlider" min="1" max="${maxBet}" value="10" style="width:100%;cursor:pointer;" oninput="updateBetAmount(this.value)">
      </div>
      
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:15px 0;">
        <button onclick="selectBet(10, ${maxBet})" style="padding:10px;background:var(--gold);color:black;border:2px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">10</button>
        <button onclick="selectBet(25, ${maxBet})" style="padding:10px;background:var(--gold);color:black;border:2px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">25</button>
        <button onclick="selectBet(50, ${maxBet})" style="padding:10px;background:var(--gold);color:black;border:2px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">50</button>
        <button onclick="selectBet(${maxBet}, ${maxBet})" style="padding:10px;background:#e94560;color:white;border:2px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">ALL</button>
      </div>
      
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:15px 0;">
        <button onclick="closeBettingUI()" style="padding:12px;background:#666;color:white;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">취소</button>
        <button onclick="confirmBet()" style="padding:12px;background:#43e6cf;color:black;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">확인</button>
      </div>
    </div>
  `;
  
  console.log('베팅 UI 열음');
}

function updateBetAmount(value){
  document.getElementById('betAmount').textContent = value;
  pokerGame.playerBet = parseInt(value);
}

function selectBet(amount, maxBet){
  const actualAmount = Math.min(amount, maxBet);
  document.getElementById('betSlider').value = actualAmount;
  document.getElementById('betAmount').textContent = actualAmount;
  pokerGame.playerBet = actualAmount;
}

function closeBettingUI(){
  const bettingDiv = document.getElementById('bettingModal');
  if(bettingDiv) bettingDiv.remove();
}

function confirmBet(){
  const betAmount = pokerGame.playerBet || 10;
  
  if(betAmount > pokerGame.playerChips) {
    alert('칩이 부족합니다');
    return;
  }
  
  if(betAmount <= 0) {
    alert('1칩 이상 베팅해주세요');
    return;
  }
  
  closeBettingUI();
  pokerBet(betAmount);
}

function pokerBet(amount){
  pokerGame.playerChips -= amount;
  pokerGame.pot += amount;
  
  setTimeout(()=>{
    if(Math.random() > 0.3){
      const dealerAmount = Math.min(amount, pokerGame.dealerChips);
      pokerGame.dealerChips -= dealerAmount;
      pokerGame.pot += dealerAmount;
    } else {
      pokerGame.playerChips += pokerGame.pot;
      pokerGame.pot = 0;
      alert('🎉 딜러 폴드! 당신의 승리!');
      closePokerGame();
      return;
    }
    renderPokerGame();
  }, 500);
}

function pokerCheck(){
  setTimeout(()=>{
    const playerValue = getHandValue(pokerGame.playerHand);
    const dealerValue = getHandValue(pokerGame.dealerHand);
    
    let result = '';
    if(playerValue > dealerValue){
      pokerGame.playerChips += pokerGame.pot;
      result = '🎉 당신이 승리!';
    } else if(dealerValue > playerValue){
      pokerGame.dealerChips += pokerGame.pot;
      result = '💀 딜러 승리';
    } else {
      pokerGame.playerChips += Math.floor(pokerGame.pot / 2);
      pokerGame.dealerChips += Math.floor(pokerGame.pot / 2);
      result = '🤝 비김!';
    }
    
    pokerGame.pot = 0;
    alert(result);
    closePokerGame();
  }, 500);
}

function pokerFold(){
  pokerGame.dealerChips += pokerGame.pot;
  pokerGame.pot = 0;
  alert('📉 폴드했습니다');
  closePokerGame();
}

function closePokerGame(){
  pokerGame.active = false;
  const finalGold = pokerGame.playerChips * 100;
  S.gold = finalGold;
  
  const pokerDiv = document.getElementById('pokerGameModal');
  if(pokerDiv) pokerDiv.remove();
  
  const bettingDiv = document.getElementById('bettingModal');
  if(bettingDiv) bettingDiv.remove();
  
  if(typeof log === 'function'){
    log('<span class="gold">🃏 포커 종료! 최종: ' + finalGold.toLocaleString() + 'G</span>');
  }
  
  saveGame(true);
  renderAll();
  console.log('포커 종료');
}

function openPoker(){
  console.log('포커 열기');
  startPokerGame();
}









// ============================================================================
// 🌍 다국어 시스템
// ============================================================================

let currentLanguage = 'ko'; // ko, en

const LANG = {
  ko: {
    game_title: '차원 균열의 만물상',
    stats: '통계',
    equip: '장비',
    arts: '유물',
    shop: '상점',
    content: '콘텐츠',
    pet: '펫',
    chat: '채팅',
    settings: '설정',
    story: '스토리',
    quest: '퀘스트',
    talk: '대화',
    accept: '수락',
    decline: '거절',
    complete: '완료',
    reward: '보상',
    level: '레벨',
    exp: '경험치',
    gold: '골드',
    stage: '스테이지',
  },
  en: {
    game_title: 'Dimensional Rift Shop',
    stats: 'Stats',
    equip: 'Equipment',
    arts: 'Artifacts',
    shop: 'Shop',
    content: 'Content',
    pet: 'Pet',
    chat: 'Chat',
    settings: 'Settings',
    story: 'Story',
    quest: 'Quest',
    talk: 'Talk',
    accept: 'Accept',
    decline: 'Decline',
    complete: 'Complete',
    reward: 'Reward',
    level: 'Level',
    exp: 'EXP',
    gold: 'Gold',
    stage: 'Stage',
  }
};

function t(key){
  return LANG[currentLanguage][key] || key;
}

function changeLanguage(lang){
  currentLanguage = lang;
  storage.setItem('rift-language', lang);
  renderAll();
  if(typeof log === 'function'){
    log('<span class="c">🌍 언어 변경: ' + (lang === 'ko' ? '한국어' : 'English') + '</span>');
  }
}

function loadLanguage(){
  const saved = storage.getItem('rift-language');
  if(saved) currentLanguage = saved;
}


// ============================================================================
// 📖 스토리 & NPC 시스템
// ============================================================================

const NPCS = [
  {
    id: 'elder',
    name: '마을 노장',
    emoji: '👴',
    desc: '이 마을의 지혜로운 지도자',
    dialogue: [
      '안녕하게나. 낯선 이여.',
      '이 마을은 차원 균열로 인해 위험에 처해있네.',
      '강해지면 균열을 막을 수 있을 거야.',
    ],
    quests: ['prologue', 'stage5'],
  },
  {
    id: 'merchant',
    name: '상인',
    emoji: '🧑‍🍳',
    desc: '생활용품을 파는 상인',
    dialogue: [
      '우리 상점에 오셨네요!',
      '모든 물품이 저렴한 가격에 준비되어 있습니다.',
      '마음에 드는 것이 있으시면 말씀하세요.',
    ],
    quests: ['shop_unlock'],
  },
  {
    id: 'warrior',
    name: '전사',
    emoji: '⚔️',
    desc: '강한 전사 훈련사',
    dialogue: [
      '약해 보이는군.',
      '더 강해져야 한다!',
      '내가 너에게 기술을 가르쳐주지.',
    ],
    quests: ['combat_100'],
  },
  {
    id: 'mage',
    name: '마법사',
    emoji: '🧙',
    desc: '신비한 마법을 다루는 마법사',
    dialogue: [
      '마법의 신비로움을 느껴보시겠어요?',
      '유물의 힘은 대단하답니다.',
      '많은 유물을 모아보세요.',
    ],
    quests: ['artifact_5'],
  },
];

const QUESTS = {
  prologue: {
    id: 'prologue',
    name: '프롤로그: 시작',
    desc: '마을 노장을 만나 이야기를 들어보자',
    npc: 'elder',
    reward: {exp: 100, gold: 50},
    condition: ()=>true,
    completed: false,
  },
  stage5: {
    id: 'stage5',
    name: '5스테이지 달성',
    desc: '강해지기 위해 5스테이지까지 진행하자',
    npc: 'elder',
    reward: {exp: 500, gold: 300},
    condition: ()=>S.stage >= 5,
    completed: false,
  },
  shop_unlock: {
    id: 'shop_unlock',
    name: '상점 이용',
    desc: '상점에서 물건을 구매해보자',
    npc: 'merchant',
    reward: {exp: 200, gold: 100},
    condition: ()=>S.bm && S.bm.bought && Object.keys(S.bm.bought).length > 0,
    completed: false,
  },
  combat_100: {
    id: 'combat_100',
    name: '100번 공격',
    desc: '몬스터를 100번 공격하자',
    npc: 'warrior',
    reward: {exp: 800, gold: 400},
    condition: ()=>(S.stats.attacks || 0) >= 100,
    completed: false,
  },
  artifact_5: {
    id: 'artifact_5',
    name: '5개 유물 수집',
    desc: '5개의 유물을 수집하자',
    npc: 'mage',
    reward: {exp: 600, gold: 350},
    condition: ()=>Object.keys(S.artifacts || {}).length >= 5,
    completed: false,
  },
};

let storyProgress = 0; // 0: 프롤로그, 1: 성장, 2: 중반, 3: 후반

function initStory(){
  const saved = storage.getItem('rift-quests');
  if(saved) {
    try {
      Object.assign(QUESTS, JSON.parse(saved));
    } catch(e) {}
  }
  storage.setItem('rift-story-progress', storyProgress);
}

function saveQuests(){
  storage.setItem('rift-quests', JSON.stringify(QUESTS));
}

function getNPC(id){
  return NPCS.find(n=>n.id===id);
}

function openNPCDialog(npcId){
  const npc = getNPC(npcId);
  if(!npc) return;
  
  let html = `
    <div style="position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--panel);border:4px solid var(--rift);padding:20px;border-radius:0;max-width:400px;z-index:9999;font-family:monospace;">
      <div style="display:flex;align-items:center;gap:15px;margin-bottom:15px;">
        <div style="font-size:48px;">${npc.emoji}</div>
        <div>
          <div style="color:var(--cyan);font-weight:bold;font-size:16px;">${npc.name}</div>
          <div style="color:var(--mut);font-size:12px;">${npc.desc}</div>
        </div>
      </div>
      
      <div style="background:var(--panel2);border:2px solid var(--line);padding:15px;border-radius:0;margin:15px 0;min-height:80px;max-height:150px;overflow-y:auto;">
        ${npc.dialogue.map((line, i) => `<div style="color:var(--txt);margin:8px 0;line-height:1.4;">"${line}"</div>`).join('')}
      </div>
      
      <div style="margin:15px 0;">
        <div style="color:var(--cyan);font-weight:bold;margin-bottom:8px;">📋 관련 퀘스트</div>
        ${npc.quests.map(qid=>{
          const q = QUESTS[qid];
          if(!q) return '';
          const done = q.completed;
          const ready = q.condition();
          return `
            <div style="background:var(--panel2);padding:10px;margin:8px 0;border:2px solid ${done?'var(--gold)':ready?'var(--cyan)':'var(--line)'};border-radius:0;">
              <div style="font-weight:bold;color:${done?'var(--gold)':ready?'var(--cyan)':'var(--mut)'};">${q.name}</div>
              <div style="color:var(--mut);font-size:11px;margin:5px 0;">${q.desc}</div>
              <div style="display:flex;gap:8px;margin-top:8px;">
                ${!done ? (ready ? `<button onclick="completeQuest('${qid}')" style="flex:1;padding:8px;background:var(--gold);color:black;border:2px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">✓ 완료</button>` : `<button onclick="" style="flex:1;padding:8px;background:var(--panel2);color:var(--mut);border:2px solid var(--line);border-radius:0;cursor:pointer;">진행중</button>`) : `<button style="flex:1;padding:8px;background:var(--gold);color:black;border:2px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">✓ 완료됨</button>`}
              </div>
            </div>
          `;
        }).join('')}
      </div>
      
      <button onclick="closeNPCDialog()" style="width:100%;padding:12px;background:var(--rift);color:white;border:3px solid #000;border-radius:0;cursor:pointer;font-weight:bold;">닫기</button>
    </div>
    <div style="position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:9998;" onclick="closeNPCDialog()"></div>
  `;
  
  let dialogDiv = document.getElementById('npcDialog');
  if(!dialogDiv){
    dialogDiv = document.createElement('div');
    dialogDiv.id = 'npcDialog';
    document.body.appendChild(dialogDiv);
  }
  dialogDiv.innerHTML = html;
}

function closeNPCDialog(){
  const dialogDiv = document.getElementById('npcDialog');
  if(dialogDiv) dialogDiv.remove();
}

function completeQuest(questId){
  const quest = QUESTS[questId];
  if(!quest || quest.completed) return;
  
  if(!quest.condition()){
    alert('아직 조건을 충족하지 못했습니다');
    return;
  }
  
  quest.completed = true;
  S.exp += quest.reward.exp || 0;
  S.gold += quest.reward.gold || 0;
  
  saveQuests();
  saveGame(true);
  
  if(typeof log === 'function'){
    log('<span class="gold">✓ 퀘스트 완료! ' + quest.name + '</span>');
    log('<span class="green">경험치 +' + (quest.reward.exp || 0) + ', 골드 +' + (quest.reward.gold || 0) + '</span>');
  }
  
  openNPCDialog(quest.npc);
}


function renderStoryUI(){
  const storyDiv = document.getElementById('storySection');
  if(!storyDiv) return;
  
  let npcHtml = NPCS.map(npc=>{
    const questCount = npc.quests.length;
    const completedCount = npc.quests.filter(qid=>QUESTS[qid] && QUESTS[qid].completed).length;
    
    return `
      <div onclick="openNPCDialog('${npc.id}')" style="background:var(--panel2);border:3px solid var(--line);padding:15px;margin:10px 0;border-radius:0;cursor:pointer;transition:all 0.2s;hover:border-color:var(--rift);">
        <div style="display:flex;align-items:center;gap:15px;">
          <div style="font-size:40px;">${npc.emoji}</div>
          <div style="flex:1;">
            <div style="color:var(--cyan);font-weight:bold;">${npc.name}</div>
            <div style="color:var(--mut);font-size:12px;">${npc.desc}</div>
            <div style="color:var(--gold);font-size:11px;margin-top:5px;">퀘스트: ${completedCount}/${questCount}</div>
          </div>
          <div style="color:var(--cyan);font-size:14px;font-weight:bold;">▶</div>
        </div>
      </div>
    `;
  }).join('');
  
  storyDiv.innerHTML = `
    <div style="border:4px solid var(--rift);padding:15px;background:var(--panel);border-radius:0;margin:15px 0;">
      <div style="color:var(--rift);font-weight:bold;font-size:16px;margin-bottom:15px;">📖 스토리 & 퀘스트</div>
      ${npcHtml}
    </div>
  `;
}







function endPokerGame(){
  pokerGame.active = false;
  const finalGold = pokerGame.playerChips * 100;
  S.gold = finalGold;
  
  const pokerModal = document.getElementById('pokerModal');
  if(pokerModal) pokerModal.remove();
  
  if(typeof log === 'function'){
    log('<span class="gold">🃏 포커 종료! 최종: ' + finalGold.toLocaleString() + 'G</span>');
  }
  
  saveGame(true);
  renderAll();
}


// ============================================================================
// 🃏 포커 게임 시스템
// ============================================================================

let pokerGame = {
  active: false,
  chips: 0,
  playerChips: 0,
  dealerChips: 0,
  pot: 0,
  playerHand: [],
  dealerHand: [],
  communityCards: [],
  stage: 'betting', // betting, flop, turn, river, showdown
  playerBet: 0,
  dealerBet: 0,
  deck: []
};

const CARD_RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'];
const CARD_SUITS = ['♠','♥','♦','♣'];

function createDeck(){
  const deck = [];
  for(let suit of CARD_SUITS){
    for(let rank of CARD_RANKS){
      deck.push({rank, suit});
    }
  }
  return deck.sort(()=>Math.random()-0.5);
}

function dealCard(){
  if(pokerGame.deck.length === 0) pokerGame.deck = createDeck();
  return pokerGame.deck.pop();
}






function getHandValue(hand){
  let value = 0;
  for(let card of hand){
    if(card.rank === '?') continue;
    const rankIndex = CARD_RANKS.indexOf(card.rank);
    value += rankIndex + 2;
  }
  return value;
}


// localStorage 폴백 (Electron/특수 환경용)
const storage = (() => {
  let memStore = {};
  try {
    localStorage.setItem('test', '1');
    localStorage.removeItem('test');
    return localStorage;
  } catch(e) {
    console.log('localStorage 불가능, 메모리 저장소 사용');
    return {
      setItem: (k,v) => memStore[k] = v,
      getItem: (k) => memStore[k] || null,
      removeItem: (k) => delete memStore[k],
      clear: () => memStore = {}
    };
  }
})();

// ============================================================================
// 🗄️ IndexedDB 저장 시스템 (브라우저 DB — 새로고침/재시작해도 유지)
// localStorage보다 안전하고 용량이 큼. localStorage와 이중 저장.
// ============================================================================
const GameDB = (() => {
  const DB_NAME = 'RiftShopDB';
  const DB_VER = 1;
  const STORE = 'gamedata';
  let dbPromise = null;

  function open(){
    if(dbPromise) return dbPromise;
    dbPromise = new Promise((resolve, reject) => {
      if(!window.indexedDB){ reject(new Error('IndexedDB 미지원')); return; }
      const req = indexedDB.open(DB_NAME, DB_VER);
      req.onupgradeneeded = (e) => {
        const db = e.target.result;
        if(!db.objectStoreNames.contains(STORE)){
          db.createObjectStore(STORE);
        }
      };
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
    return dbPromise;
  }

  function tx(mode, fn){
    return open().then(db => new Promise((resolve, reject) => {
      const t = db.transaction(STORE, mode);
      const store = t.objectStore(STORE);
      const req = fn(store);
      t.oncomplete = () => resolve(req ? req.result : undefined);
      t.onerror = () => reject(t.error);
      t.onabort = () => reject(t.error);
    }));
  }

  return {
    set: (key, value) => tx('readwrite', s => s.put(value, key)),
    get: (key) => tx('readonly', s => s.get(key)),
    del: (key) => tx('readwrite', s => s.delete(key)),
    keys: () => tx('readonly', s => s.getAllKeys()),
    available: () => !!window.indexedDB,
  };
})();

// 게임이 저장하는 모든 키
const PERSIST_KEYS = [
  'rift-shop-save-v1', 'rift-shop-backup-v1', 'rift-last-save-time',
  'rift-chat-v2', 'rift-autosell', 'rift-language', 'rift-quests',
  'rift-story-progress', 'rift-rankings', 'rift-nicknames', 'rift-difficulty'
];

// storage.setItem을 가로채서 IndexedDB에도 동시 기록
(function hookStorageToDB(){
  if(!GameDB.available()) { console.log('⚠️ IndexedDB 미지원 — localStorage만 사용'); return; }
  const _set = storage.setItem.bind(storage);
  const _remove = storage.removeItem.bind(storage);
  storage.setItem = function(key, value){
    _set(key, value);
    GameDB.set(key, value).catch(e => console.error('DB 저장 실패:', key, e));
  };
  storage.removeItem = function(key){
    _remove(key);
    GameDB.del(key).catch(()=>{});
  };
  console.log('🗄️ IndexedDB 저장 활성화');
})();

// 게임 시작 시 DB → localStorage 복원 (새로고침/재접속 대응)
async function restoreFromDB(){
  if(!GameDB.available()) return 0;
  let restored = 0;
  for(const key of PERSIST_KEYS){
    try {
      const val = await GameDB.get(key);
      if(val !== undefined && val !== null && localStorage.getItem(key) === null){
        localStorage.setItem(key, val);
        restored++;
      }
    } catch(e) {}
  }
  if(restored > 0) console.log('🗄️ IndexedDB에서 ' + restored + '개 복원됨');
  return restored;
}


// ============================================================================
// 🖥️ Electron(EXE) 파일 저장 브릿지
// EXE로 실행 시: 모든 저장이 파일(AppData)에도 기록됨 → 나갔다 와도 유지
// 브라우저 실행 시: 기존 localStorage 그대로 사용
// ============================================================================
const IS_ELECTRON = !!(window.electronAPI && window.electronAPI.isElectron);

if(IS_ELECTRON){
  console.log('🖥️ Electron 모드: 파일 기반 저장 활성화');
  
  // storage(localStorage 래퍼)의 setItem/removeItem을 가로채서 파일에도 저장
  const _origSet = storage.setItem.bind(storage);
  const _origRemove = storage.removeItem.bind(storage);
  
  storage.setItem = function(key, value){
    _origSet(key, value);
    // 파일에도 비동기 기록 (실패해도 localStorage는 유지됨)
    window.electronAPI.storageSet(key, value).catch(e=>console.error('파일 저장 실패:', e));
  };
  
  storage.removeItem = function(key){
    _origRemove(key);
    window.electronAPI.storageRemove(key).catch(e=>console.error('파일 삭제 실패:', e));
  };
  
  // 앱 시작 시: 파일 저장소 → localStorage로 복원
  async function restoreFromFileStorage(){
    const keys = [
      'rift-shop-save-v1', 'rift-shop-backup-v1', 'rift-last-save-time',
      'rift-chat-v2', 'rift-autosell', 'rift-language', 'rift-quests',
      'rift-story-progress', 'rift-rankings', 'rift-nicknames', 'rift-difficulty'
    ];
    let restored = 0;
    for(const key of keys){
      try {
        const res = await window.electronAPI.storageGet(key);
        if(res && res.success && res.value !== null){
          // 파일 값이 있으면 localStorage보다 우선 (EXE 재설치 등에도 복원)
          const localVal = _origSet ? localStorage.getItem(key) : null;
          if(localVal === null || localVal === undefined){
            _origSet(key, res.value);
            restored++;
          }
        }
      } catch(e) {}
    }
    if(restored > 0){
      console.log('📂 파일에서 ' + restored + '개 데이터 복원됨');
    }
    
    // 메인 세이브 파일도 확인 (game-save.json)
    try {
      const res = await window.electronAPI.loadGame();
      if(res && res.success && res.data){
        const localSave = localStorage.getItem('rift-shop-save-v1');
        if(!localSave){
          _origSet('rift-shop-save-v1', res.data);
          console.log('📂 메인 세이브 파일에서 복원' + (res.fromBackup ? ' (백업)' : ''));
        }
      }
    } catch(e) {}
  }
  
  // 앱 종료 직전 강제 저장
  if(window.electronAPI.onAppClosing){
    window.electronAPI.onAppClosing(()=>{
      try {
        if(typeof S !== 'undefined' && S){
          const json = JSON.stringify(S);
          window.electronAPI.saveGame(json);
          console.log('🖥️ 종료 전 저장 완료');
        }
      } catch(e) {}
    });
  }
  
  window.restoreFromFileStorage = restoreFromFileStorage;
  
  // 게임 세이브를 파일에도 주기적으로 기록 (10초마다)
  setInterval(()=>{
    try {
      if(typeof S !== 'undefined' && S && S.nickname){
        window.electronAPI.saveGame(JSON.stringify(S)).catch(()=>{});
      }
    } catch(e) {}
  }, 10000);
}

// ============================================================================
// 🐍 Python(pywebview) 파일 저장 브릿지
// python run_game.py 로 실행 시: 파일 기반 영구 저장 (EXE 빌드 가능)
// ============================================================================
let IS_PYWEBVIEW = !!(window.pywebview && window.pywebview.api);

const PYWEBVIEW_READY = new Promise((resolve)=>{
  if(IS_PYWEBVIEW){ setupPyBridge(); resolve(true); return; }
  let settled = false;
  window.addEventListener('pywebviewready', ()=>{
    if(!settled){ settled = true; IS_PYWEBVIEW = true; setupPyBridge(); resolve(true); }
  });
  // 파이썬 환경이 아니면 0.8초 후 그냥 진행 (브라우저/Electron)
  setTimeout(()=>{ if(!settled){ settled = true; resolve(false); } }, 800);
});

function setupPyBridge(){
  console.log('🐍 Python 모드: 파일 기반 저장 활성화');
  const api = window.pywebview.api;
  
  // storage 쓰기를 가로채서 파이썬 파일에도 저장
  const _pySet = storage.setItem.bind(storage);
  const _pyRemove = storage.removeItem.bind(storage);
  
  storage.setItem = function(key, value){
    _pySet(key, value);
    try { api.storage_set(key, value); } catch(e) { console.error('py 저장 실패:', e); }
  };
  storage.removeItem = function(key){
    _pyRemove(key);
    try { api.storage_remove(key); } catch(e) {}
  };
  
  // 10초마다 메인 세이브를 파일에 기록
  setInterval(()=>{
    try {
      if(typeof S !== 'undefined' && S && S.nickname){
        api.save_game(JSON.stringify(S));
      }
    } catch(e) {}
  }, 10000);
  
  // 창 닫기 직전 강제 저장
  window.addEventListener('beforeunload', ()=>{
    try {
      if(typeof S !== 'undefined' && S){
        api.save_game(JSON.stringify(S));
      }
    } catch(e) {}
  });
}

async function restoreFromPyStorage(){
  if(!IS_PYWEBVIEW) return;
  const api = window.pywebview.api;
  const keys = [
    'rift-shop-save-v1', 'rift-shop-backup-v1', 'rift-last-save-time',
    'rift-chat-v2', 'rift-autosell', 'rift-language', 'rift-quests',
    'rift-story-progress', 'rift-rankings', 'rift-nicknames', 'rift-difficulty'
  ];
  let restored = 0;
  for(const key of keys){
    try {
      const res = await api.storage_get(key);
      if(res && res.success && res.value !== null && res.value !== undefined){
        if(localStorage.getItem(key) === null){
          localStorage.setItem(key, res.value);
          restored++;
        }
      }
    } catch(e) {}
  }
  if(restored > 0) console.log('🐍 파일에서 ' + restored + '개 데이터 복원됨');
  
  // 메인 세이브 파일 확인
  try {
    const res = await api.load_game();
    if(res && res.success && res.data){
      if(!localStorage.getItem('rift-shop-save-v1')){
        localStorage.setItem('rift-shop-save-v1', res.data);
        console.log('🐍 메인 세이브 파일에서 복원' + (res.fromBackup ? ' (백업)' : ''));
      }
    }
  } catch(e) {}
}



"use strict";


/* ---------- 🌐 소셜 시스템 (길드·채팅) ---------- */
const FIREBASE_CONFIG = null;
let gChat = [], guildChat = {}, guilds = {};

function esc(html){ return html.replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function guildSafe(n){ return n.replace(/[^a-zA-Z0-9가-힣_-]/g,'').slice(0,20); }

async function initSocial(){
  await loadChat();
  renderSocial();
  setInterval(()=>renderSocial(), 3000);
}

async function sendGlobalChat(){
  const inp = $('gChatInput');
  const msg = inp.value.trim();
  if(!msg || msg.length>100) return;
  inp.value = '';
  
  // 👑 / 로 시작하면 개발자 명령어로 처리 (채팅 전송 안 함)
  if(msg.startsWith('/')){
    runDevCommand(msg);
    return;
  }
  const entry = {nick: S.nickname||'비로그인', msg: esc(msg), t: Date.now()};
  if(NET.isOnline()){ NET.req('/chat/send', {nick:S.nickname||'익명', msg:msg, room:'global'}).then(()=>netSyncChat()); return; }
  gChat.push(entry);
  if(gChat.length>30) gChat.shift();
  renderSocial();
  saveChat();
}

async function createOrJoinGuild(){
  const inp = $('guildNameInput');
  let gn = inp.value.trim();
  if(gn.length<2 || gn.length>12) return;
  gn = guildSafe(gn);
  inp.value = '';
  if(!guilds[gn]) guilds[gn] = {members:{}};
  S.guild = gn;
  guilds[gn].members[S.nickname||'비로그인'] = Date.now();
  guildChat[gn] = guildChat[gn]||[];
  renderSocial();
  saveChat();
  log('<span class="c">🏰 길드 ['+gn+']에 참여했습니다!</span>');
}

function leaveGuild(){
  if(!S.guild) return;
  delete guilds[S.guild].members[S.nickname||'비로그인'];
  S.guild = null;
  renderSocial();
  saveChat();
  log('<span class="r">길드를 탈퇴했습니다.</span>');
}

async function sendGuildChat(){
  if(!S.guild) return;
  const inp = $('guildChatInput');
  const msg = inp.value.trim();
  if(!msg || msg.length>100) return;
  inp.value = '';
  
  if(msg.startsWith('/')){
    runDevCommand(msg);
    return;
  }
  guildChat[S.guild] = guildChat[S.guild]||[];
  if(NET.isOnline()){ NET.req('/chat/send', {nick:S.nickname||'익명', msg:msg, room:'guild:'+S.guild}).then(()=>netSyncChat()); return; }
  guildChat[S.guild].push({nick: S.nickname||'비로그인', msg: esc(msg), t: Date.now()});
  if(guildChat[S.guild].length>30) guildChat[S.guild].shift();
  renderSocial();
  saveChat();
}

function toggleGuildList(){
  const el = $('guildList');
  el.style.display = el.style.display==='none' ? 'block' : 'none';
  if(el.style.display==='block'){
    el.innerHTML = Object.keys(guilds).map(gn=>{
      const cnt = Object.keys(guilds[gn].members).length;
      const d = document.createElement('div');
      d.className='row';
      d.innerHTML = '<div class="info">'+gn+' <small>'+cnt+'명</small></div>';
      const b = document.createElement('button');
      b.textContent = '가입';
      b.onclick = ()=>{ S.guild=gn; guilds[gn].members[S.nickname||'비로그인']=Date.now(); renderSocial(); saveChat(); log('<span class="c">🏰 길드 가입!</span>'); };
      d.appendChild(b);
      return d;
    }).reduce((p,c)=>(p.appendChild(c),p), el) ? '' : (el.innerHTML='<div style="color:var(--mut); padding:8px; font-size:11px;">아직 길드가 없습니다.</div>');
  }
}

function renderSocial(){
  const gcl = $('gChatLog');
  if(!gcl) { console.log('⚠️ gChatLog 요소 없음'); } 
  if(gcl) { gcl.innerHTML = gChat.slice(-20).map(e=>'<div><b>'+esc(e.nick)+':</b> '+esc(e.msg)+'</div>').join(''); }
  if(S.guild){
    $('guildJoinUI').style.display = 'none';
    $('guildMemberUI').style.display = 'block';
    $('curGuildName').textContent = S.guild;
    $('guildMemberCount').textContent = '('+Object.keys(guilds[S.guild].members||{}).length+'명)';
    $('guildMembers').innerHTML = Object.keys(guilds[S.guild].members||{}).map(n=>'<div>● '+esc(n)+'</div>').join('');
    const gchatl = $('guildChatLog');
    if(gchatl) gchatl.innerHTML = (guildChat[S.guild]||[]).slice(-15).map(e=>'<div><b>'+esc(e.nick)+':</b> '+esc(e.msg)+'</div>').join('');
  } else {
    $('guildJoinUI').style.display = 'block';
    $('guildMemberUI').style.display = 'none';
  }
}


// ============================================================================
// 🌐 온라인 시스템 (서버 연동) — server.py 가 켜져 있으면 자동 연결
// ============================================================================
const NET = (() => {
  let base = null, online = false, lastErr = 0;

  function candidates(){
    const saved = (typeof storage!=='undefined' && storage.getItem('rift-server-url')) || '';
    const list = [];
    if(saved) list.push(saved.replace(/\/+$/,''));
    if(location.protocol === 'http:' || location.protocol === 'https:'){
      list.push(location.origin.replace(/\/+$/,''));
      list.push(location.protocol + '//' + location.hostname + ':8777');
    }
    list.push('http://127.0.0.1:8777');
    list.push('http://localhost:8777');
    return [...new Set(list)];
  }

  async function req(path, data){
    if(!base) return null;
    try{
      const res = await fetch(base + path, {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(data || {})
      });
      let payload = null;
      try{ payload = await res.json(); }catch(_e){}
      if(res.ok){
        online = true;
        return payload;
      }
      // 429 같은 서버 응답은 "서버 꺼짐"이 아니라 정상적인 거절 응답으로 취급
      if(res.status === 429){
        online = true;
        return payload || {ok:false, error:'rate_limited'};
      }
      throw new Error('http ' + res.status);
    }catch(e){
      online = false;
      if(Date.now() - lastErr > 30000){
        lastErr = Date.now();
        console.warn('서버 통신 실패:', e.message);
      }
      return null;
    }
  }

  async function connect(){
    for(const url of candidates()){
      try{
        const res = await fetch(url + '/ping', {method:'POST',
          headers:{'Content-Type':'application/json'}, body:'{}'});
        if(res.ok){
          const j = await res.json();
          if(j && j.server === 'rift'){
            base = url; online = true;
            try{ storage.setItem('rift-server-url', url); }catch(e){}
            console.log('🌐 온라인 서버 연결:', url);
            if(typeof log === 'function') log('<span class="g">🌐 온라인 서버 연결됨 — 채팅·랭킹·길드 사용 가능</span>');
            updateNetBadge();
            return true;
          }
        }
      }catch(e){}
    }
    online = false; base = null;
    console.log('⚠️ 오프라인 모드 (server.py 미실행)');
    updateNetBadge();
    return false;
  }

  return {
    connect, req,
    isOnline: () => online,
    getBase: () => base,
    setBase: (u) => { base = (u||'').replace(/\/+$/,''); try{storage.setItem('rift-server-url', base);}catch(e){} return connect(); },
  };
})();


// ============================================================================
// 🌐 온라인 부가 기능 5종
//   ① 접속자 목록  ② 월드보스 레이드  ③ 거래소  ④ 우편함  ⑤ 길드 랭킹
// ============================================================================

// ---------- ① 접속자 ----------
let onlinePlayers = [], onlineCount = 0;
async function netSyncOnline(){
  if(!NET.isOnline()) return;
  const r = await NET.req('/online', {});
  if(r && r.ok){
    onlinePlayers = r.players || [];
    onlineCount = r.count || 0;
    const el = document.getElementById('onlineList');
    if(el){
      el.innerHTML = '<div style="color:var(--cyan);margin-bottom:6px">👥 접속 중 ' + onlineCount + '명</div>' +
        (onlinePlayers.length ? onlinePlayers.map(p =>
          '<div style="font-size:11px;padding:2px 0">· ' + esc(p.nick) +
          ' <span style="color:var(--mut)">LV.' + p.level + ' · ' + p.stage + '층' +
          (p.guild ? ' · ' + esc(p.guild) : '') + '</span></div>').join('')
        : '<div style="color:var(--mut);font-size:11px">아무도 없습니다</div>');
    }
  }
}

// ---------- ② 월드보스 레이드 ----------
let worldBoss = null;
async function netSyncBoss(){
  if(!NET.isOnline()) return;
  const r = await NET.req('/boss/state', {});
  if(r && r.ok){
    worldBoss = r.boss;
    const el = document.getElementById('worldBossBox');
    if(el){
      const pct = safePct(worldBoss.hp, worldBoss.max_hp);
      el.innerHTML =
        '<div style="color:#ff5470;font-weight:bold">🐉 월드보스 · 시즌 ' + worldBoss.season + '</div>' +
        '<div style="font-size:12px;margin:4px 0">' + esc(worldBoss.name) + '</div>' +
        '<div style="background:#2a1020;height:14px;border:1px solid #ff5470">' +
        '<div style="background:linear-gradient(90deg,#ff5470,#ff8a3a);height:100%;width:' + pct + '%"></div></div>' +
        '<div style="font-size:11px;color:var(--mut);margin-top:3px">' + fmt(worldBoss.hp) + ' / ' + fmt(worldBoss.max_hp) + '</div>' +
        '<button class="buy" style="width:100%;margin-top:6px" onclick="attackWorldBoss()">⚔️ 공격 (내 전투력만큼 피해)</button>' +
        (r.top && r.top.length ?
          '<div style="margin-top:8px;font-size:11px"><div style="color:var(--gold)">🏆 기여도 TOP</div>' +
          r.top.slice(0,5).map((t,i) => '<div>' + (i+1) + '. ' + esc(t.nick) + ' — ' + fmt(t.dmg) + '</div>').join('') +
          '</div>' : '');
    }
  }
}
let bossAttackPending = false;
let bossAttackLastAt = 0;
async function attackWorldBoss(){
  if(!NET.isOnline()){ log('<span class="r">서버에 연결되어 있지 않습니다.</span>'); return; }
  if(!S || !S.nickname){ log('<span class="r">고유이름을 먼저 설정하세요.</span>'); return; }
  const nowTs = Date.now();
  if(bossAttackPending || nowTs - bossAttackLastAt < 120) return;
  bossAttackPending = true;
  bossAttackLastAt = nowTs;
  let dmg = playerATK();
  if(!isFinite(dmg)) dmg = 1e30;              // 개발자 무한 장비 상한 처리
  try{
    const r = await NET.req('/boss/hit', {nick:S.nickname, dmg:dmg});
    if(r && r.ok){
      log('<span class="p">🐉 월드보스에게 ' + fmt(dmg) + ' 피해!</span>');
      if(r.killed){
        log('<span class="gP">🎉 월드보스 처치! 시즌 ' + r.season + ' 개시 · 보상 우편 발송</span>');
        netSyncMail();
      }
      netSyncBoss();
    }else if(r && r.error === 'rate_limited'){
      log('<span class="y">🐉 공격이 너무 빠릅니다. 잠깐만 기다려 주세요.</span>');
    }
  } finally {
    bossAttackPending = false;
  }
}

// ---------- ③ 거래소 ----------
async function netMarketList(){
  if(!NET.isOnline()) return;
  const r = await NET.req('/market/list', {});
  const el = document.getElementById('marketList');
  if(!el) return;
  if(r && r.ok && r.items.length){
    el.innerHTML = r.items.map(it =>
      '<div style="border:1px solid var(--line);padding:6px;margin:4px 0;font-size:11px">' +
      '<b class="' + (GRADE_CLS[it.grade]||'') + '">' + esc(it.item) + '</b>' +
      ' <span style="color:var(--mut)">' + esc(it.seller) + '</span><br>' +
      '<span style="color:var(--gold)">' + fmt(it.price) + 'G</span> ' +
      '<button class="buy" style="float:right;padding:2px 8px" onclick="marketBuy(' + it.id + ')">구매</button></div>'
    ).join('');
  } else {
    el.innerHTML = '<div style="color:var(--mut);font-size:11px">매물이 없습니다</div>';
  }
}
async function marketSell(){
  if(!NET.isOnline()){ log('<span class="r">서버 미연결</span>'); return; }
  const e = eqById(S.weapon) || eqById(S.armor);
  if(!e){ log('<span class="r">장착 중인 장비가 없습니다.</span>'); return; }
  if(typeof isDevItem === 'function' && isDevItem(e)){ log('<span class="r">개발자 장비는 판매 불가</span>'); return; }
  const price = Math.max(1, Math.floor(eqPower(e) * 100));
  const r = await NET.req('/market/sell', {nick:S.nickname, item:e.name, grade:e.grade, price:price});
  if(r && r.ok){
    log('<span class="g">🏪 거래소 등록: ' + e.name + ' (' + fmt(price) + 'G)</span>');
    netMarketList();
  }
}
async function marketBuy(id){
  if(!NET.isOnline()) return;
  const r = await NET.req('/market/buy', {id:id, nick:S.nickname});
  if(r && r.ok){
    const it = r.item;
    if(S.gold < it.price){ log('<span class="r">골드가 부족합니다.</span>'); return; }
    S.gold -= it.price;
    S.equips.push({id:S.nextId++, type:'weapon', grade:it.grade||'Rare', name:it.item,
                   base: Math.max(1, Math.floor(it.price/100)), enh:0});
    log('<span class="g">🏪 구매 완료: ' + esc(it.item) + '</span>');
    renderAll(); saveGame(true); netMarketList();
  } else {
    log('<span class="r">이미 판매된 매물입니다.</span>');
    netMarketList();
  }
}

// ---------- ④ 우편함 ----------
async function netSyncMail(){
  if(!NET.isOnline() || !S || !S.nickname) return;
  const r = await NET.req('/mail/list', {nick:S.nickname});
  const el = document.getElementById('mailList');
  if(!el) return;
  if(r && r.ok && r.mails.length){
    el.innerHTML = '<div style="color:var(--gold);margin-bottom:4px">📬 우편 ' + r.mails.length + '통</div>' +
      r.mails.map(m =>
      '<div style="border:1px solid var(--line);padding:6px;margin:4px 0;font-size:11px">' +
      '<b>' + esc(m.subject) + '</b> <span style="color:var(--mut)">from ' + esc(m.sender) + '</span><br>' +
      esc(m.body||'') + (m.gold ? ' <span style="color:var(--gold)">+' + fmt(m.gold) + 'G</span>' : '') +
      ' <button class="buy" style="float:right;padding:2px 8px" onclick="mailTake(' + m.id + ')">받기</button></div>'
    ).join('');
  } else {
    el.innerHTML = '<div style="color:var(--mut);font-size:11px">우편이 없습니다</div>';
  }
}
async function mailTake(id){
  const r = await NET.req('/mail/take', {id:id, nick:S.nickname});
  if(r && r.ok){
    if(r.gold){ S.gold += r.gold; recGold(r.gold); }
    log('<span class="g">📬 우편 수령! +' + fmt(r.gold||0) + 'G</span>');
    renderAll(); saveGame(true); netSyncMail();
  }
}

// ---------- ⑤ 길드 랭킹 ----------
async function netGuildList(){
  if(!NET.isOnline()) return;
  const r = await NET.req('/guild/list', {});
  const el = document.getElementById('guildRankList');
  if(!el) return;
  if(r && r.ok && r.guilds.length){
    el.innerHTML = '<div style="color:var(--cyan);margin-bottom:4px">🏰 길드 랭킹</div>' +
      r.guilds.map((g,i) =>
      '<div style="font-size:11px;padding:3px 0;border-bottom:1px solid var(--line)">' +
      '<b style="color:var(--gold)">' + (i+1) + '위</b> ' + esc(g.name) +
      ' <span style="color:var(--mut)">' + g.members + '명 · ' + fmt(g.score) + '</span>' +
      ' <button class="buy" style="float:right;padding:1px 6px" onclick="guildJoin(\'' + esc(g.name).replace(/'/g,"\\'") + '\')">가입</button></div>'
    ).join('');
  } else {
    el.innerHTML = '<div style="color:var(--mut);font-size:11px">길드가 없습니다</div>';
  }
}
async function guildCreateNet(){
  const inp = document.getElementById('guildNameInput');
  const name = inp ? inp.value.trim() : '';
  if(!name){ log('<span class="r">길드명을 입력하세요.</span>'); return; }
  if(!NET.isOnline()){ log('<span class="r">서버 미연결</span>'); return; }
  const r = await NET.req('/guild/create', {name:name, nick:S.nickname});
  if(r && r.ok){ S.guild = name; log('<span class="g">🏰 길드 [' + esc(name) + '] 창설!</span>');
    if(inp) inp.value=''; saveGame(true); netGuildList(); }
  else log('<span class="r">이미 존재하는 길드명입니다.</span>');
}
async function guildJoin(name){
  if(!NET.isOnline()) return;
  const r = await NET.req('/guild/join', {name:name, nick:S.nickname});
  if(r && r.ok){ S.guild = name; log('<span class="g">🏰 [' + esc(name) + '] 길드 가입!</span>');
    saveGame(true); netGuildList(); }
}

// 서버 주소 수동 설정 (친구 PC 접속용)



// ============================================================================
// 🪟 공용 GUI 모달 (alert 대체)
// ============================================================================
let activeGuiKey = null;
let rankPollTimer = null;
function stopRankPoll(){
  if(rankPollTimer){ clearInterval(rankPollTimer); rankPollTimer = null; }
}
function openGUI(title, bodyHtml, opts){
  opts = opts || {};
  stopRankPoll();
  activeGuiKey = opts.key || null;
  let bg = document.getElementById('guiModalBg');
  if(!bg){
    bg = document.createElement('div');
    bg.id = 'guiModalBg';
    bg.style.cssText = 'position:fixed;inset:0;background:rgba(5,3,15,.88);z-index:12000;'+
      'display:flex;align-items:center;justify-content:center;padding:16px;';
    bg.addEventListener('click', e => { if(e.target === bg) closeGUI(); });
    document.body.appendChild(bg);
  }
  bg.innerHTML =
    '<div style="background:var(--panel);border:3px solid '+(opts.color||'var(--rift)')+';'+
    'width:min('+(opts.width||560)+'px,96vw);max-height:88vh;display:flex;flex-direction:column;'+
    'box-shadow:0 0 40px '+(opts.color||'rgba(168,107,255,.5)')+'">'+
      '<div style="display:flex;justify-content:space-between;align-items:center;'+
      'padding:12px 14px;border-bottom:2px solid var(--line);flex:0 0 auto">'+
        '<b style="color:'+(opts.color||'var(--cyan)')+';font-size:15px">'+title+'</b>'+
        '<button onclick="closeGUI()" style="background:none;border:none;color:var(--mut);'+
        'font-size:22px;cursor:pointer;padding:0 4px;line-height:1">×</button>'+
      '</div>'+
      '<div id="guiModalBody" style="padding:14px;overflow-y:auto;flex:1 1 auto">'+bodyHtml+'</div>'+
    '</div>';
  bg.style.display = 'flex';
  sfx('ui');
}
function closeGUI(){
  stopRankPoll();
  activeGuiKey = null;
  const bg = document.getElementById('guiModalBg');
  if(bg) bg.style.display = 'none';
  sfx('ui');
}
document.addEventListener('keydown', e => {
  if(e.key === 'Escape') closeGUI();
});

// ---------------- 🏆 랭킹 GUI ----------------
function renderRankRows(rows, online){
  const me = S ? S.nickname : '';
  let h = '<div style="font-size:11px;color:'+(online?'#43e6cf':'#888')+';margin-bottom:8px">'+
          (online ? '🌐 온라인 랭킹 · 전체 서버 (5초마다 자동 갱신)' : '📴 로컬 랭킹 (서버 미연결)')+'</div>';
  if(!rows.length){
    h += '<div style="color:var(--mut);text-align:center;padding:30px">기록이 없습니다</div>';
  } else {
    h += '<table style="width:100%;border-collapse:collapse;font-size:12px">'+
         '<tr style="color:var(--cyan);border-bottom:2px solid var(--line)">'+
         '<th style="text-align:left;padding:6px">순위</th><th style="text-align:left">이름</th>'+
         '<th style="text-align:right">전투력</th><th style="text-align:right">차원</th>'+
         '<th style="text-align:right">LV</th></tr>';
    rows.slice(0,50).forEach((r,i) => {
      const mine = r.nick === me;
      const medal = i===0?'🥇':i===1?'🥈':i===2?'🥉':(i+1)+'';
      h += '<tr style="border-bottom:1px solid var(--line);'+
           (mine?'background:rgba(255,210,63,.14)':'')+'">'+
           '<td style="padding:5px">'+medal+'</td>'+
           '<td style="'+(mine?'color:var(--gold);font-weight:bold':'')+'">'+esc(r.nick)+(mine?' (나)':'')+'</td>'+
           '<td style="text-align:right;color:var(--gold)">'+fmt(r.power)+'</td>'+
           '<td style="text-align:right;font-size:11px">'+(r.tier||'')+' '+(r.stage||1)+'</td>'+
           '<td style="text-align:right">'+(r.level||1)+'</td></tr>';
    });
    h += '</table>';
  }
  return h;
}

async function refreshRankings(){
  if(activeGuiKey !== 'rank') return;
  let rows = null, online = false;
  if(typeof NET !== 'undefined' && NET.isOnline()){
    rows = await netFetchRank(); online = !!rows;
  }
  if(!rows){
    try { rows = rankingSystem.getAll().map(r => ({...r, tier:''})); } catch(e){ rows = []; }
  }
  if(activeGuiKey !== 'rank') return; // 그 사이 다른 창으로 전환됐으면 반영하지 않음
  const b = document.getElementById('guiModalBody');
  if(b) b.innerHTML = renderRankRows(rows, online);
}

async function showRankings(){
  openGUI('🏆 랭킹', '<div style="color:var(--mut);text-align:center;padding:20px">불러오는 중...</div>',
          {color:'#ffd23f', width:640, key:'rank'});
  await refreshRankings();
  rankPollTimer = setInterval(refreshRankings, 5000);
}

// ---------------- 👥 접속자 GUI ----------------
async function showOnlineGUI(){
  openGUI('👥 접속자', '<div style="color:var(--mut);text-align:center;padding:20px">불러오는 중...</div>',
          {color:'#43e6cf'});
  await netSyncOnline();
  let h;
  if(!NET.isOnline()){
    h = '<div style="color:var(--mut);text-align:center;padding:24px">'+
        '서버에 연결되어 있지 않습니다.<br><br>'+
        '<button class="buy" onclick="closeGUI();setServerUrl()">서버 주소 설정</button></div>';
  } else if(!onlinePlayers.length){
    h = '<div style="color:var(--mut);text-align:center;padding:24px">접속 중인 플레이어가 없습니다</div>';
  } else {
    h = '<div style="color:var(--cyan);margin-bottom:8px">현재 '+onlineCount+'명 접속 중</div>'+
      onlinePlayers.map(p =>
      '<div style="display:flex;justify-content:space-between;padding:6px;border-bottom:1px solid var(--line);font-size:12px">'+
      '<span>'+esc(p.nick)+(p.guild?' <span style="color:var(--mut)">['+esc(p.guild)+']</span>':'')+'</span>'+
      '<span style="color:var(--mut)">LV.'+p.level+' · '+p.stage+'층</span></div>').join('');
  }
  const b = document.getElementById('guiModalBody'); if(b) b.innerHTML = h;
}

// ---------------- 🏰 길드 GUI ----------------
async function showGuildGUI(){
  openGUI('🏰 길드', '<div style="color:var(--mut);text-align:center;padding:20px">불러오는 중...</div>',
          {color:'#a86bff'});
  const r = (typeof NET!=='undefined' && NET.isOnline()) ? await NET.req('/guild/list', {}) : null;
  let h = '<div style="display:flex;gap:6px;margin-bottom:10px">'+
    '<input id="guiGuildName" placeholder="새 길드명" style="flex:1;background:var(--panel2);'+
    'border:1px solid var(--line);color:var(--txt);padding:6px;font-family:inherit;font-size:12px">'+
    '<button class="buy" onclick="guiCreateGuild()">창설</button></div>';
  if(!r || !r.ok){
    h += '<div style="color:var(--mut);text-align:center;padding:20px">서버 미연결</div>';
  } else if(!r.guilds.length){
    h += '<div style="color:var(--mut);text-align:center;padding:20px">길드가 없습니다</div>';
  } else {
    h += r.guilds.map((g,i) =>
      '<div style="display:flex;justify-content:space-between;align-items:center;'+
      'padding:8px;border-bottom:1px solid var(--line);font-size:12px">'+
      '<span><b style="color:var(--gold)">'+(i+1)+'위</b> '+esc(g.name)+
      '<br><span style="color:var(--mut);font-size:11px">'+g.members+'명 · 전투력 '+fmt(g.score)+'</span></span>'+
      '<button class="buy" style="padding:3px 10px" onclick="guiJoinGuild(\''+esc(g.name).replace(/'/g,"\\'")+'\')">가입</button></div>'
    ).join('');
  }
  const b = document.getElementById('guiModalBody'); if(b) b.innerHTML = h;
}
async function guiCreateGuild(){
  const i = document.getElementById('guiGuildName');
  const n = i ? i.value.trim() : '';
  if(!n){ sfx('error'); return; }
  if(!NET.isOnline()){ log('<span class="r">서버 미연결</span>'); sfx('error'); return; }
  const r = await NET.req('/guild/create', {name:n, nick:S.nickname});
  if(r && r.ok){ S.guild = n; sfx('buy'); log('<span class="g">🏰 길드 ['+esc(n)+'] 창설!</span>');
                 saveGame(true); showGuildGUI(); }
  else { sfx('error'); log('<span class="r">이미 존재하는 길드명입니다.</span>'); }
}
async function guiJoinGuild(n){
  if(!NET.isOnline()) return;
  const r = await NET.req('/guild/join', {name:n, nick:S.nickname});
  if(r && r.ok){ S.guild = n; sfx('buy'); log('<span class="g">🏰 ['+esc(n)+'] 가입!</span>');
                 saveGame(true); showGuildGUI(); }
}

// ---------------- 📬 우편 GUI ----------------
async function showMailGUI(){
  openGUI('📬 우편함', '<div style="color:var(--mut);text-align:center;padding:20px">불러오는 중...</div>',
          {color:'#ffd23f'});
  const r = (typeof NET!=='undefined' && NET.isOnline() && S && S.nickname)
            ? await NET.req('/mail/list', {nick:S.nickname}) : null;
  let h;
  if(!r || !r.ok){ h = '<div style="color:var(--mut);text-align:center;padding:20px">서버 미연결</div>'; }
  else if(!r.mails.length){ h = '<div style="color:var(--mut);text-align:center;padding:20px">우편이 없습니다</div>'; }
  else {
    h = '<button class="buy" style="width:100%;margin-bottom:8px" onclick="guiTakeAllMail()">📥 전체 수령</button>' +
      r.mails.map(m =>
      '<div style="border:1px solid var(--line);padding:8px;margin:5px 0;font-size:12px">'+
      '<b>'+esc(m.subject)+'</b> <span style="color:var(--mut);font-size:11px">from '+esc(m.sender)+'</span><br>'+
      '<span style="color:var(--mut);font-size:11px">'+esc(m.body||'')+'</span> '+
      (m.gold?'<span style="color:var(--gold)">+'+fmt(m.gold)+'G</span> ':'')+
      '<button class="buy" style="float:right;padding:2px 10px" onclick="guiTakeMail('+m.id+')">받기</button></div>'
      ).join('');
  }
  const b = document.getElementById('guiModalBody'); if(b) b.innerHTML = h;
}
async function guiTakeMail(id){
  const r = await NET.req('/mail/take', {id:id, nick:S.nickname});
  if(r && r.ok){
    if(r.gold){ S.gold += r.gold; recGold(r.gold); }
    sfx('gold'); log('<span class="g">📬 수령! +'+fmt(r.gold||0)+'G</span>');
    renderAll(); saveGame(true); showMailGUI();
  }
}
async function guiTakeAllMail(){
  const r = await NET.req('/mail/list', {nick:S.nickname});
  if(!r || !r.ok) return;
  let total = 0;
  for(const m of r.mails){
    const t = await NET.req('/mail/take', {id:m.id, nick:S.nickname});
    if(t && t.ok && t.gold) total += t.gold;
  }
  if(total){ S.gold += total; recGold(total); }
  sfx('levelup'); log('<span class="g">📬 전체 수령! +'+fmt(total)+'G</span>');
  renderAll(); saveGame(true); showMailGUI();
}

// ---------------- 🐉 월드보스 GUI ----------------
async function showBossGUI(){
  openGUI('🐉 월드보스', '<div style="color:var(--mut);text-align:center;padding:20px">불러오는 중...</div>',
          {color:'#ff5470'});
  const r = (typeof NET!=='undefined' && NET.isOnline()) ? await NET.req('/boss/state', {}) : null;
  let h;
  if(!r || !r.ok){ h = '<div style="color:var(--mut);text-align:center;padding:20px">서버 미연결</div>'; }
  else {
    const b = r.boss, pct = safePct(b.hp, b.max_hp);
    h = '<div style="text-align:center;margin-bottom:10px">'+
        '<div style="font-size:15px;color:#ff5470;font-weight:bold">'+esc(b.name)+'</div>'+
        '<div style="font-size:11px;color:var(--mut)">시즌 '+b.season+'</div></div>'+
        '<div style="background:#2a1020;height:22px;border:2px solid #ff5470;margin:8px 0">'+
        '<div style="background:linear-gradient(90deg,#ff5470,#ff8a3a);height:100%;width:'+pct+'%"></div></div>'+
        '<div style="text-align:center;font-size:12px;margin-bottom:10px">'+fmt(b.hp)+' / '+fmt(b.max_hp)+'</div>'+
        '<button class="buy" style="width:100%;padding:10px" onclick="attackWorldBoss().then(showBossGUI)">⚔️ 공격</button>';
    if(r.top && r.top.length){
      h += '<div style="margin-top:12px;color:var(--gold);font-size:12px">🏆 기여도 랭킹</div>'+
        r.top.map((t,i)=>'<div style="display:flex;justify-content:space-between;font-size:12px;'+
        'padding:4px;border-bottom:1px solid var(--line)"><span>'+(i+1)+'. '+esc(t.nick)+
        '</span><span style="color:var(--gold)">'+fmt(t.dmg)+'</span></div>').join('');
    }
  }
  const b2 = document.getElementById('guiModalBody'); if(b2) b2.innerHTML = h;
}

// ---------------- 🏪 거래소 GUI ----------------
async function showMarketGUI(){
  openGUI('🏪 거래소', '<div style="color:var(--mut);text-align:center;padding:20px">불러오는 중...</div>',
          {color:'#43e6cf', width:600});
  const r = (typeof NET!=='undefined' && NET.isOnline()) ? await NET.req('/market/list', {}) : null;
  let h = '<button class="buy" style="width:100%;margin-bottom:10px" onclick="marketSell().then(showMarketGUI)">'+
          '📤 장착 중인 장비 등록</button>';
  if(!r || !r.ok){ h += '<div style="color:var(--mut);text-align:center;padding:20px">서버 미연결</div>'; }
  else if(!r.items.length){ h += '<div style="color:var(--mut);text-align:center;padding:20px">매물이 없습니다</div>'; }
  else {
    h += r.items.map(it =>
      '<div style="display:flex;justify-content:space-between;align-items:center;'+
      'border:1px solid var(--line);padding:8px;margin:5px 0;font-size:12px">'+
      '<span><b class="'+(GRADE_CLS[it.grade]||'')+'">'+esc(it.item)+'</b>'+
      '<br><span style="color:var(--mut);font-size:11px">판매자 '+esc(it.seller)+'</span></span>'+
      '<span style="text-align:right"><span style="color:var(--gold)">'+fmt(it.price)+'G</span><br>'+
      '<button class="buy" style="padding:2px 10px;margin-top:3px" onclick="marketBuy('+it.id+').then(showMarketGUI)">구매</button>'+
      '</span></div>').join('');
  }
  const b = document.getElementById('guiModalBody'); if(b) b.innerHTML = h;
}


// ============================================================================
// 👗 스킨 시스템 (상점 뽑기) + 🗡️ 장비 외형 반영
// ============================================================================
const SKINS = [
  {id:'wizard',    name:'견습 마법사', grade:'Normal',     spr:'wizard',    pal:'wizard',    desc:'기본 외형'},
  {id:'sk_knight', name:'강철 기사',   grade:'Rare',       spr:'sk_knight', pal:'sk_knight', desc:'은빛 판금 갑주'},
  {id:'sk_ninja',  name:'그림자 닌자', grade:'Epic',       spr:'sk_ninja',  pal:'sk_ninja',  desc:'어둠에 스며든 자'},
  {id:'sk_mage',   name:'대마법사',    grade:'Unique',     spr:'sk_mage',   pal:'sk_mage',   desc:'심연의 마력'},
  {id:'sk_demon',  name:'마족 군주',   grade:'Legendary',  spr:'sk_demon',  pal:'sk_demon',  desc:'뿔과 화염의 화신'},
  {id:'sk_angel',  name:'천상의 사자', grade:'Mythic',     spr:'sk_angel',  pal:'sk_angel',  desc:'빛나는 날개'},
  {id:'sk_king',   name:'만물의 왕',   grade:'Primordial', spr:'sk_king',   pal:'sk_king',   desc:'모든 차원의 지배자'},
];
const SKIN_WEIGHT = {Normal:1000, Rare:400, Epic:150, Unique:50, Legendary:15, Mythic:4, Primordial:1};
const SKIN_COST = 30;   // 균열의 조각

function ownedSkins(){ return (S && S.skins) ? S.skins : {}; }
function curSkin(){
  const id = (S && S.skin) || 'wizard';
  return SKINS.find(s => s.id === id) || SKINS[0];
}

function rollSkin(){
  let total = 0;
  const w = SKINS.map(s => { const v = SKIN_WEIGHT[s.grade] || 1; total += v; return v; });
  let r = Math.random() * total;
  for(let i=0;i<SKINS.length;i++){ r -= w[i]; if(r <= 0) return SKINS[i]; }
  return SKINS[0];
}

function gachaSkin(){
  if(!S){ return; }
  if((S.shards||0) < SKIN_COST){
    sfx('error');
    log('<span class="r">균열의 조각이 부족합니다 (' + (S.shards||0) + '/' + SKIN_COST + ')</span>');
    return;
  }
  S.shards -= SKIN_COST;
  sfx('gacha');
  const got = rollSkin();
  if(!S.skins) S.skins = {};
  const dup = !!S.skins[got.id];
  S.skins[got.id] = true;

  setTimeout(() => {
    const gi = GRADES.indexOf(got.grade);
    sfx(gi >= 4 ? 'legend' : 'enhance');
    const col = GRADE_COLOR[got.grade] || '#fff';
    log('<span style="color:' + col + ';font-weight:bold">👗 [' + (GRADE_KO[got.grade]||got.grade) + '] ' +
        got.name + (dup ? ' (중복 → 조각 10 환급)' : ' 획득!') + '</span>');
    if(dup) S.shards += 10;
    else S.skin = got.id;   // 새 스킨은 자동 장착
    renderAll(); saveGame(true);
    if(document.getElementById('guiModalBody')) showSkinGUI();
  }, 520);
}

function equipSkin(id){
  if(!S.skins || !S.skins[id]){ if(id !== 'wizard'){ sfx('error'); return; } }
  S.skin = id; sfx('buy');
  log('<span class="g">👗 스킨 변경: ' + (SKINS.find(s=>s.id===id)||{}).name + '</span>');
  renderAll(); saveGame(true); showSkinGUI();
}

// ---------- 스킨 상점 GUI ----------
function showSkinGUI(){
  const owned = ownedSkins();
  let h = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">'+
    '<span style="font-size:12px">보유 조각 <b style="color:var(--gold)">'+(S.shards||0)+'</b></span>'+
    '<button class="buy" onclick="gachaSkin()">🎲 스킨 뽑기 ('+SKIN_COST+' 조각)</button></div>'+
    '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:8px">';
  SKINS.forEach(s => {
    const has = s.id === 'wizard' || !!owned[s.id];
    const on = (S.skin||'wizard') === s.id;
    const col = GRADE_COLOR[s.grade] || '#fff';
    h += '<div style="border:2px solid '+(on?col:'var(--line)')+';padding:8px;text-align:center;'+
      'background:'+(on?'rgba(255,255,255,.06)':'transparent')+';'+(has?'':'opacity:.35')+'">'+
      '<canvas class="skinPrev" data-spr="'+s.spr+'" data-pal="'+s.pal+'" width="60" height="70" '+
      'style="image-rendering:pixelated;width:60px;height:70px"></canvas>'+
      '<div style="font-size:11px;color:'+col+';font-weight:bold;margin-top:4px">'+s.name+'</div>'+
      '<div style="font-size:10px;color:var(--mut)">'+(GRADE_KO[s.grade]||s.grade)+'</div>'+
      (has ? (on ? '<div style="font-size:10px;color:var(--gold);margin-top:4px">✔ 장착 중</div>'
                 : '<button class="buy" style="width:100%;margin-top:4px;padding:2px;font-size:10px" '+
                   'onclick="equipSkin(\''+s.id+'\')">장착</button>')
           : '<div style="font-size:10px;color:var(--mut);margin-top:4px">미보유</div>')+
      '</div>';
  });
  h += '</div>';
  openGUI('👗 스킨 상점', h, {color:'#a86bff', width:600});
  setTimeout(drawSkinPreviews, 30);
}

function drawSkinPreviews(){
  document.querySelectorAll('.skinPrev').forEach(cv => {
    const sp = SPR[cv.dataset.spr], pl = PAL[cv.dataset.pal];
    if(!sp || !pl) return;
    const c = cv.getContext('2d');
    c.clearRect(0,0,cv.width,cv.height);
    const rows = sp[0], px = 5;
    const ox = (cv.width - 12*px)/2, oy = 2;
    rows.forEach((row,y)=>{
      for(let x=0;x<row.length;x++){
        const ch = row[x];
        if(ch !== '.' && pl[ch]){ c.fillStyle = pl[ch]; c.fillRect(ox+x*px, oy+y*px, px, px); }
      }
    });
  });
}

// ---------- 🗡️ 장비 외형 매핑 ----------
function weaponSprOf(e){
  if(!e) return null;
  const n = e.name || '';
  if(/도끼|망치|퇴/.test(n)) return 'wp_axe';
  if(/지팡이|홀/.test(n))    return 'wp_staff';
  if(/서$|마도서|금서/.test(n)) return 'wp_book';
  if(/활|궁/.test(n))        return 'wp_bow';
  if(/창|폴암|미늘/.test(n)) return 'wp_spear';
  return 'wp_sword';
}
function weaponPalOf(e){
  if(!e) return 'wp_common';
  if(e.dev || e.grade === 'Developer') return 'wp_dev';
  const m = {Normal:'wp_common', Rare:'wp_rare', Epic:'wp_epic', Unique:'wp_unique',
             Legendary:'wp_legend', Mythic:'wp_mythic', Celestial:'wp_celestial',
             Primordial:'wp_primordial'};
  return m[e.grade] || 'wp_common';
}
// 방어구 등급에 따라 스킨 몸통 색을 덧입힘
function armorTintOf(e){
  if(!e) return null;
  if(e.dev || e.grade === 'Developer') return '#ff2d95';
  return GRADE_COLOR[e.grade] || null;
}


// ---------- 🌐 서버 연결 GUI (EXE는 콘솔이 없어 여기서 주소 확인) ----------
async function setServerUrl(){
  let mine = null;
  if(window.pywebview && window.pywebview.api && window.pywebview.api.get_server_info){
    try{ const r = await window.pywebview.api.get_server_info(); if(r && r.success) mine = r.info; }catch(e){}
  }
  const cur = NET.getBase() || '';
  let h = '<div style="font-size:12px;margin-bottom:10px">'+
    '현재 상태: <b style="color:'+(NET.isOnline()?'#43e6cf':'#888')+'">'+
    (NET.isOnline() ? '🌐 온라인 · '+esc(cur) : '📴 오프라인')+'</b></div>';

  if(mine && mine.running){
    h += '<div style="border:2px solid var(--gold);padding:10px;margin-bottom:10px">'+
      '<div style="color:var(--gold);font-weight:bold;margin-bottom:6px">📡 내 PC에서 서버가 실행 중입니다</div>'+
      '<div style="font-size:12px;margin-bottom:4px">친구에게 아래 주소를 알려주세요:</div>'+
      '<div style="background:var(--panel2);padding:8px;font-size:14px;color:var(--cyan);'+
      'text-align:center;user-select:all;border:1px solid var(--line)">'+esc(mine.lan_url)+'</div>'+
      '<div style="font-size:11px;color:var(--mut);margin-top:6px">'+
      '※ 같은 와이파이일 때 접속됩니다. 인터넷으로 열려면 공유기 포트포워딩(8777)이 필요합니다.</div></div>';
  }

  h += '<div style="font-size:12px;margin-bottom:6px">다른 서버에 접속하기</div>'+
    '<div style="display:flex;gap:6px">'+
    '<input id="srvUrlInput" value="'+esc(cur||'http://127.0.0.1:8777')+'" '+
    'style="flex:1;background:var(--panel2);border:1px solid var(--line);color:var(--txt);'+
    'padding:8px;font-family:inherit;font-size:12px">'+
    '<button class="buy" onclick="applyServerUrl()">접속</button></div>'+
    '<div style="font-size:11px;color:var(--mut);margin-top:8px">'+
    '예) http://192.168.0.5:8777 (친구 PC) · http://내서버IP:8777 (VM)</div>';

  openGUI('🌐 서버 연결', h, {color:'#43e6cf', width:480});
}

async function applyServerUrl(){
  const i = document.getElementById('srvUrlInput');
  const u = i ? i.value.trim() : '';
  if(!u){ sfx('error'); return; }
  const b = document.getElementById('guiModalBody');
  if(b) b.innerHTML = '<div style="text-align:center;padding:24px;color:var(--mut)">연결 중...</div>';
  const okc = await NET.setBase(u);
  sfx(okc ? 'buy' : 'error');
  log(okc ? '<span class="g">🌐 연결 성공: '+esc(u)+'</span>'
          : '<span class="r">연결 실패: '+esc(u)+' (서버가 켜져 있는지, 방화벽이 열렸는지 확인)</span>');
  setServerUrl();
}
window.setServerUrl = setServerUrl;
window.applyServerUrl = applyServerUrl;

function updateNetBadge(){
  const el = document.getElementById('netBadge');
  if(!el) return;
  const on = NET.isOnline();
  el.textContent = on ? '🌐 온라인' : '📴 오프라인';
  el.style.color = on ? '#43e6cf' : '#777';
  el.title = on ? ('서버: ' + NET.getBase()) : 'server.py 를 실행하면 온라인 기능이 켜집니다';
}

// ---------- 주기 동기화 ----------
let _chatLastId = 0;
async function netSyncChat(){
  if(!NET.isOnline()) return;
  const r = await NET.req('/chat/list', {room:'global', since:0});
  if(r && r.ok){
    gChat = r.messages.map(m => ({nick:m.nick, msg:m.msg, t:m.ts*1000}));
    if(typeof renderSocial === 'function') renderSocial();
  }
  if(S && S.guild){
    const g = await NET.req('/chat/list', {room:'guild:'+S.guild, since:0});
    if(g && g.ok){
      guildChat[S.guild] = g.messages.map(m => ({nick:m.nick, msg:m.msg, t:m.ts*1000}));
      if(typeof renderSocial === 'function') renderSocial();
    }
  }
}

async function netSubmitRank(){
  if(!NET.isOnline() || !S || !S.nickname) return;
  const t = (typeof tierOf === 'function') ? tierOf(S.stage) : null;
  await NET.req('/rank/submit', {
    nick: S.nickname,
    power: (typeof calcPower === 'function') ? calcPower() : 0,
    stage: S.stage, level: S.level,
    tier: t ? (t.icon + t.name) : '',
    guild: S.guild || ''
  });
}

async function netFetchRank(){
  if(!NET.isOnline()) return null;
  const r = await NET.req('/rank/list', {});
  return (r && r.ok) ? r.rankings : null;
}

// 서버 연결 + 주기 작업 시작
async function initNetwork(){
  await NET.connect();
  setInterval(netSyncChat, 3000);
  setInterval(netSubmitRank, 15000);
  setInterval(netSyncOnline, 20000);
  setInterval(netSyncBoss, 10000);
  setInterval(netSyncMail, 30000);
  netSubmitRank();
}

function saveChat(){
  try{ storage.setItem('rift-chat', JSON.stringify({gChat, guildChat, guilds})); }catch(e){}
}

async function loadChat(){
  
    if(!S) return;
    try{
    const d = JSON.parse(storage.getItem('rift-chat')||'{}');
    if(d.gChat) gChat = d.gChat;
    if(d.guildChat) guildChat = d.guildChat;
    if(d.guilds) guilds = d.guilds;
  }catch(e){}
}

function regSW(){
  if('serviceWorker' in navigator && location.protocol==='https:'){
    navigator.serviceWorker.register('sw.js').catch(e=>console.log('SW', e));
  }
}

/* =========================================================
   차원 균열의 만물상 — 방치형 RPG (전체 시스템)
   밸런스: 몹HP x1.20/스테이지, 골드 x1.15, 강화비용 x1.07(효과 x1.05)
   ========================================================= */

/* ---------- 밸런스 공식 ---------- */
const DIFFICULTY = {
  easy: { hpMul: 1.15, atkMul: 1.10 },
  normal: { hpMul: 1.25, atkMul: 1.20 },
  hard: { hpMul: 1.35, atkMul: 1.30 }
};

let currentDifficulty = 'normal';


// ============================================================================
// 🌌 상위 티어 시스템 (100스테이지 클리어 후 진입)
//   1~100   일반 차원
//   101~125 ⚡ 강화 차원  (Enhanced)
//   126~150 🌠 초월 차원  (Transcendent)
//   151~175 ✨ 신의 차원  (Divine)
//   176~200 👑 DEV 차원   (Developer)
// ============================================================================
const MAX_STAGE = 1700;

const TIERS = [
  {id:'normal', name:'일반',  icon:'',   start:1,   end:100, hpMul:1,      atkMul:1,     goldMul:1,    color:'#43e6cf', pfx:''},
  {id:'enhanced', name:'강화', icon:'⚡', start:101, end:125, hpMul:50,      atkMul:12,     goldMul:20,     color:'#ffd23f', pfx:'강화된'},
  {id:'transcend',name:'초월', icon:'🌠', start:126, end:150, hpMul:9000,    atkMul:400,    goldMul:1200,   color:'#a86bff', pfx:'초월한'},
  {id:'divine',   name:'신',   icon:'✨', start:151, end:175, hpMul:1.6e6,   atkMul:14000,  goldMul:70000,  color:'#ff8a3a', pfx:'신성한'},
  {id:'dev',      name:'DEV',  icon:'👑', start:176, end:200, hpMul:2.9e8,   atkMul:5e5,    goldMul:4.2e6,  color:'#ff2d95', pfx:'DEV'},
  {id:'t1', name:'혼돈', icon:'🌀', start:201, end:225, hpMul:5.142e+10, atkMul:3.718e+07, goldMul:2.546e+08, color:'#ff2d95', pfx:'혼돈의'},
  {id:'t2', name:'심연', icon:'🕳️', start:226, end:250, hpMul:9.421e+12, atkMul:2.843e+09, goldMul:1.587e+10, color:'#ff5470', pfx:'심연의'},
  {id:'t3', name:'허무', icon:'⬛', start:251, end:275, hpMul:1.782e+15, atkMul:2.235e+11, goldMul:1.017e+12, color:'#ff8a3a', pfx:'허무한'},
  {id:'t4', name:'종말', icon:'☄️', start:276, end:300, hpMul:3.475e+17, atkMul:1.804e+13, goldMul:6.694e+13, color:'#ffd23f', pfx:'종말의'},
  {id:'t5', name:'무한', icon:'♾️', start:301, end:325, hpMul:6.983e+19, atkMul:1.495e+15, goldMul:4.521e+15, color:'#a8e86a', pfx:'무한한'},
  {id:'t6', name:'영겁', icon:'⏳', start:326, end:350, hpMul:1.445e+22, atkMul:1.27e+17, goldMul:3.132e+17, color:'#43e6cf', pfx:'영겁의'},
  {id:'t7', name:'공허', icon:'🌌', start:351, end:375, hpMul:3.074e+24, atkMul:1.106e+19, goldMul:2.224e+19, color:'#43a0e6', pfx:'공허한'},
  {id:'t8', name:'파멸', icon:'💥', start:376, end:400, hpMul:6.721e+26, atkMul:9.87e+20, goldMul:1.618e+21, color:'#a86bff', pfx:'파멸의'},
  {id:'t9', name:'절멸', icon:'☠️', start:401, end:425, hpMul:1.509e+29, atkMul:9.016e+22, goldMul:1.205e+23, color:'#e06be0', pfx:'절멸의'},
  {id:'t10', name:'태초', icon:'🥚', start:426, end:450, hpMul:3.479e+31, atkMul:8.427e+24, goldMul:9.181e+24, color:'#ffffff', pfx:'태초의'},
  {id:'t11', name:'창세', icon:'🌅', start:451, end:475, hpMul:8.226e+33, atkMul:8.056e+26, goldMul:7.155e+26, color:'#ff2d95', pfx:'창세의'},
  {id:'t12', name:'개벽', icon:'🌄', start:476, end:500, hpMul:1.993e+36, atkMul:7.873e+28, goldMul:5.7e+28, color:'#ff5470', pfx:'개벽의'},
  {id:'t13', name:'윤회', icon:'🔄', start:501, end:525, hpMul:4.948e+38, atkMul:7.86e+30, goldMul:4.64e+30, color:'#ff8a3a', pfx:'윤회하는'},
  {id:'t14', name:'열반', icon:'🕉️', start:526, end:550, hpMul:1.257e+41, atkMul:8.015e+32, goldMul:3.857e+32, color:'#ffd23f', pfx:'열반의'},
  {id:'t15', name:'해탈', icon:'☸️', start:551, end:575, hpMul:3.27e+43, atkMul:8.343e+34, goldMul:3.273e+34, color:'#a8e86a', pfx:'해탈한'},
  {id:'t16', name:'각성', icon:'👁️', start:576, end:600, hpMul:8.697e+45, atkMul:8.862e+36, goldMul:2.835e+36, color:'#43e6cf', pfx:'각성한'},
  {id:'t17', name:'초각성', icon:'👀', start:601, end:625, hpMul:2.364e+48, atkMul:9.601e+38, goldMul:2.504e+38, color:'#43a0e6', pfx:'초각성한'},
  {id:'t18', name:'극한', icon:'🔺', start:626, end:650, hpMul:6.568e+50, atkMul:1.061e+41, goldMul:2.255e+40, color:'#a86bff', pfx:'극한의'},
  {id:'t19', name:'초극', icon:'🔻', start:651, end:675, hpMul:1.863e+53, atkMul:1.194e+43, goldMul:2.07e+42, color:'#e06be0', pfx:'초극의'},
  {id:'t20', name:'절대', icon:'🅰️', start:676, end:700, hpMul:5.396e+55, atkMul:1.37e+45, goldMul:1.936e+44, color:'#ffffff', pfx:'절대적'},
  {id:'t21', name:'진리', icon:'📖', start:701, end:725, hpMul:1.595e+58, atkMul:1.601e+47, goldMul:1.844e+46, color:'#ff2d95', pfx:'진리의'},
  {id:'t22', name:'섭리', icon:'⚖️', start:726, end:750, hpMul:4.807e+60, atkMul:1.904e+49, goldMul:1.788e+48, color:'#ff5470', pfx:'섭리의'},
  {id:'t23', name:'운명', icon:'🎴', start:751, end:775, hpMul:1.477e+63, atkMul:2.306e+51, goldMul:1.765e+50, color:'#ff8a3a', pfx:'운명의'},
  {id:'t24', name:'숙명', icon:'🔗', start:776, end:800, hpMul:4.627e+65, atkMul:2.841e+53, goldMul:1.773e+52, color:'#ffd23f', pfx:'숙명의'},
  {id:'t25', name:'인과', icon:'🧬', start:801, end:825, hpMul:1.477e+68, atkMul:3.561e+55, goldMul:1.812e+54, color:'#a8e86a', pfx:'인과의'},
  {id:'t26', name:'차원', icon:'🔷', start:826, end:850, hpMul:4.801e+70, atkMul:4.539e+57, goldMul:1.883e+56, color:'#43e6cf', pfx:'차원의'},
  {id:'t27', name:'평행', icon:'🔶', start:851, end:875, hpMul:1.589e+73, atkMul:5.881e+59, goldMul:1.989e+58, color:'#43a0e6', pfx:'평행한'},
  {id:'t28', name:'다중', icon:'🔱', start:876, end:900, hpMul:5.353e+75, atkMul:7.746e+61, goldMul:2.136e+60, color:'#a86bff', pfx:'다중의'},
  {id:'t29', name:'초월계', icon:'🌠', start:901, end:925, hpMul:1.835e+78, atkMul:1.037e+64, goldMul:2.33e+62, color:'#e06be0', pfx:'초월계의'},
  {id:'t30', name:'상위계', icon:'⬆️', start:926, end:950, hpMul:6.398e+80, atkMul:1.41e+66, goldMul:2.583e+64, color:'#ffffff', pfx:'상위계의'},
  {id:'t31', name:'천계', icon:'☁️', start:951, end:975, hpMul:2.269e+83, atkMul:1.946e+68, goldMul:2.908e+66, color:'#ff2d95', pfx:'천계의'},
  {id:'t32', name:'마계', icon:'😈', start:976, end:1000, hpMul:8.18e+85, atkMul:2.729e+70, goldMul:3.324e+68, color:'#ff5470', pfx:'마계의'},
  {id:'t33', name:'명계', icon:'💀', start:1001, end:1025, hpMul:2.997e+88, atkMul:3.884e+72, goldMul:3.857e+70, color:'#ff8a3a', pfx:'명계의'},
  {id:'t34', name:'신계', icon:'🏛️', start:1026, end:1050, hpMul:1.116e+91, atkMul:5.611e+74, goldMul:4.542e+72, color:'#ffd23f', pfx:'신계의'},
  {id:'t35', name:'창조계', icon:'🎨', start:1051, end:1075, hpMul:4.222e+93, atkMul:8.224e+76, goldMul:5.428e+74, color:'#a8e86a', pfx:'창조계의'},
  {id:'t36', name:'원초', icon:'🔥', start:1076, end:1100, hpMul:1.622e+96, atkMul:1.223e+79, goldMul:6.58e+76, color:'#43e6cf', pfx:'원초의'},
  {id:'t37', name:'근원', icon:'🌱', start:1101, end:1125, hpMul:6.326e+98, atkMul:1.845e+81, goldMul:8.091e+78, color:'#43a0e6', pfx:'근원의'},
  {id:'t38', name:'본질', icon:'💠', start:1126, end:1150, hpMul:2.505e+101, atkMul:2.821e+83, goldMul:1.009e+81, color:'#a86bff', pfx:'본질의'},
  {id:'t39', name:'실재', icon:'🗿', start:1151, end:1175, hpMul:1.007e+104, atkMul:4.375e+85, goldMul:1.276e+83, color:'#e06be0', pfx:'실재의'},
  {id:'t40', name:'허상', icon:'🎭', start:1176, end:1200, hpMul:4.106e+106, atkMul:6.878e+87, goldMul:1.635e+85, color:'#ffffff', pfx:'허상의'},
  {id:'t41', name:'광휘', icon:'🌟', start:1201, end:1225, hpMul:1.699e+109, atkMul:1.096e+90, goldMul:2.123e+87, color:'#ff2d95', pfx:'광휘의'},
  {id:'t42', name:'암흑', icon:'🌑', start:1226, end:1250, hpMul:7.128e+111, atkMul:1.769e+92, goldMul:2.795e+89, color:'#ff5470', pfx:'암흑의'},
  {id:'t43', name:'여명', icon:'🌇', start:1251, end:1275, hpMul:3.033e+114, atkMul:2.894e+94, goldMul:3.727e+91, color:'#ff8a3a', pfx:'여명의'},
  {id:'t44', name:'황혼', icon:'🌆', start:1276, end:1300, hpMul:1.309e+117, atkMul:4.796e+96, goldMul:5.035e+93, color:'#ffd23f', pfx:'황혼의'},
  {id:'t45', name:'영원', icon:'∞', start:1301, end:1325, hpMul:5.724e+119, atkMul:8.048e+98, goldMul:6.889e+95, color:'#a8e86a', pfx:'영원한'},
  {id:'t46', name:'찰나', icon:'⚡', start:1326, end:1350, hpMul:2.537e+122, atkMul:1.368e+101, goldMul:9.545e+97, color:'#43e6cf', pfx:'찰나의'},
  {id:'t47', name:'무량', icon:'🔢', start:1351, end:1375, hpMul:1.14e+125, atkMul:2.354e+103, goldMul:1.339e+100, color:'#43a0e6', pfx:'무량한'},
  {id:'t48', name:'불가사의', icon:'❓', start:1376, end:1400, hpMul:5.186e+127, atkMul:4.1e+105, goldMul:1.902e+102, color:'#a86bff', pfx:'불가사의한'},
  {id:'t49', name:'나유타', icon:'🔟', start:1401, end:1425, hpMul:2.391e+130, atkMul:7.229e+107, goldMul:2.733e+104, color:'#e06be0', pfx:'나유타의'},
  {id:'t50', name:'아승기', icon:'💯', start:1426, end:1450, hpMul:1.116e+133, atkMul:1.29e+110, goldMul:3.977e+106, color:'#ffffff', pfx:'아승기의'},
  {id:'t51', name:'항하사', icon:'🏜️', start:1451, end:1475, hpMul:5.278e+135, atkMul:2.329e+112, goldMul:5.854e+108, color:'#ff2d95', pfx:'항하사의'},
  {id:'t52', name:'극', icon:'🎯', start:1476, end:1500, hpMul:2.527e+138, atkMul:4.256e+114, goldMul:8.719e+110, color:'#ff5470', pfx:'극의'},
  {id:'t53', name:'재', icon:'🔸', start:1501, end:1525, hpMul:1.225e+141, atkMul:7.865e+116, goldMul:1.314e+113, color:'#ff8a3a', pfx:'재의'},
  {id:'t54', name:'구', icon:'9️⃣', start:1526, end:1550, hpMul:6.007e+143, atkMul:1.47e+119, goldMul:2.002e+115, color:'#ffd23f', pfx:'구의'},
  {id:'t55', name:'간', icon:'🟨', start:1551, end:1575, hpMul:2.982e+146, atkMul:2.78e+121, goldMul:3.086e+117, color:'#a8e86a', pfx:'간의'},
  {id:'t56', name:'정', icon:'🟦', start:1576, end:1600, hpMul:1.498e+149, atkMul:5.315e+123, goldMul:4.81e+119, color:'#43e6cf', pfx:'정의'},
  {id:'t57', name:'재초', icon:'🔹', start:1601, end:1625, hpMul:7.616e+151, atkMul:1.028e+126, goldMul:7.581e+121, color:'#43a0e6', pfx:'재초의'},
  {id:'t58', name:'무극', icon:'⭕', start:1626, end:1650, hpMul:3.916e+154, atkMul:2.008e+128, goldMul:1.208e+124, color:'#a86bff', pfx:'무극의'},
  {id:'t59', name:'태극', icon:'☯️', start:1651, end:1675, hpMul:2.037e+157, atkMul:3.967e+130, goldMul:1.946e+126, color:'#e06be0', pfx:'태극의'},
  {id:'t60', name:'만물', icon:'🌈', start:1676, end:1700, hpMul:1.071e+160, atkMul:7.923e+132, goldMul:3.167e+128, color:'#ffffff', pfx:'만물의'},
];

function tierOf(stage){
  for(let i = TIERS.length - 1; i >= 0; i--){
    if(stage >= TIERS[i].start) return TIERS[i];
  }
  return TIERS[0];
}
function tierIndex(stage){ return TIERS.indexOf(tierOf(stage)); }
function isSpecialTier(stage){ return stage > 100; }

// 티어 배수 적용 (일반 구간은 1이라 기존 밸런스 그대로)

// 티어 내부 진행도에 따른 추가 배수 (강화 1-1 → 5-5 로 갈수록 강해짐)
function tierLocalMul(stage, per){
  const t = tierOf(stage);
  if(t.id === 'normal') return 1;
  const local = stage - t.start;      // 0 ~ 24
  return Math.pow(per, local);
}
function tierHpMul(stage){ return tierOf(stage).hpMul * tierLocalMul(stage, 1.22); }
function tierAtkMul(stage){ return tierOf(stage).atkMul * tierLocalMul(stage, 1.18); }
function tierGoldMul(stage){ return tierOf(stage).goldMul * tierLocalMul(stage, 1.17); }

// 상위 티어 스테이지 표시: "⚡강화 3-2" 형태
function tierStageLabel(stage){
  const t = tierOf(stage);
  if(t.id === 'normal') return Math.ceil(stage/10) + '-' + ((stage-1)%10+1);
  const local = stage - t.start + 1;          // 1~25
  return t.icon + t.name + ' ' + Math.ceil(local/5) + '-' + ((local-1)%5+1);
}

// 상위 티어 몬스터: 일반 몹을 재활용하되 접두어와 색을 입힘
function tierMobName(stage, baseName){
  const t = tierOf(stage);
  return t.pfx ? (t.pfx + ' ' + baseName) : baseName;
}

// 새 티어 진입 연출
let _lastTierId = null;
function checkTierUnlock(stage){
  const t = tierOf(stage);
  if(_lastTierId === null){ _lastTierId = t.id; return; }
  if(t.id !== _lastTierId){
    _lastTierId = t.id;
    if(t.id !== 'normal'){
      log('<span style="color:' + t.color + ';font-weight:bold;text-shadow:0 0 8px ' + t.color + '">');
      log('<span style="color:' + t.color + ';font-weight:bold">━━━━━━━━━━━━━━━━━━━━</span>');
      log('<span style="color:' + t.color + ';font-weight:bold;font-size:14px">' + t.icon + ' ' + t.name + ' 차원 개방! ' + t.icon + '</span>');
      log('<span style="color:' + t.color + '">몬스터 체력 ×' + fmt(t.hpMul) + ' · 골드 ×' + fmt(t.goldMul) + '</span>');
      log('<span style="color:' + t.color + ';font-weight:bold">━━━━━━━━━━━━━━━━━━━━</span>');
    }
  }
}

const BAL = {
  monsterHP : s => (s<=3 ? 10+s*3 : 15 * Math.pow(DIFFICULTY[currentDifficulty].hpMul, Math.min(s,100)-1)) * tierHpMul(s),
  monsterATK: s => 3  * Math.pow(DIFFICULTY[currentDifficulty].atkMul, Math.min(s,100)-1) * tierAtkMul(s),
  goldDrop  : s => 6  * Math.pow(1.15, Math.min(s,100)-1) * tierGoldMul(s),
  expDrop   : s => 4  * Math.pow(1.12, Math.min(s,100)-1) * Math.sqrt(tierGoldMul(s)),
  expReq    : L => Math.round(50 * Math.pow(L,1.5) * Math.pow(1.10,L)),
  upCost    : (base,n) => Math.round(base * Math.pow(1.07, n)),
  upBonus   : (base,n) => Math.floor(base * (Math.pow(1.05, n)-1) / 0.05),
  shardsFor : s => Math.floor(Math.pow(s,1.6)/10),
  bossHPMul : 5, bossTime : 30, killsForBoss : 10,
};

/* ---------- 월드 테마 & 드랍 테이블 ---------- */
const WORLDS = [
  {name:'슬라임 습지', mob:'끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴', mob:'그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원', mob:'서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'백은 늑대왕', el:'물'},
  {name:'골렘 폐허', mob:'폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'고대 수호 골렘', el:'빛'},
  {name:'용의 심연', mob:'새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'라그나로크 드래곤', el:'불'},
  {name:'해골 무덤', mob:'해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'해골 군주', el:'어둠'},
  {name:'버섯 숲', mob:'광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'버섯 대왕', el:'풀'},
  {name:'유령 저택', mob:'떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'저택의 주인', el:'물'},
  {name:'감시자의 성소', mob:'부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'심연의 감시자', el:'빛'},
  {name:'불사조 화산', mob:'새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (강화)', mob:'강화 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'강화 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (강화)', mob:'강화 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'강화 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (강화)', mob:'강화 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'강화 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (강화)', mob:'강화 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'강화 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (강화)', mob:'강화 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'강화 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (강화)', mob:'강화 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'강화 해골 군주', el:'어둠'},
  {name:'버섯 숲 (강화)', mob:'강화 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'강화 버섯 대왕', el:'풀'},
  {name:'유령 저택 (강화)', mob:'강화 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'강화 저택의 주인', el:'물'},
  {name:'감시자의 성소 (강화)', mob:'강화 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'강화 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (강화)', mob:'강화 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'강화 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (심화)', mob:'심화 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'심화 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (심화)', mob:'심화 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'심화 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (심화)', mob:'심화 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'심화 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (심화)', mob:'심화 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'심화 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (심화)', mob:'심화 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'심화 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (심화)', mob:'심화 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'심화 해골 군주', el:'어둠'},
  {name:'버섯 숲 (심화)', mob:'심화 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'심화 버섯 대왕', el:'풀'},
  {name:'유령 저택 (심화)', mob:'심화 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'심화 저택의 주인', el:'물'},
  {name:'감시자의 성소 (심화)', mob:'심화 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'심화 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (심화)', mob:'심화 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'심화 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (극악)', mob:'극악 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'극악 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (극악)', mob:'극악 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'극악 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (극악)', mob:'극악 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'극악 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (극악)', mob:'극악 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'극악 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (극악)', mob:'극악 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'극악 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (극악)', mob:'극악 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'극악 해골 군주', el:'어둠'},
  {name:'버섯 숲 (극악)', mob:'극악 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'극악 버섯 대왕', el:'풀'},
  {name:'유령 저택 (극악)', mob:'극악 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'극악 저택의 주인', el:'물'},
  {name:'감시자의 성소 (극악)', mob:'극악 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'극악 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (극악)', mob:'극악 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'극악 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (악몽)', mob:'악몽 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'악몽 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (악몽)', mob:'악몽 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'악몽 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (악몽)', mob:'악몽 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'악몽 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (악몽)', mob:'악몽 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'악몽 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (악몽)', mob:'악몽 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'악몽 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (악몽)', mob:'악몽 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'악몽 해골 군주', el:'어둠'},
  {name:'버섯 숲 (악몽)', mob:'악몽 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'악몽 버섯 대왕', el:'풀'},
  {name:'유령 저택 (악몽)', mob:'악몽 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'악몽 저택의 주인', el:'물'},
  {name:'감시자의 성소 (악몽)', mob:'악몽 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'악몽 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (악몽)', mob:'악몽 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'악몽 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (도깨비)', mob:'도깨비 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'도깨비 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (도깨비)', mob:'도깨비 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'도깨비 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (도깨비)', mob:'도깨비 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'도깨비 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (도깨비)', mob:'도깨비 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'도깨비 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (도깨비)', mob:'도깨비 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'도깨비 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (도깨비)', mob:'도깨비 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'도깨비 해골 군주', el:'어둠'},
  {name:'버섯 숲 (도깨비)', mob:'도깨비 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'도깨비 버섯 대왕', el:'풀'},
  {name:'유령 저택 (도깨비)', mob:'도깨비 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'도깨비 저택의 주인', el:'물'},
  {name:'감시자의 성소 (도깨비)', mob:'도깨비 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'도깨비 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (도깨비)', mob:'도깨비 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'도깨비 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (신수)', mob:'신수 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'신수 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (신수)', mob:'신수 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'신수 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (신수)', mob:'신수 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'신수 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (신수)', mob:'신수 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'신수 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (신수)', mob:'신수 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'신수 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (신수)', mob:'신수 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'신수 해골 군주', el:'어둠'},
  {name:'버섯 숲 (신수)', mob:'신수 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'신수 버섯 대왕', el:'풀'},
  {name:'유령 저택 (신수)', mob:'신수 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'신수 저택의 주인', el:'물'},
  {name:'감시자의 성소 (신수)', mob:'신수 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'신수 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (신수)', mob:'신수 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'신수 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (신급)', mob:'신급 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'신급 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (신급)', mob:'신급 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'신급 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (신급)', mob:'신급 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'신급 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (신급)', mob:'신급 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'신급 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (신급)', mob:'신급 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'신급 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (신급)', mob:'신급 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'신급 해골 군주', el:'어둠'},
  {name:'버섯 숲 (신급)', mob:'신급 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'신급 버섯 대왕', el:'풀'},
  {name:'유령 저택 (신급)', mob:'신급 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'신급 저택의 주인', el:'물'},
  {name:'감시자의 성소 (신급)', mob:'신급 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'신급 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (신급)', mob:'신급 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'신급 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (초월)', mob:'초월 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'초월 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (초월)', mob:'초월 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'초월 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (초월)', mob:'초월 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'초월 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (초월)', mob:'초월 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'초월 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (초월)', mob:'초월 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'초월 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (초월)', mob:'초월 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'초월 해골 군주', el:'어둠'},
  {name:'버섯 숲 (초월)', mob:'초월 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'초월 버섯 대왕', el:'풀'},
  {name:'유령 저택 (초월)', mob:'초월 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'초월 저택의 주인', el:'물'},
  {name:'감시자의 성소 (초월)', mob:'초월 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'초월 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (초월)', mob:'초월 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'초월 영겁의 불사조', el:'불'},
  {name:'슬라임 습지 (절대)', mob:'절대 끈적 슬라임', mat:'슬라임 젤리', spr:'slime', bossName:'절대 거대 슬라임 킹', el:'풀'},
  {name:'박쥐 동굴 (절대)', mob:'절대 그림자 박쥐', mat:'박쥐 날개', spr:'bat', bossName:'절대 심연의 흡혈박쥐', el:'어둠'},
  {name:'늑대 설원 (절대)', mob:'절대 서리 늑대', mat:'늑대 털', spr:'wolf', bossName:'절대 백은 늑대왕', el:'물'},
  {name:'골렘 폐허 (절대)', mob:'절대 폐허 골렘', mat:'골렘 파편', spr:'golem', bossName:'절대 고대 수호 골렘', el:'빛'},
  {name:'용의 심연 (절대)', mob:'절대 새끼 화룡', mat:'용의 비늘', spr:'dragon', bossName:'절대 라그나로크 드래곤', el:'불'},
  {name:'해골 무덤 (절대)', mob:'절대 해골 병사', mat:'낡은 뼈', spr:'skeleton', bossName:'절대 해골 군주', el:'어둠'},
  {name:'버섯 숲 (절대)', mob:'절대 광대버섯', mat:'포자 주머니', spr:'mushroom', bossName:'절대 버섯 대왕', el:'풀'},
  {name:'유령 저택 (절대)', mob:'절대 떠도는 원혼', mat:'영혼 조각', spr:'ghost', bossName:'절대 저택의 주인', el:'물'},
  {name:'감시자의 성소 (절대)', mob:'절대 부유하는 눈', mat:'수정 눈동자', spr:'eye', bossName:'절대 심연의 감시자', el:'빛'},
  {name:'불사조 화산 (절대)', mob:'절대 새끼 불사조', mat:'불꽃 깃털', spr:'phoenix', bossName:'절대 영겁의 불사조', el:'불'},
];

// ============================================================================
// 👾 확장 몬스터 도감 (기존 10 + 신규 30 = 총 40종)
// 스테이지마다 정해진 몬스터가 등장 (STAGE_MOBS 테이블)
// ============================================================================

const EXTRA_MOBS = [
  // 풀 — 앞 3종: 슬라임 습지 / 뒤 3종: 버섯 숲
  {mob:'가시 달팽이', mat:'가시 껍질', spr:'m_snail', pal:'m_snail', el:'풀'},
  {mob:'독버섯 요정', mat:'독 포자', spr:'m_toxfairy', pal:'m_toxfairy', el:'풀'},
  {mob:'덩굴 마귀', mat:'질긴 덩굴', spr:'m_vine', pal:'m_vine', el:'풀'},
  {mob:'숲의 도깨비', mat:'도깨비 뿔', spr:'m_dokkaebi', pal:'m_dokkaebi', el:'풀'},
  {mob:'맹독 두꺼비', mat:'독샘', spr:'m_toxtoad', pal:'m_toxtoad', el:'풀'},
  {mob:'꽃잎 정령', mat:'빛나는 꽃잎', spr:'m_petalspirit', pal:'m_petalspirit', el:'풀'},
  // 어둠 — 앞 3종: 박쥐 동굴 / 뒤 3종: 해골 무덤
  {mob:'동굴 거미', mat:'거미줄', spr:'m_spider', pal:'m_spider', el:'어둠'},
  {mob:'그림자 살쾡이', mat:'검은 발톱', spr:'m_shadowcat', pal:'m_shadowcat', el:'어둠'},
  {mob:'어둠의 구울', mat:'썩은 살점', spr:'m_ghoul', pal:'m_ghoul', el:'어둠'},
  {mob:'밤의 까마귀', mat:'검은 깃털', spr:'m_crow', pal:'m_crow', el:'어둠'},
  {mob:'심연 벌레', mat:'심연 껍데기', spr:'m_abyssworm', pal:'m_abyssworm', el:'어둠'},
  {mob:'저주받은 갑옷', mat:'녹슨 갑주', spr:'m_cursedarmor', pal:'m_cursedarmor', el:'어둠'},
  // 물 — 앞 3종: 늑대 설원 / 뒤 3종: 유령 저택
  {mob:'얼음 정령', mat:'얼음 결정', spr:'m_icespirit', pal:'m_icespirit', el:'물'},
  {mob:'눈보라 펭귄', mat:'차가운 깃털', spr:'m_penguin', pal:'m_penguin', el:'물'},
  {mob:'서리 거인', mat:'거인의 얼음', spr:'m_frostgiant', pal:'m_frostgiant', el:'물'},
  {mob:'심해 문어', mat:'말랑 촉수', spr:'m_octopus', pal:'m_octopus', el:'물'},
  {mob:'물의 나가', mat:'나가 비늘', spr:'m_naga', pal:'m_naga', el:'물'},
  {mob:'안개 유령', mat:'안개 정수', spr:'m_mistghost', pal:'m_mistghost', el:'물'},
  // 빛 — 앞 3종: 골렘 폐허 / 뒤 3종: 감시자의 성소
  {mob:'타락 천사상', mat:'천사의 파편', spr:'m_angelstatue', pal:'m_angelstatue', el:'빛'},
  {mob:'빛의 슬라임', mat:'광휘 젤리', spr:'m_lightslime', pal:'m_lightslime', el:'빛'},
  {mob:'수정 나비', mat:'수정 가루', spr:'m_crystalbfly', pal:'m_crystalbfly', el:'빛'},
  {mob:'성소 파수꾼', mat:'성스러운 문장', spr:'m_sentinel', pal:'m_sentinel', el:'빛'},
  {mob:'프리즘 골렘', mat:'프리즘 조각', spr:'m_prismgolem', pal:'m_prismgolem', el:'빛'},
  {mob:'섬광 여우', mat:'빛나는 꼬리털', spr:'m_flashfox', pal:'m_flashfox', el:'빛'},
  // 불 — 앞 3종: 용의 심연 / 뒤 3종: 불사조 화산
  {mob:'용암 슬라임', mat:'용암 방울', spr:'m_lavaslime', pal:'m_lavaslime', el:'불'},
  {mob:'화염 임프', mat:'임프의 뿔', spr:'m_fireimp', pal:'m_fireimp', el:'불'},
  {mob:'재의 해골', mat:'불탄 뼛조각', spr:'m_ashskel', pal:'m_ashskel', el:'불'},
  {mob:'마그마 거북', mat:'마그마 등딱지', spr:'m_magmaturtle', pal:'m_magmaturtle', el:'불'},
  {mob:'화산 박쥐', mat:'그을린 날개', spr:'m_volcanobat', pal:'m_volcanobat', el:'불'},
  {mob:'불꽃 정령', mat:'정령의 불씨', spr:'m_flamespirit', pal:'m_flamespirit', el:'불'},
];

const EXTRA_MOBS2 = [
  {mob:'고목 트렌트', mat:'나무 심재', spr:'n_treant', pal:'n_treant', el:'풀'},
  {mob:'뿔 딱정벌레', mat:'단단한 뿔', spr:'n_beetle', pal:'n_beetle', el:'풀'},
  {mob:'낫 사마귀', mat:'예리한 낫', spr:'n_mantis', pal:'n_mantis', el:'풀'},
  {mob:'해바라기 괴물', mat:'황금 씨앗', spr:'n_sunflower', pal:'n_sunflower', el:'풀'},
  {mob:'대나무 골렘', mat:'청죽 마디', spr:'n_bamboo', pal:'n_bamboo', el:'풀'},
  {mob:'이끼 덩어리', mat:'축축한 이끼', spr:'n_moss', pal:'n_moss', el:'풀'},
  {mob:'가시 선인장', mat:'날카로운 가시', spr:'n_cactus', pal:'n_cactus', el:'풀'},
  {mob:'벌레잡이 통풀', mat:'소화액', spr:'n_pitcher', pal:'n_pitcher', el:'풀'},
  {mob:'숲의 도깨비불', mat:'반딧 정수', spr:'n_wisp', pal:'n_wisp', el:'풀'},
  {mob:'뿌리 야수', mat:'굵은 뿌리', spr:'n_rootbeast', pal:'n_rootbeast', el:'풀'},
  {mob:'사신', mat:'부러진 낫', spr:'n_reaper', pal:'n_reaper', el:'어둠'},
  {mob:'그림자 망령', mat:'짙은 그림자', spr:'n_shade', pal:'n_shade', el:'어둠'},
  {mob:'석상 가고일', mat:'부서진 석상', spr:'n_gargoyle', pal:'n_gargoyle', el:'어둠'},
  {mob:'악몽마', mat:'검은 갈기', spr:'n_nightmare', pal:'n_nightmare', el:'어둠'},
  {mob:'리치', mat:'마력 결정', spr:'n_lich', pal:'n_lich', el:'어둠'},
  {mob:'박쥐 떼', mat:'수많은 날개', spr:'n_batswarm', pal:'n_batswarm', el:'어둠'},
  {mob:'공허의 아가리', mat:'공허 조각', spr:'n_voidmaw', pal:'n_voidmaw', el:'어둠'},
  {mob:'원귀', mat:'한 맺힌 혼', spr:'n_wraith', pal:'n_wraith', el:'어둠'},
  {mob:'암흑기사', mat:'칠흑 갑주', spr:'n_darkknight', pal:'n_darkknight', el:'어둠'},
  {mob:'지옥견', mat:'불타는 송곳니', spr:'n_hellhound', pal:'n_hellhound', el:'어둠'},
  {mob:'크라켄', mat:'거대 촉수', spr:'n_kraken', pal:'n_kraken', el:'물'},
  {mob:'인어', mat:'진주 비늘', spr:'n_mermaid', pal:'n_mermaid', el:'물'},
  {mob:'해파리', mat:'투명 젤리', spr:'n_jellyfish', pal:'n_jellyfish', el:'물'},
  {mob:'거대 게', mat:'두꺼운 집게', spr:'n_crab', pal:'n_crab', el:'물'},
  {mob:'해마', mat:'말린 꼬리', spr:'n_seahorse', pal:'n_seahorse', el:'물'},
  {mob:'리바이어던', mat:'심해 비늘', spr:'n_leviathan', pal:'n_leviathan', el:'물'},
  {mob:'물방울 정령', mat:'맑은 물방울', spr:'n_bubble', pal:'n_bubble', el:'물'},
  {mob:'심해 아귀', mat:'발광 기관', spr:'n_anglerfish', pal:'n_anglerfish', el:'물'},
  {mob:'조수 사제', mat:'조수의 홀', spr:'n_tidepriest', pal:'n_tidepriest', el:'물'},
  {mob:'산호 골렘', mat:'산호 가지', spr:'n_coral', pal:'n_coral', el:'물'},
  {mob:'세라핌', mat:'성스러운 깃털', spr:'n_seraph', pal:'n_seraph', el:'빛'},
  {mob:'성기사', mat:'축복 갑주', spr:'n_paladin', pal:'n_paladin', el:'빛'},
  {mob:'광휘 구체', mat:'순수한 빛', spr:'n_lightorb', pal:'n_lightorb', el:'빛'},
  {mob:'유니콘', mat:'신성한 뿔', spr:'n_unicorn', pal:'n_unicorn', el:'빛'},
  {mob:'태양매', mat:'작열 깃털', spr:'n_solarhawk', pal:'n_solarhawk', el:'빛'},
  {mob:'등불 파수꾼', mat:'꺼지지 않는 심지', spr:'n_beacon', pal:'n_beacon', el:'빛'},
  {mob:'별빛 새', mat:'별 부스러기', spr:'n_starling', pal:'n_starling', el:'빛'},
  {mob:'성직 망령', mat:'기도문 조각', spr:'n_clericghost', pal:'n_clericghost', el:'빛'},
  {mob:'거울 골렘', mat:'은빛 파편', spr:'n_mirrorgolem', pal:'n_mirrorgolem', el:'빛'},
  {mob:'새벽 여우', mat:'여명 꼬리털', spr:'n_dawnfox', pal:'n_dawnfox', el:'빛'},
  {mob:'이프리트', mat:'작열 정수', spr:'n_ifrit', pal:'n_ifrit', el:'불'},
  {mob:'불씨 쥐', mat:'그을린 털', spr:'n_emberrat', pal:'n_emberrat', el:'불'},
  {mob:'화염 뱀', mat:'뜨거운 허물', spr:'n_flamesnake', pal:'n_flamesnake', el:'불'},
  {mob:'용암 거인', mat:'녹은 핵', spr:'n_moltengiant', pal:'n_moltengiant', el:'불'},
  {mob:'잿불 새', mat:'잿빛 깃털', spr:'n_cinderbird', pal:'n_cinderbird', el:'불'},
  {mob:'대장간 골렘', mat:'달군 강철', spr:'n_forgegolem', pal:'n_forgegolem', el:'불'},
  {mob:'연기 망령', mat:'매캐한 연기', spr:'n_smokewraith', pal:'n_smokewraith', el:'불'},
  {mob:'화염 거미', mat:'불타는 실', spr:'n_pyrospider', pal:'n_pyrospider', el:'불'},
  {mob:'용암 지렁이', mat:'마그마 점액', spr:'n_lavaworm', pal:'n_lavaworm', el:'불'},
  {mob:'태양 불꽃', mat:'작은 태양', spr:'n_sunspark', pal:'n_sunspark', el:'불'},
];


// 스테이지별 몬스터 배정: 각 월드(10스테이지)마다 몹 4종이 로테이션
// 1~9 스테이지: 일반몹 (스테이지 번호에 따라 정해진 몹), 10스테이지: 보스
const STAGE_MOBS = (function(){
  const table = {};
  const ALL_EXTRA = EXTRA_MOBS.concat(EXTRA_MOBS2);  // 30 + 50 = 80종
  const elCount = {};
  const worldPool = [];
  
  for(let wIdx = 0; wIdx < WORLDS.length; wIdx++){
    const world = WORLDS[wIdx];
    const nth = elCount[world.el] || 0;   // 이 속성의 몇 번째 월드인가 (0 or 1)
    elCount[world.el] = nth + 1;
    
    // 같은 속성 몹을 두 월드가 절반씩 나눠 가짐 → 80종 전부 사용
    const themed = ALL_EXTRA.filter(m => m.el === world.el);
    const half = Math.ceil(themed.length / 2);
    const mine = themed.slice(nth * half, nth * half + half);
    
    // 월드별 몹 = [기본몹, ...전용몹들] (9종 로테이션)
    worldPool.push([
      {mob: world.mob, mat: world.mat, spr: world.spr, pal: world.spr, el: world.el},
      ...mine
    ]);
  }
  
  for(let s = 1; s <= 100; s++){
    const wIdx = Math.floor((s-1)/10) % WORLDS.length;
    const world = WORLDS[wIdx];
    const inStage = (s-1) % 10;
    
    if(inStage === 9){
      table[s] = {mob: world.bossName, mat: world.mat, spr: world.spr, pal: world.spr, el: world.el, isBoss: true};
    } else {
      const pool = worldPool[wIdx];
      const pick = pool[inStage % pool.length];   // 1~9스테이지 = 9종이 차례대로!
      table[s] = {mob: pick.mob, mat: world.mat, spr: pick.spr, pal: pick.pal || pick.spr, el: pick.el, isBoss: false};
    }
  }
  return table;
})();

// 현재 스테이지의 몬스터 정보 가져오기
function getStageMob(stage){
  let s = Math.max(1, Math.min(MAX_STAGE, stage));
  // 101 이상은 1~100 몬스터를 재사용하되 티어 접두어를 붙임
  const base = s > 100 ? ((s - 101) % 100) + 1 : s;
  const m = STAGE_MOBS[base] || STAGE_MOBS[1];
  if(s > 100){
    return Object.assign({}, m, { mob: tierMobName(s, m.mob) });
  }
  return m;
}


const ELEMS = {불:'🔥', 물:'💧', 풀:'🌿', 빛:'✨', 어둠:'🌑'};
const ELEM_KEYS = Object.keys(ELEMS);
const BEATS = {불:'풀', 풀:'물', 물:'불', 빛:'어둠', 어둠:'빛'};
function elemMult(a, d){ if(!a || !d) return 1; if(BEATS[a]===d) return 2; if(BEATS[d]===a) return 0.5; return 1; }
const GRADES = ['Normal','Rare','Epic','Unique','Legendary','Mythic','Celestial','Primordial'];
const GRADE_KO = {Developer:'개발자', Normal:'일반', Rare:'희귀', Epic:'영웅', Unique:'유니크', Legendary:'전설', Mythic:'신화', Celestial:'천상', Primordial:'태초'};
const GRADE_CLS = {Developer:'gDEV', Normal:'gN', Rare:'gR', Epic:'gE', Unique:'gU', Legendary:'gL', Mythic:'gM', Celestial:'gC', Primordial:'gP'};
const GRADE_PFX = {Developer:'', Normal:'낡은', Rare:'빛나는', Epic:'정교한', Unique:'유일한', Legendary:'전설의', Mythic:'신화의', Celestial:'천상의', Primordial:'태초의'};
const GRADE_COLOR = {Developer:'#ff2d95', Normal:'#9aa0b0', Rare:'#43a0e6', Epic:'#a86bff', Unique:'#ffd23f', Legendary:'#ff8a3a', Mythic:'#ff5470', Celestial:'#43e6cf', Primordial:'#ffffff'};
// 등급별 드랍 가중치 (낮은 등급일수록 흔함)
const GRADE_WEIGHT = {Normal:1000, Rare:300, Epic:90, Unique:28, Legendary:9, Mythic:3, Celestial:0.8, Primordial:0.2};

const WEAPON_BASE = [
  '철검',
  '단검',
  '장검',
  '대검',
  '기사검',
  '룬검',
  '성검',
  '마검',
  '용살검',
  '흑요석 검',
  '서리검',
  '화염검',
  '뇌전검',
  '심연검',
  '창세검',
  '손도끼',
  '전투도끼',
  '양날도끼',
  '거인의 도끼',
  '철퇴',
  '성스러운 망치',
  '파괴의 망치',
  '대장간 망치',
  '운석 망치',
  '폭풍 도끼',
  '용암 도끼',
  '파멸의 대검',
  '창',
  '장창',
  '삼지창',
  '미늘창',
  '기사창',
  '용기병 창',
  '뇌창',
  '성창',
  '심연의 창',
  '천공창',
  '단궁',
  '장궁',
  '석궁',
  '사냥꾼의 활',
  '정령의 활',
  '달빛 활',
  '태양궁',
  '폭풍궁',
  '용뼈 활',
  '신궁',
  '나무 지팡이',
  '수정 지팡이',
  '룬 지팡이',
  '현자의 지팡이',
  '원소 지팡이',
  '대마법 지팡이',
  '별빛 홀',
  '생명의 홀',
  '죽음의 홀',
  '차원 지팡이',
  '마도서',
  '금서',
  '창세의 서'
];
const ARMOR_BASE  = [
  '천 로브',
  '수도복',
  '마법사 로브',
  '견습생 튜닉',
  '비단 로브',
  '룬 각인 로브',
  '성직자 예복',
  '현자의 로브',
  '별빛 로브',
  '심연의 로브',
  '누더기 옷',
  '여행자 외투',
  '상인의 조끼',
  '연금술사 앞치마',
  '점성술사 가운',
  '주술사 의복',
  '영혼 술사 로브',
  '대마법사 로브',
  '시간의 예복',
  '창세의 로브',
  '가죽 갑옷',
  '사냥꾼 조끼',
  '늑대 가죽옷',
  '도적 정장',
  '추적자 코트',
  '그림자 가죽옷',
  '용병 가죽갑옷',
  '비룡 가죽옷',
  '괴수 가죽갑옷',
  '야수왕 가죽',
  '거친 가죽조끼',
  '정글 가죽옷',
  '설원 방한복',
  '사막 순찰복',
  '습지 방수복',
  '암살자 흑의',
  '밀림 수렵복',
  '고룡 가죽갑주',
  '태고의 가죽',
  '신수의 가죽',
  '사슬 갑옷',
  '기사 흉갑',
  '근위병 갑주',
  '강철 판금갑',
  '미스릴 사슬',
  '흑철 흉갑',
  '성기사 판금',
  '용비늘 판금',
  '오리하르콘 갑주',
  '신성 판금갑',
  '녹슨 철갑',
  '병사 흉갑',
  '중장 판금',
  '요새 갑주',
  '파수꾼 갑주',
  '철벽 흉갑',
  '수호기사 판금',
  '불멸의 판금',
  '천공 판금갑',
  '창천의 갑주',
  '나무껍질 갑옷',
  '이끼 갑옷',
  '덩굴 갑주',
  '꽃잎 드레스',
  '대나무 갑주',
  '수정 갑옷',
  '얼음 갑주',
  '화염 갑옷',
  '뇌전 갑주',
  '대지의 갑옷',
  '산호 갑주',
  '조개 갑옷',
  '폭풍 망토',
  '회오리 갑주',
  '화산암 갑주',
  '서리 갑옷',
  '정령 드레스',
  '세계수 갑옷',
  '원소 갑주',
  '자연왕의 갑옷',
  '해골 갑주',
  '망령 로브',
  '저주받은 갑옷',
  '흡혈귀 예복',
  '리치의 예복',
  '공허 갑주',
  '악마 갑옷',
  '천사 예복',
  '세라핌 갑주',
  '신의 갑옷',
  '별의 갑주',
  '달빛 드레스',
  '태양 갑주',
  '혼돈 갑옷',
  '질서의 갑주',
  '차원 갑옷',
  '균열 갑주',
  '무한의 예복',
  '종말의 갑주',
  '창조의 갑옷'
];
// 드랍 테이블: [확률, 종류]
const DROP_TABLE = [
  {p:0.60, kind:'mat'},     // 잡템(재료)
  {p:0.12, kind:'stone'},   // 강화석
  {p:0.08, kind:'equip'},   // 장비 (그 중 Rare 10%)
];
const INV_CAP = 30; // 장비 인벤토리 한도

/* ---------- 유물 ---------- */
const ARTS = {
  atk : {name:'공격의 유물', desc:'공격력 +5%/Lv'},
  gold: {name:'황금의 유물', desc:'골드 획득 +5%/Lv'},
  boss: {name:'시간의 유물', desc:'보스 제한시간 +2초/Lv'},
  crit: {name:'급소의 유물', desc:'치명타 확률 +1%/Lv'},
};

/* ---------- 동료 ---------- */
const PETS = [
  {id:'slimep',  name:'미니 슬라임',   emoji:'🟢', mat:'슬라임 젤리',  need:30, desc:'협공 20%'},
  {id:'batp',    name:'아기 박쥐',     emoji:'🦇', mat:'박쥐 날개',    need:30, desc:'골드 +15%'},
  {id:'golemp',  name:'꼬마 골렘',     emoji:'🪨', mat:'골렘 파편',    need:30, desc:'방어력 +20%'},
  {id:'phoenix', name:'불꽃새',       emoji:'🔥', mat:'불꽃 깃털',   need:30, desc:'공격력 +15%'},
  {id:'specter', name:'유령',         emoji:'👻', mat:'유령 숨결',   need:30, desc:'회피 +20%'},
  {id:'p_wolf', name:'서리 늑대 새끼', emoji:'🐺', mat:'늑대 털', need:40, desc:'공격력 +20%', grade:'Rare', eff:'atk20'},
  {id:'p_crow', name:'까마귀 친구', emoji:'🐦‍⬛', mat:'검은 깃털', need:40, desc:'골드 +20%', grade:'Rare', eff:'gold20'},
  {id:'p_beetle', name:'뿔 딱정벌레', emoji:'🪲', mat:'단단한 뿔', need:40, desc:'방어력 +25%', grade:'Rare', eff:'def25'},
  {id:'p_jelly', name:'작은 해파리', emoji:'🪼', mat:'투명 젤리', need:40, desc:'회피 +25%', grade:'Rare', eff:'eva25'},
  {id:'p_wisp', name:'도깨비불', emoji:'🔥', mat:'반딧 정수', need:40, desc:'협공 25%', grade:'Rare', eff:'assist25'},
  {id:'p_mantis', name:'낫 사마귀', emoji:'🦗', mat:'예리한 낫', need:80, desc:'공격력 +30%', grade:'Epic', eff:'atk30'},
  {id:'p_crab', name:'아기 게', emoji:'🦀', mat:'두꺼운 집게', need:80, desc:'방어력 +35%', grade:'Epic', eff:'def35'},
  {id:'p_seahorse', name:'해마', emoji:'🐠', mat:'말린 꼬리', need:80, desc:'골드 +30%', grade:'Epic', eff:'gold30'},
  {id:'p_bubble', name:'물방울 정령', emoji:'💧', mat:'맑은 물방울', need:80, desc:'회피 +30%', grade:'Epic', eff:'eva30'},
  {id:'p_ember', name:'불씨 쥐', emoji:'🐁', mat:'그을린 털', need:80, desc:'협공 35%', grade:'Epic', eff:'assist35'},
  {id:'p_fox', name:'새벽 여우', emoji:'🦊', mat:'여명 꼬리털', need:150, desc:'공격력 +45%', grade:'Unique', eff:'atk45'},
  {id:'p_starling', name:'별빛 새', emoji:'🐤', mat:'별 부스러기', need:150, desc:'골드 +45%', grade:'Unique', eff:'gold45'},
  {id:'p_mirror', name:'거울 골렘', emoji:'🪞', mat:'은빛 파편', need:150, desc:'방어력 +50%', grade:'Unique', eff:'def50'},
  {id:'p_shade', name:'작은 그림자', emoji:'🌑', mat:'짙은 그림자', need:150, desc:'회피 +45%', grade:'Unique', eff:'eva45'},
  {id:'p_pyro', name:'화염 거미', emoji:'🕷️', mat:'불타는 실', need:150, desc:'협공 50%', grade:'Unique', eff:'assist50'},
  {id:'p_unicorn', name:'유니콘', emoji:'🦄', mat:'신성한 뿔', need:300, desc:'공격력 +70%', grade:'Legendary', eff:'atk70'},
  {id:'p_kraken', name:'새끼 크라켄', emoji:'🐙', mat:'거대 촉수', need:300, desc:'방어력 +75%', grade:'Legendary', eff:'def75'},
  {id:'p_solar', name:'태양매', emoji:'🦅', mat:'작열 깃털', need:300, desc:'골드 +70%', grade:'Legendary', eff:'gold70'},
  {id:'p_seraph', name:'세라핌', emoji:'😇', mat:'성스러운 깃털', need:600, desc:'공격력 +100%', grade:'Mythic', eff:'atk100'},
  {id:'p_void', name:'공허의 아가리', emoji:'🕳️', mat:'공허 조각', need:600, desc:'협공 80%', grade:'Mythic', eff:'assist80'},
];

/* ---------- 펫 픽셀 외형 매핑 (장착 펫이 캐릭터 옆에서 따라다니며 표시됨) ---------- */
const PET_SPR = {
  slimep:  {spr:'slime',   pal:'slime',   rows:10},
  batp:    {spr:'bat',     pal:'bat',     rows:10},
  golemp:  {spr:'golem',   pal:'golem',   rows:12},
  phoenix: {spr:'phoenix', pal:'phoenix', rows:12},
  specter: {spr:'ghost',   pal:'ghost',   rows:10},
  p_wolf: {spr:'wolf', pal:'wolf', rows:10},
  p_crow: {spr:'m_crow', pal:'m_crow', rows:10},
  p_beetle: {spr:'n_beetle', pal:'n_beetle', rows:10},
  p_jelly: {spr:'n_jellyfish', pal:'n_jellyfish', rows:10},
  p_wisp: {spr:'n_wisp', pal:'n_wisp', rows:10},
  p_mantis: {spr:'n_mantis', pal:'n_mantis', rows:10},
  p_crab: {spr:'n_crab', pal:'n_crab', rows:10},
  p_seahorse: {spr:'n_seahorse', pal:'n_seahorse', rows:10},
  p_bubble: {spr:'n_bubble', pal:'n_bubble', rows:10},
  p_ember: {spr:'n_emberrat', pal:'n_emberrat', rows:10},
  p_fox: {spr:'n_dawnfox', pal:'n_dawnfox', rows:10},
  p_starling: {spr:'n_starling', pal:'n_starling', rows:10},
  p_mirror: {spr:'n_mirrorgolem', pal:'n_mirrorgolem', rows:10},
  p_shade: {spr:'n_shade', pal:'n_shade', rows:10},
  p_pyro: {spr:'n_pyrospider', pal:'n_pyrospider', rows:10},
  p_unicorn: {spr:'n_unicorn', pal:'n_unicorn', rows:10},
  p_kraken: {spr:'n_kraken', pal:'n_kraken', rows:10},
  p_solar: {spr:'n_solarhawk', pal:'n_solarhawk', rows:10},
  p_seraph: {spr:'n_seraph', pal:'n_seraph', rows:10},
  p_void: {spr:'n_voidmaw', pal:'n_voidmaw', rows:10},
};

/* ---------- 게임 상태 ---------- */
let S = null;
function freshState(){
  return {
    level:1, exp:0, gold:300,
    skin:'wizard', skins:{wizard:true},
    atkLv:0, defLv:0,
    statPoints:0, stats:{str:10, dex:10, vit:10},
    quest:{current:0, targetMax:5, goldReward:50, expReward:20},
    critLv:0,
    coll:{}, mastery:0, totalKills:0, enhSuccess:0, maxStage:1,
    feverGauge:0, feverUntil:0, potionUntil:0,
    pity:0, pickup:0,
    talents:{aps:0, dtap:0, steal:0, critd:0, atk:0, gold:0, revive:0},
    reviveUsed:false,
    tower:1,
    invCap:30, autoSell:false,
    ach:{},
    day:'', goldDgnUses:0, bounty:{need:20, cur:0},
    mine:{on:false, start:0}, exp2:{start:0},
    bm:{seed:0, bought:{}},
    freeAt:0,
    runStart:Date.now(), runDone:false, speedBest:0,
    petStars:{},
    settings:{sfx:true, bgm:true, shake:true, dmgSize:1, dmgColor:'default', theme:'purple'},
    stage:1, kills:0,
    pHp:1, // 비율로 저장
    inv:{}, stones:0, equips:[], nextId:1,
    weapon:null, armor:null,
    shards:0, shardsEarned:0, rebirths:0,
    artifacts:{atk:0, gold:0, boss:0, crit:0},
    pets:{},
    dlc:{supporter:false, offline:false},
    savedAt:Date.now(),
  };
}


// ---------- 펫 효과 합산 (보유한 모든 펫의 eff를 합산) ----------
function petBonus(kind){
  let mult = 1;
  if(!S || !S.pets) return mult;
  for(const p of PETS){
    if(!S.pets[p.id] || !p.eff) continue;
    const m = p.eff.match(/^([a-z]+)(\d+)$/);
    if(!m) continue;
    if(m[1] !== kind) continue;
    let v = parseInt(m[2]) / 100;
    const stars = (S.petStars && S.petStars[p.id]) || 0;
    v *= (1 + stars * 0.1);   // 성급당 효과 +10%
    mult *= (1 + v);
  }
  return mult;
}
function petAssistRate(){
  let r = 0;
  if(!S || !S.pets) return r;
  for(const p of PETS){
    if(!S.pets[p.id] || !p.eff) continue;
    const m = p.eff.match(/^assist(\d+)$/);
    if(m) r += parseInt(m[1]) / 100;
  }
  return Math.min(2, r);
}
/* ---------- 파생 스탯 ---------- */

// 개발자 장비의 Infinity를 JSON에 안전하게 저장/복원
function reviveDevItems(st){
  // 구버전 세이브 호환 (스킨/사운드 필드 보강)
  if(st && typeof st === 'object'){
    if(!st.skin) st.skin = 'wizard';
    if(!st.skins) st.skins = {wizard:true};
    if(!st.settings) st.settings = {};
    if(st.settings.bgm === undefined) st.settings.bgm = true;
    if(st.settings.sfx === undefined) st.settings.sfx = true;
  }
  if(st && Array.isArray(st.equips)){
    st.equips.forEach(e => {
      if(e && (e.dev || e.grade === 'Developer')) e.base = Infinity;
    });
  }
  return st;
}
function eqById(id){ return S.equips.find(e=>e.id===id) || null; }
function eqPower(e){
  if(!e) return 0;
  if(e.dev || e.grade === 'Developer' || e.base === Infinity) return Infinity;
  return Math.round(e.base * (1 + 0.1*e.enh) * Math.pow(2, e.awk||0));
}
function playerATK(){
  // ⚖️ 초반 약화 밸런스: 기본 공격력을 낮추고, 강화/스탯 투자 비중을 높임
  let a = 3 + S.level*1 + BAL.upBonus(8, S.atkLv);   // 기본 3, 레벨당 +1, 강화 보너스 강화(base 5→8)
  a += (S.stats.str-10)*5;                            // 힘 1당 +5 (기존 +3) → 스탯 찍는 맛

  const w = eqById(S.weapon); if(w) a += eqPower(w);
  a *= 1 + 0.05*S.artifacts.atk;
  a *= 1 + 0.05*(S.talents.atk||0);                              // 특성 트리
  a *= 1 + 0.01*Object.keys(S.coll||{}).length;                  // 무기 도감
  a *= 1 + Math.min(0.5, (S.mastery||0)*0.0001);                 // 숙련도
  a *= 1 + 0.02*totalPetStars();                                 // 펫 성급
  if(Date.now() < S.potionUntil) a *= 1.5;                       // 물약
  if(Date.now() < S.feverUntil) a *= 2;                          // 피버
  a *= petBonus('atk');
  return Math.round(a);
}
function playerDEF(){
  // ⚖️ 초반 약화: 레벨 비중↓, 방어 강화 비중↑
  let d = 1 + Math.floor(S.level*0.5) + BAL.upBonus(4, S.defLv);
  const ar = eqById(S.armor); if(ar) d += eqPower(ar);
  if(S.pets.golemp) d *= 1.20;
  d *= petBonus('def');
  return Math.round(d);
}
function playerMaxHP(){ return 60 + S.level*10 + playerDEF()*3 + (S.stats.vit-10)*40; }  // ⚖️ 기본↓ 레벨↓, 체력 스탯 1당 +40
function critRate(){ return Math.min(0.8, 0.05 + 0.01*S.artifacts.crit + 0.01*(S.stats.dex-10)); }
function goldMult(){
  let m = 1 + 0.05*S.artifacts.gold;
  if(S.pets.batp) m *= 1.15;
  m *= petBonus('gold');
  if(S.dlc.supporter) m *= 2;
  m *= 1 + 0.05*(S.talents.gold||0);
  if(Date.now() < S.feverUntil) m *= 3;
  return m;
}
function bossTimeMax(){ return BAL.bossTime + 2*S.artifacts.boss; }
function worldOf(stage){
  const s = stage > 100 ? ((stage - 101) % 100) + 1 : stage;
  return WORLDS[(Math.ceil(s/10)-1) % WORLDS.length];
}
function worldIdx(stage){ const s = stage > 100 ? ((stage-101)%100)+1 : stage; return (Math.ceil(s/10)-1) % WORLDS.length; }
function stageLabel(stage){ return tierStageLabel(stage); }

/* ---------- 숫자 표기 (K/M/B…) ---------- */
const UNITS = ['','K','M','B','T','Qa','Qi','Sx','Sp','Oc','No','Dc','UDc','DDc','TDc','QaDc','QiDc','SxDc','SpDc','OcDc','NoDc','Vg','UVg','DVg','TVg','QaVg','QiVg','SxVg','SpVg','OcVg','NoVg','Tg','UTg','DTg','TTg','QaTg','QiTg','SxTg','SpTg','OcTg','NoTg','Qd','UQd','DQd','TQd','QaQd','QiQd','SxQd','SpQd','OcQd','NoQd','Qq','UQq','DQq','TQq','QaQq','QiQq','SxQq','SpQq','OcQq','NoQq'];

// 무한(∞) HP에서도 안전한 퍼센트 계산 (Infinity/Infinity = NaN 방지)
function safePct(cur, max){
  if(!isFinite(max) || max <= 0) return 100;
  if(!isFinite(cur)) return 100;
  const p = cur / max * 100;
  return isNaN(p) ? 0 : Math.max(0, Math.min(100, p));
}
function fmt(n){
  if(!isFinite(n)) return '∞';      // 개발자 장비 = 무한(∞) 표시
  if(isNaN(n)) return '0';
  if(n < 1000) return Math.floor(n).toString();
  let u = 0;
  while(n >= 1000 && u < UNITS.length-1){ n/=1000; u++; }
  return (n>=100? n.toFixed(0) : n.toFixed(1)) + UNITS[u];
}

/* ---------- 저장 / 불러오기 (window.storage → 메모리 폴백) ---------- */
const SAVE_KEY = 'rift-shop-save-v1';
const BACKUP_KEY = 'rift-shop-backup-v1';
const SYNC_KEY = 'rift-shop-sync-time';
let memSave = null;

/* ---------- 고유이름 / 관리자 계정 ---------- */
const ADMIN_NICK = '개발자';
const ADMIN_PASSWORD = 'adadawdsajdiqahdxahudguxajhdhasgdxhagdahzgdahgrhagert324513461741241247162415462712471264521561756607906jasbfuhsabfuhsgbauhabf';  // 이 비밀번호를 아는 사람만 "개발자" 닉네임을 쓸 수 있음



/* ---------- 오프라인 보상 ----------
   초당 골드 = 현재 스테이지 골드드랍 / 평균 처치시간(3.5s) x 50% 효율 */
function calcOffline(elapsedSec){
  const capH = S.dlc.offline ? 24 : 12;
  const sec = Math.min(elapsedSec, capH*3600);
  const gps = BAL.goldDrop(S.stage) / 3.5 * 0.6 * goldMult();
  const eps = BAL.expDrop(S.stage)  / 3.5 * 0.6;
  return { sec, gold:Math.floor(gps*sec), exp:Math.floor(eps*sec), capH };
}
function fmtDur(sec){
  const h = Math.floor(sec/3600), m = Math.floor(sec%3600/60);
  return (h>0? h+'시간 ' : '') + m + '분';
}

/* ---------- 전투 엔티티 ---------- */
let mob = null;        // {hp, maxHp, atk, isBoss}
let bossLeft = 0;      // 보스 남은 시간(초)
let deadUntil = 0;     // 플레이어 사망 후 부활 시각
let pHpCur = 1;        // 실수 HP

function spawnMob(isBoss){
  const s = S.stage;
  if(battleMode==='tower'){
    const thp = 30*Math.pow(1.4, S.tower);
    mob = {hp:thp, maxHp:thp, atk:BAL.monsterATK(Math.max(1,Math.min(s,S.tower)))*1.2, isBoss:true, tower:true, el:worldOf(S.tower).el, shield:0};
    mFlash=0; mShake=0; mobX=470; return;
  }
  if(battleMode==='golddgn'){
    mob = {hp:1e18, maxHp:1e18, atk:0, isBoss:true, sandbag:true, el:null, shield:0};
    mFlash=0; mShake=0; mobX=470; return;
  }
  const w = worldOf(s);
  const stageMob = getStageMob(s);  // 스테이지별 고정 몬스터
  const hp = BAL.monsterHP(s) * (isBoss ? BAL.bossHPMul : 1);
  mob = { hp, maxHp:hp, atk:BAL.monsterATK(s)*(isBoss?1.5:1), isBoss:!!isBoss, el:stageMob.el, shield:0, name: isBoss ? w.bossName : stageMob.mob, spr: stageMob.spr, pal: stageMob.pal || stageMob.spr };
  if(isBoss && worldIdx(s)%2===1){
    mob.shield = hp*0.3; mob.shieldMax = mob.shield;
    log('<span class="c">🛡 보호막 보스! 파란 보호막을 먼저 부수세요.</span>');
  }
  if(!isBoss && Math.random()<0.01){
    mob.golden = true; mob.until = Date.now()+10000;
    mob.hp = mob.maxHp = hp*3;
    log('<span class="g">✨ 황금 슬라임 출현! 10초 안에 최대한 두들기세요!</span>');
  }
  if(isBoss){ bossLeft = bossTimeMax(); if(S.settings.shake) bgShake = 7; flashT = 0.9; }
  mFlash = 0; mShake = 0;
  mobX = 470; // 차원 균열에서 등장해 걸어 들어옴
}

/* ---------- 드랍 처리 ---------- */
function rollDrops(isBoss){
  const w = worldOf(S.stage), wi = worldIdx(S.stage);
  const mult = isBoss ? 3 : 1;
  for(let i=0;i<mult;i++){
    const r = Math.random();
    let acc = 0;
    for(const d of DROP_TABLE){
      acc += d.p;
      if(r < acc){
        if(d.kind==='mat'){ addMat(w.mat, 1); }
        else if(d.kind==='stone'){ S.stones++; log('<span class="c">강화석</span> 획득!'); }
        else { dropEquip(wi, isBoss); }
        break;
      }
    }
  }
  if(isBoss){ addMat(w.mat, 3); }
}
function addMat(name, n){
  S.inv[name] = (S.inv[name]||0) + n;
}
function rollGrade(isBoss, stage){
  // 스테이지가 높을수록 상위 등급 확률 상승, 보스는 추가 보너스
  const lucky = (stage/100) + (isBoss ? 0.6 : 0);
  let total = 0;
  const weights = GRADES.map((g, i) => {
    // i가 높은(희귀한) 등급일수록 lucky 보정을 크게 받음
    const w = GRADE_WEIGHT[g] * (1 + lucky * i * 0.9);
    total += w;
    return w;
  });
  let r = Math.random() * total;
  for(let i = 0; i < GRADES.length; i++){
    r -= weights[i];
    if(r <= 0) return GRADES[i];
  }
  return GRADES[0];
}

function dropEquip(wi, isBoss){
  const type = Math.random()<0.5 ? 'weapon' : 'armor';
  const grade = rollGrade(isBoss, S.stage);
  const pool = (type==='weapon' ? WEAPON_BASE : ARMOR_BASE);
  // 스테이지가 오를수록 후반부(강한) 장비가 나올 확률 증가
  const span = Math.max(6, Math.floor(pool.length * (0.12 + S.stage/100 * 0.88)));
  const baseName = pool[Math.floor(Math.random() * Math.min(span, pool.length))];
  const gm = Math.pow(2.4, GRADES.indexOf(grade));
  const base = Math.round((type==='weapon'?8:5) * Math.pow(1.18, S.stage-1) * gm);
  // 자동 판매 필터
  if(S.autoSell && (grade==='Normal' || grade==='Rare')){
    S.gold += Math.floor(base*2); recGold(Math.floor(base*2));
    return;
  }
  if(S.equips.length >= S.invCap){
    const sell = Math.floor(base*2);
    S.gold += sell; recGold(sell);
    log('인벤토리가 가득 차 <span class="g">'+fmt(sell)+' 골드</span>로 자동 판매!');
    return;
  }
  const it = {id:S.nextId++, type, grade, name:baseName, base, enh:0};
  if(type==='weapon' && Math.random()<0.35) it.el = ELEM_KEYS[Math.floor(Math.random()*5)];
  S.equips.push(it);
  if(type==='weapon') collAdd(baseName);
  const gi = GRADES.indexOf(grade);
  const msg = '<span class="'+GRADE_CLS[grade]+'" style="color:'+GRADE_COLOR[grade]+'">['+GRADE_KO[grade]+'] '+GRADE_PFX[grade]+' '+baseName+'</span> 드랍!';
  log(gi >= 4 ? '✨ ' + msg : msg);
  renderEquip();
}

/* ---------- 장비: 장착 / 합성 / 강화 ---------- */
function equipItem(id){
  const e = eqById(id); if(!e) return;
  if(e.type==='weapon') S.weapon = id; else S.armor = id;
  renderEquip(); renderStats(); saveGame(true);
}
function mergeItem(id){
  { const _e = eqById(id); if(isDevItem(_e)){ log('<span class="r">개발자 장비는 합성이 필요 없습니다.</span>'); return; } }

  const e = eqById(id); if(!e) return;
  const gi = GRADES.indexOf(e.grade);
  if(gi >= GRADES.length-1) return;
  const same = S.equips.filter(x=>x.name===e.name && x.grade===e.grade && x.type===e.type && !x.lock);
  if(same.length < 3){ log('<span class="r">합성 재료 부족 (동일 장비 3개 필요)</span>'); return; }
  const three = same.slice(0,3);
  if(three.some(isDevItem)){ log('<span class="r">개발자 장비는 합성 재료가 될 수 없습니다.</span>'); return; }
  const best = Math.max(...three.map(x=>x.base));
  three.forEach(x=>{
    if(S.weapon===x.id) S.weapon=null;
    if(S.armor===x.id) S.armor=null;
    S.equips.splice(S.equips.indexOf(x),1);
  });
  const ng = GRADES[gi+1];
  const item = {id:S.nextId++, type:e.type, grade:ng, name:e.name, base:Math.round(best*3), enh:0};
  S.equips.push(item);
  log('합성 성공! <span class="'+GRADE_CLS[ng]+'">['+GRADE_KO[ng]+'] '+GRADE_PFX[ng]+' '+item.name+'</span> 획득!');
  renderEquip(); renderStats(); saveGame(true);
}
function enhCost(e){ return {stone:e.enh+1, gold:Math.round(50*Math.pow(1.8, e.enh)*Math.pow(1.1, S.stage/5))}; }
function enhanceItem(id){
  const e = eqById(id); if(!e || e.enh>=10) return;
  const c = enhCost(e);
  if(S.stones < c.stone || S.gold < c.gold){ log('<span class="r">강화 재료 부족</span>'); return; }
  S.stones -= c.stone; S.gold -= c.gold; e.enh++;
  S.enhSuccess = (S.enhSuccess||0)+1;
  log('<span class="c">'+GRADE_PFX[e.grade]+' '+e.name+' +'+e.enh+'</span> 강화 성공! (+10% 성능)');
  renderEquip(); renderStats(); saveGame(true);
}

/* ---------- 스탯 강화 ---------- */
function upStat(kind){
  const n = kind==='atk'? S.atkLv : kind==='def'? S.defLv : S.critLv;
  const cost = BAL.upCost(kind==='atk'?15: kind==='def'?12:20, n);
  if(S.gold < cost) return false;
  S.gold -= cost;
  if(kind==='atk') S.atkLv++; else if(kind==='def') S.defLv++; else S.critLv++;
  renderStats(); saveGame(true);
  return true;
}

/* ---------- 레벨업 ---------- */
function gainExp(x){
  S.exp += x;
  let req = BAL.expReq(S.level);
  while(S.exp >= req){
    S.exp -= req; S.level++;
    S.statPoints += 4;
    pHpCur = playerMaxHP();
    sfx('levelup'); log('<span class="p">LEVEL UP!</span> LV.'+S.level+' 달성 (HP 완전 회복)');
    req = BAL.expReq(S.level);
  }
}

/* ---------- 환생 & 유물 ---------- */
function rebirthGain(){ return Math.max(0, BAL.shardsFor(S.stage) - S.shardsEarned); }
function doRebirth(){
  const gain = rebirthGain();
  if(gain <= 0){ log('<span class="r">아직 조각을 얻을 수 없습니다. 더 깊은 차원으로!</span>'); return; }
  S.shards += gain; S.shardsEarned += gain; S.rebirths++;
  S.level=1; S.exp=0; S.gold=0; S.atkLv=0; S.defLv=0;
  S.stage=1; S.kills=0; S.inv={}; S.stones=0;
  S.equips=[]; S.weapon=null; S.armor=null;
  S.runStart = Date.now(); S.runDone = false;
  S.reviveUsed = false; S.feverGauge = 0; S.feverUntil = 0; S.potionUntil = 0;
  battleMode = 'field';
  S.shardsEarned = 0; // 다음 주기 기준 재설정
  pHpCur = playerMaxHP();
  spawnMob(false);
  showModal('차원 붕괴!', '차원이 무너지고 만물상만 남았습니다.<br><span class="big">균열의 조각 +'+gain+'</span><br><b>환생 횟수: '+S.rebirths+'회</b><br>유물과 동료, DLC 효과는 유지됩니다.');
  renderAll(); saveGame(true);
}
function gachaArtifact(){
  if(S.shards < 1) return;
  S.shards--;
  const keys = Object.keys(ARTS);
  const k = keys[Math.floor(Math.random()*keys.length)];
  S.artifacts[k]++;
  log('<span class="p">'+ARTS[k].name+' Lv.'+S.artifacts[k]+'</span> 각인! ('+ARTS[k].desc+')');
  renderAll(); saveGame(true);
}

/* ---------- 동료 ---------- */
function buyPet(id){
  const p = PETS.find(x=>x.id===id); if(!p || S.pets[id]) return;
  if((S.inv[p.mat]||0) < p.need){ log('<span class="r">'+p.mat+' '+p.need+'개가 필요합니다.</span>'); return; }
  S.inv[p.mat] -= p.need; S.pets[id] = true;
  log('<span class="c">'+p.name+'</span>이(가) 동료가 되었습니다!');
  renderAll(); saveGame(true);
}

/* ---------- DLC (스팀 자리표시자) ---------- */
function buyDLC(which){
  // 실제 빌드: SteamApps.BIsDlcInstalled(APP_ID) 확인으로 대체
  S.dlc[which] = true;
  log('<span class="g">[DLC 데모] '+(which==='supporter'?'서포터 팩':'차원 시계')+' 적용!</span>');
  renderAll(); saveGame(true);
}

/* ---------- 전투 루프 ---------- */
const PLAYER_ATK_MS = 700, MOB_ATK_MS = 1100, PET_ATK_MS = 1200;
let tP=0, tM=0, tPet=0, lastTick=performance.now();

function combatTick(now){
  const dt = Math.min(200, now - lastTick); lastTick = now;
  if(!mob) spawnMob(false);
  const dead = now < deadUntil;

  // 보스 타이머
  if(mob.isBoss && !mob.tower && !mob.sandbag){
    bossLeft -= dt/1000;
    // 😡 분노(Enrage): 남은 시간 10초 이하 → 공격력 5배
    if(!mob.enraged && bossLeft <= 10){
      mob.enraged = true; mob.atk *= 5;
      log('<span class="r">😡 보스 분노! 공격력이 5배로 폭등합니다!</span>');
      if(S.settings.shake) bgShake = 8;
    }
    if(bossLeft <= 0){
      log('<span class="r">보스 격퇴 실패… 일반 사냥으로 복귀합니다.</span>');
      S.kills = 0; spawnMob(false);
    }
  }
  // ✨ 황금 슬라임 도주
  if(mob.golden && Date.now() > mob.until){
    log('<span class="g">황금 슬라임이 도망쳤습니다…</span>');
    spawnMob(false);
  }
  // ⛏ 미다스의 방 종료
  if(battleMode==='golddgn' && Date.now() > dgnUntil){
    battleMode = 'field';
    log('<span class="g">⛏ 미다스의 방 종료! 총 획득: '+fmt(dgnGold)+'G</span>');
    spawnMob(false);
  }

  // 몬스터 입장 걸음 (사거리 밖이면 서로 공격 불가)
  if(mob && mobX > mobTX()){
    mobX = Math.max(mobTX(), mobX - (mob.isBoss? 0.22 : 0.34)*dt);
  }

  if(!dead){
    // 자연 회복 (초당 최대 HP 1.5%)
    pHpCur = Math.min(playerMaxHP(), pHpCur + playerMaxHP()*0.015*dt/1000);

    // ⚡ APS 특성: 특성을 찍으면 초당 자동 공격 (기본은 수동 클릭)
    if((S.talents.aps||0) > 0){
      apsAcc += dt;
      const interval = 1000/(0.5*S.talents.aps);
      let guard = 0;
      while(apsAcc >= interval && guard++ < 10){ apsAcc -= interval; heroStrike(false, false); }
    }
    if(S.pets.slimep){
      tPet += dt;
      if(tPet >= PET_ATK_MS && mobInRange()){ tPet=0; hitMob(playerATK()*0.2, false, true); }
    }
    tM += dt;
    if(tM >= MOB_ATK_MS && mob.hp > 0 && mobInRange() && !mob.sandbag && now > reviveInvUntil){
      tM = 0;
      const dmg = Math.max(1, mob.atk*(0.9+Math.random()*0.2) - playerDEF()*0.5);
      pHpCur -= dmg;
      addDmgNum(dmg, 'player', false);
      pFlash = 1; mLunge = 1;
      if(pHpCur <= 0){
        if((S.talents.revive||0) > 0 && !S.reviveUsed){
          S.reviveUsed = true;
          pHpCur = playerMaxHP()*0.2;
          reviveInvUntil = now + 3000;
          log('<span class="p">✝ 불굴 발동! 3초 무적 · HP 20% 회복</span>');
        } else {
          pHpCur = 0; deadUntil = now + 3000;
          if(S.settings.shake) bgShake = 6;
          log('<span class="r">쓰러졌습니다… 3초 후 부활</span>');
          if(mob.isBoss && !mob.tower && !mob.sandbag){ S.kills=0; spawnMob(false); }
        }
      }
    }
  } else if(now >= deadUntil - 50 && pHpCur <= 0){
    pHpCur = playerMaxHP();
  }
}
function hitMob(dmg, crit, byPet){
  if(!mob) return;
  // 🛡 실드: 보호막 먼저 파괴
  if(mob.shield > 0){
    mob.shield -= dmg;
    addDmgNum(dmg, 'shield', false, byPet);
    mFlash = 1; mShake = 1;
    if(mob.shield <= 0){ mob.shield = 0; log('<span class="c">🛡 보호막 파괴! 본체 공격 가능!</span>'); }
    sfx('hit');
    return;
  }
  // ⛏ 미다스의 방: 때리는 만큼 골드
  if(mob.sandbag){
    const g = Math.floor(dmg*0.4*goldMult());
    S.gold += g; dgnGold += g; recGold(g); recDmg(dmg);
    addDmgNum(dmg, 'mob', crit, byPet);
    mFlash = 1; mShake = 1;
    sfx(crit?'crit':'hit');
    return;
  }
  if(mob.hp<=0) return;
  mob.hp -= dmg;
  recDmg(dmg);
  addDmgNum(dmg, 'mob', crit, byPet);
  addSlash(byPet, crit);
  mFlash = 1; mShake = 1;
  if(crit && S.settings.shake) bgShake = Math.max(bgShake, 3);
  sfx(crit?'crit':'hit');
  // ✨ 황금 슬라임: 때릴 때마다 골드
  if(mob.golden){
    const gg = Math.floor(BAL.goldDrop(S.stage)*2*goldMult());
    S.gold += gg; recGold(gg);
  }
  if(mob.hp <= 0){
    deathFX(); sfx('kill');
    S.totalKills = (S.totalKills||0)+1;
    if(eqById(S.weapon)) S.mastery = (S.mastery||0)+1;                       // 숙련도
    if(S.talents.steal>0) pHpCur = Math.min(playerMaxHP(), pHpCur + playerMaxHP()*0.01*S.talents.steal); // 흡혈
    // 🔥 피버 게이지
    if(Date.now() >= S.feverUntil){
      S.feverGauge = Math.min(100, (S.feverGauge||0)+4);
      if(S.feverGauge >= 100){
        S.feverGauge = 0; S.feverUntil = Date.now()+10000;
        log('<span class="g">🔥 피버 타임! 10초간 대미지 x2 · 골드 x3</span>');
        if(S.settings.shake) bgShake = 6;
      }
    }
    // 🗼 무한의 탑
    if(battleMode==='tower'){
      const fg = Math.floor(20*Math.pow(1.3, S.tower)*goldMult());
      S.gold += fg; recGold(fg);
      let bonus='';
      if(S.tower%5===0){ S.shards++; bonus=' <span class="p">+조각 1</span>'; }
      log('<span class="c">🗼 '+S.tower+'층 클리어!</span> <span class="g">+'+fmt(fg)+'G</span>'+bonus);
      S.tower++;
      checkAchievements();
      spawnMob(false); renderStats(); return;
    }
    const wasBoss = mob.isBoss, wasGold = mob.golden;
    // 일반 몬스터는 골드를 조금만 지급 (보스/황금 슬라임은 대량)
    const g = Math.max(1, Math.floor(BAL.goldDrop(S.stage) * (wasBoss?5: wasGold?30:0.3) * goldMult()));
    S.gold += g; recGold(g);
    gainExp(Math.floor(BAL.expDrop(S.stage) * (wasBoss?5:1)));
    rollDrops(wasBoss);
    // 📜 현상 수배
    if(S.bounty && S.bounty.cur < S.bounty.need){
      S.bounty.cur++;
      if(S.bounty.cur >= S.bounty.need){
        const bg = Math.floor(BAL.goldDrop(S.stage)*40);
        S.gold += bg; recGold(bg); S.shards++;
        log('<span class="g">📜 현상 수배 완료! +'+fmt(bg)+'G · 조각 +1</span>');
      }
    }
    if(wasBoss){
      const _prevStage = S.stage;
      if(S.stage >= MAX_STAGE){
        // 🔁 최종 스테이지 무한 반복 (클리어 횟수 누적)
        S.kills = 0; S.reviveUsed = false;
        S.endlessClears = (S.endlessClears || 0) + 1;
        if(!S.allClear){
          S.allClear = true;
          const _t = tierOf(MAX_STAGE);
          log('<span class="gP" style="font-size:14px">🌈 모든 ' + TIERS.length + '개 차원 정복! 진정한 만물상이 되었습니다!</span>');
          log('<span class="gP">이제 ' + _t.icon + _t.name + ' 차원 최심부가 무한 반복됩니다.</span>');
        }
        // 반복할수록 보상 증가
        const _bonus = Math.floor(BAL.goldDrop(MAX_STAGE) * 10 * (1 + S.endlessClears * 0.1));
        S.gold += _bonus; recGold(_bonus);
        S.shards += 10;
        log('<span class="gP">🔁 최심부 격파 ' + S.endlessClears + '회차! +' + fmt(_bonus) + 'G · 조각 +10</span>');
        checkAchievements(); spawnMob(true);
        renderStats(); renderAll(); saveGame(true);
        return;
      }
      S.stage++; S.kills = 0; S.reviveUsed = false;
      // ⏩ 스테이지 스킵 (상위 티어에서는 스킵 없음 — 난이도 유지)
      let skip = 0;
      if(!isSpecialTier(S.stage)){
        while(skip < 4 && S.stage < 100 && playerATK() > BAL.monsterHP(S.stage)*3){ S.stage++; skip++; }
      }
      if(skip > 0) log('<span class="c">⏩ 압도적인 힘! 스테이지 '+skip+'개 스킵!</span>');
      if(S.stage > MAX_STAGE) S.stage = MAX_STAGE;
      checkTierUnlock(S.stage);   // 새 티어 진입 연출
      S.maxStage = Math.max(S.maxStage||1, S.stage);
      // ⏱ 스피드런 (50층 도달)
      if(S.stage >= 50 && !S.runDone){
        S.runDone = true;
        const t = Math.floor((Date.now()-(S.runStart||Date.now()))/1000);
        if(!S.speedBest || t < S.speedBest){ S.speedBest = t; log('<span class="p">⏱ 스피드런 신기록! 50층 도달: '+fmtDur(t)+'</span>'); }
        S.shards += 5;
        log('<span class="p">⏱ 스피드런 달성 보상: 조각 +5</span>');
      }
      // 🚪 비밀 방 (1%)
      if(Math.random() < 0.01) secretRoom();
      sfx('kill'); log('<span class="p">보스 격파!</span> 차원 <b>'+stageLabel(S.stage)+'</b> 진입 <span class="g">+'+fmt(g)+'G</span>');
      checkAchievements();
      spawnMob(false);
    } else {
      S.kills = Math.min(BAL.killsForBoss, S.kills+1);
      questProgress();
      checkAchievements();
      spawnMob(false);
    }
    renderStats();
  }
}
function tryBoss(){
  if(battleMode!=='field') return;
  if(S.kills < BAL.killsForBoss || (mob && mob.isBoss)) return;
  spawnMob(true);
  log('<span class="r">⚔ 보스전 시작! '+worldOf(S.stage).bossName+'</span> ('+bossTimeMax()+'초 제한)');
}

/* ---------- 픽셀 아트 스프라이트 (2프레임 애니메이션) ---------- */
const PAL = {
  /* ===== 스킨 팔레트 ===== */
  sk_knight:{ a:'#8a95b0', A:'#c8d2e8', d:'#4a5470', w:'#ffd23f', k:'#1a2038', s:'#f0c8a0', e:'#2a3050', h:'#6a7490' },
  sk_ninja:{ a:'#2e3444', A:'#525a70', d:'#181c28', w:'#ff5470', k:'#0a0c14', s:'#3a4254', e:'#ff5470', h:'#1a1e2a' },
  sk_mage:{ a:'#6a3aa8', A:'#a86bff', d:'#3e1f68', w:'#43e6cf', k:'#1a0a2e', s:'#f0c8a0', e:'#2a1a40', h:'#8a5ac8' },
  sk_demon:{ a:'#8a1a2e', A:'#d03a52', d:'#4a0a18', w:'#ff8a3a', k:'#1e0408', s:'#c86a70', e:'#ffd23f', h:'#6a1424' },
  sk_angel:{ a:'#e8dcb0', A:'#fff8e0', d:'#a89860', w:'#ffd23f', k:'#3a3218', s:'#f8e0c0', e:'#5a8ad0', h:'#c8b890' },
  sk_king:{ a:'#7a2a8a', A:'#c85ad8', d:'#4a1050', w:'#ffd23f', k:'#200630', s:'#f0c8a0', e:'#3a1044', h:'#9a3aaa' },
  /* ===== 무기 팔레트 (등급별로 동적 변경) ===== */
  wp_common:{ w:'#c8d2e8', s:'#8a95b0', h:'#6a4a2a', A:'#e8f0ff' },
  wp_rare:{ w:'#5ab0ff', s:'#2a70c8', h:'#6a4a2a', A:'#a8d8ff' },
  wp_epic:{ w:'#c88eff', s:'#8a3ad0', h:'#6a4a2a', A:'#e8c8ff' },
  wp_unique:{ w:'#ffd23f', s:'#c89010', h:'#6a4a2a', A:'#fff0a0' },
  wp_legend:{ w:'#ff8a3a', s:'#c85010', h:'#6a4a2a', A:'#ffc890' },
  wp_mythic:{ w:'#ff5470', s:'#c81a3a', h:'#6a4a2a', A:'#ffa8b8' },
  wp_celestial:{ w:'#43e6cf', s:'#10a890', h:'#6a4a2a', A:'#a8fff0' },
  wp_primordial:{ w:'#ffffff', s:'#c8c8ff', h:'#8a6a4a', A:'#ffffff' },
  wp_dev:{ w:'#ff2d95', s:'#ffd23f', h:'#43e6cf', A:'#ffffff' },

  /* ===== 추가 몬스터 50종 팔레트 ===== */
  n_treant:{ a:'#6a8a3a', A:'#9ac25e', d:'#3e5220', w:'#d8f0a0', k:'#16220a' },
  n_beetle:{ a:'#5a7a2e', A:'#8ab04e', d:'#324516', w:'#e0ff90', k:'#141e06' },
  n_mantis:{ a:'#6ec24e', A:'#a8e880', d:'#3a7028', w:'#ffe86a', k:'#12300a' },
  n_sunflower:{ a:'#c8a02a', A:'#f0d060', d:'#8a6a10', w:'#ffe86a', k:'#3a2c04' },
  n_bamboo:{ a:'#7ab04e', A:'#a8d878', d:'#48702a', w:'#e8ffc0', k:'#1c3008', W:'#ffffff' },
  n_moss:{ a:'#4e8a4a', A:'#7ec278', d:'#2a5228', w:'#c8f0b0', k:'#0e2210' },
  n_cactus:{ a:'#3e9a5e', A:'#6ec888', d:'#20603a', w:'#ffd8e8', k:'#0a2614' },
  n_pitcher:{ a:'#8ac24e', A:'#b8e888', d:'#527a28', w:'#d0409a', k:'#1e3208' },
  n_wisp:{ a:'#8ae86a', A:'#c0ffa0', d:'#4a9a3a', w:'#e8ffd0', k:'#1a3a12' },
  n_rootbeast:{ a:'#7a6a3a', A:'#a89a5e', d:'#4a3e1e', w:'#c8e878', k:'#1e1808' },
  n_reaper:{ a:'#3a3448', A:'#5e5674', d:'#201c2c', w:'#ff5470', k:'#0c0a14' },
  n_shade:{ a:'#4a4260', A:'#6e648a', d:'#2a2438', w:'#a86bff', k:'#100c18' },
  n_gargoyle:{ a:'#5a5a68', A:'#82828e', d:'#34343e', w:'#ff8a3a', k:'#141418' },
  n_nightmare:{ a:'#2e2a3e', A:'#4e4864', d:'#181524', w:'#ff5470', k:'#0a0810' },
  n_lich:{ a:'#4a3a6a', A:'#d8d0b8', d:'#2a1f42', w:'#43e6cf', k:'#120a24' },
  n_batswarm:{ a:'#3a2e48', A:'#5e4e70', d:'#221a2c', w:'#ffd23f', k:'#0e0a14' },
  n_voidmaw:{ a:'#1a1424', A:'#4a3a68', d:'#0c0810', w:'#a86bff', k:'#000000' },
  n_wraith:{ a:'#5e5478', A:'#8a80a4', d:'#382f4c', w:'#43e6cf', k:'#181428' },
  n_darkknight:{ a:'#3e3848', A:'#625a72', d:'#241f2e', w:'#ff5470', k:'#0e0c14' },
  n_hellhound:{ a:'#4a2a2e', A:'#7a4a4e', d:'#2a1418', w:'#ff8a3a', k:'#100608' },
  n_kraken:{ a:'#2a4a9a', A:'#5a7ec8', d:'#162a60', w:'#a8e8ff', k:'#080f28' },
  n_mermaid:{ a:'#2a9a8e', A:'#f0d0b0', d:'#146258', w:'#ffd23f', k:'#062622' },
  n_jellyfish:{ a:'#7ac8e8', A:'#c8ecfa', d:'#4088b0', w:'#ffffff', k:'#143246' },
  n_crab:{ a:'#c2542a', A:'#e88a5a', d:'#7a2e12', w:'#ffe0c0', k:'#280e04' },
  n_seahorse:{ a:'#3aa8c2', A:'#7ad0e0', d:'#1e6478', w:'#ffd23f', k:'#0a2632' },
  n_leviathan:{ a:'#1e3a7a', A:'#4a6ab0', d:'#101f48', w:'#43e6cf', k:'#060c22' },
  n_bubble:{ a:'#8ad8f0', A:'#d0f2ff', d:'#4a9ab8', w:'#ffffff', k:'#164050' },
  n_anglerfish:{ a:'#2a3a5e', A:'#4e648e', d:'#161f36', w:'#ffe86a', k:'#080c18' },
  n_tidepriest:{ a:'#3a7ab0', A:'#e0f0ff', d:'#204a70', w:'#43e6cf', k:'#0c1e30' },
  n_coral:{ a:'#e0709a', A:'#f8a8c2', d:'#a03a62', w:'#a8e8ff', k:'#3a1024' },
  n_seraph:{ a:'#e8dcb0', A:'#fff8e0', d:'#a89860', w:'#ffd23f', k:'#3a3218' },
  n_paladin:{ a:'#d8d0c0', A:'#f8f4e8', d:'#9a8f78', w:'#ffd23f', k:'#342e20' },
  n_lightorb:{ a:'#f0e08a', A:'#fffce0', d:'#b8a040', w:'#ffffff', k:'#4a3e10' },
  n_unicorn:{ a:'#f0eae0', A:'#ffffff', d:'#b8aca0', w:'#ffd23f', k:'#3a3228' },
  n_solarhawk:{ a:'#e8a83a', A:'#ffd88a', d:'#a06e10', w:'#fffbe0', k:'#3a2808' },
  n_beacon:{ a:'#c8b878', A:'#f0e8b8', d:'#8a7a40', w:'#ffe86a', k:'#2e2810' },
  n_starling:{ a:'#c8d8f8', A:'#f0f6ff', d:'#8a9ac8', w:'#ffe86a', k:'#2a3450' },
  n_clericghost:{ a:'#e0e8f0', A:'#ffffff', d:'#a0aab8', w:'#ffd23f', k:'#303840' },
  n_mirrorgolem:{ a:'#d0dae8', A:'#f4f8ff', d:'#8e98a8', w:'#43e6cf', k:'#2a3038' },
  n_dawnfox:{ a:'#f0c8a0', A:'#ffe8d0', d:'#b0865a', w:'#ffd23f', k:'#3a2818' },
  n_ifrit:{ a:'#d8442a', A:'#f08a4a', d:'#8a2010', w:'#ffe86a', k:'#300a04' },
  n_emberrat:{ a:'#b0562a', A:'#e08a52', d:'#6a2e12', w:'#ffb03a', k:'#241004' },
  n_flamesnake:{ a:'#e06a2a', A:'#ffa860', d:'#963a10', w:'#ffe86a', k:'#301004' },
  n_moltengiant:{ a:'#c2402a', A:'#e8783a', d:'#762010', w:'#ffd23f', k:'#2a0a04' },
  n_cinderbird:{ a:'#a86a4a', A:'#d89a70', d:'#684028', w:'#ff8a3a', k:'#241408' },
  n_forgegolem:{ a:'#8a6a4a', A:'#b89a70', d:'#523c28', w:'#ff6a2a', k:'#1e1408', W:'#fff0b0' },
  n_smokewraith:{ a:'#7a6a68', A:'#a89896', d:'#4a3e3c', w:'#ff8a3a', k:'#1e1818' },
  n_pyrospider:{ a:'#a03a2a', A:'#d06a4a', d:'#601a10', w:'#ffb03a', k:'#200806' },
  n_lavaworm:{ a:'#d0522a', A:'#f89a4a', d:'#802810', w:'#ffe86a', k:'#2a0c04' },
  n_sunspark:{ a:'#f0a03a', A:'#ffd88a', d:'#a86a10', w:'#fffbe0', k:'#3a2808' },

  /* ===== 신규 몬스터 30종 고유 팔레트 ===== */
  m_snail:{ a:'#8a9a4e', A:'#c2d078', d:'#55622c', w:'#e8ffd0', k:'#26300f' },
  m_toxfairy:{ a:'#9a4ed1', A:'#c88ef2', d:'#5c287e', w:'#f2d8ff', k:'#2a1236', s:'#e0c8f0' },
  m_vine:{ a:'#4ea86a', A:'#8ee0a8', d:'#2a6a40', w:'#eaffea', k:'#123a20' },
  m_dokkaebi:{ a:'#4e8a3a', A:'#7ac05e', d:'#2a5220', w:'#ffd23f', k:'#10260c' },
  m_toxtoad:{ a:'#7aa02a', A:'#b0d858', d:'#46600e', w:'#f8ffd0', k:'#1c2606' },
  m_petalspirit:{ a:'#e88ea8', A:'#fac8d8', d:'#a84e70', w:'#fff0f6', k:'#40142a' },
  m_spider:{ a:'#4a3a5e', A:'#7a659a', d:'#2a1f38', w:'#ff5470', k:'#120a1c', i:'#ff5470' },
  m_shadowcat:{ a:'#3a3348', A:'#5e5474', d:'#221d2e', w:'#ffd23f', k:'#0f0c16', n:'#191424' },
  m_ghoul:{ a:'#7a8a6a', A:'#a8ba96', d:'#4a5940', w:'#ff5470', k:'#1e2618' },
  m_crow:{ a:'#2e2e3a', A:'#4e4e60', d:'#18181f', w:'#ffd23f', k:'#0a0a0e' },
  m_abyssworm:{ a:'#5e3a8a', A:'#8e64c2', d:'#341f52', w:'#43e6cf', k:'#160a28', i:'#43e6cf' },
  m_cursedarmor:{ a:'#6a5a4a', A:'#8e7a62', d:'#3e332a', w:'#ff5470', k:'#1a1510' },
  m_icespirit:{ a:'#7ac8e8', A:'#c2ecfa', d:'#4088b0', w:'#ffffff', k:'#143246' },
  m_penguin:{ a:'#e8f2fa', A:'#ffffff', d:'#9ab8cf', w:'#3a4a5e', k:'#1c2733' },
  m_frostgiant:{ a:'#6a9ac2', A:'#a8d0ea', d:'#3a5f80', w:'#e0f6ff', k:'#16293a' },
  m_octopus:{ a:'#3a5ec2', A:'#6a8ee8', d:'#1f347e', w:'#a8e8ff', k:'#0c1436' },
  m_naga:{ a:'#2a9a8e', A:'#5ecfc2', d:'#14625a', w:'#ffd23f', k:'#062622', p:'#a06bff' },
  m_mistghost:{ a:'#9aa8b8', A:'#cfd8e2', d:'#5e6a7a', w:'#ffffff', k:'#242c36', i:'#9adcff' },
  m_angelstatue:{ a:'#d8d0b8', A:'#f2ecd8', d:'#9a8f6a', w:'#ffd23f', k:'#332c18' },
  m_lightslime:{ a:'#e8d23a', A:'#fff08a', d:'#a8901c', w:'#ffffff', k:'#4a3c0a' },
  m_crystalbfly:{ a:'#d88ee0', A:'#f2c8f8', d:'#8e4a9a', w:'#ffffff', k:'#3a1440' },
  m_sentinel:{ a:'#e8e2c8', A:'#fffbe8', d:'#b0a06a', w:'#43e6cf', k:'#3a3216' },
  m_prismgolem:{ a:'#c28ee0', A:'#ffc8f0', d:'#7a4a9a', w:'#a8fff2', k:'#2e1440' },
  m_flashfox:{ a:'#e8b23a', A:'#ffe28a', d:'#9a7210', w:'#ffffff', k:'#3a2c08', n:'#5c4610' },
  m_lavaslime:{ a:'#e05a2a', A:'#ffa03a', d:'#8e2a10', w:'#fff2b0', k:'#360e04' },
  m_fireimp:{ a:'#c23a2a', A:'#f27a4a', d:'#701a10', w:'#ffd23f', k:'#2a0806' },
  m_ashskel:{ a:'#8a8078', A:'#b8aea4', d:'#544c46', w:'#ff8a3a', k:'#201c18' },
  m_magmaturtle:{ a:'#a2402a', A:'#e07a3a', d:'#5e2010', w:'#ffd23f', k:'#260a04' },
  m_volcanobat:{ a:'#8e3a2a', A:'#c26a4a', d:'#521a10', w:'#ffa03a', k:'#1e0806' },
  m_flamespirit:{ a:'#f2843a', A:'#ffc26a', d:'#a8481c', w:'#fff2b0', k:'#33100a' },

  wizard:{ h:'#3b2a6e', H:'#6a4bd6', s:'#f2c9a0', r:'#4633a0', R:'#6a52d8', b:'#2a1f56', w:'#ffffff', e:'#43e6cf', E:'#b0fff2', g:'#ffd23f' },
  wizardG:{ h:'#6e5410', H:'#e8c33a', s:'#f2c9a0', r:'#a07a10', R:'#e8c33a', b:'#5c450e', w:'#ffffff', e:'#fff2b0', E:'#ffffff', g:'#ffd23f' },
  slime:{ a:'#2fae6f', A:'#63e89f', d:'#1c7a4b', w:'#ffffff', k:'#0c3a24' },
  bat:{ a:'#5a3f8f', A:'#8a6cd0', d:'#3a2760', w:'#ff5470', k:'#1c1233' },
  wolf:{ a:'#9fb6cf', A:'#dce9f5', d:'#5f7692', w:'#ffffff', k:'#22303f', n:'#31414f' },
  golem:{ a:'#7a6f5e', A:'#a89a83', d:'#4e463a', w:'#43e6cf', k:'#2c271f' },
  dragon:{ a:'#a23238', A:'#d8555a', d:'#5e1c22', w:'#ffd23f', k:'#2e0f13', p:'#a06bff' },
  skeleton:{ a:'#cdd3dd', A:'#f2f5f9', d:'#8a93a3', w:'#ff5470', k:'#20242e' },
  mushroom:{ a:'#d1495b', A:'#f28e9a', d:'#7e2836', w:'#fff2d8', k:'#2e1216', s:'#e8d5b0' },
  ghost:{ a:'#9db8e8', A:'#d9e6fb', d:'#5a72a8', w:'#ffffff', k:'#1c2740' },
  eye:{ a:'#b48ce8', A:'#e2d2fa', d:'#6a4bb0', w:'#ffffff', k:'#140a28', i:'#43e6cf' },
  phoenix:{ a:'#e86a2a', A:'#ffb03a', d:'#9a3410', w:'#fff2b0', k:'#3a1206' },
  goldslime:{ a:'#e8b23a', A:'#ffe28a', d:'#9a7210', w:'#ffffff', k:'#4a3608' },
};
const SPR = {
/* ===== 스킨 6종 + 무기 오버레이 6종 ===== */
sk_knight:[[
'....dddd....',
'...dAAAAd...',
'..dAAAAAAd..',
'..dhsssshd..',
'..dh.ee.hd..',
'..dhsssshd..',
'...aAAAAa...',
'..aAAwwAAa..',
'.aAAAwwAAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAd..',
'..dAAAAAAd..',
'...dd..dd...',
'...dd..dd...'],[
'............',
'....dddd....',
'...dAAAAd...',
'..dAAAAAAd..',
'..dhsssshd..',
'..dh.ee.hd..',
'..dhsssshd..',
'...aAAAAa...',
'..aAAwwAAa..',
'.aAAAwwAAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAd..',
'..dAAAAAAd..',
'...dd..dd...']],
sk_ninja:[[
'....aaaa....',
'...aaaaaa...',
'..aaaaaaaa..',
'..assssssa..',
'..as.ww.sa..',
'..assssssa..',
'...aaaaaa...',
'..aaaAAaaa..',
'.aaaaAAaaaa.',
'.aaaaAAaaaa.',
'..aaaaaaad..',
'..daaaaaad..',
'...dd..dd...',
'...dd..dd...'],[
'............',
'....aaaa....',
'...aaaaaa...',
'..aaaaaaaa..',
'..assssssa..',
'..as.ww.sa..',
'..assssssa..',
'...aaaaaa...',
'..aaaAAaaa..',
'.aaaaAAaaaa.',
'.aaaaAAaaaa.',
'..aaaaaaad..',
'..daaaaaad..',
'...dd..dd...']],
sk_mage:[[
'.....A......',
'....AAA.....',
'...AAAAA....',
'..Ahssssh...',
'..Ahs.eeh...',
'..Ahssssh...',
'...aAAAAa...',
'..aAAwwAAa..',
'.aAAAwwAAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAa..',
'..aAAAAAAa..',
'...aa..aa...',
'...dd..dd...'],[
'............',
'.....A......',
'....AAA.....',
'...AAAAA....',
'..Ahssssh...',
'..Ahs.eeh...',
'..Ahssssh...',
'...aAAAAa...',
'..aAAwwAAa..',
'.aAAAwwAAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAa..',
'..aAAAAAAa..',
'...aa..aa...']],
sk_demon:[[
'..w......w..',
'..dw....wd..',
'...dAAAAd...',
'..dAssssAd..',
'..dAs.wwsAd.',
'..dAssssAd..',
'...aAAAAa...',
'.w.aAAAAa.w.',
'.waAAAAAAaw.',
'.waAAAAAAaw.',
'..aAAAAAAa..',
'..dAAAAAAd..',
'...dd..dd...',
'...dd..dd...'],[
'............',
'..w......w..',
'..dw....wd..',
'...dAAAAd...',
'..dAssssAd..',
'..dAs.wwsAd.',
'..dAssssAd..',
'...aAAAAa...',
'.w.aAAAAa.w.',
'.waAAAAAAaw.',
'.waAAAAAAaw.',
'..aAAAAAAa..',
'..dAAAAAAd..',
'...dd..dd...']],
sk_angel:[[
'A...wwww...A',
'AA..dAAd..AA',
'AAAdAAAAdAAA',
'.AAhsssshAA.',
'.AAhs.eehAA.',
'.AAhsssshAA.',
'..AaAAAAaA..',
'..aAAwwAAa..',
'.aAAAwwAAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAa..',
'..dAAAAAAd..',
'...aa..aa...',
'...dd..dd...'],[
'............',
'A...wwww...A',
'AA..dAAd..AA',
'AAAdAAAAdAAA',
'.AAhsssshAA.',
'.AAhs.eehAA.',
'.AAhsssshAA.',
'..AaAAAAaA..',
'..aAAwwAAa..',
'.aAAAwwAAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAa..',
'..dAAAAAAd..',
'...aa..aa...']],
sk_king:[[
'..w.wwww.w..',
'..wwAAAAww..',
'...dAAAAd...',
'..dhsssshd..',
'..dh.ee.hd..',
'..dhsssshd..',
'...aAAAAa...',
'..aAAwwAAa..',
'.wAAAwwAAAw.',
'.wAAAwwAAAw.',
'..aAAAAAAa..',
'..dAAAAAAd..',
'...dd..dd...',
'...dd..dd...'],[
'............',
'..w.wwww.w..',
'..wwAAAAww..',
'...dAAAAd...',
'..dhsssshd..',
'..dh.ee.hd..',
'..dhsssshd..',
'...aAAAAa...',
'..aAAwwAAa..',
'.wAAAwwAAAw.',
'.wAAAwwAAAw.',
'..aAAAAAAa..',
'..dAAAAAAd..',
'...dd..dd...']],
wp_sword:[[
'............',
'............',
'..........w.',
'.........ww.',
'........wws.',
'.......wws..',
'......wws...',
'.....wws....',
'....hhs.....',
'...hhh......',
'..hh........',
'............',
'............',
'............'],[
'............',
'..........w.',
'.........ww.',
'........wws.',
'.......wws..',
'......wws...',
'.....wws....',
'....hhs.....',
'...hhh......',
'..hh........',
'............',
'............',
'............',
'............']],
wp_axe:[[
'............',
'.........ww.',
'........wAAw',
'.......wAAAw',
'.......wAAAw',
'........wAAw',
'.......ws...',
'......ws....',
'.....hs.....',
'....hh......',
'...hh.......',
'............',
'............',
'............'],[
'.........ww.',
'........wAAw',
'.......wAAAw',
'.......wAAAw',
'........wAAw',
'.......ws...',
'......ws....',
'.....hs.....',
'....hh......',
'...hh.......',
'............',
'............',
'............',
'............']],
wp_staff:[[
'.........A..',
'........AwA.',
'.......AwwwA',
'........AwA.',
'.........A..',
'........s...',
'.......s....',
'......s.....',
'.....s......',
'....h.......',
'...h........',
'............',
'............',
'............'],[
'............',
'.........A..',
'........AwA.',
'.......AwwwA',
'........AwA.',
'.........A..',
'........s...',
'.......s....',
'......s.....',
'.....s......',
'....h.......',
'...h........',
'............',
'............']],
wp_bow:[[
'.........h..',
'........h.h.',
'.......h..h.',
'.......h..h.',
'.......w..h.',
'.......h..h.',
'.......h..h.',
'........h.h.',
'.........h..',
'............',
'............',
'............',
'............',
'............'],[
'............',
'.........h..',
'........h.h.',
'.......h..h.',
'.......h..h.',
'.......w..h.',
'.......h..h.',
'.......h..h.',
'........h.h.',
'.........h..',
'............',
'............',
'............',
'............']],
wp_spear:[[
'..........w.',
'.........ww.',
'.........ws.',
'........ws..',
'........s...',
'.......s....',
'......s.....',
'.....s......',
'....s.......',
'...h........',
'..h.........',
'............',
'............',
'............'],[
'............',
'..........w.',
'.........ww.',
'.........ws.',
'........ws..',
'........s...',
'.......s....',
'......s.....',
'.....s......',
'....s.......',
'...h........',
'..h.........',
'............',
'............']],
wp_book:[[
'............',
'............',
'............',
'............',
'.......wwww.',
'......wAAAAw',
'......wAwAAw',
'......wAAAAw',
'......wwwww.',
'............',
'............',
'............',
'............',
'............'],[
'............',
'............',
'............',
'.......wwww.',
'......wAAAAw',
'......wAwAAw',
'......wAAAAw',
'......wwwww.',
'............',
'............',
'............',
'............',
'............',
'............']],

/* ===== 추가 몬스터 50종 픽셀 아트 ===== */
n_treant:[[
'..A..AA..A..',
'.AAAAAAAAAA.',
'..AAAAAAAA..',
'...aaaaaa...',
'..akaaaaka..',
'..aaawwaaa..',
'...aaaaaa...',
'...aa..aa...',
'..da....ad..',
'..dd....dd..'],[
'............',
'..A..AA..A..',
'.AAAAAAAAAA.',
'..AAAAAAAA..',
'...aaaaaa...',
'..akaaaaka..',
'..aaawwaaa..',
'...aaaaaa...',
'...aa..aa...',
'..da....ad..']],
n_beetle:[[
'.....w......',
'....dwd.....',
'...dAAAd....',
'..dAAAAAd...',
'.dAAkAAkAd..',
'.dAAAwwAAd..',
'.ddAAAAAdd..',
'a.dddddddd.a',
'aa.d.dd.d.aa',
'.a..a..a..a.'],[
'............',
'.....w......',
'....dwd.....',
'...dAAAd....',
'..dAAAAAd...',
'.dAAkAAkAd..',
'.dAAAwwAAd..',
'.ddAAAAAdd..',
'a.dddddddd.a',
'aa.d.dd.d.aa']],
n_mantis:[[
'..a......a..',
'..aa....aa..',
'...aaaaaa...',
'...akaaka...',
'..aaawwaaa..',
'.aa.aaaa.aa.',
'.aa.aaaa.aa.',
'....aaaa....',
'....adda....',
'...dd..dd...'],[
'............',
'..a......a..',
'..aa....aa..',
'...aaaaaa...',
'...akaaka...',
'..aaawwaaa..',
'.aa.aaaa.aa.',
'.aa.aaaa.aa.',
'....aaaa....',
'....adda....']],
n_sunflower:[[
'....wwww....',
'..wwAAAAww..',
'.wAAaaaaAAw.',
'.wAakaakAAw.',
'.wAaawwaaAw.',
'..wwAAAAww..',
'....wwww....',
'.....dd.....',
'....dddd....',
'...dd..dd...'],[
'............',
'....wwww....',
'..wwAAAAww..',
'.wAAaaaaAAw.',
'.wAakaakAAw.',
'.wAaawwaaAw.',
'..wwAAAAww..',
'....wwww....',
'.....dd.....',
'....dddd....']],
n_bamboo:[[
'...aa..aa...',
'...aa..aa...',
'..daaddaad..',
'..aakaakaa..',
'..aaaWWaaa..',
'..daaddaad..',
'..aaaaaaaa..',
'..daaddaad..',
'...aa..aa...',
'...dd..dd...'],[
'............',
'...aa..aa...',
'...aa..aa...',
'..daaddaad..',
'..aakaakaa..',
'..aaaWWaaa..',
'..daaddaad..',
'..aaaaaaaa..',
'..daaddaad..',
'...aa..aa...']],
n_moss:[[
'............',
'..aaa..aaa..',
'.aaaaaaaaaa.',
'aaAaaaaaaAaa',
'aakaaaaaakaa',
'aaaaawwaaaaa',
'.aaaaaaaaaa.',
'..daaaaaad..',
'...dddddd...',
'............'],[
'..aaa..aaa..',
'.aaaaaaaaaa.',
'aaAaaaaaaAaa',
'aakaaaaaakaa',
'aaaaawwaaaaa',
'.aaaaaaaaaa.',
'..daaaaaad..',
'...dddddd...',
'............',
'............']],
n_cactus:[[
'.....aa.....',
'.w...aa...w.',
'.aw.daad.wa.',
'.aa.akka.aa.',
'.aad.aa.daa.',
'..adaaaada..',
'...aaaaaa...',
'...aawwaa...',
'...aaaaaa...',
'...dddddd...'],[
'............',
'.....aa.....',
'.w...aa...w.',
'.aw.daad.wa.',
'.aa.akka.aa.',
'.aad.aa.daa.',
'..adaaaada..',
'...aaaaaa...',
'...aawwaa...',
'...aaaaaa...']],
n_pitcher:[[
'...ddddd....',
'..dAAAAAd...',
'..dAAAAAd...',
'.daaaaaaad..',
'.akaaaaaka..',
'.aaawwwaaa..',
'.aaaaaaaaa..',
'..aaaaaaa...',
'...aaaaa....',
'...ddddd....'],[
'............',
'...ddddd....',
'..dAAAAAd...',
'..dAAAAAd...',
'.daaaaaaad..',
'.akaaaaaka..',
'.aaawwwaaa..',
'.aaaaaaaaa..',
'..aaaaaaa...',
'...aaaaa....']],
n_wisp:[[
'.....w......',
'....wAw.....',
'...wAAAw....',
'..wAAkAAw...',
'..wAAAAAw...',
'..wAAwwAw...',
'...wAAAw....',
'....wAw.....',
'.....w......',
'............'],[
'............',
'.....w......',
'....wAw.....',
'...wAAAw....',
'..wAAkAAw...',
'..wAAAAAw...',
'..wAAwwAw...',
'...wAAAw....',
'....wAw.....',
'.....w......']],
n_rootbeast:[[
'.a........a.',
'.aa......aa.',
'..aaaaaaaa..',
'..akaaaaka..',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'.aa.aaaa.aa.',
'.dd.aaaa.dd.',
'..d.d..d.d..',
'..d.d..d.d..'],[
'............',
'.a........a.',
'.aa......aa.',
'..aaaaaaaa..',
'..akaaaaka..',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'.aa.aaaa.aa.',
'.dd.aaaa.dd.',
'..d.d..d.d..']],
n_reaper:[[
'....dddd....',
'...dAAAAd...',
'...dkAAkd..a',
'...dAAAAd.aa',
'..ddddddd.aa',
'.daaaaaaadaa',
'.daaaaaaad..',
'..daaaaad...',
'...ddddd....',
'....d.d.....'],[
'............',
'....dddd....',
'...dAAAAd...',
'...dkAAkd..a',
'...dAAAAd.aa',
'..ddddddd.aa',
'.daaaaaaadaa',
'.daaaaaaad..',
'..daaaaad...',
'...ddddd....']],
n_shade:[[
'............',
'...aaaaaa...',
'..akaaaaka..',
'..aaaaaaaa..',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'..aaaaaaaa..',
'...a.aa.a...',
'....a..a....',
'............'],[
'...aaaaaa...',
'..akaaaaka..',
'..aaaaaaaa..',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'..aaaaaaaa..',
'...a.aa.a...',
'....a..a....',
'............',
'............']],
n_gargoyle:[[
'..a......a..',
'..aa....aa..',
'.aaaaaaaaaa.',
'.aakaaaakaa.',
'.aaaawwaaaa.',
'aaaaaaaaaaaa',
'aa.aaaaaa.aa',
'...aaaaaa...',
'...dd..dd...',
'...dd..dd...'],[
'............',
'..a......a..',
'..aa....aa..',
'.aaaaaaaaaa.',
'.aakaaaakaa.',
'.aaaawwaaaa.',
'aaaaaaaaaaaa',
'aa.aaaaaa.aa',
'...aaaaaa...',
'...dd..dd...']],
n_nightmare:[[
'..w......w..',
'..aa....aa..',
'.aaaaaaaaaa.',
'.aakaaaakaa.',
'.aaaaaaaaaa.',
'..aaawwaaa..',
'..aaaaaaaa..',
'..aa.aa.aa..',
'..dd.dd.dd..',
'..dd.dd.dd..'],[
'............',
'..w......w..',
'..aa....aa..',
'.aaaaaaaaaa.',
'.aakaaaakaa.',
'.aaaaaaaaaa.',
'..aaawwaaa..',
'..aaaaaaaa..',
'..aa.aa.aa..',
'..dd.dd.dd..']],
n_lich:[[
'....dddd....',
'...dAAAAd...',
'...AkAAkA...',
'...AAAAAA...',
'..wdddddddw.',
'..waaaaaaw..',
'..waaaaaaw..',
'...aaaaaa...',
'...a.aa.a...',
'...d.dd.d...'],[
'............',
'....dddd....',
'...dAAAAd...',
'...AkAAkA...',
'...AAAAAA...',
'..wdddddddw.',
'..waaaaaaw..',
'..waaaaaaw..',
'...aaaaaa...',
'...a.aa.a...']],
n_batswarm:[[
'.a..a..a..a.',
'aaa.aaa.aaa.',
'.a...a...a..',
'..aa..aa..a.',
'.aaaa.aaaa..',
'..aa...aa...',
'.a..aaa..a..',
'aaa.akka.aaa',
'.a..aaaa..a.',
'.....aa.....'],[
'............',
'.a..a..a..a.',
'aaa.aaa.aaa.',
'.a...a...a..',
'..aa..aa..a.',
'.aaaa.aaaa..',
'..aa...aa...',
'.a..aaa..a..',
'aaa.akka.aaa',
'.a..aaaa..a.']],
n_voidmaw:[[
'..dddddddd..',
'.dAAAAAAAAd.',
'.dAwwwwwwAd.',
'.dAwaaaawAd.',
'.dAwaaaawAd.',
'.dAwwwwwwAd.',
'.dAAAAAAAAd.',
'..dddddddd..',
'............',
'............'],[
'............',
'..dddddddd..',
'.dAAAAAAAAd.',
'.dAwwwwwwAd.',
'.dAwaaaawAd.',
'.dAwaaaawAd.',
'.dAwwwwwwAd.',
'.dAAAAAAAAd.',
'..dddddddd..',
'............']],
n_wraith:[[
'.....d......',
'....ddd.....',
'...daaad....',
'..dakaakd...',
'..daaaaad...',
'..daawwad...',
'..daaaaad...',
'...daaad....',
'....d.d.....',
'............'],[
'............',
'.....d......',
'....ddd.....',
'...daaad....',
'..dakaakd...',
'..daaaaad...',
'..daawwad...',
'..daaaaad...',
'...daaad....',
'....d.d.....']],
n_darkknight:[[
'....w..w....',
'...dddddd...',
'..ddkddkdd..',
'..ddddddddd.',
'.daaaaaaad.d',
'.daaaaaaad.d',
'.dd.aaaa.dd.',
'....aaaa....',
'...dd..dd...',
'...dd..dd...'],[
'............',
'....w..w....',
'...dddddd...',
'..ddkddkdd..',
'..ddddddddd.',
'.daaaaaaad.d',
'.daaaaaaad.d',
'.dd.aaaa.dd.',
'....aaaa....',
'...dd..dd...']],
n_hellhound:[[
'.w.......w..',
'.aw.....wa..',
'.aaaaaaaaa..',
'.akaaaaaka..',
'.aaaawwwaa..',
'aaaaaaaaaa.a',
'aaaaaaaaaaaa',
'.aa.aa.aa.a.',
'.dd.dd.dd...',
'............'],[
'............',
'.w.......w..',
'.aw.....wa..',
'.aaaaaaaaa..',
'.akaaaaaka..',
'.aaaawwwaa..',
'aaaaaaaaaa.a',
'aaaaaaaaaaaa',
'.aa.aa.aa.a.',
'.dd.dd.dd...']],
n_kraken:[[
'...aAAAAa...',
'..aAAAAAAa..',
'.aAAkAAkAAa.',
'.aAAAwwAAAa.',
'.aaaaaaaaaa.',
'a.a.a..a.a.a',
'a.a.a..a.a.a',
'.a.a.aa.a.a.',
'.d.d.dd.d.d.',
'............'],[
'............',
'...aAAAAa...',
'..aAAAAAAa..',
'.aAAkAAkAAa.',
'.aAAAwwAAAa.',
'.aaaaaaaaaa.',
'a.a.a..a.a.a',
'a.a.a..a.a.a',
'.a.a.aa.a.a.',
'.d.d.dd.d.d.']],
n_mermaid:[[
'....aaaa....',
'...aAAAAa...',
'...AkAAkA...',
'...AAwwAA...',
'..aaAAAAaa..',
'...aaaaaa...',
'....aaaa....',
'...aaaaaa...',
'..aa.aa.aa..',
'.aa...aa..a.'],[
'............',
'....aaaa....',
'...aAAAAa...',
'...AkAAkA...',
'...AAwwAA...',
'..aaAAAAaa..',
'...aaaaaa...',
'....aaaa....',
'...aaaaaa...',
'..aa.aa.aa..']],
n_jellyfish:[[
'...AAAAAA...',
'..AAAAAAAA..',
'.AAAkAAkAAA.',
'.AAAAwwAAAA.',
'.AAAAAAAAAA.',
'..aa.aa.aa..',
'..a..a..a...',
'..a..a..a...',
'..d..d..d...',
'............'],[
'............',
'...AAAAAA...',
'..AAAAAAAA..',
'.AAAkAAkAAA.',
'.AAAAwwAAAA.',
'.AAAAAAAAAA.',
'..aa.aa.aa..',
'..a..a..a...',
'..a..a..a...',
'..d..d..d...']],
n_crab:[[
'.a........a.',
'.aa......aa.',
'..aaaaaaaa..',
'.aAkAAAAkAa.',
'.aAAAwwAAAa.',
'.aAAAAAAAAa.',
'..aaaaaaaa..',
'..a.a..a.a..',
'.d..d..d..d.',
'............'],[
'............',
'.a........a.',
'.aa......aa.',
'..aaaaaaaa..',
'.aAkAAAAkAa.',
'.aAAAwwAAAa.',
'.aAAAAAAAAa.',
'..aaaaaaaa..',
'..a.a..a.a..',
'.d..d..d..d.']],
n_seahorse:[[
'....aaa.....',
'...akaa.....',
'...aaaaw....',
'....aaa.....',
'....aaa.....',
'...aaaa.....',
'...aaa......',
'...aaa......',
'...aaaa.....',
'....aaa.....'],[
'............',
'....aaa.....',
'...akaa.....',
'...aaaaw....',
'....aaa.....',
'....aaa.....',
'...aaaa.....',
'...aaa......',
'...aaa......',
'...aaaa.....']],
n_leviathan:[[
'..w......w..',
'..aa....aa..',
'.aaaaaaaaaa.',
'aakaaaaaakaa',
'aaaawwwwaaaa',
'aaaaaaaaaaaa',
'.aaaaaaaaaa.',
'..aa.aa.aa..',
'...a..a..a..',
'............'],[
'............',
'..w......w..',
'..aa....aa..',
'.aaaaaaaaaa.',
'aakaaaaaakaa',
'aaaawwwwaaaa',
'aaaaaaaaaaaa',
'.aaaaaaaaaa.',
'..aa.aa.aa..',
'...a..a..a..']],
n_bubble:[[
'....AAAA....',
'..AAwAAAAA..',
'.AAAAAAAAAA.',
'.AAkAAAAkAA.',
'.AAAAwwAAAA.',
'.AAAAAAAAAA.',
'..AAAAAAAA..',
'...AAAAAA...',
'.....dd.....',
'............'],[
'............',
'....AAAA....',
'..AAwAAAAA..',
'.AAAAAAAAAA.',
'.AAkAAAAkAA.',
'.AAAAwwAAAA.',
'.AAAAAAAAAA.',
'..AAAAAAAA..',
'...AAAAAA...',
'.....dd.....']],
n_anglerfish:[[
'.....w......',
'....dw......',
'...da.......',
'..daaaaaa...',
'.daakaaaaa..',
'.daaaaaaaad.',
'.dwwwwwwaad.',
'.daaaaaaaad.',
'..daaaaaad..',
'...dd..dd...'],[
'............',
'.....w......',
'....dw......',
'...da.......',
'..daaaaaa...',
'.daakaaaaa..',
'.daaaaaaaad.',
'.dwwwwwwaad.',
'.daaaaaaaad.',
'..daaaaaad..']],
n_tidepriest:[[
'....dddd....',
'...dAAAAd...',
'...AkAAkA...',
'...AAwwAA...',
'..daaaaaad..',
'.daaaaaaaad.',
'.daa.aa.aad.',
'..d.aaaa.d..',
'....aaaa....',
'...dd..dd...'],[
'............',
'....dddd....',
'...dAAAAd...',
'...AkAAkA...',
'...AAwwAA...',
'..daaaaaad..',
'.daaaaaaaad.',
'.daa.aa.aad.',
'..d.aaaa.d..',
'....aaaa....']],
n_coral:[[
'..a..aa..a..',
'..aa.aa.aa..',
'..aaaaaaaa..',
'.aakaaaakaa.',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'..aaaaaaaa..',
'..aa.aa.aa..',
'..dd.dd.dd..',
'............'],[
'............',
'..a..aa..a..',
'..aa.aa.aa..',
'..aaaaaaaa..',
'.aakaaaakaa.',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'..aaaaaaaa..',
'..aa.aa.aa..',
'..dd.dd.dd..']],
n_seraph:[[
'A..w.ww.w..A',
'AA.dAAAAd.AA',
'AAAdkAAkdAAA',
'AAAdAAAAdAAA',
'.AAdAwwAdAA.',
'..adaaaada..',
'..adaaaada..',
'...aaaaaa...',
'...aa..aa...',
'...dd..dd...'],[
'............',
'A..w.ww.w..A',
'AA.dAAAAd.AA',
'AAAdkAAkdAAA',
'AAAdAAAAdAAA',
'.AAdAwwAdAA.',
'..adaaaada..',
'..adaaaada..',
'...aaaaaa...',
'...aa..aa...']],
n_paladin:[[
'....dddd....',
'...dAAAAd...',
'...dkAAkd...',
'...dAwwAd...',
'..dddddddd..',
'.dAaaaaaAd.w',
'.dAaaaaaAd.w',
'..d.aaaa.d.w',
'....aaaa....',
'...dd..dd...'],[
'............',
'....dddd....',
'...dAAAAd...',
'...dkAAkd...',
'...dAwwAd...',
'..dddddddd..',
'.dAaaaaaAd.w',
'.dAaaaaaAd.w',
'..d.aaaa.d.w',
'....aaaa....']],
n_lightorb:[[
'.....ww.....',
'...wwAAww...',
'..wAAAAAAw..',
'.wAAkAAkAAw.',
'.wAAAwwAAAw.',
'.wAAAAAAAAw.',
'..wAAAAAAw..',
'...wwAAww...',
'.....ww.....',
'............'],[
'............',
'.....ww.....',
'...wwAAww...',
'..wAAAAAAw..',
'.wAAkAAkAAw.',
'.wAAAwwAAAw.',
'.wAAAAAAAAw.',
'..wAAAAAAw..',
'...wwAAww...',
'.....ww.....']],
n_unicorn:[[
'.....w......',
'....wA......',
'...AAAA.....',
'..AAkAAA....',
'..AAAAAAAA..',
'.AAAAAAAAAA.',
'.AAAAAAAAAw.',
'.AA.AA.AAw..',
'.dd.dd.dd...',
'............'],[
'............',
'.....w......',
'....wA......',
'...AAAA.....',
'..AAkAAA....',
'..AAAAAAAA..',
'.AAAAAAAAAA.',
'.AAAAAAAAAw.',
'.AA.AA.AAw..',
'.dd.dd.dd...']],
n_solarhawk:[[
'w..........w',
'wA........Aw',
'wAAA.AA.AAAw',
'.AAAAAAAAAA.',
'..AAkAAkAA..',
'..AAAwwAAA..',
'...AAAAAA...',
'....AAAA....',
'....d..d....',
'............'],[
'............',
'w..........w',
'wA........Aw',
'wAAA.AA.AAAw',
'.AAAAAAAAAA.',
'..AAkAAkAA..',
'..AAAwwAAA..',
'...AAAAAA...',
'....AAAA....',
'....d..d....']],
n_beacon:[[
'.....w......',
'....www.....',
'...wAAAw....',
'...dAAAd....',
'...dkAkd....',
'..ddAAAdd...',
'..daaaaad...',
'..daaaaad...',
'...dd.dd....',
'............'],[
'............',
'.....w......',
'....www.....',
'...wAAAw....',
'...dAAAd....',
'...dkAkd....',
'..ddAAAdd...',
'..daaaaad...',
'..daaaaad...',
'...dd.dd....']],
n_starling:[[
'.w.......w..',
'..w.....w...',
'...AAAAA....',
'..AAkAAAA...',
'..AAAwwAA...',
'.AAAAAAAAA..',
'..AAAAAAA...',
'...AAAAA....',
'....d.d.....',
'............'],[
'............',
'.w.......w..',
'..w.....w...',
'...AAAAA....',
'..AAkAAAA...',
'..AAAwwAA...',
'.AAAAAAAAA..',
'..AAAAAAA...',
'...AAAAA....',
'....d.d.....']],
n_clericghost:[[
'....AAAA....',
'...AAAAAA...',
'...AkAAkA...',
'...AAwwAA...',
'..AAAAAAAA..',
'..AAAwAAAA..',
'..AAwwwAAA..',
'..AAAwAAAA..',
'...A.AA.A...',
'............'],[
'............',
'....AAAA....',
'...AAAAAA...',
'...AkAAkA...',
'...AAwwAA...',
'..AAAAAAAA..',
'..AAAwAAAA..',
'..AAwwwAAA..',
'..AAAwAAAA..',
'...A.AA.A...']],
n_mirrorgolem:[[
'..dddddddd..',
'.dAAAAAAAAd.',
'.dAwAAAAwAd.',
'.dAAkAAkAAd.',
'.dAAAwwAAAd.',
'.dAAAAAAAAd.',
'..dddddddd..',
'..dd....dd..',
'..dd....dd..',
'..dd....dd..'],[
'............',
'..dddddddd..',
'.dAAAAAAAAd.',
'.dAwAAAAwAd.',
'.dAAkAAkAAd.',
'.dAAAwwAAAd.',
'.dAAAAAAAAd.',
'..dddddddd..',
'..dd....dd..',
'..dd....dd..']],
n_dawnfox:[[
'.w........w.',
'.Aw......wA.',
'.AAA....AAA.',
'.AAAAAAAAAA.',
'.AAkAAAAkAA.',
'.AAAwwwwAAA.',
'..AAAAAAA.w.',
'..AAAAAAAww.',
'..dd..dd.w..',
'............'],[
'............',
'.w........w.',
'.Aw......wA.',
'.AAA....AAA.',
'.AAAAAAAAAA.',
'.AAkAAAAkAA.',
'.AAAwwwwAAA.',
'..AAAAAAA.w.',
'..AAAAAAAww.',
'..dd..dd.w..']],
n_ifrit:[[
'..w..ww..w..',
'..aw.aa.wa..',
'..aaaaaaaa..',
'.aakaaaakaa.',
'.aaaawwaaaa.',
'aaaaaaaaaaaa',
'aa.aaaaaa.aa',
'...aaaaaa...',
'...aa..aa...',
'...dd..dd...'],[
'............',
'..w..ww..w..',
'..aw.aa.wa..',
'..aaaaaaaa..',
'.aakaaaakaa.',
'.aaaawwaaaa.',
'aaaaaaaaaaaa',
'aa.aaaaaa.aa',
'...aaaaaa...',
'...aa..aa...']],
n_emberrat:[[
'..a......a..',
'..aa....aa..',
'..aaaaaaaa..',
'..akaaaaka..',
'..aaawwaaa..',
'.aaaaaaaaa.w',
'.aaaaaaaaaww',
'..aa.aa.aa.w',
'..dd.dd.dd..',
'............'],[
'............',
'..a......a..',
'..aa....aa..',
'..aaaaaaaa..',
'..akaaaaka..',
'..aaawwaaa..',
'.aaaaaaaaa.w',
'.aaaaaaaaaww',
'..aa.aa.aa.w',
'..dd.dd.dd..']],
n_flamesnake:[[
'....aaaa....',
'...akaakw...',
'...aaaaaw...',
'....aaa.....',
'...aaaa.....',
'..aaaa......',
'.aaaa...w...',
'.aaa...ww...',
'..aaaaaww...',
'...aaaaa....'],[
'............',
'....aaaa....',
'...akaakw...',
'...aaaaaw...',
'....aaa.....',
'...aaaa.....',
'..aaaa......',
'.aaaa...w...',
'.aaa...ww...',
'..aaaaaww...']],
n_moltengiant:[[
'...dddddd...',
'..daaaaaad..',
'..dakaakad..',
'..daawwaad..',
'.ddaaaaaadd.',
'.daaaaaaaad.',
'.dd.aaaa.dd.',
'....aaaa....',
'...ww..ww...',
'...dd..dd...'],[
'............',
'...dddddd...',
'..daaaaaad..',
'..dakaakad..',
'..daawwaad..',
'.ddaaaaaadd.',
'.daaaaaaaad.',
'.dd.aaaa.dd.',
'....aaaa....',
'...ww..ww...']],
n_cinderbird:[[
'.w........w.',
'.aw......wa.',
'.aaa.aa.aaa.',
'..aaaaaaaa..',
'..aakaakaa..',
'...aawwaa...',
'...aaaaaa...',
'....aaaa....',
'....w..w....',
'....w..w....'],[
'............',
'.w........w.',
'.aw......wa.',
'.aaa.aa.aaa.',
'..aaaaaaaa..',
'..aakaakaa..',
'...aawwaa...',
'...aaaaaa...',
'....aaaa....',
'....w..w....']],
n_forgegolem:[[
'..dd....dd..',
'..dddddddd..',
'.ddaAAAAadd.',
'.daakAAkaad.',
'.daaaWWaaad.',
'.daaaaaaaad.',
'..dddddddd..',
'..dd.dd.dd..',
'..dd.dd.dd..',
'............'],[
'............',
'..dd....dd..',
'..dddddddd..',
'.ddaAAAAadd.',
'.daakAAkaad.',
'.daaaWWaaad.',
'.daaaaaaaad.',
'..dddddddd..',
'..dd.dd.dd..',
'..dd.dd.dd..']],
n_smokewraith:[[
'.....a......',
'....aaa.....',
'...aaaaa....',
'..aakaakaa..',
'..aaawwaaa..',
'.aaaaaaaaaa.',
'..aaaaaaaa..',
'...aa.aa.a..',
'....a..a....',
'............'],[
'............',
'.....a......',
'....aaa.....',
'...aaaaa....',
'..aakaakaa..',
'..aaawwaaa..',
'.aaaaaaaaaa.',
'..aaaaaaaa..',
'...aa.aa.a..',
'....a..a....']],
n_pyrospider:[[
'.w..w..w..w.',
'.d..d..d..d.',
'..dddddddd..',
'..daaaaaad..',
'.daakaakaad.',
'.daaaaaaaad.',
'..daawwaad..',
'...dddddd...',
'..d..d..d...',
'.w...w...w..'],[
'............',
'.w..w..w..w.',
'.d..d..d..d.',
'..dddddddd..',
'..daaaaaad..',
'.daakaakaad.',
'.daaaaaaaad.',
'..daawwaad..',
'...dddddd...',
'..d..d..d...']],
n_lavaworm:[[
'....aAAa....',
'...aAwwAa...',
'...aAAAAa...',
'....aAAa....',
'...aAwwAa...',
'..aAAAAAAa..',
'...aAwwAa...',
'..aAAAAAAa..',
'.aAAAAAAAAa.',
'.dddddddddd.'],[
'............',
'....aAAa....',
'...aAwwAa...',
'...aAAAAa...',
'....aAAa....',
'...aAwwAa...',
'..aAAAAAAa..',
'...aAwwAa...',
'..aAAAAAAa..',
'.aAAAAAAAAa.']],
n_sunspark:[[
'.....w......',
'..w..A..w...',
'...wAAAw....',
'..wAAkAAw...',
'.wAAAwwAAw..',
'..wAAAAAw...',
'...wAAAw....',
'..w..A..w...',
'.....w......',
'............'],[
'............',
'.....w......',
'..w..A..w...',
'...wAAAw....',
'..wAAkAAw...',
'.wAAAwwAAw..',
'..wAAAAAw...',
'...wAAAw....',
'..w..A..w...',
'.....w......']],

/* ===== 신규 몬스터 30종 전용 픽셀 아트 ===== */
m_snail:[[
'.....w..w...',
'....dwddwd..',
'...dAaaaAd..',
'..dAadadaAd.',
'.kdAaaaaaAd.',
'.k.dAdadAd..',
'.aa.dddddd..',
'.aaaaaaaaaa.',
'aaaaaaaaaaad',
'.dddddddddd.'],[
'............',
'.....w..w...',
'....dwddwd..',
'...dAaaaAd..',
'..dAadadaAd.',
'.kdAaaaaaAd.',
'.k.dAdadAd..',
'.aa.dddddd..',
'.aaaaaaaaaa.',
'aaaaaaaaaaad']],
m_toxfairy:[[
'....AAAA....',
'..AAwAAwAA..',
'.AAAAAAAAAA.',
'.dddddddddd.',
'...ssssss...',
'...sk..ks...',
'...ssssss...',
'..w.ssss.w..',
'....d..d....',
'...dd..dd...'],[
'............',
'....AAAA....',
'..AAwAAwAA..',
'.AAAAAAAAAA.',
'.dddddddddd.',
'...ssssss...',
'...sk..ks...',
'...ssssss...',
'..w.ssss.w..',
'....d..d....']],
m_vine:[[
'..a......a..',
'..da....ad..',
'...aa..aa...',
'..aAaaaaAa..',
'.aAakaakAaa.',
'.aaaaaaaaaa.',
'..aAawwaAa..',
'...aa..aa...',
'..ad....da..',
'..a......a..'],[
'............',
'..a......a..',
'..da....ad..',
'...aa..aa...',
'..aAaaaaAa..',
'.aAakaakAaa.',
'.aaaaaaaaaa.',
'..aAawwaAa..',
'...aa..aa...',
'..ad....da..']],
m_dokkaebi:[[
'.....w......',
'....dwd.....',
'...aAAAa....',
'..aAAAAAa...',
'..akAAAka...',
'..aAAwwAa.d.',
'...aaaaa.dd.',
'..aaaaaaadd.',
'..a.aaa.add.',
'...dd.dd.d..'],[
'............',
'.....w......',
'....dwd.....',
'...aAAAa....',
'..aAAAAAa...',
'..akAAAka...',
'..aAAwwAa.d.',
'...aaaaa.dd.',
'..aaaaaaadd.',
'..a.aaa.add.']],
m_toxtoad:[[
'..kA....Ak..',
'.aAAa..aAAa.',
'.aaaaaaaaaa.',
'aAaaaaaaaaAa',
'aaawwwwwwaaa',
'aaaaaaaaaaaa',
'.aaadddaaaa.',
'.ad......da.',
'.dd......dd.',
'............'],[
'............',
'..kA....Ak..',
'.aAAa..aAAa.',
'.aaaaaaaaaa.',
'aAaaaaaaaaAa',
'aaawwwwwwaaa',
'aaaaaaaaaaaa',
'.aaadddaaaa.',
'.ad......da.',
'.dd......dd.']],
m_petalspirit:[[
'.....AA.....',
'...AAAAAA...',
'..AAaAAaAA..',
'.AAAaaaaAAA.',
'.AAakaakAAA.',
'..AAawwaAA..',
'...AAAAAA...',
'....wAAw....',
'.....ww.....',
'............'],[
'............',
'.....AA.....',
'...AAAAAA...',
'..AAaAAaAA..',
'.AAAaaaaAAA.',
'.AAakaakAAA.',
'..AAawwaAA..',
'...AAAAAA...',
'....wAAw....',
'.....ww.....']],
m_spider:[[
'.d..d..d..d.',
'.d..d..d..d.',
'..dddddddd..',
'..daaaaaad..',
'.daaiaaiaad.',
'.daaaaaaaad.',
'..daawwaad..',
'...dddddd...',
'..d..d..d...',
'.d...d...d..'],[
'............',
'.d..d..d..d.',
'.d..d..d..d.',
'..dddddddd..',
'..daaaaaad..',
'.daaiaaiaad.',
'.daaaaaaaad.',
'..daawwaad..',
'...dddddd...',
'..d..d..d...']],
m_shadowcat:[[
'.k.......k..',
'.ak.....ka..',
'.aaa...aaa..',
'.aaaaaaaaa..',
'.awa...awa..',
'.aaaaaaaaa..',
'..aaaaaaa.n.',
'..aaaaaaan..',
'..aa...aa...',
'..dd...dd...'],[
'............',
'.k.......k..',
'.ak.....ka..',
'.aaa...aaa..',
'.aaaaaaaaa..',
'.awa...awa..',
'.aaaaaaaaa..',
'..aaaaaaa.n.',
'..aaaaaaan..',
'..aa...aa...']],
m_ghoul:[[
'....aaaa....',
'...aAAAAa...',
'...akAAka...',
'...aAAAAa...',
'..aaawwaaa..',
'.aa.aaaa.aa.',
'.aa.aaaa.aa.',
'.dd.aaaa.dd.',
'....aa.aa...',
'....dd.dd...'],[
'............',
'....aaaa....',
'...aAAAAa...',
'...akAAka...',
'...aAAAAa...',
'..aaawwaaa..',
'.aa.aaaa.aa.',
'.aa.aaaa.aa.',
'.dd.aaaa.dd.',
'....aa.aa...']],
m_crow:[[
'....aa......',
'...aaaa.....',
'..akaaa.....',
'..aaaaww....',
'...aaaa.....',
'..aAAAaa....',
'.aAAAAaaa...',
'.aaAAaaaa...',
'..aaaaaa....',
'...dd.dd....'],[
'............',
'....aa......',
'...aaaa.....',
'..akaaa.....',
'..aaaaww....',
'...aaaa.....',
'..aAAAaa....',
'.aAAAAaaa...',
'.aaAAaaaa...',
'..aaaaaa....']],
m_abyssworm:[[
'....aAAa....',
'...aAiiAa...',
'...aAAAAa...',
'....aAAa....',
'...aAAAAa...',
'..aAAAAAAa..',
'...aAAAAa...',
'..aAAAAAAa..',
'.aAAAAAAAAa.',
'.dddddddddd.'],[
'............',
'....aAAa....',
'...aAiiAa...',
'...aAAAAa...',
'....aAAa....',
'...aAAAAa...',
'..aAAAAAAa..',
'...aAAAAa...',
'..aAAAAAAa..',
'.aAAAAAAAAa.']],
m_cursedarmor:[[
'....dddd....',
'...dAAAAd...',
'...dAwwAd...',
'...dddddd...',
'.ddaaaaaadd.',
'.dAaaaaaaAd.',
'.dd.aaaa.dd.',
'....aaaa....',
'....adda....',
'...dd..dd...'],[
'............',
'....dddd....',
'...dAAAAd...',
'...dAwwAd...',
'...dddddd...',
'.ddaaaaaadd.',
'.dAaaaaaaAd.',
'.dd.aaaa.dd.',
'....aaaa....',
'....adda....']],
m_icespirit:[[
'.....AA.....',
'....AAAA....',
'...AAaaAA...',
'..AAakkaAA..',
'..AaawwaaA..',
'...AaaaaA...',
'....AaaA....',
'.....AA.....',
'....w..w....',
'...w....w...'],[
'............',
'.....AA.....',
'....AAAA....',
'...AAaaAA...',
'..AAakkaAA..',
'..AaawwaaA..',
'...AaaaaA...',
'....AaaA....',
'.....AA.....',
'....w..w....']],
m_penguin:[[
'....dddd....',
'...dddddd...',
'..ddkddkdd..',
'..dddwwddd..',
'..dAAAAAAd..',
'.ddAAAAAAdd.',
'.ddAAAAAAdd.',
'..dAAAAAAd..',
'...dddddd...',
'...w....w...'],[
'............',
'....dddd....',
'...dddddd...',
'..ddkddkdd..',
'..dddwwddd..',
'..dAAAAAAd..',
'.ddAAAAAAdd.',
'.ddAAAAAAdd.',
'..dAAAAAAd..',
'...dddddd...']],
m_frostgiant:[[
'...aAAAAa...',
'..aAAAAAAa..',
'..aAkAAkAa..',
'..aAAwwAAa..',
'.aaAAAAAAaa.',
'.aAaaaaaaAa.',
'.aa.aaaa.aa.',
'.dd.aaaa.dd.',
'....adda....',
'...dd..dd...'],[
'............',
'...aAAAAa...',
'..aAAAAAAa..',
'..aAkAAkAa..',
'..aAAwwAAa..',
'.aaAAAAAAaa.',
'.aAaaaaaaAa.',
'.aa.aaaa.aa.',
'.dd.aaaa.dd.',
'....adda....']],
m_octopus:[[
'....aAAa....',
'..aAAAAAAa..',
'.aAAAAAAAAa.',
'.aAkAAAAkAa.',
'.aAAAwwAAAa.',
'.aaaaaaaaaa.',
'.a.a.aa.a.a.',
'.a.a.aa.a.a.',
'.d.a.dd.a.d.',
'...d....d...'],[
'............',
'....aAAa....',
'..aAAAAAAa..',
'.aAAAAAAAAa.',
'.aAkAAAAkAa.',
'.aAAAwwAAAa.',
'.aaaaaaaaaa.',
'.a.a.aa.a.a.',
'.a.a.aa.a.a.',
'.d.a.dd.a.d.']],
m_naga:[[
'....aAAa....',
'...aAAAAa...',
'..aAkAAkAa..',
'..aAAwwAAa..',
'...aAAAAa...',
'....aAAa....',
'...aAAa.....',
'..aAAa..a...',
'..aAAaaAa...',
'...aaaaa....'],[
'............',
'....aAAa....',
'...aAAAAa...',
'..aAkAAkAa..',
'..aAAwwAAa..',
'...aAAAAa...',
'....aAAa....',
'...aAAa.....',
'..aAAa..a...',
'..aAAaaAa...']],
m_mistghost:[[
'............',
'...aaAAa....',
'..aAAAAAa...',
'.aAAiAAiAa..',
'.aAAAAAAAAa.',
'..aAAAAAAa..',
'.aAAaAAaAAa.',
'..aa..aa.a..',
'...a...a....',
'............'],[
'...aaAAa....',
'..aAAAAAa...',
'.aAAiAAiAa..',
'.aAAAAAAAAa.',
'..aAAAAAAa..',
'.aAAaAAaAAa.',
'..aa..aa.a..',
'...a...a....',
'............',
'............']],
m_angelstatue:[[
'....wwww....',
'....aAAa....',
'A..aAkkAa..A',
'AA.aAAAAa.AA',
'AAAaAwwAaAAA',
'.AAaaaaaaAA.',
'..AaaaaaaA..',
'...aaaaaa...',
'...aadaaa...',
'...dddddd...'],[
'............',
'....wwww....',
'....aAAa....',
'A..aAkkAa..A',
'AA.aAAAAa.AA',
'AAAaAwwAaAAA',
'.AAaaaaaaAA.',
'..AaaaaaaA..',
'...aaaaaa...',
'...aadaaa...']],
m_lightslime:[[
'.....w......',
'....www.....',
'.....w......',
'...AAAAAA...',
'..AaaaaaaA..',
'.Aaak..kaaA.',
'.Aaaaaaaaaa.',
'aaaaawwaaaaa',
'.aaaaaaaaad.',
'..dd.dd.dd..'],[
'............',
'.....w......',
'....www.....',
'.....w......',
'...AAAAAA...',
'..AaaaaaaA..',
'.Aaak..kaaA.',
'.Aaaaaaaaaa.',
'aaaaawwaaaaa',
'.aaaaaaaaad.']],
m_crystalbfly:[[
'.aAA....AAa.',
'aAAAa..aAAAa',
'aAwAAddAAwAa',
'aAAAAddAAAAa',
'.aAAAddAAAa.',
'..aAAddAAa..',
'...aAddAa...',
'....kddk....',
'.....dd.....',
'.....dd.....'],[
'............',
'.aAA....AAa.',
'aAAAa..aAAAa',
'aAwAAddAAwAa',
'aAAAAddAAAAa',
'.aAAAddAAAa.',
'..aAAddAAa..',
'...aAddAa...',
'....kddk....',
'.....dd.....']],
m_sentinel:[[
'....aaaa....',
'...aAkkAa...',
'...aaaaaa...',
'..dddddddd..',
'..dAAwwAAd..',
'..dAAwwAAd..',
'..dAAAAAAd..',
'..dddddddd..',
'....a..a....',
'...dd..dd...'],[
'............',
'....aaaa....',
'...aAkkAa...',
'...aaaaaa...',
'..dddddddd..',
'..dAAwwAAd..',
'..dAAwwAAd..',
'..dAAAAAAd..',
'..dddddddd..',
'....a..a....']],
m_prismgolem:[[
'..A......A..',
'..AA.AA.AA..',
'...AAAAAA...',
'..AAkAAkAA..',
'..AAAwwAAA..',
'.AAAaaaaAAA.',
'..AAaaaaAA..',
'...AAaaAA...',
'....AAAA....',
'...dd..dd...'],[
'............',
'..A......A..',
'..AA.AA.AA..',
'...AAAAAA...',
'..AAkAAkAA..',
'..AAAwwAAA..',
'.AAAaaaaAAA.',
'..AAaaaaAA..',
'...AAaaAA...',
'....AAAA....']],
m_flashfox:[[
'.k........k.',
'.ak......ka.',
'.aaa....aaa.',
'.aaaaaaaaaa.',
'.akaaaaaaka.',
'.aaawwwwaaa.',
'..aaaaaaa.n.',
'..aaaaaaann.',
'..aa..aa.n..',
'..dd..dd....'],[
'............',
'.k........k.',
'.ak......ka.',
'.aaa....aaa.',
'.aaaaaaaaaa.',
'.akaaaaaaka.',
'.aaawwwwaaa.',
'..aaaaaaa.n.',
'..aaaaaaann.',
'..aa..aa.n..']],
m_lavaslime:[[
'..w..w..w...',
'...AAAAAA...',
'..AaaaaaaA..',
'.Aaak..kaaA.',
'.AaawAAwaaA.',
'aaaaaaaaaaaa',
'aaawaaaawaad',
'.aaaaaaaaad.',
'..dddddddd..',
'...w....w...'],[
'............',
'..w..w..w...',
'...AAAAAA...',
'..AaaaaaaA..',
'.Aaak..kaaA.',
'.AaawAAwaaA.',
'aaaaaaaaaaaa',
'aaawaaaawaad',
'.aaaaaaaaad.',
'..dddddddd..']],
m_fireimp:[[
'.w.......w..',
'.aw.....wa..',
'..aaaaaaa...',
'..akaaaka...',
'..aaawwaa...',
'.d.aaaaa.d..',
'.ddaaaaadd..',
'...aaaaa....',
'...a...a..A.',
'...d...d.AA.'],[
'............',
'.w.......w..',
'.aw.....wa..',
'..aaaaaaa...',
'..akaaaka...',
'..aaawwaa...',
'.d.aaaaa.d..',
'.ddaaaaadd..',
'...aaaaa....',
'...a...a..A.']],
m_ashskel:[[
'....aaaa....',
'...aAAAAa...',
'..aAAAAAAa..',
'..akkAAkka..',
'..aAAkkAAa..',
'...aakkaa...',
'...adadad...',
'..w..aa..w..',
'.aa.aaaa.aa.',
'.dddddddddd.'],[
'............',
'....aaaa....',
'...aAAAAa...',
'..aAAAAAAa..',
'..akkAAkka..',
'..aAAkkAAa..',
'...aakkaa...',
'...adadad...',
'..w..aa..w..',
'.aa.aaaa.aa.']],
m_magmaturtle:[[
'............',
'....dddd....',
'...dAwAAd...',
'..dAAwwAAd..',
'.adAwAAwAAd.',
'aadAAAAAAAd.',
'kaadddddddd.',
'aa.aa.aa.aa.',
'.d.dd.dd.d..',
'............'],[
'....dddd....',
'...dAwAAd...',
'..dAAwwAAd..',
'.adAwAAwAAd.',
'aadAAAAAAAd.',
'kaadddddddd.',
'aa.aa.aa.aa.',
'.d.dd.dd.d..',
'............',
'............']],
m_volcanobat:[[
'w..........w',
'aw........wa',
'aaw..aa..waa',
'aaaaaaaaaaaa',
'aaaakaakaaaa',
'.aaaawwaaaa.',
'..aaaaaaaa..',
'...aa..aa...',
'...w....w...',
'............'],[
'............',
'w..........w',
'aw........wa',
'aaw..aa..waa',
'aaaaaaaaaaaa',
'aaaakaakaaaa',
'.aaaawwaaaa.',
'..aaaaaaaa..',
'...aa..aa...',
'...w....w...']],
m_flamespirit:[[
'.....a......',
'....aAa.....',
'...aAAAa.a..',
'..aAAwAAaAa.',
'..aAkwwkAAa.',
'.aAAwwwwAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAa..',
'...aAAAAa...',
'....aaaa....'],[
'............',
'.....a......',
'....aAa.....',
'...aAAAa.a..',
'..aAAwAAaAa.',
'..aAkwwkAAa.',
'.aAAwwwwAAa.',
'.aAAAwwAAAa.',
'..aAAAAAAa..',
'...aAAAAa...']],

wizard:[[
'....hhhh....',
'...hHHHHh...',
'..hHHHHHHh..',
'..hssssssh..',
'..hs.ee.sh..',
'..hssssssh..',
'...rRRRRr...',
'..rRRRRRRr..',
'.rRRRgRRRRr.',
'.rRRRgRRRRr.',
'..rRRRRRRb..',
'..bRRRRRRb..',
'...bb..bb...',
'...bb..bb...'],[
'....hhhh....',
'...hHHHHh...',
'..hHHHHHHh..',
'..hssssssh..',
'..hs.ee.sh..',
'..hssssssh..',
'...rRRRRr...',
'..rRRRRRRr..',
'.rRRRERRRRr.',
'.rRRRgRRRRr.',
'..rRRRRRRb..',
'..bRRRRRRRb.',
'...bb.bb....',
'...bb.bb....']],
slime:[[
'............',
'....AAAA....',
'..AAAAAAAA..',
'.AAaaaaaaAA.',
'.Aaak..kaaA.',
'.Aaaaaaaaaa.',
'aaaaawwaaaaa',
'aaaaaaaaaaad',
'.aaaaaaaaad.',
'..dddddddd..'],[
'............',
'............',
'...AAAAAA...',
'.AAaaaaaaAA.',
'Aaak....kaaA',
'Aaaaaaaaaaaa',
'aaaaawwaaaaa',
'aaaaaaaaaaad',
'.aaaaaaaaad.',
'..dddddddd..']],
bat:[[
'............',
'.A........A.',
'AAA......AAA',
'AaaA.aa.AaaA',
'Aaaaaaaaaaa.',
'.aaakaakaaa.',
'..aaaaaaaa..',
'...aawwaa...',
'....adda....',
'....d..d....'],[
'............',
'............',
'....aaaa....',
'.a.AaaaaA.a.',
'AAAaaaaaaAAA',
'.AAakaakAAA.',
'..aaaaaaaa..',
'...aawwaa...',
'....adda....',
'....d..d....']],
wolf:[[
'............',
'.AA......A..',
'.AaA....AA..',
'.Aaaaaaaaa..',
'.aakaaaaaan.',
'.aaaaaaaaann',
'..aaaaaaaa..',
'..aa.aa.aa..',
'..dd.dd.dd..',
'............'],[
'............',
'.AA......A..',
'.AaA....AA..',
'.Aaaaaaaaa..',
'.aakaaaaaan.',
'.aaaaaaaaann',
'..aaaaaaaa..',
'..aa.aa.aa..',
'..d.dd.dd.d.',
'............']],
golem:[[
'....AAAA....',
'...AaaaaA...',
'...aawwaa...',
'...aaaaaa...',
'.AAaaaaaaAA.',
'AaaaaaaaaaaA',
'Aaa.aaaa.aaA',
'daa.aaaa.aad',
'.d..aaaa..d.',
'....dddd....',
'...dd..dd...',
'...dd..dd...'],[
'....AAAA....',
'...AaaaaA...',
'...aakkaa...',
'...aaaaaa...',
'AAAaaaaaaAAA',
'AaaaaaaaaaaA',
'Aaa.aaaa.aaA',
'.aa.aaaa.aa.',
'.d..aaaa..d.',
'....dddd....',
'...dd..dd...',
'...dd..dd...']],
dragon:[[
'.....AAAA......',
'....AaaaaA..A..',
'...Aaawwaa.AA..',
'..AaaaaaaaAAA..',
'.AaaaaaaaaaaA..',
'AaapaaaaapaaA..',
'Aaaaapapaaaaad.',
'.aaaaaaaaaaaad.',
'.aaAAaaaaAAaa..',
'..aaaaaaaaaa...',
'...ddaaaaadd...',
'...dd.dd.dd....',
'..ddd.dd.ddd...'],[
'...............',
'.....AAAA...A..',
'....AaawwaaAA..',
'...AaaaaaaAAA..',
'..AaaaaaaaaaA..',
'.AaapaaaaapaA..',
'.aaaaapapaaaad.',
'Aaaaaaaaaaaaad.',
'AaaAAaaaaAAaa..',
'..aaaaaaaaaa...',
'...ddaaaaadd...',
'...dd.dd.dd....',
'..ddd.dd.ddd...']],
skeleton:[[
'....AAAA....',
'...AaaaaA...',
'...akaaka...',
'...aaaaaa...',
'....adda....',
'..AAaaaaAA..',
'.Aa.aaaa.aA.',
'.d..aaaa..d.',
'....aaaa....',
'...aa..aa...',
'...dd..dd...',
'............'],[
'....AAAA....',
'...AaaaaA...',
'...akaaka...',
'...aaaaaa...',
'....adda....',
'.AAAaaaaAAA.',
'.a..aaaa..a.',
'.d..aaaa..d.',
'....aaaa....',
'...aa..aa...',
'..dd....dd..',
'............']],
mushroom:[[
'...AAAAAA...',
'..AAwAAwAA..',
'.AaaaaaaaaA.',
'.Aawaaaawaa.',
'.aaaaaaaaaa.',
'..dddddddd..',
'....ssss....',
'...skssks...',
'...ssssss...',
'...ss..ss...'],[
'............',
'...AAAAAA...',
'..AAwAAwAA..',
'.Aawaaaawaa.',
'.aaaaaaaaaa.',
'..dddddddd..',
'...ssssss...',
'...skssks...',
'...ssssss...',
'...ss..ss...']],
ghost:[[
'....AAAA....',
'..AAaaaaAA..',
'.Aaak..kaaA.',
'.Aaaaaaaaaa.',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'.aaaaaaaaaa.',
'.aa.aa.aa.a.',
'.a...a...a..',
'............'],[
'............',
'....AAAA....',
'..AAaaaaAA..',
'.Aaak..kaaA.',
'.aaaawwaaaa.',
'.aaaaaaaaaa.',
'.aaaaaaaaaa.',
'.a.aa.aa.aa.',
'..a...a...a.',
'............']],
eye:[[
'....aaaa....',
'..aaAAAAaa..',
'.aAAwwwwAAa.',
'aAwwikkiwwAa',
'aAwwikkiwwAa',
'.aAAwwwwAAa.',
'..aaAAAAaa..',
'....aaaa....',
'...d.dd.d...',
'..d..dd..d..'],[
'....aaaa....',
'..aaAAAAaa..',
'.aAAwwwwAAa.',
'aAwikkiwwwAa',
'aAwikkiwwwAa',
'.aAAwwwwAAa.',
'..aaAAAAaa..',
'....aaaa....',
'..d..dd..d..',
'...d.dd.d...']],
phoenix:[[
'.....AA.....',
'....AaaA....',
'...Aaakaa...',
'..AAaaaaA...',
'.AaAaaaaaA..',
'AaaAaaaaaaA.',
'AaaAaaaaaad.',
'.aaaaaaaad..',
'..aaaaaad...',
'...dddd.....',
'...d..d.....',
'............'],[
'.....AA.....',
'....AaaA....',
'...Aaakaa...',
'.AAAaaaaA...',
'AaaAaaaaaA..',
'.aaAaaaaaaA.',
'..aAaaaaaad.',
'.aaaaaaaad..',
'..aaaaaad...',
'...dddd.....',
'....dd......',
'............']],
};

/* ---------- 월드별 패럴랙스 배경 테마 ---------- */
const BGS = [
  {sky:['#08131c','#0b1f16'], far:'#14352a', mid:'#0f2a20', floor:'#102818', tile:'#1a4028', star:'#2e5d43', fog:'rgba(99,232,159,.07)'},
  {sky:['#0c081c','#150b28'], far:'#251646', mid:'#1a0f33', floor:'#160e2a', tile:'#2a1c4e', star:'#5a3fb0', fog:'rgba(160,107,255,.08)'},
  {sky:['#0a1424','#102232'], far:'#20395a', mid:'#16293d', floor:'#142438', tile:'#26466a', star:'#5a7ea6', fog:'rgba(220,233,245,.07)'},
  {sky:['#150f0a','#1e1810'], far:'#3d2f1a', mid:'#2a2013', floor:'#241c10', tile:'#463620', star:'#6b5228', fog:'rgba(67,230,207,.06)'},
  {sky:['#140713','#200a16'], far:'#44112a', mid:'#2c0b1e', floor:'#240a1a', tile:'#48142e', star:'#8a2040', fog:'rgba(255,84,112,.08)'},
  {sky:['#12101a','#1a1524'], far:'#2e2840', mid:'#221d30', floor:'#1c1826', tile:'#3a3350', star:'#6a6288', fog:'rgba(205,211,221,.06)'},
  {sky:['#0c1810','#122414'], far:'#274a2a', mid:'#1c381f', floor:'#183018', tile:'#2e5a30', star:'#d1495b', fog:'rgba(242,142,154,.07)'},
  {sky:['#0a0e1c','#101830'], far:'#25304e', mid:'#1a2338', floor:'#161e30', tile:'#2c3a58', star:'#9db8e8', fog:'rgba(157,184,232,.08)'},
  {sky:['#100a1e','#181030'], far:'#302050', mid:'#241838', floor:'#1e1430', tile:'#3c2a60', star:'#b48ce8', fog:'rgba(180,140,232,.08)'},
  {sky:['#1a0c06','#28120a'], far:'#4e2410', mid:'#38180a', floor:'#2e140a', tile:'#5e2c12', star:'#ffb03a', fog:'rgba(232,106,42,.09)'},
];

/* ---------- 캔버스 & 연출 상태 ---------- */
const cv = document.getElementById('game'), ctx = cv.getContext('2d');
ctx.imageSmoothingEnabled = false;
let pFlash=0, mFlash=0, pLunge=0, mLunge=0, mShake=0;
let mobX = 552, bgOff = 0, fogOff = 0, bgShake = 0, flashT = 0;
let dmgNums = [], parts = [], slashes = [];
let prevRender = 0;
const FLOOR_Y = 218, PLAYER_X = 96;

function mobTX(){ return mob && mob.isBoss ? 314 : 340; }
function mobInRange(){ return mob && mobX <= mobTX() + 2; }

function addDmgNum(v, who, crit, byPet){
  const x = who!=='player' ? mobX+40+Math.random()*30 : PLAYER_X+20+Math.random()*40;
  let color, txt;
  if(who==='miss'){ color='#8a93a3'; txt='MISS'; }
  else if(who==='shield'){ color='#4aa8ff'; txt='🛡'+fmt(v); }
  else if(who==='mob'){
    const cs = {gold:'#ffd23f', cyan:'#43e6cf', red:'#ff5470'};
    color = crit ? '#ffd23f' : byPet ? '#63e89f' : (cs[S.settings.dmgColor]||'#ffffff');
    txt = (crit?'★':'')+fmt(v);
  } else { color='#ff5470'; txt=fmt(v); }
  dmgNums.push({x, y:126, txt, t:1, color, big:crit, sc:(S.settings&&S.settings.dmgSize)||1});
  if(dmgNums.length>14) dmgNums.shift();
}
function addSlash(byPet, crit){
  slashes.push({x:mobX+34+Math.random()*22, y:142+Math.random()*36, t:1,
    a:-0.9+Math.random()*0.7, c: byPet?'#63e89f': crit?'#fff6c8':'#ffd23f', big:crit});
}
function burst(x, y, colors, n, up){
  for(let i=0;i<n;i++){
    parts.push({x, y, vx:(Math.random()-0.5)*3.4, vy: up? -1.5-Math.random()*2.6 : (Math.random()-0.5)*3,
      c:colors[Math.floor(Math.random()*colors.length)], t:1, s:2+Math.random()*3});
  }
}
function deathFX(){
  const w = worldOf(S.stage);
  const body = Object.values(PAL[w.spr]).slice(0,3);
  burst(mobX+40, 165, body, mob.isBoss?26:12, false);       // 몸통 파편
  burst(mobX+40, 150, ['#ffd23f','#fff2b0'], 6, true);      // 골드 코인
}

/* ---------- 픽셀 드로잉 ---------- */
function drawSprite(name, pal, frame, x, y, px, flip){
  const pat = SPR[name][frame], map = PAL[pal];
  const w = SPR[name][0][0].length;
  for(let r=0;r<pat.length;r++){
    const row = pat[r] || '';
    for(let c=0;c<w;c++){
      const ch = row[flip ? w-1-c : c];
      if(!ch || ch==='.' || !map[ch]) continue;
      ctx.fillStyle = map[ch];
      ctx.fillRect(x+c*px, y+r*px, px, px);
    }
  }
}
function shadow(x, y, w){
  ctx.fillStyle = 'rgba(0,0,0,.4)';
  ctx.fillRect(x, y, w, 5);
}
function pyramid(x, baseY, w, h, c){
  ctx.fillStyle = c;
  const steps = 5;
  for(let i=0;i<steps;i++){
    const sw = w * (1 - i/steps);
    ctx.fillRect(x + (w-sw)/2, baseY - h*(i+1)/steps, sw, h/steps + 1);
  }
}
function drawSil(theme, x, baseY, seed){
  const t = worldIdx(S.stage) % 5;
  if(t===0){ // 습지: 둔덕 + 갈대
    ctx.fillStyle = theme;
    ctx.fillRect(x, baseY-16, 56, 16); ctx.fillRect(x+8, baseY-26, 40, 12);
    ctx.fillRect(x+62+seed%8, baseY-30, 3, 30); ctx.fillRect(x+60+seed%8, baseY-32, 7, 4);
  } else if(t===1){ // 동굴: 종유석/석순
    pyramid(x, baseY, 26, 34+seed%14, theme);
    ctx.fillStyle = theme;
    const sh = 40+seed%20;
    for(let i=0;i<4;i++) ctx.fillRect(x+44+i*3, 0, 3+ (i===1?2:0), sh - i*8);
  } else if(t===2){ // 설원: 침엽수
    pyramid(x, baseY, 34, 44+seed%12, theme);
    ctx.fillStyle = theme; ctx.fillRect(x+15, baseY-6, 5, 6);
  } else if(t===3){ // 폐허: 부서진 기둥
    ctx.fillStyle = theme;
    const h = 36+seed%16;
    ctx.fillRect(x+8, baseY-h, 14, h);
    ctx.fillRect(x+4, baseY-h, 22, 5);
    ctx.fillRect(x+8, baseY-h-4, 8, 4); // 부러진 윗부분
    ctx.fillRect(x+40, baseY-12, 18, 12);
  } else { // 심연: 가시 바위
    pyramid(x, baseY, 20, 46+seed%18, theme);
    pyramid(x+26, baseY, 14, 26+seed%10, theme);
  }
}

/* ---------- 배경 (패럴랙스 3겹) ---------- */
function drawBG(now, walking){
  const th = BGS[worldIdx(S.stage)];
  const W = cv.width, H = cv.height;
  // 하늘 (플랫 밴드 + 디더링 경계)
  ctx.fillStyle = th.sky[0]; ctx.fillRect(0,0,W,90);
  ctx.fillStyle = th.sky[1]; ctx.fillRect(0,90,W,FLOOR_Y-90);
  for(let x=0;x<W;x+=8){ if((x/8)%2===0){ ctx.fillStyle = th.sky[0]; ctx.fillRect(x,90,4,4); } }
  // 별/광석 (0.15배 속도)
  ctx.fillStyle = th.star;
  for(let i=0;i<22;i++){
    const bx = (i*137 + 40 - bgOff*0.15) % (W+40);
    const x = bx < 0 ? bx+W+40 : bx;
    const tw = (Math.floor(now/500)+i)%5===0 ? 3 : 2;
    ctx.fillRect(x-20, (i*53)%(FLOOR_Y-110)+10, tw, tw);
  }
  // 원경 실루엣 (0.35배)
  for(let k=-1;k<6;k++){
    const x = ((k*150 - bgOff*0.35) % (W+150) + (W+150)) % (W+150) - 75;
    drawSil(th.far, x, FLOOR_Y, k*7+3);
  }
  // 중경 실루엣 (0.6배)
  for(let k=-1;k<5;k++){
    const x = ((k*210+70 - bgOff*0.6) % (W+210) + (W+210)) % (W+210) - 105;
    drawSil(th.mid, x, FLOOR_Y+4, k*13+8);
  }
  // 차원 균열 (몬스터가 나오는 포탈)
  drawRift(now);
  // 바닥 (1.0배 타일 스크롤)
  ctx.fillStyle = th.floor; ctx.fillRect(0, FLOOR_Y, W, H-FLOOR_Y);
  ctx.fillStyle = th.tile;  ctx.fillRect(0, FLOOR_Y, W, 3);
  for(let k=0;k<20;k++){
    const x = ((k*48 - bgOff) % (W+48) + (W+48)) % (W+48) - 48;
    ctx.fillRect(x, FLOOR_Y+3, 2, H-FLOOR_Y);
    ctx.fillRect(x+24, FLOOR_Y+34, 2, H-FLOOR_Y-34);
  }
  ctx.fillStyle = 'rgba(0,0,0,.25)'; ctx.fillRect(0, H-14, W, 14);
  // 떠다니는 안개 (근경)
  fogOff += walking? 1.4 : 0.35;
  ctx.fillStyle = th.fog;
  for(let i=0;i<3;i++){
    const x = ((i*220 - fogOff*(0.6+i*0.3)) % (W+180) + (W+180)) % (W+180) - 90;
    ctx.fillRect(x, 150+i*34, 170, 16);
  }
}
function drawRift(t){
  const cx = 492, cy = 120;
  const pulse = 0.55 + 0.45*Math.sin(t/380);
  const pts = [[0,-70],[-10,-44],[7,-24],[-8,-2],[9,20],[-5,44],[3,68]];
  for(let pass=0; pass<2; pass++){
    ctx.strokeStyle = pass===0 ? 'rgba(160,107,255,'+(0.18*pulse)+')' : '#a06bff';
    ctx.lineWidth = pass===0 ? 12 : 3;
    ctx.beginPath();
    pts.forEach((p,i)=>{ const jx = Math.sin(t/300+i)*2;
      i===0 ? ctx.moveTo(cx+p[0]+jx, cy+p[1]) : ctx.lineTo(cx+p[0]+jx, cy+p[1]); });
    ctx.stroke();
  }
  ctx.fillStyle = 'rgba(160,107,255,'+(0.55*pulse)+')';
  for(let i=0;i<6;i++){
    const a = t/900 + i*1.1;
    ctx.fillRect(cx + Math.cos(a)*(20+i*7), cy + Math.sin(a*1.4)*(42+i*5), 3, 3);
  }
}

/* ---------- 메인 렌더 ---------- */
function render(now){
  if(!prevRender) prevRender = now;
  const rdt = Math.min(60, now - prevRender); prevRender = now;
  const walking = mob && mobX > mobTX()+2;
  bgOff += (walking? 0.11 : 0.016) * rdt;

  const W = cv.width, H = cv.height;
  ctx.setTransform(1,0,0,1,0,0);
  ctx.clearRect(0,0,W,H);
  if(S && S.settings && !S.settings.shake) bgShake = 0;
  if(bgShake > 0.2){
    ctx.translate((Math.random()-0.5)*bgShake, (Math.random()-0.5)*bgShake);
  }
  drawBG(now, walking);

  const dead = performance.now() < deadUntil;
  const bob = Math.sin(now/280)*3;

  // ---- 플레이어 ----
  const pl = pLunge>0 ? pLunge*26 : 0;
  const pFrame = Math.floor(now/(walking?130:280))%2;
  shadow(PLAYER_X+14, FLOOR_Y-4, 46);
  if(!dead || Math.floor(now/150)%2===0){
    if(pFlash>0.5) ctx.globalAlpha = 0.55;
    // 👗 스킨 + 🗡️ 장비 외형 반영
    const _sk = curSkin();
    const _skSpr = (_sk.id === 'wizard' && S.dlc.supporter) ? 'wizard' : _sk.spr;
    const _skPal = (_sk.id === 'wizard') ? (S.dlc.supporter?'wizardG':'wizard') : _sk.pal;
    const _py = 130 + (walking ? Math.abs(Math.sin(now/130))*-4 : bob);

    // ⚔️ 공격 모션: 돌진 + 회전 + 잔상
    const _atkT = pLunge;                       // 0~1
    if(_atkT > 0.05){
      ctx.save();
      const cx = PLAYER_X + pl + 36, cy = _py + 42;
      ctx.translate(cx, cy);
      ctx.rotate(-_atkT * 0.30);                // 휘두르는 회전
      ctx.translate(-cx, -cy);
      // 잔상
      ctx.globalAlpha = 0.28 * _atkT;
      drawSprite(_skSpr, _skPal, pFrame, PLAYER_X + pl - 14*_atkT, _py, 6, false);
      ctx.globalAlpha = 1;
    }

    drawSprite(_skSpr, _skPal, pFrame, PLAYER_X+pl, _py, 6, false);

    // 방어구 등급 틴트 (은은한 오라)
    const _ar = eqById(S.armor), _tint = armorTintOf(_ar);
    if(_tint){
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      ctx.globalAlpha = 0.14 + Math.sin(now/420)*0.05;
      ctx.fillStyle = _tint;
      ctx.fillRect(PLAYER_X+pl+8, _py+30, 56, 52);
      ctx.restore();
    }

    // 무기 오버레이
    const _w = eqById(S.weapon);
    if(_w){
      const _ws = weaponSprOf(_w), _wp = weaponPalOf(_w);
      if(SPR[_ws]) drawSprite(_ws, _wp, pFrame, PLAYER_X+pl, _py, 6, false);
      // 고등급 무기 발광
      const _gi = GRADES.indexOf(_w.grade);
      if(_gi >= 4 || _w.dev){
        ctx.save();
        ctx.globalCompositeOperation = 'lighter';
        ctx.globalAlpha = 0.22 + Math.sin(now/200)*0.12;
        ctx.fillStyle = (PAL[_wp] && PAL[_wp].w) || '#fff';
        ctx.fillRect(PLAYER_X+pl+30, _py+8, 34, 52);
        ctx.restore();
      }
    }

    if(_atkT > 0.05){
      ctx.restore();
      // 참격 이펙트
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      ctx.globalAlpha = _atkT * 0.75;
      ctx.strokeStyle = _w ? ((PAL[weaponPalOf(_w)]||{}).w || '#fff') : '#fff';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(PLAYER_X+pl+70, _py+40, 30 + (1-_atkT)*26, -0.9, 0.9);
      ctx.stroke();
      ctx.restore();
    }
    ctx.globalAlpha = 1;
  }
  // 장착한 펫 외형 표시 (졸졸 따라다님)
  if(equippedPetId && PET_SPR[equippedPetId] && S.pets[equippedPetId]){
    const ps = PET_SPR[equippedPetId];
    const ppx = 3;
    const py = 208 - ps.rows*ppx + Math.sin(now/240)*2;
    shadow(36, FLOOR_Y+18, 28);
    drawSprite(ps.spr, ps.pal, Math.floor(now/300)%2, 28, py, ppx, false);
    const pStars = (S.petStars && S.petStars[equippedPetId]) || 0;
    if(pStars>0){
      ctx.fillStyle = '#ffd23f'; ctx.font = '9px Galmuri11, monospace'; ctx.textAlign = 'center';
      ctx.fillText('★'.repeat(Math.min(pStars,5)), 28+18, py-6);
      ctx.textAlign = 'left';
    }
  }

  // ---- 몬스터 ----
  if(mob){
    const w = mob.tower ? worldOf(S.tower) : worldOf(S.stage);
    const sprN = mob.golden ? 'slime' : (mob.sandbag ? 'golem' : (mob.spr || w.spr));
    const palN = (mob.golden || mob.sandbag) ? 'goldslime' : (mob.pal || sprN);
    const ml = mLunge>0 ? mLunge*24 : 0;
    const shk = mShake>0 ? (Math.random()*6-3) : 0;
    const px = mob.isBoss ? 9 : 6;
    const mFrame = Math.floor(now/(walking?140:300))%2;
    const my = (mob.isBoss?92:132) + (walking? Math.abs(Math.sin(now/140))*-5 : bob*0.7);
    shadow(mobX+10, FLOOR_Y-4, mob.isBoss? 110 : 60);
    if(mFlash>0.5){
      ctx.save(); ctx.filter = 'brightness(2.4)';
      drawSprite(sprN, palN, mFrame, mobX-ml+shk, my, px, true);
      ctx.restore();
    } else {
      drawSprite(sprN, palN, mFrame, mobX-ml+shk, my, px, true);
    }
    if(mob.isBoss){
      ctx.fillStyle = '#a06bff'; ctx.font = '12px Galmuri11, monospace';
      ctx.fillText('BOSS', mobX+42, 84);
    }
  }

  // ---- 검격 이펙트 ----
  slashes.forEach(s=>{
    ctx.save(); ctx.translate(s.x, s.y); ctx.rotate(s.a);
    ctx.globalAlpha = Math.max(0, s.t);
    ctx.fillStyle = s.c;
    const L = s.big? 30 : 22;
    ctx.fillRect(-L, -2, L*2, 4);
    ctx.fillRect(-L*0.7, -6, L*1.4, 2);
    ctx.fillRect(-L*0.7, 4, L*1.4, 2);
    ctx.restore();
    s.t -= 0.12;
  });
  slashes = slashes.filter(s=>s.t>0);

  // ---- 파티클 ----
  parts.forEach(p=>{
    p.x += p.vx; p.y += p.vy; p.vy += 0.12; p.t -= 0.022;
    ctx.globalAlpha = Math.max(0, p.t);
    ctx.fillStyle = p.c;
    ctx.fillRect(p.x, p.y, p.s, p.s);
  });
  ctx.globalAlpha = 1;
  parts = parts.filter(p=>p.t>0 && p.y < H);

  // ---- 데미지 숫자 ----
  ctx.textAlign = 'center';
  dmgNums.forEach(d=>{
    d.t -= 0.016; d.y -= 0.9;
    ctx.globalAlpha = Math.max(0, d.t);
    ctx.fillStyle = d.color;
    ctx.font = Math.round((d.big?16:13)*(d.sc||1))+'px Galmuri11, monospace';
    ctx.fillText(d.txt, d.x, d.y);
  });
  ctx.globalAlpha = 1; ctx.textAlign = 'left';
  dmgNums = dmgNums.filter(d=>d.t>0);

  // ---- 보스 등장 섬광 ----
  if(flashT > 0){
    ctx.fillStyle = 'rgba(160,107,255,'+(flashT*0.4)+')';
    ctx.fillRect(0,0,W,H);
    flashT -= 0.04;
  }

  pFlash = Math.max(0, pFlash-0.08); mFlash = Math.max(0, mFlash-0.12);
  pLunge = Math.max(0, pLunge-0.12); mLunge = Math.max(0, mLunge-0.12);
  mShake = Math.max(0, mShake-0.1);  bgShake = Math.max(0, bgShake-0.25);
}

/* ---------- UI 렌더링 ---------- */
const $ = id => document.getElementById(id);
function log(html){
  const el = $('log');
  el.innerHTML = '<div>'+html+'</div>' + el.innerHTML;
  while(el.children.length > 4) el.removeChild(el.lastChild);
}
function renderStats(){
  $('goldTxt').textContent = fmt(S.gold);
  $('shardTxt').textContent = S.shards;
  const w = worldOf(S.stage);
  {
    const _t = tierOf(S.stage);
    const _tag = _t.id === 'normal' ? '' :
      ' <span style="color:'+_t.color+';font-weight:bold;text-shadow:0 0 6px '+_t.color+'">['+_t.icon+_t.name+']</span>';
    $('stageName').innerHTML = '스테이지 <em style="color:'+_t.color+'">'+stageLabel(S.stage)+'</em> · '+w.name+_tag;
  }
  $('pName').textContent = '['+rankTitle()+'] LV.'+S.level + (S.rebirths>0? ' ✦'+S.rebirths : '');
  $('mName').textContent = !mob ? getStageMob(S.stage).mob
    : mob.sandbag ? '💰 미다스 샌드백'
    : mob.tower ? '🗼 탑 수호자 '+S.tower+'층 '+(ELEMS[mob.el]||'')
    : mob.golden ? '✨ 황금 슬라임'
    : (mob.name || (mob.isBoss ? w.bossName : w.mob)) + ' ' + (ELEMS[mob.el]||'');
  // 킬 카운트 핍
  const pips = $('pips');
  if(pips.children.length !== BAL.killsForBoss){
    pips.innerHTML = '';
    for(let i=0;i<BAL.killsForBoss;i++){ const d=document.createElement('div'); d.className='pip'; pips.appendChild(d); }
  }
  [...pips.children].forEach((p,i)=> p.className = 'pip'+(i < S.kills ? ' on':''));
  // 강화 버튼
  const ca = BAL.upCost(15,S.atkLv), cd = BAL.upCost(12,S.defLv);
  $('atkLvTxt').textContent = 'Lv.'+S.atkLv;
  $('defLvTxt').textContent = 'Lv.'+S.defLv;
  $('atkGainTxt').textContent = '현재 보너스 +'+fmt(BAL.upBonus(5,S.atkLv))+' → 다음 +'+fmt(BAL.upBonus(5,S.atkLv+1));
  $('defGainTxt').textContent = '현재 보너스 +'+fmt(BAL.upBonus(2,S.defLv))+' → 다음 +'+fmt(BAL.upBonus(2,S.defLv+1));
  $('upAtk').textContent = fmt(ca)+' G'; $('upAtk').disabled = S.gold < ca;
  $('upDef').textContent = fmt(cd)+' G'; $('upDef').disabled = S.gold < cd;
  const cc = BAL.upCost(20, S.critLv);
  $('critLvTxt').textContent = 'Lv.'+S.critLv;
  $('critGainTxt').textContent = '치명타 대미지 x'+critDmgMult().toFixed(1)+' → x'+(critDmgMult()+0.1).toFixed(1);
  $('upCrit').textContent = fmt(cc)+' G'; $('upCrit').disabled = S.gold < cc;
  // 스탯 라인
  $('statLine').innerHTML =
    'ATK <b>'+fmt(playerATK())+'</b>'+
    ' · DEF <b>'+fmt(playerDEF())+'</b>'+
    ' · 치명타 <b>'+Math.round(critRate()*100)+'%</b>'+
    ' · 골드 배율 <b>x'+goldMult().toFixed(2)+'</b>'+
    ' · 강화석 <b>'+S.stones+'</b>';
  // 보스 버튼
  const ready = S.kills >= BAL.killsForBoss && !(mob && mob.isBoss) && battleMode==='field';
  $('bossBtn').disabled = !ready;
  $('bossBtn').className = ready ? 'ready' : '';
  $('bossBtn').textContent = (mob && mob.isBoss) ? '보스전 진행 중…'
    : ready ? '⚔ 보스 도전! — '+worldOf(S.stage).bossName
    : '보스 도전 ('+S.kills+'/'+BAL.killsForBoss+' 처치)';
  $('rebirthGainTxt').textContent = '지금 붕괴 시 균열의 조각 +'+rebirthGain()+' (스테이지가 깊을수록 증가)';
  $('rebirthBtn').disabled = rebirthGain() <= 0;
  $('gachaBtn').disabled = S.shards < 1;
  // ---- 원본 이식: 스탯/퀘스트/제련 UI ----
  $('statPtTxt').textContent = S.statPoints;
  $('stStr').textContent = S.stats.str;
  $('stDex').textContent = S.stats.dex;
  $('stVit').textContent = S.stats.vit;
  $('questDesc').textContent = getStageMob(S.stage).mob+' '+S.quest.targetMax+'마리 처치하기';
  $('questBar').style.width = Math.min(100, S.quest.current/S.quest.targetMax*100)+'%';
  $('questCount').textContent = '진행도: '+S.quest.current+' / '+S.quest.targetMax;
  $('questReward').textContent = '보상: +'+fmt(S.quest.goldReward)+'G / +'+fmt(S.quest.expReward)+' EXP';
  const fw = eqById(S.weapon);
  $('forgeName').innerHTML = fw ? eqLabel(fw) : '<span style="color:var(--mut)">장착 무기 없음</span>';
  $('forgeChance').textContent = fw ? '성공 확률 '+Math.round(Math.max(0.15,1-fw.enh*0.08)*100)+'% · 실패 시 강화 -1' : '무기를 장착하면 제련할 수 있습니다';
  $('forgeBtn').textContent = fw ? fmt((fw.enh+1)*30)+' G' : '-';
  $('forgeBtn').disabled = !fw || fw.enh>=10 || S.gold < (fw?(fw.enh+1)*30:0);
}
function renderHpBars(){
  const pm = playerMaxHP();
  $('pHpBar').style.width = safePct(pHpCur, pm)+'%';
  $('pHpTxt').textContent = fmt(Math.max(0,pHpCur))+' / '+fmt(pm);
  const req = BAL.expReq(S.level);
  $('expBar').style.width = Math.min(100, S.exp/req*100)+'%';
  if(mob){
    if(mob.shield > 0){
      $('mHpBar').style.background = '#4aa8ff';
      $('mHpBar').style.width = Math.max(0, mob.shield/mob.shieldMax*100)+'%';
      $('mHpTxt').textContent = '🛡 '+fmt(mob.shield)+' / '+fmt(mob.shieldMax);
    } else if(mob.sandbag){
      $('mHpBar').style.background = '';
      $('mHpBar').style.width = '100%';
      $('mHpTxt').textContent = '∞ · 남은 '+Math.max(0,Math.ceil((dgnUntil-Date.now())/1000))+'초';
    } else {
      $('mHpBar').style.background = '';
      $('mHpBar').style.width = safePct(mob.hp, mob.maxHp)+'%';
      $('mHpTxt').textContent = fmt(Math.max(0,mob.hp))+' / '+fmt(mob.maxHp);
    }
  }
  const btw = $('bossTimerWrap');
  if(mob && mob.isBoss && !mob.tower && !mob.sandbag){
    btw.style.display = 'block';
    $('bossTimer').style.width = Math.max(0, bossLeft/bossTimeMax()*100)+'%';
    $('bossTimerTxt').textContent = Math.max(0,bossLeft).toFixed(1)+'s';
  } else btw.style.display = 'none';
}
function eqLabel(e){
  return '<span class="'+GRADE_CLS[e.grade]+'">'+(e.awk?'☀'.repeat(e.awk)+' ':'')+'['+GRADE_KO[e.grade]+'] '+(e.fx?'':GRADE_PFX[e.grade]+' ')+(e.el?ELEMS[e.el]+' ':'')+e.name+(e.enh>0?' +'+e.enh:'')+(e.lock?' 🔒':'')+'</span>';
}
function renderEquip(){
  const w = eqById(S.weapon), a = eqById(S.armor);
  $('slotW').innerHTML = w ? '🗡 '+eqLabel(w)+' <small style="color:var(--mut)">ATK +'+fmt(eqPower(w))+'</small>' : '<span class="empty">🗡 무기 없음</span>';
  $('slotA').innerHTML = a ? '🛡 '+eqLabel(a)+' <small style="color:var(--mut)">DEF +'+fmt(eqPower(a))+'</small>' : '<span class="empty">🛡 방어구 없음</span>';
  // 재료 칩
  const chips = $('matChips');
  const mats = Object.entries(S.inv).filter(([,n])=>n>0);
  chips.innerHTML = mats.length
    ? mats.map(([k,n])=>'<span class="chip">'+k+' <b>x'+n+'</b></span>').join('') + '<span class="chip">강화석 <b>x'+S.stones+'</b></span>'
    : '<span class="chip">아직 전리품이 없습니다</span>';
  // 장비 목록 (등급 내림차순)
  $('invCount').textContent = '('+S.equips.length+'/'+S.invCap+') — 가득 차면 자동 판매';
  const list = $('eqList');
  const sorted = [...S.equips].sort((x,y)=> GRADES.indexOf(y.grade)-GRADES.indexOf(x.grade) || y.base-x.base);
  list.innerHTML = sorted.length ? '' : '<div style="color:var(--mut); font-size:12px;">몬스터를 잡으면 장비가 드랍됩니다 (드랍률 8%)</div>';
  sorted.forEach(e=>{
    const row = document.createElement('div'); row.className = 'row';
    const c = enhCost(e);
    const sameCnt = S.equips.filter(x=>x.name===e.name&&x.grade===e.grade&&x.type===e.type).length;
    const equipped = (S.weapon===e.id || S.armor===e.id);
    row.innerHTML = '<div class="info">'+(e.type==='weapon'?'🗡':'🛡')+' '+eqLabel(e)+
      '<small>'+(e.type==='weapon'?'ATK':'DEF')+' +'+fmt(eqPower(e))+(equipped?' · <span style="color:var(--cyan)">장착 중</span>':'')+'</small></div>';
    const btns = document.createElement('div');
    btns.style.cssText = 'display:flex; gap:4px; flex-wrap:wrap; justify-content:flex-end;';
    const bE = document.createElement('button'); bE.textContent = equipped?'해제됨':'장착'; bE.disabled = equipped;
    bE.onclick = ()=>equipItem(e.id);
    const bM = document.createElement('button'); bM.textContent = '합성 '+Math.min(3,sameCnt)+'/3';
    bM.disabled = sameCnt<3 || e.grade==='Legendary';
    bM.onclick = ()=>mergeItem(e.id);
    const bH = document.createElement('button'); bH.className='buy';
    if(e.enh>=10){
      const ak = e.awk||0;
      bH.textContent = ak>=3 ? '초월 MAX' : '☀ 초월(조각3)';
      bH.disabled = ak>=3 || S.shards<3;
      bH.onclick = ()=>awakenItem(e.id);
    } else {
      bH.textContent = '강화(석'+c.stone+'·'+fmt(c.gold)+'G)';
      bH.disabled = S.stones<c.stone || S.gold<c.gold;
      bH.onclick = ()=>enhanceItem(e.id);
    }
    const bL = document.createElement('button'); bL.textContent = e.lock?'🔒':'🔓';
    bL.title = '잠금 (분해·합성 보호)';
    bL.onclick = ()=>{ e.lock = !e.lock; renderEquip(); saveGame(true); };
    const bD = document.createElement('button'); bD.className='danger'; bD.textContent='분해';
    bD.disabled = equipped || !!e.lock;
    bD.onclick = ()=>dismantleItem(e.id);
    btns.append(bE,bM,bH,bL,bD); row.appendChild(btns); list.appendChild(row);
  });
}
function renderArts(){
  $('artList').innerHTML = Object.entries(ARTS).map(([k,a])=>
    '<div class="art"><span>'+a.name+' <b>Lv.'+S.artifacts[k]+'</b></span><span style="color:var(--mut)">'+a.desc+'</span></div>').join('');
}
function renderShop(){
  $('buySupporter').style.display = S.dlc.supporter ? 'none':'';
  $('buyOffline').style.display = S.dlc.offline ? 'none':'';
  if(S.dlc.supporter && !$('dlcSupporter').querySelector('.owned'))
    $('dlcSupporter').insertAdjacentHTML('beforeend','<div class="owned">✔ 적용됨 — 골드 x2 · 황금 로브</div>');
  if(S.dlc.offline && !$('dlcOffline').querySelector('.owned'))
    $('dlcOffline').insertAdjacentHTML('beforeend','<div class="owned">✔ 적용됨 — 오프라인 24시간</div>');
}
function renderAll(){ renderStats(); renderEquip(); renderArts(); renderShop(); renderPetUI();; renderContent(); renderTalents(); renderSettings();
  renderSocial();
  updateSkillUI();
  updateAutoSellUI();
  updatePowerDisplay(); }

/* ---------- 모달 ---------- */

function showModal(title, bodyHtml){
  $('modalTitle').textContent = title;
  $('modalBody').innerHTML = bodyHtml;
  $('modalBg').style.display = 'flex';
}
$('modalOk').onclick = ()=> $('modalBg').style.display = 'none';

/* ---------- 탭 ---------- */
document.querySelectorAll('.tabs button').forEach(b=>{
  b.onclick = ()=>{
    document.querySelectorAll('.tabs button').forEach(x=>x.classList.remove('on'));
    document.querySelectorAll('.tabpage').forEach(x=>x.classList.remove('on'));
    b.classList.add('on');
    $('tab-'+b.dataset.tab).classList.add('on');
  };
});

/* ---------- 이벤트 ---------- */
$('upAtk').onclick = ()=>upStat('atk');
$('upDef').onclick = ()=>upStat('def');
$('upCrit').onclick = ()=>upStat('crit');
$('bossBtn').onclick = tryBoss;
$('rebirthBtn').onclick = doRebirth;
$('gachaBtn').onclick = gachaArtifact;
$('buySupporter').onclick = ()=>buyDLC('supporter');
$('buyOffline').onclick = ()=>buyDLC('offline');
$('saveBtn').onclick = ()=>saveGame(false);

/* ---------- 원본 기능 이식: 스탯분배·상점가챠·퀘스트·제련·보안·콘솔 ---------- */
const W_PREFIX = ["불타는","얼어붙은","심연의","멸망의","고결한","타락한","시공의","차원의","전설의","망령의"];
const W_CORE   = ["장검","카타나","도끼","단검","그레이트소드","스태프","스피어","헬버드","크로스보우","가디언블레이드"];
const W_SUFFIX = ["of 파멸","of 무한","of 그림자","of 광휘","of 영혼","of 균열","of 우주","of 종말"];
let activeKeys = {};

function addStatMulti(type){
  let amt = parseInt($('statAmt').value)||1; if(amt<1) amt=1;
  if(S.statPoints<=0){ log('<span class="r">분배할 스탯 포인트가 부족합니다.</span>'); return; }
  const inv = Math.min(S.statPoints, amt);
  S.statPoints -= inv; S.stats[type] += inv;
  if(type==='vit') pHpCur = Math.min(playerMaxHP(), pHpCur + 25*inv);
  log('<span class="c">'+({str:'힘',dex:'민첩',vit:'체력'})[type]+' 스탯을 한 번에 '+inv+'개 투자!</span>');
  renderStats(); saveGame(true);
}

function makeGachaWeapon(premium, forceLegend){
  let gi = premium ? 1+Math.floor(Math.random()*3) : Math.floor(Math.random()*3);
  if(forceLegend) gi = 3;
  const grade = GRADES[gi];
  let name = W_PREFIX[Math.floor(Math.random()*W_PREFIX.length)]+' '+W_CORE[Math.floor(Math.random()*W_CORE.length)];
  if(premium) name += ' '+W_SUFFIX[Math.floor(Math.random()*W_SUFFIX.length)];
  const mult = (premium?1.8:1.2) + gi*0.5;
  const base = Math.round(8 * Math.pow(1.18, S.stage-1) * mult * Math.pow(2, gi));
  const el = ELEM_KEYS[Math.floor(Math.random()*5)];
  return {id:S.nextId++, type:'weapon', grade, name, base, enh:0, fx:true, el};
}

function buyShopItemMulti(mode, count){
  const price = mode==='weapon_gacha'?800 : mode==='pet_gacha'?1200 : 300;
  const total = price*count;
  if(S.gold < total){ log('<span class="r">골드 부족! 필요량: '+fmt(total)+' G</span>'); return; }
  S.gold -= total;
  let sold = 0;
  for(let i=0;i<count;i++){
    if(mode==='pet_gacha'){
      const remain = PETS.filter(p=>!S.pets[p.id]);
      if(remain.length===0){
        // ⭐ 펫 진화: 중복 뽑기 → 무작위 펫 성급 상승 (최대 5성)
        const pid = PETS[Math.floor(Math.random()*PETS.length)].id;
        const st = S.petStars[pid]||0;
        if(st>=5){ S.gold += 600; sold++; }
        else {
          S.petStars[pid] = st+1;
          log('<span class="c">⭐ '+PETS.find(p=>p.id===pid).name+' '+(st+1)+'성 진화! (공격 +2%)</span>');
        }
        continue;
      }
      const p = remain[Math.floor(Math.random()*remain.length)];
      S.pets[p.id] = true;
      log('<span class="c">'+p.name+'</span> 영입! ('+p.desc+')');
    } else {
      const prem = mode==='weapon_gacha';
      let force = false;
      if(prem){
        S.pity = (S.pity||0)+1;
        if(S.pity >= 40){ force = true; S.pity = 0; log('<span class="g">🎯 마일리지 천장 도달! 전설 등급 확정!</span>'); }
        if(!force && S.pickup > 0){ S.pickup--; if(Math.random() < 0.25) force = true; }
      }
      const wpn = makeGachaWeapon(prem, force);
      collAdd(wpn.name.split(' ').slice(0,2).join(' '));
      if(S.equips.length >= S.invCap){ S.gold += Math.floor(wpn.base*2); sold++; continue; }
      S.equips.push(wpn);
    }
  }
  log('<span class="g">🛒 '+count+'회 대량 구매 완료!</span>'+(sold? ' <span style="color:var(--mut)">(가득/중복 '+sold+'건 골드 환급)</span>':''));
  renderAll(); saveGame(true);
}

function equipBestGear(){
  const bw = S.equips.filter(e=>e.type==='weapon').sort((a,b)=>eqPower(b)-eqPower(a))[0];
  const ba = S.equips.filter(e=>e.type==='armor').sort((a,b)=>eqPower(b)-eqPower(a))[0];
  if(!bw && !ba){ log('<span class="r">인벤토리에 장비가 없습니다.</span>'); return; }
  if(bw) S.weapon = bw.id;
  if(ba) S.armor = ba.id;
  log('<span class="c">⚡ 최고 성능 장비 자동 장착 완료!</span>');
  renderAll(); saveGame(true);
}

function forgeWeapon(){
  const w = eqById(S.weapon);
  if(!w){ log('<span class="r">장착된 무기가 없습니다.</span>'); return; }
  if(w.enh >= 10){ log('<span class="r">이미 최대 제련입니다.</span>'); return; }
  const cost = (w.enh+1)*30;
  if(S.gold < cost) return;
  S.gold -= cost;
  const chance = Math.max(0.15, 1.0 - w.enh*0.08);
  if(Math.random() <= chance){
    w.enh++;
    log('<span class="c">🔨 제련 성공! +'+w.enh+' (+10% 성능)</span>');
  } else {
    w.enh = Math.max(0, w.enh-1);
    log('<span class="r">🔨 제련 실패… +'+w.enh+'로 하락</span>');
  }
  renderAll(); saveGame(true);
}

function questProgress(){
  S.quest.current++;
  if(S.quest.current >= S.quest.targetMax){
    S.gold += S.quest.goldReward;
    gainExp(S.quest.expReward);
    log('<span class="g">🎯 퀘스트 완료! +'+fmt(S.quest.goldReward)+'G / +'+fmt(S.quest.expReward)+' EXP</span>');
    S.quest.current = 0;
    S.quest.targetMax = 5 + S.stage;
    S.quest.goldReward = Math.floor(50 * Math.pow(1.15, S.stage-1));
    S.quest.expReward = Math.floor(20 * Math.pow(1.12, S.stage-1));
  }
}

function initIdentity(){
  if(S.nickname){
    // 이미 저장된 고유이름이 있으면 그대로 사용
    try{ localStorage.setItem('rift-nick', S.nickname); }catch(e){}
  } else {
    let n = null;
    try{ n = localStorage.getItem('rift-nick'); }catch(e){}
    if(!n){
      n = '모험가_' + Math.floor(1000 + Math.random()*9000);
      try{ localStorage.setItem('rift-nick', n); }catch(e){}
    }
    S.nickname = n;
  }
  $('nickTag').textContent = '내 고유이름: ' + S.nickname + (S.nickname===ADMIN_NICK ? ' 👑' : '');
  const inp = $('nickInput');
  if(inp) inp.value = S.nickname;
}

// ============================================================================
// 👑 개발자 전용 명령어 시스템 (닉네임이 "개발자"일 때만 동작)
// ============================================================================
const DEV_GRADE = 'Developer';

// 무한 장비 판정 (base가 Infinity면 무한 장비)
function isDevItem(e){ return !!(e && e.grade === DEV_GRADE); }

// 개발자 전용 무기/방어구 지급
function devGiveGear(){
  if(!checkAdminAccess()) return devDeny();
  const mk = (type, name) => ({
    id: S.nextId++, type, grade: DEV_GRADE, name,
    base: Infinity, enh: 0, awk: 0, dev: true,
    el: type === 'weapon' ? '빛' : undefined
  });
  const w = mk('weapon', '개발자의 창조검');
  const a = mk('armor',  '개발자의 절대갑주');
  S.equips.push(w, a);
  S.weapon = w.id;
  S.armor  = a.id;
  log('<span class="gP">👑 [개발자] 창조검 · 절대갑주 지급 및 장착 완료 (공격력/방어력 ∞)</span>');
  renderAll(); saveGame(true);
}

// 스테이지 건너뛰기
function devSkipStage(n){
  if(!checkAdminAccess()) return devDeny();
  n = parseInt(n) || 1;
  S.stage = Math.max(1, Math.min(MAX_STAGE, S.stage + n));
  if(S.stage > (S.maxStage||1)) S.maxStage = S.stage;
  S.quest.current = 0;
  S.bossKills = 0;
  if(typeof spawnMob === 'function') spawnMob(false);
  log('<span class="gP">👑 [개발자] 스테이지 ' + (n>0?'+':'') + n + ' → 현재 ' + S.stage + '</span>');
  renderAll(); saveGame(true);
}

// 특정 스테이지로 이동
function devGotoStage(n){
  if(!checkAdminAccess()) return devDeny();
  n = Math.max(1, Math.min(MAX_STAGE, parseInt(n) || 1));
  S.stage = n;
  if(S.stage > (S.maxStage||1)) S.maxStage = S.stage;
  S.quest.current = 0;
  S.bossKills = 0;
  if(typeof spawnMob === 'function') spawnMob(false);
  log('<span class="gP">👑 [개발자] 스테이지 ' + n + ' 로 이동</span>');
  renderAll(); saveGame(true);
}

// 레벨 올리기 (무한)
function devLevelUp(n){
  if(!checkAdminAccess()) return devDeny();
  n = parseInt(n) || 1;
  if(n < 1) n = 1;
  S.level += n;
  S.exp = 0;
  S.statPoints += n * 4;
  pHpCur = playerMaxHP();
  log('<span class="gP">👑 [개발자] 레벨 +' + n + ' → LV.' + S.level + ' (스탯포인트 +' + (n*4) + ')</span>');
  renderAll(); saveGame(true);
}

// 스탯 무한 강화
function devMaxStats(){
  if(!checkAdminAccess()) return devDeny();
  S.stats.str += 10000;
  S.stats.dex += 10000;
  S.stats.vit += 10000;
  S.atkLv += 1000;
  S.defLv += 1000;
  S.critLv += 100;
  pHpCur = playerMaxHP();
  log('<span class="gP">👑 [개발자] 전 스탯 대폭 강화 완료</span>');
  renderAll(); saveGame(true);
}

function devGiveGold(n){
  if(!checkAdminAccess()) return devDeny();
  n = parseInt(n) || 1000000;
  S.gold += n;
  log('<span class="gP">👑 [개발자] 골드 +' + fmt(n) + '</span>');
  renderAll(); saveGame(true);
}

function devGiveAllPets(){
  if(!checkAdminAccess()) return devDeny();
  if(!S.petStars) S.petStars = {};
  PETS.forEach(p => { S.pets[p.id] = true; S.petStars[p.id] = 5; });
  log('<span class="gP">👑 [개발자] 전체 펫 ' + PETS.length + '종 획득 (5성)</span>');
  renderAll(); saveGame(true);
}

function devDeny(){
  log('<span class="r">⛔ 개발자 전용 명령어입니다. (고유이름을 "개발자"로 설정하세요)</span>');
}

// ---------- 명령어 파서 ----------
function runDevCommand(raw){
  const line = String(raw || '').trim();
  if(!line) return;
  if(!line.startsWith('/')){
    log('<span class="r">명령어는 / 로 시작합니다. /help 입력</span>');
    return;
  }
  const parts = line.slice(1).split(/\s+/);
  const cmd = parts[0].toLowerCase();
  const arg = parts[1];

  switch(cmd){
    case 'help': case '도움말':
      log('<span class="c">━━ 개발자 명령어 ━━</span>');
      log('<span class="c">/gear</span> — 무한 무기·방어구 지급');
      log('<span class="c">/skip [n]</span> — 스테이지 n칸 건너뛰기 (기본 1)');
      log('<span class="c">/stage [n]</span> — n 스테이지로 이동');
      log('<span class="c">/level [n]</span> — 레벨 n만큼 상승 (기본 1)');
      log('<span class="c">/stats</span> — 전 스탯 대폭 강화');
      log('<span class="c">/gold [n]</span> — 골드 지급');
      log('<span class="c">/pets</span> — 전체 펫 5성 획득');
      log('<span class="c">/tier [이름]</span> — 티어 이동 (강화/초월/신/dev)');
      log('<span class="c">/god</span> — 위 항목 전부 한번에');
      break;
    case 'tier': case '티어': {
      if(!checkAdminAccess()) return devDeny();
      const map = {normal:1, enhanced:101, transcend:126, divine:151, dev:176,
                   일반:1, 강화:101, 초월:126, 신:151};
      const key = (arg||'').toLowerCase();
      if(map[key] !== undefined){ devGotoStage(map[key]); }
      else {
        log('<span class="c">/tier normal | enhanced | transcend | divine | dev</span>');
        TIERS.forEach(t => log('<span style="color:'+t.color+'">'+(t.icon||'·')+' '+t.name+' : '+t.start+'~'+t.end+'</span>'));
      }
      break;
    }
    case 'gear': case '장비':   devGiveGear(); break;
    case 'skip': case '스킵':   devSkipStage(arg || 1); break;
    case 'stage': case '스테이지': devGotoStage(arg || 1); break;
    case 'level': case 'lv': case '레벨': devLevelUp(arg || 1); break;
    case 'stats': case '스탯':  devMaxStats(); break;
    case 'gold': case '골드':   devGiveGold(arg); break;
    case 'pets': case '펫':     devGiveAllPets(); break;
    case 'god': case '갓':
      if(!checkAdminAccess()) return devDeny();
      devGiveGear(); devMaxStats(); devGiveAllPets();
      devLevelUp(99); devGiveGold(999999999);
      log('<span class="gP">👑 GOD MODE 적용 완료</span>');
      break;
    default:
      log('<span class="r">알 수 없는 명령어: /' + cmd + ' (/help 로 목록 확인)</span>');
  }
}


// ---------- 개발자 콘솔 열기/닫기 ----------
function toggleDevConsole(force){
  const p = document.getElementById('adminPanel');
  if(!p) return;
  const isOpen = p.style.display === 'block';
  const next = (force === undefined) ? !isOpen : !!force;
  if(next && !checkAdminAccess()){
    log('<span class="r">⛔ 개발자 전용 기능입니다. (고유이름을 "개발자"로 설정하세요)</span>');
    p.style.display = 'none';
    return;
  }
  p.style.display = next ? 'block' : 'none';
  if(next){
    const inp = document.getElementById('devCmd');
    if(inp) setTimeout(()=>inp.focus(), 50);
    log('<span class="r">🔓 개발자 콘솔 개방! 명령어: /help</span>');
  }
}
window.toggleDevConsole = toggleDevConsole;

// 백틱(`) 또는 Ctrl+Shift+D 로 콘솔 토글 (브라우저 devtools와 충돌 없음)
window.addEventListener('keydown', e=>{
  const tag = document.activeElement && document.activeElement.tagName;
  if(tag === 'INPUT' || tag === 'TEXTAREA') return;
  if(e.key === '`' || e.key === '~'){
    e.preventDefault();
    toggleDevConsole();
  }
  if(e.ctrlKey && e.shiftKey && (e.key === 'D' || e.key === 'd')){
    e.preventDefault();
    toggleDevConsole();
  }
});

function executeAdminGift(kind){
  if(!checkAdminAccess()) return devDeny();
  if($('admTarget').value.trim() !== S.nickname){ log('<span class="r">이름이 올바르지 않습니다.</span>'); return; }
  if(kind==='gold') S.gold += 50000;
  else S.statPoints += 100;
  log('<span class="p">⚡ [관리자] 치트 코드가 적용되었습니다.</span>');
  renderAll(); saveGame(true);
}

// 📤 개발자 콘솔: 온라인 플레이어에게 아이템 전송
async function executeAdminSendItem(){
  if(!checkAdminAccess()) return devDeny();
  if(($('admTarget').value || '').trim() !== S.nickname){
    log('<span class="r">먼저 위에 내 고유이름을 입력하세요.</span>'); return;
  }
  const target = ($('admItemTarget').value || '').trim();
  const item   = ($('admItemName').value   || '').trim();
  const grade  = ($('admItemGrade').value  || 'normal').trim();
  const qty    = Math.max(1, parseInt(($('admItemQty').value || '1'), 10) || 1);
  if(!target){ log('<span class="r">받는 사람 이름을 입력하세요.</span>'); return; }
  if(!item){   log('<span class="r">아이템 이름을 입력하세요.</span>'); return; }
  if(!NET.isOnline()){
    log('<span class="r">서버에 연결되어 있지 않습니다. server.py 를 같은 PC에서 실행하세요.</span>');
    return;
  }
  const r = await NET.req('/item/send', {
    nick: S.nickname, to: target, item: item, grade: grade, qty: qty
  });
  if(r && r.ok){
    log('<span class="g">📤 [' + esc(target) + '] 에게 [' + esc(item) + '] ×' + qty + ' 전송 완료!</span>');
    $('admItemTarget').value = '';
    $('admItemName').value   = '';
  } else {
    log('<span class="r">전송 실패: ' + (r && r.error ? r.error : '서버 응답 없음') + '</span>');
  }
}
window.executeAdminSendItem = executeAdminSendItem;
window.addEventListener('keydown', e=>{
  activeKeys[e.key] = true;
  if(activeKeys['F12'] && activeKeys['Delete'] && activeKeys['Shift']){
    e.preventDefault();
    toggleDevConsole();
  }
});
window.addEventListener('keyup', e=>{ delete activeKeys[e.key]; });

document.addEventListener('keydown', e=>{
  // 입력란/콘솔 안에서는 단축키 비활성
  const ae = document.activeElement;
  if(ae && (ae.tagName === 'INPUT' || ae.tagName === 'TEXTAREA' || ae.isContentEditable)) return;
  // ⛔ 키 반복(repeat) 차단: Space bar / Enter 자동 연타 방지
  if(e.repeat) return;
  if(e.code === 'Space' || e.code === 'Enter'){ e.preventDefault(); playerManualAttack(); }
  if(e.key.toLowerCase() === 'b'){ e.preventDefault(); tryBoss(); }
  const n = parseInt(e.key);
  if(n >= 1 && n <= 8){
    const t = ['up','eq','art','shop','content','talent','set','social'][n-1];
    if(t){
      document.querySelectorAll('.tabs button').forEach(x => x.classList.remove('on'));
      document.querySelectorAll('.tabpage').forEach(x => x.classList.remove('on'));
      const b = document.querySelector('[data-tab="' + t + '"]');
      if(b) b.classList.add('on');
      $('tab-' + t).classList.add('on');
    }
  }
});

/* ==================================================================
   대규모 기능 블록: 특성·도감·업적·콘텐츠·설정·사운드·통계
   ================================================================== */
let battleMode = 'field';           // field | tower | golddgn
let apsAcc = 0, reviveInvUntil = 0;
let dgnUntil = 0, dgnGold = 0;
let dmgEv = [], goldEv = [];
function recDmg(d){ dmgEv.push([Date.now(), d]); if(dmgEv.length>600) dmgEv.shift(); }
function recGold(g){ goldEv.push([Date.now(), g]); if(goldEv.length>600) goldEv.shift(); }
function totalPetStars(){ return Object.values(S.petStars||{}).reduce((a,b)=>a+b,0); }
function critDmgMult(){ return 2 + 0.1*(S.critLv||0) + 0.2*((S.talents&&S.talents.critd)||0); }
function collAdd(n){ if(!S.coll[n]) S.coll[n] = true; }
function rankTitle(){
  const sc = (S.rebirths||0)*50 + (S.maxStage||1);
  return sc>=500?'우주 대장상' : sc>=200?'차원 거상' : sc>=80?'차원 상인' : sc>=30?'골목 상인' : '동네 상인';
}
function ensureDaily(){
  const day = new Date().toDateString();
  if(S.day !== day){ S.day = day; S.goldDgnUses = 0; S.bounty = {need:20, cur:0}; }
}

/* ---------- 🔊 사운드 (WebAudio) ---------- */
let AC = null, bgmInt = null;

// ============================================================================
// 🔊 고품질 사운드 엔진 (Web Audio · 마스터 볼륨 대폭 상향)
// ============================================================================
const Audio8 = (() => {
  let ctx = null, master = null, sfxBus = null, bgmBus = null, comp = null;
  let ready = false;
  let vol = { master: 1.0, sfx: 0.9, bgm: 0.5 };

  function init(){
    if(ctx) return ctx;
    try{
      ctx = new (window.AudioContext || window.webkitAudioContext)();
      // 리미터/컴프레서 → 크게 키워도 찢어지지 않게
      comp = ctx.createDynamicsCompressor();
      comp.threshold.value = -10;
      comp.knee.value = 20;
      comp.ratio.value = 12;
      comp.attack.value = 0.003;
      comp.release.value = 0.25;

      master = ctx.createGain();
      master.gain.value = vol.master * 3.2;   // ⬆️ 기존 대비 훨씬 크게
      sfxBus = ctx.createGain(); sfxBus.gain.value = vol.sfx;
      bgmBus = ctx.createGain(); bgmBus.gain.value = vol.bgm;

      sfxBus.connect(master); bgmBus.connect(master);
      master.connect(comp); comp.connect(ctx.destination);
      ready = true;
    }catch(e){ console.warn('오디오 초기화 실패', e); }
    return ctx;
  }

  function resume(){
    init();
    if(ctx && ctx.state === 'suspended') ctx.resume();
  }

  // ---- 기본 신디사이저 ----
  function tone(o){
    if(!ready) init();
    if(!ctx) return;
    const t0 = ctx.currentTime + (o.delay || 0);
    const osc = ctx.createOscillator();
    const g = ctx.createGain();
    osc.type = o.type || 'square';
    osc.frequency.setValueAtTime(o.f0, t0);
    if(o.f1 && o.f1 !== o.f0){
      if(o.slide === 'exp') osc.frequency.exponentialRampToValueAtTime(Math.max(1,o.f1), t0 + o.dur);
      else osc.frequency.linearRampToValueAtTime(o.f1, t0 + o.dur);
    }
    const peak = (o.vol == null ? 0.5 : o.vol);
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(peak, t0 + (o.attack || 0.008));
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + o.dur);

    let node = osc;
    if(o.filter){
      const f = ctx.createBiquadFilter();
      f.type = o.filter.type || 'lowpass';
      f.frequency.setValueAtTime(o.filter.f0 || 2000, t0);
      if(o.filter.f1) f.frequency.exponentialRampToValueAtTime(Math.max(1,o.filter.f1), t0 + o.dur);
      f.Q.value = o.filter.q || 1;
      node.connect(f); node = f;
    }
    node.connect(g);
    g.connect(o.bus === 'bgm' ? bgmBus : sfxBus);
    osc.start(t0); osc.stop(t0 + o.dur + 0.02);
  }

  // ---- 노이즈 (타격/폭발감) ----
  function noise(o){
    if(!ready) init();
    if(!ctx) return;
    const t0 = ctx.currentTime + (o.delay || 0);
    const len = Math.max(1, Math.floor(ctx.sampleRate * o.dur));
    const buf = ctx.createBuffer(1, len, ctx.sampleRate);
    const d = buf.getChannelData(0);
    for(let i=0;i<len;i++){
      const decay = Math.pow(1 - i/len, o.curve || 2);
      d[i] = (Math.random()*2-1) * decay;
    }
    const src = ctx.createBufferSource(); src.buffer = buf;
    const f = ctx.createBiquadFilter();
    f.type = o.type || 'lowpass';
    f.frequency.setValueAtTime(o.f0 || 1200, t0);
    if(o.f1) f.frequency.exponentialRampToValueAtTime(Math.max(1,o.f1), t0 + o.dur);
    f.Q.value = o.q || 1;
    const g = ctx.createGain();
    g.gain.value = (o.vol == null ? 0.5 : o.vol);
    src.connect(f); f.connect(g); g.connect(sfxBus);
    src.start(t0); src.stop(t0 + o.dur + 0.02);
  }

  function setVol(kind, v){
    vol[kind] = v;
    if(!ready) init();
    if(!ctx) return;
    if(kind==='master' && master) master.gain.value = v * 3.2;
    if(kind==='sfx' && sfxBus) sfxBus.gain.value = v;
    if(kind==='bgm' && bgmBus) bgmBus.gain.value = v;
  }

  return { init, resume, tone, noise, setVol,
           getVol: k => vol[k], isReady: () => ready,
           ctx: () => ctx };
})();

// ---------------- 효과음 정의 ----------------
function sfx(t){
  if(!S || !S.settings || !S.settings.sfx) return;
  try{
    switch(t){
      case 'hit':      // 기본 타격: 노이즈 펀치 + 저음 임팩트
        Audio8.noise({dur:0.09, f0:3800, f1:600, vol:0.42, curve:2.4});
        Audio8.tone({type:'triangle', f0:320, f1:120, dur:0.10, vol:0.5, slide:'exp'});
        break;
      case 'crit':     // 치명타: 금속성 상승 + 강한 노이즈
        Audio8.noise({dur:0.13, f0:7000, f1:900, vol:0.55, curve:2});
        Audio8.tone({type:'square', f0:880, f1:1760, dur:0.09, vol:0.42, slide:'exp'});
        Audio8.tone({type:'sawtooth', f0:1320, f1:440, dur:0.16, vol:0.3, delay:0.03, slide:'exp',
                     filter:{type:'lowpass', f0:6000, f1:900}});
        break;
      case 'kill':     // 처치: 하강 3음
        [0,0.05,0.1].forEach((d,i)=>Audio8.tone({
          type:'square', f0:660-i*140, f1:520-i*140, dur:0.1, vol:0.4, delay:d}));
        Audio8.noise({dur:0.2, f0:2000, f1:200, vol:0.3, delay:0.02});
        break;
      case 'boss':     // 보스 등장: 저음 굉음
        Audio8.tone({type:'sawtooth', f0:70, f1:38, dur:1.0, vol:0.55, slide:'exp',
                     filter:{type:'lowpass', f0:900, f1:200}});
        Audio8.tone({type:'square', f0:140, f1:76, dur:0.8, vol:0.28, slide:'exp'});
        Audio8.noise({dur:0.7, f0:400, f1:80, vol:0.35, curve:1.4});
        break;
      case 'levelup':  // 레벨업: 상승 아르페지오
        [523,659,784,1047].forEach((f,i)=>Audio8.tone({
          type:'square', f0:f, f1:f, dur:0.16, vol:0.42, delay:i*0.07}));
        Audio8.tone({type:'triangle', f0:1047, f1:2093, dur:0.3, vol:0.3, delay:0.28, slide:'exp'});
        break;
      case 'gold':     // 골드: 동전 짤랑
        [1400,1900].forEach((f,i)=>Audio8.tone({
          type:'square', f0:f, f1:f*1.25, dur:0.07, vol:0.3, delay:i*0.045}));
        break;
      case 'buy':      // 구매 확정
        Audio8.tone({type:'square', f0:700, f1:1050, dur:0.09, vol:0.38});
        Audio8.tone({type:'square', f0:1050, f1:1400, dur:0.1, vol:0.32, delay:0.08});
        break;
      case 'enhance': // 강화 성공: 반짝
        [880,1174,1568].forEach((f,i)=>Audio8.tone({
          type:'triangle', f0:f, f1:f*1.5, dur:0.14, vol:0.4, delay:i*0.05, slide:'exp'}));
        break;
      case 'fail':     // 실패: 하강 부저
        Audio8.tone({type:'sawtooth', f0:300, f1:90, dur:0.32, vol:0.45, slide:'exp',
                     filter:{type:'lowpass', f0:1600, f1:300}});
        break;
      case 'legend':   // 전설 등급 드랍: 화려한 팡파레
        [784,988,1175,1568].forEach((f,i)=>Audio8.tone({
          type:'square', f0:f, f1:f, dur:0.2, vol:0.45, delay:i*0.09}));
        Audio8.noise({dur:0.5, f0:9000, f1:2500, vol:0.24, delay:0.3, type:'highpass'});
        break;
      case 'fever':    // 피버 돌입
        Audio8.tone({type:'sawtooth', f0:220, f1:880, dur:0.45, vol:0.42, slide:'exp',
                     filter:{type:'lowpass', f0:800, f1:6000}});
        Audio8.noise({dur:0.4, f0:1000, f1:8000, vol:0.28, type:'highpass'});
        break;
      case 'skill':    // 스킬 발동
        Audio8.tone({type:'sawtooth', f0:180, f1:1200, dur:0.28, vol:0.45, slide:'exp',
                     filter:{type:'bandpass', f0:600, f1:3000, q:3}});
        Audio8.noise({dur:0.3, f0:5000, f1:800, vol:0.34});
        break;
      case 'gacha':    // 뽑기 드럼롤
        for(let i=0;i<8;i++) Audio8.tone({
          type:'square', f0:400+i*70, f1:430+i*70, dur:0.05, vol:0.26, delay:i*0.06});
        break;
      case 'ui':       // UI 클릭
        Audio8.tone({type:'square', f0:1000, f1:1300, dur:0.045, vol:0.26});
        break;
      case 'error':
        Audio8.tone({type:'square', f0:200, f1:150, dur:0.14, vol:0.34});
        break;
      case 'stage':    // 스테이지 진입
        [523,784].forEach((f,i)=>Audio8.tone({
          type:'triangle', f0:f, f1:f*1.5, dur:0.2, vol:0.36, delay:i*0.1, slide:'exp'}));
        break;
      default:
        Audio8.tone({type:'square', f0:660, f1:660, dur:0.07, vol:0.3});
    }
  }catch(e){}
}

// ---------------- 배경음악 (차원별 자동 전환) ----------------
const BGM = (() => {
  let timer = null, step = 0, curTrack = null, playing = false;

  // 스케일 (반음 단위)
  const TRACKS = {
    normal:  {bpm:112, root:220, scale:[0,3,5,7,10], wave:'square',   bassWave:'triangle', mood:0},
    enhanced:{bpm:126, root:233, scale:[0,2,4,7,9],  wave:'square',   bassWave:'sawtooth', mood:1},
    dark:    {bpm:96,  root:174, scale:[0,1,5,7,8],  wave:'sawtooth', bassWave:'sawtooth', mood:2},
    divine:  {bpm:104, root:262, scale:[0,4,7,11,14],wave:'triangle', bassWave:'sine',     mood:3},
    chaos:   {bpm:140, root:196, scale:[0,1,4,6,7,10],wave:'sawtooth',bassWave:'sawtooth', mood:4},
    boss:    {bpm:150, root:147, scale:[0,1,3,6,7],  wave:'sawtooth', bassWave:'sawtooth', mood:5},
  };

  function pickTrack(){
    if(typeof mob !== 'undefined' && mob && mob.isBoss) return 'boss';
    if(!S) return 'normal';
    const s = S.stage || 1;
    if(s > 200) return 'chaos';
    if(s > 150) return 'divine';
    if(s > 100) return 'enhanced';
    const w = (typeof worldIdx === 'function') ? worldIdx(s) : 0;
    return (w===1 || w===5 || w===7) ? 'dark' : 'normal';
  }

  function note(semi, root){ return root * Math.pow(2, semi/12); }

  function tick(){
    if(!S || !S.settings || !S.settings.bgm){ return; }
    const key = pickTrack();
    if(key !== curTrack){ curTrack = key; step = 0; }
    const T = TRACKS[key];
    const bar = step % 16;

    // 베이스 (4비트)
    if(bar % 4 === 0){
      const bn = note(T.scale[(Math.floor(step/16) + (bar?2:0)) % T.scale.length] - 12, T.root);
      Audio8.tone({type:T.bassWave, f0:bn, f1:bn, dur:0.34, vol:0.30, bus:'bgm',
                   filter:{type:'lowpass', f0:900, f1:400}});
    }
    // 멜로디
    if(bar % 2 === 0 || Math.random() < 0.35){
      const idx = (step*3 + Math.floor(step/8)) % T.scale.length;
      const oct = (step % 32 < 16) ? 0 : 12;
      const n = note(T.scale[idx] + oct, T.root);
      Audio8.tone({type:T.wave, f0:n, f1:n, dur:0.16, vol:0.16, bus:'bgm'});
    }
    // 하이햇
    if(bar % 2 === 1){
      Audio8.noise({dur:0.045, f0:9000, f1:6000, vol:0.10, type:'highpass'});
    }
    // 킥
    if(bar % 8 === 0){
      Audio8.tone({type:'sine', f0:110, f1:45, dur:0.16, vol:0.34, slide:'exp', bus:'bgm'});
    }
    step++;
  }

  function start(){
    if(playing) return;
    Audio8.init();
    playing = true;
    const T = TRACKS[pickTrack()];
    const interval = 60000 / (T.bpm * 4);
    timer = setInterval(tick, interval);
  }
  function stop(){ if(timer) clearInterval(timer); timer=null; playing=false; }
  function toggle(on){ on ? start() : stop(); }
  return { start, stop, toggle, isPlaying: () => playing };
})();

// 첫 사용자 입력 시 오디오 활성화 (브라우저 정책)
(function unlockAudio(){
  const un = () => {
    Audio8.resume();
    if(S && S.settings && S.settings.bgm) BGM.start();
    ['click','keydown','touchstart'].forEach(e => document.removeEventListener(e, un));
  };
  ['click','keydown','touchstart'].forEach(e => document.addEventListener(e, un, {once:false}));
})();

function updateBgm(){
  if(S.settings.bgm && !bgmInt){
    const notes = [262,330,392,523,392,330,294,330];
    let i = 0;
    bgmInt = setInterval(()=>{
      try{
        AC = AC || new (window.AudioContext||window.webkitAudioContext)();
        const o = AC.createOscillator(), g = AC.createGain();
        o.connect(g); g.connect(AC.destination);
        o.type = 'triangle'; o.frequency.value = notes[i++%notes.length];
        g.gain.setValueAtTime(0.018, AC.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, AC.currentTime+0.28);
        o.start(); o.stop(AC.currentTime+0.3);
      }catch(e){}
    }, 320);
  } else if(!S.settings.bgm && bgmInt){ clearInterval(bgmInt); bgmInt = null; }
}

/* ---------- 🏆 업적 ---------- */
const ACHS = [
  {id:'k100',  name:'몬스터 100마리 처치',   c:()=>S.totalKills>=100,   r:20},
  {id:'k1000', name:'몬스터 1,000마리 처치', c:()=>S.totalKills>=1000,  r:60},
  {id:'k10000',name:'몬스터 10,000마리 처치',c:()=>S.totalKills>=10000, r:200},
  {id:'s10',   name:'스테이지 10 도달',      c:()=>(S.maxStage||1)>=10, r:30},
  {id:'s30',   name:'스테이지 30 도달',      c:()=>(S.maxStage||1)>=30, r:100},
  {id:'s50',   name:'스테이지 50 도달',      c:()=>(S.maxStage||1)>=50, r:300},
  {id:'e10',   name:'강화 10번 성공',        c:()=>(S.enhSuccess||0)>=10, r:40},
  {id:'e50',   name:'강화 50번 성공',        c:()=>(S.enhSuccess||0)>=50, r:150},
  {id:'r1',    name:'첫 환생',               c:()=>S.rebirths>=1, r:80},
  {id:'r5',    name:'환생 5회',              c:()=>S.rebirths>=5, r:250},
  {id:'t10',   name:'무한의 탑 10층 돌파',   c:()=>S.tower>=11, r:100},
  {id:'c10',   name:'무기 도감 10종 수집',   c:()=>Object.keys(S.coll||{}).length>=10, r:80},
];
function checkAchievements(){
  ACHS.forEach(a=>{
    if(!S.ach[a.id] && a.c()){
      S.ach[a.id] = true;
      const g = Math.floor(BAL.goldDrop(S.stage)*a.r);
      S.gold += g; recGold(g);
      log('<span class="g">🏆 업적 달성 ['+a.name+'] 보너스 +'+fmt(g)+'G</span>');
    }
  });
}

/* ---------- 🚪 비밀 방 ---------- */
function secretRoom(){
  log('<span class="p">🚪 비밀의 방 발견! 상자 5개를 엽니다…</span>');
  for(let i=0;i<5;i++){
    const r = Math.random();
    if(r < 0.5){ const g = Math.floor(BAL.goldDrop(S.stage)*20); S.gold += g; recGold(g); log('📦 <span class="g">+'+fmt(g)+'G</span>'); }
    else if(r < 0.8){ S.stones += 3; log('📦 <span class="c">강화석 +3</span>'); }
    else { dropEquip(worldIdx(S.stage), true); }
  }
}

/* ---------- 🛠 장비: 분해 / 초월 ---------- */
function dismantleItem(id){
  { const _e = eqById(id); if(isDevItem(_e)){ log('<span class="r">개발자 장비는 분해할 수 없습니다.</span>'); return; } }

  const e = eqById(id); if(!e || e.lock) return;
  if(S.weapon===id || S.armor===id){ log('<span class="r">장착 중인 장비는 분해할 수 없습니다.</span>'); return; }
  const st = 1 + GRADES.indexOf(e.grade);
  S.equips.splice(S.equips.indexOf(e), 1);
  S.stones += st;
  log('<span class="c">♻ 분해: '+e.name+' → 강화석 +'+st+'</span>');
  renderAll(); saveGame(true);
}
function awakenItem(id){
  const e = eqById(id); if(!e || e.enh<10 || (e.awk||0)>=3) return;
  if(S.shards < 3){ log('<span class="r">균열의 조각 3개가 필요합니다.</span>'); return; }
  S.shards -= 3; e.awk = (e.awk||0)+1;
  log('<span class="p">☀ 초월 '+e.awk+'단계! 기본 성능 2배!</span>');
  renderAll(); saveGame(true);
}

/* ---------- 🌳 특성 트리 ---------- */
const TALENTS = {
  atk:   {n:'⚔ 공격 특화', d:'공격력 +5%/Lv', max:20},
  gold:  {n:'💰 황금 감각', d:'골드 획득 +5%/Lv', max:20},
  aps:   {n:'⚡ 자동 공격', d:'초당 자동 공격 +0.5회/Lv (방치 코어)', max:6},
  dtap:  {n:'👆 더블 탭', d:'클릭 시 2연타 확률 +6%/Lv', max:8},
  steal: {n:'🩸 흡혈', d:'처치 시 최대HP +1% 회복/Lv', max:5},
  critd: {n:'💥 치명 증폭', d:'치명타 대미지 +20%/Lv', max:10},
  revive:{n:'✝ 불굴', d:'사망 시 1회 부활 (HP 20% · 무적 3초, 스테이지마다 충전)', max:1},
};

/* ---------- 🕐 암시장 ---------- */
const BM_POOL = [
  {name:'강화석 3개', p:s=>Math.floor(BAL.goldDrop(s)*10), f:()=>{S.stones+=3;}},
  {name:'강화석 8개 (특가!)', p:s=>Math.floor(BAL.goldDrop(s)*22), f:()=>{S.stones+=8;}},
  {name:'공격 물약 (5분)', p:s=>Math.floor(BAL.goldDrop(s)*25), f:()=>{S.potionUntil=Math.max(Date.now(),S.potionUntil)+300000;}},
  {name:'픽업 부적 — 프리미엄 10회 전설 확률 UP', p:s=>Math.floor(BAL.goldDrop(s)*40), f:()=>{S.pickup+=10;}},
  {name:'균열의 조각 1개 (희귀 매물!)', p:s=>Math.floor(BAL.goldDrop(s)*120), f:()=>{S.shards++;}},
];
function bmItems(){
  const seed = Math.floor(Date.now()/3600000);
  if(S.bm.seed !== seed) S.bm = {seed, bought:{}};
  let r = seed;
  const rand = ()=>{ r = (r*1103515245+12345) % 2147483648; return r/2147483648; };
  const out = [];
  for(let i=0;i<3;i++) out.push(BM_POOL[Math.floor(rand()*BM_POOL.length)]);
  return out;
}

/* ---------- 🎮 콘텐츠 기능 ---------- */
function toggleTower(){
  if(battleMode==='golddgn'){ log('<span class="r">던전 진행 중에는 이동할 수 없습니다.</span>'); return; }
  if(battleMode==='tower'){ battleMode='field'; log('🗼 탑에서 나와 필드로 복귀합니다.'); }
  else { battleMode='tower'; log('<span class="c">🗼 무한의 탑 '+S.tower+'층 도전!</span>'); }
  spawnMob(false); renderStats(); renderContent();
}
function enterGoldDgn(){
  ensureDaily();
  if(battleMode!=='field'){ log('<span class="r">필드에서만 입장할 수 있습니다.</span>'); return; }
  if(S.goldDgnUses>=3){ log('<span class="r">오늘 입장 횟수를 모두 사용했습니다. (3/3)</span>'); return; }
  S.goldDgnUses++;
  battleMode='golddgn'; dgnUntil=Date.now()+60000; dgnGold=0;
  log('<span class="g">⛏ 미다스의 방 입장! 60초 동안 마음껏 두들기세요!</span>');
  spawnMob(false); renderStats();
}
function toggleMine(){
  if(!S.pets.golemp){ log('<span class="r">꼬마 골렘이 필요합니다. (상점 → 동료 영입)</span>'); return; }
  if(S.mine.on){
    const n = Math.min(24, Math.floor((Date.now()-S.mine.start)/600000));
    S.stones += n; S.mine.on = false;
    log('<span class="c">⛏ 광산 회수 완료: 강화석 +'+n+'</span>');
  } else {
    S.mine.on = true; S.mine.start = Date.now();
    log('⛏ 꼬마 골렘을 광산에 보냈습니다. (10분당 강화석 1개)');
  }
  renderAll(); saveGame(true);
}
function doExped(){
  if(S.exp2.start > 0){
    if(Date.now()-S.exp2.start < 1800000) return;
    S.exp2.start = 0;
    const g = Math.floor(BAL.goldDrop(S.stage)*60); S.gold += g; recGold(g);
    S.stones += 3;
    let extra = '';
    if(Math.random()<0.3){ dropEquip(worldIdx(S.stage), true); extra=' · 장비 획득!'; }
    if(Math.random()<0.2){ S.shards++; extra+=' · <span class="p">조각 +1</span>'; }
    log('<span class="g">🎁 탐험 복귀! 전리품: +'+fmt(g)+'G · 강화석 +3'+extra+'</span>');
  } else {
    if(Object.keys(S.pets).length < 2){ log('<span class="r">동료가 2마리 이상 필요합니다.</span>'); return; }
    S.exp2.start = Date.now();
    log('🚪 동료들이 차원의 문으로 떠났습니다. (30분 후 복귀)');
  }
  renderAll(); saveGame(true);
}
function playDice(){
  let bet = Math.floor(parseInt($('diceBet').value)||0);
  if(bet < 1) return;
  if(bet > S.gold){ log('<span class="r">걸 골드가 부족합니다.</span>'); return; }
  const me = 1+Math.floor(Math.random()*6), house = 1+Math.floor(Math.random()*6);
  if(me > house){ S.gold += bet; recGold(bet); log('🎲 나 <b>'+me+'</b> vs 딜러 '+house+' — <span class="g">승리! +'+fmt(bet)+'G</span>'); }
  else if(me === house){ log('🎲 '+me+' vs '+house+' — 무승부, 판돈 환불'); }
  else { S.gold -= bet; log('🎲 나 '+me+' vs 딜러 <b>'+house+'</b> — <span class="r">패배… -'+fmt(bet)+'G</span>'); }
  renderStats(); saveGame(true);
}
function claimFree(){
  if(Date.now() < S.freeAt) return;
  const g = Math.floor(BAL.goldDrop(S.stage)*15);
  S.gold += g; recGold(g);
  S.freeAt = Date.now()+300000;
  log('<span class="g">🎁 무료 보상 +'+fmt(g)+'G (5분 후 다시)</span>');
  renderAll(); saveGame(true);
}
function buyPotion(){
  const c = Math.floor(BAL.goldDrop(S.stage)*30);
  if(S.gold < c) return;
  S.gold -= c;
  S.potionUntil = Math.max(Date.now(), S.potionUntil) + 300000;
  log('<span class="c">🧪 공격 물약 사용! 5분간 공격력 +50%</span>');
  renderAll(); saveGame(true);
}

/* ---------- ⚙️ 설정 기능 ---------- */
function togSet(k){ S.settings[k] = !S.settings[k]; if(k==='bgm') updateBgm(); renderSettings(); saveGame(true); }
function togAutoSell(){ S.autoSell = !S.autoSell; renderSettings(); saveGame(true); }
function setDmgSize(v){ S.settings.dmgSize = v; saveGame(true); log('대미지 숫자 크기 변경: x'+v); }
function setDmgColor(v){ S.settings.dmgColor = v; saveGame(true); log('대미지 색상 변경: '+v); }
const THEMES = {
  purple:{'--rift':'#a06bff','--cyan':'#43e6cf','--bg':'#0c0a1a','--panel':'#161231','--panel2':'#1d1840','--line':'#2e2560'},
  blue:{'--rift':'#4aa8ff','--cyan':'#6be8ff','--bg':'#060d18','--panel':'#0c1830','--panel2':'#102040','--line':'#1c3a60'},
  green:{'--rift':'#4ade80','--cyan':'#d8ff6b','--bg':'#06120a','--panel':'#0c2414','--panel2':'#10301c','--line':'#1c5030'},
};
function applyTheme(n){
  const t = THEMES[n] || THEMES.purple;
  for(const k in t) document.documentElement.style.setProperty(k, t[k]);
  S.settings.theme = n;
}
function smartUp(kind){
  let cnt = 0;
  while(cnt < 999 && upStat(kind)) cnt++;
  const nm = kind==='atk' ? '공격' : kind==='def' ? '방어' : '치명';
  log('<span class="c">🤖 스마트 자동 강화: '+nm+' +'+cnt+'회 (골드 소진까지)</span>');
}
function bagCost(){ return Math.floor(500*Math.pow(3, (S.invCap-30)/10)); }
function expandBag(){
  if(S.invCap >= 100) return;
  const c = bagCost();
  if(S.gold < c) return;
  S.gold -= c; S.invCap += 10;
  log('<span class="c">🎒 가방 확장! 현재 '+S.invCap+'칸</span>');
  renderAll(); saveGame(true);
}
function exportSave(){
  try{
    const code = btoa(unescape(encodeURIComponent(JSON.stringify(S))));
    prompt('아래 세이브 코드를 복사해 보관하세요:', code);
  }catch(e){ alert('내보내기 실패'); }
}
function importSave(){
  const code = prompt('세이브 코드를 붙여넣으세요:');
  if(!code) return;
  try{
    const d = JSON.parse(decodeURIComponent(escape(atob(code.trim()))));
    localStorage.setItem(SAVE_KEY, JSON.stringify(d));
    location.reload();
  }catch(e){ alert('코드가 올바르지 않습니다.'); }
}

/* ---------- 렌더: 콘텐츠 / 특성·도감 / 설정 ---------- */
function renderContent(){
  if(!S) return;
  $('towerFloorTxt').textContent = '현재 '+S.tower+'층';
  $('towerBtn').textContent = battleMode==='tower' ? '나가기' : '입장';
  $('dgnUseTxt').textContent = '오늘 '+(3-S.goldDgnUses)+'/3회 남음';
  if(S.mine.on){
    const n = Math.min(24, Math.floor((Date.now()-S.mine.start)/600000));
    $('mineInfo').innerHTML = '⛏ 채굴 중… 적재량 <b>'+n+'/24</b><small>10분당 강화석 1개</small>';
    $('mineBtn').textContent = '회수';
  } else {
    $('mineInfo').innerHTML = '꼬마 골렘을 광산에 보내 강화석 채굴<small>10분당 1개 · 최대 24개'+(S.pets.golemp?'':' · <span style="color:var(--red)">꼬마 골렘 필요</span>')+'</small>';
    $('mineBtn').textContent = '보내기';
  }
  if(S.exp2.start > 0){
    const left = 1800000-(Date.now()-S.exp2.start);
    if(left > 0){ $('expInfo').innerHTML = '🚪 탐험 중… <b>'+fmtDur(Math.ceil(left/1000))+'</b> 후 복귀'; $('expBtn').textContent='탐험 중'; $('expBtn').disabled=true; }
    else { $('expInfo').innerHTML = '🎁 <b style="color:var(--gold)">전리품 상자 도착!</b>'; $('expBtn').textContent='상자 열기'; $('expBtn').disabled=false; }
  } else {
    const cnt = Object.keys(S.pets).length;
    $('expInfo').innerHTML = '동료들을 30분 탐험 보내기<small>복귀 시 무작위 전리품'+(cnt>=2?'':' · <span style="color:var(--red)">동료 2마리 필요</span>')+'</small>';
    $('expBtn').textContent = '출발'; $('expBtn').disabled = cnt<2;
  }
  $('bountyInfo').innerHTML = '오늘의 수배 대상: <b>'+worldOf(S.stage).mob+'</b> '+S.bounty.need+'마리<small>진행 '+Math.min(S.bounty.cur,S.bounty.need)+'/'+S.bounty.need+(S.bounty.cur>=S.bounty.need?' · <span style="color:var(--green)">완료! (보상 지급됨)</span>':' · 보상: 골드 + 조각 1')+'</small>';
  const fl = S.freeAt - Date.now();
  $('freeInfo').textContent = fl>0 ? fmtDur(Math.ceil(fl/1000))+' 후 수령 가능' : '지금 받을 수 있어요!';
  $('freeBtn').disabled = fl>0;
  const pl2 = S.potionUntil - Date.now();
  $('potionInfo').textContent = pl2>0 ? '🧪 효과 지속: '+fmtDur(Math.ceil(pl2/1000)) : '';
  const pc = Math.floor(BAL.goldDrop(S.stage)*30);
  $('potionBtn').textContent = fmt(pc)+' G';
  $('potionBtn').disabled = S.gold < pc;
  // 암시장
  const items = bmItems();
  const bl = $('bmList'); bl.innerHTML='';
  items.forEach((it, i)=>{
    const row = document.createElement('div'); row.className='row';
    const price = it.p(S.stage);
    const bought = !!S.bm.bought['i'+i];
    row.innerHTML = '<div class="info">'+it.name+'</div>';
    const b = document.createElement('button'); b.className='gold-btn';
    b.textContent = bought ? '품절' : fmt(price)+' G';
    b.disabled = bought || S.gold < price;
    b.onclick = ()=>{ S.gold -= price; it.f(); S.bm.bought['i'+i]=true; log('<span class="g">🕐 암시장 구매: '+it.name+'</span>'); renderAll(); saveGame(true); };
    row.appendChild(b); bl.appendChild(row);
  });
  // 📊 통계
  const now = Date.now();
  dmgEv = dmgEv.filter(e=>now-e[0] < 10000);
  goldEv = goldEv.filter(e=>now-e[0] < 60000);
  const dps = dmgEv.reduce((a,e)=>a+e[1],0)/10;
  const gpm = goldEv.reduce((a,e)=>a+e[1],0);
  const dash = $('statsDash');
  if(dash) dash.innerHTML =
    'DPS (10초 평균): <b>'+fmt(dps)+'</b><br>'+
    '골드/분: <b>'+fmt(gpm)+'</b><br>'+
    '총 처치 수: <b>'+fmt(S.totalKills||0)+'</b> · 무기 숙련 보너스: <b>+'+Math.min(50,(S.mastery||0)*0.01).toFixed(1)+'%</b><br>'+
    '가챠 천장: <b>'+(S.pity||0)+'/40</b> · 픽업 부적: <b>'+(S.pickup||0)+'회</b><br>'+
    '스피드런 최고기록 (50층): <b>'+(S.speedBest?fmtDur(S.speedBest):'—')+'</b>';
  // 🔥 피버 & DPS 라인
  $('feverBar').style.width = (now < S.feverUntil ? 100 : (S.feverGauge||0))+'%';
  $('feverTxt').textContent = now < S.feverUntil ? '🔥 피버!! x2대미지·x3골드' : (S.feverGauge||0)+'%';
  const myEl = eqById(S.weapon) && eqById(S.weapon).el;
  $('dpsLine').innerHTML = '📊 DPS <b>'+fmt(dps)+'</b> · 골드/분 <b>'+fmt(gpm)+'</b> · 무기 속성 '+(myEl?ELEMS[myEl]+myEl:'무')+' vs 몹 '+(mob&&mob.el?ELEMS[mob.el]+mob.el:'무')+' '+(myEl&&mob&&mob.el?(BEATS[myEl]===mob.el?'<span style="color:var(--green)">(유리 x2)</span>':BEATS[mob.el]===myEl?'<span style="color:var(--red)">(불리 x0.5)</span>':''):'');
}
function renderTalents(){
  if(!S) return;
  const list = $('talentList'); list.innerHTML='';
  Object.entries(TALENTS).forEach(([k, t])=>{
    const lv = S.talents[k]||0, cost = lv+1;
    const row = document.createElement('div'); row.className='row';
    row.innerHTML = '<div class="info">'+t.n+' <b style="color:var(--rift)">Lv.'+lv+'/'+t.max+'</b><small>'+t.d+'</small></div>';
    const b = document.createElement('button'); b.className='buy';
    b.textContent = lv>=t.max ? 'MAX' : '조각 '+cost;
    b.disabled = lv>=t.max || S.shards < cost;
    b.onclick = ()=>{ S.shards -= cost; S.talents[k] = lv+1; log('<span class="p">🌳 특성 ['+t.n+'] Lv.'+(lv+1)+' 습득!</span>'); renderAll(); saveGame(true); };
    row.appendChild(b); list.appendChild(row);
  });
  $('collCnt').textContent = '('+Object.keys(S.coll||{}).length+'종 수집 · 공격 +'+Object.keys(S.coll||{}).length+'%)';
  $('masteryInfo').innerHTML =
    '⚔ 무기 숙련도: <b>'+fmt(S.mastery||0)+'</b>회 사냥 (대미지 +'+Math.min(50,(S.mastery||0)*0.01).toFixed(1)+'% / 최대 50%)<br>'+
    '👑 명성 등급: <b style="color:var(--gold)">'+rankTitle()+'</b> <small style="color:var(--mut)">(환생 '+S.rebirths+'회 · 최고 스테이지 '+(S.maxStage||1)+')</small><br>'+
    '⭐ 펫 성급 합계: <b>'+totalPetStars()+'★</b> (공격 +'+(totalPetStars()*2)+'%)';
  const al = $('achList'); al.innerHTML='';
  ACHS.forEach(a=>{
    const done = !!S.ach[a.id];
    const d = document.createElement('div'); d.className='art';
    d.innerHTML = '<span>'+(done?'✅ ':'⬜ ')+a.name+'</span><span style="color:var(--mut)">'+(done?'달성 완료':'보상 ≈'+fmt(Math.floor(BAL.goldDrop(S.stage)*a.r))+'G')+'</span>';
    al.appendChild(d);
  });
}
function renderSettings(){
  if(!S) return;
  $('sfxBtn').textContent = S.settings.sfx ? 'ON' : 'OFF';
  $('bgmBtn').textContent = S.settings.bgm ? 'ON' : 'OFF';
  $('shakeBtn').textContent = S.settings.shake ? 'ON' : 'OFF';
  $('autoSellBtn').textContent = S.autoSell ? 'ON' : 'OFF';
  const c = bagCost();
  $('bagTxt').textContent = '현재 '+S.invCap+'칸';
  $('bagBtn').textContent = S.invCap>=100 ? 'MAX' : fmt(c)+' G';
  $('bagBtn').disabled = S.invCap>=100 || S.gold < c;
}

/* ---------- 수동 전투: 몹 클릭 공격 (쿨타임 0.01초) ---------- */
const MANUAL_CD_MS = 10; // 0.01초
let lastManualAtk = 0;
function heroStrike(fromClick, isEcho){
  if(performance.now() < deadUntil) return;
  if(!mob || (mob.hp <= 0 && !mob.sandbag) || !mobInRange()) return;
  // 🎯 미스: 민첩이 높을수록 감소
  const missCh = Math.max(0.01, 0.06 - (S.stats.dex-10)*0.002);
  if(Math.random() < missCh){ addDmgNum(0, 'miss', false, false); return; }
  let dmg = playerATK() * (0.9 + Math.random()*0.2);
  // 🔥 속성 상성 (무기 vs 몬스터)
  const wep = eqById(S.weapon);
  dmg *= elemMult(wep && wep.el, mob.el);
  const crit = Math.random() < critRate();
  if(crit) dmg *= critDmgMult();
  hitMob(dmg, crit, false);
  pLunge = 1;
  // 👆 더블 탭 특성
  if(fromClick && !isEcho && Math.random() < 0.06*(S.talents.dtap||0)){
    setTimeout(()=>heroStrike(true, true), 60);
  }
}
function playerManualAttack(){
  const now = Date.now();
  if(now - lastManualAtk < MANUAL_CD_MS) return; // 클릭 쿨타임 0.01초
  lastManualAtk = now;
  heroStrike(true, false);
}
cv.style.cursor = 'crosshair';
cv.addEventListener('pointerdown', e=>{
  const r = cv.getBoundingClientRect();
  const x = (e.clientX - r.left) * (cv.width / r.width);
  const y = (e.clientY - r.top) * (cv.height / r.height);
  const bw = mob && mob.isBoss ? 150 : 100; // 몹 히트박스 (넉넉하게)
  if(mob && x >= mobX - 25 && x <= mobX + bw && y >= 60 && y <= FLOOR_Y + 12){
    playerManualAttack();
  }
});

/* ---------- 메인 루프 & 초기화 ---------- */
let uiTimer = 0;
function loop(now){
  combatTick(now);
  render(now);
  renderHpBars();
  uiTimer += 16;
  if(uiTimer > 400){ uiTimer = 0; ensureDaily(); renderStats(); renderContent(); }
  requestAnimationFrame(loop);
}

// ===== (병합됨: 난이도/자동저장 - init보다 먼저 정의) =====

// 페이지를 나갈 때 자동 저장
window.addEventListener('beforeunload', function() {
  if(S) {
    saveGame(true);
    updateRanking();
  }
});

// 페이지 언로드 시 저장
window.addEventListener('unload', function() {
  if(S) {
    saveGame(true);
  }
});

// 페이지가 백그라운드로 갈 때 저장 (모바일)
document.addEventListener('visibilitychange', function() {
  if(document.hidden && S) {
    saveGame(true);
    updateRanking();
  }
});

// 페이지 포커스를 잃을 때 저장
window.addEventListener('blur', function() {
  if(S) {
    saveGame(true);
  }
});

function setDifficulty(diff) {
  currentDifficulty = diff;
  storage.setItem('rift-difficulty', diff);
  const _dm = document.getElementById('difficultyModal'); if(_dm) _dm.style.display = 'none';
  log('<span class="c">난이도: ' + (diff === 'easy' ? '🟢 쉬움' : diff === 'normal' ? '🟡 보통' : '🔴 어려움') + '</span>');
  spawnMob(false);
  renderStats();
}

function loadDifficulty() {
  const saved = storage.getItem('rift-difficulty');
  const modal = document.getElementById('difficultyModal');
  if(saved && DIFFICULTY[saved]) {
    currentDifficulty = saved;
    if(modal) modal.style.display = 'none';
  } else {
    if(modal) modal.style.display = 'flex';
  }
}


// ===== 병합 끝 =====
(async function init(){
  // 🗄️ IndexedDB에서 먼저 복원 (새로고침/재접속해도 이어서 플레이)
  initNetwork();
  setTimeout(()=>{ if(S && S.settings && S.settings.bgm) BGM.start(); }, 800);
  try { await restoreFromDB(); } catch(e) { console.error('DB 복원 실패:', e); }
  // 🖥️ EXE 모드: 파일 저장소에서 먼저 복원 (localStorage가 비어있어도 파일에서 복구)
  if(IS_ELECTRON && typeof window.restoreFromFileStorage === 'function'){
    try { await window.restoreFromFileStorage(); } catch(e) { console.error('파일 복원 실패:', e); }
  }
  // 🐍 Python 모드: pywebview 준비 대기 후 파일에서 복원
  try {
    const hasPy = await PYWEBVIEW_READY;
    if(hasPy){ await restoreFromPyStorage(); }
  } catch(e) { console.error('py 복원 실패:', e); }
  const loaded = await loadGame();
  if(loaded){
    loadDifficulty();
    S = loaded;
    const elapsed = (Date.now() - (S.savedAt || Date.now()))/1000;
    if(elapsed > 60){
      const r = calcOffline(elapsed);
      S.gold += r.gold; gainExp(r.exp);
      showModal('⏰ 오프라인 보상',
        '<b>'+fmtDur(r.sec)+'</b> 동안 만물상이 자동으로 사냥했습니다!<br>'+
        '<span class="big">골드 +'+fmt(r.gold)+'</span><br>경험치 +'+fmt(r.exp)+
        '<br><small style="color:var(--mut)">누적 한도 '+r.capH+'시간 · 온라인 효율의 50%</small>');
    }
    log('<span class="c">저장된 차원에서 이어서 시작합니다.</span>');
  } else {
    S = freshState();
    loadDifficulty();
    log('<span class="p">차원 균열이 열렸습니다. 만물상 영업 개시!</span>');
  }
  initIdentity();
  applyTheme(S.settings.theme);
  ensureDaily();
  updateBgm();
  initSocial();
  regSW();
  pHpCur = playerMaxHP();
  spawnMob(false);
  renderAll();
  lastTick = performance.now();
  requestAnimationFrame(loop);
  startAutoSave();
})().catch(err=>{ console.error('게임 초기화 에러:', err); alert('게임 로드 실패: '+err.message); });


// 채팅 입력 창에서 Enter 키 처리
document.addEventListener('DOMContentLoaded', ()=>{
  const gChatInput = document.getElementById('gChatInput');
  const guildChatInput = document.getElementById('guildChatInput');
  
  if(gChatInput) {
    gChatInput.addEventListener('keypress', e=>{
      if(e.key==='Enter' && !e.shiftKey) {
        e.preventDefault();
        sendGlobalChat();
      }
    });
  }
  
  if(guildChatInput) {
    guildChatInput.addEventListener('keypress', e=>{
      if(e.key==='Enter' && !e.shiftKey) {
        e.preventDefault();
        sendGuildChat();
      }
    });
  }
});


// ============================================================================
// 🐾 펫 시스템 (외형 + 장착)
// ============================================================================

let equippedPetId = null;

function equipPet(petId){
  const p = PETS.find(x=>x.id===petId);
  if(!p || !S.pets[petId]){
    alert('펫을 보유하지 않았습니다');
    return;
  }
  equippedPetId = petId;
  renderPetUI();
  alert(p.emoji+' '+p.name+'을(를) 장착했습니다!');
}

function unequipPet(){
  equippedPetId = null;
  renderPetUI();
}

function renderPetUI(){
  // 펫 보관함 표시
  const petInv = document.getElementById('petInventory');
  if(!petInv) {
    console.log('⚠️ petInventory 요소 없음');
    return;
  }
  
  if(!S || !S.pets) {
    petInv.innerHTML = '<div style="color:var(--mut);">펫을 보유하지 않았습니다</div>';
    return;
  }
  
  petInv.innerHTML = PETS
    .filter(p=>S.pets[p.id])
    .map(p=>{
      const stars = S.petStars[p.id] || 0;
      return `
        <div style="
          position:relative;
          padding:8px;
          border:2px solid ${equippedPetId===p.id ? 'var(--gold)' : 'var(--line)'};
          background:var(--panel2);
          color:var(--txt);
          border-radius:4px;
          cursor:pointer;
          text-align:center;
          transition:all 0.2s;
        " onclick="equipPet('${p.id}')" title="${p.name}">
          <div style="font-size:24px;">${p.emoji || '🟢'}</div>
          <div style="font-size:9px;">${p.name}</div>
          <div style="font-size:9px; color:var(--gold);">⭐${stars}</div>
          <button onclick="event.stopPropagation(); enhancePetStar('${p.id}')" 
            style="width:100%; margin-top:4px; padding:3px; font-size:9px; background:var(--rift); border:none; color:var(--txt); border-radius:2px; cursor:pointer;">
            강화
          </button>
        </div>
      `;
    }).join('');
  
  // 현재 장착 펫 표시
  const equipped = document.getElementById('equippedPet');
  if(!equipped) {
    console.log('⚠️ equippedPet 요소 없음');
    return;
  }
  
  if(equippedPetId && S && S.pets && S.pets[equippedPetId]){
    const p = PETS.find(x=>x.id===equippedPetId);
    const stars = S.petStars[equippedPetId] || 0;
    if(p) {
      equipped.innerHTML = `
        <div style="font-size:32px;">${p.emoji || '🟢'}</div>
        <div style="font-size:14px; color:var(--cyan); font-weight:bold;">${p.name}</div>
        <div style="font-size:11px; color:var(--mut); margin:5px 0; line-height:1.4;">${p.desc}</div>
        <div style="font-size:11px; color:var(--gold); margin:8px 0;">⭐ ${stars}성</div>
      `;
    }
  } else {
    equipped.innerHTML = '<span style="color:var(--mut);">펫을 선택하세요</span>';
  }
}

function getEquippedPetEffect(){
  if(!equippedPetId) return '';
  const p = PETS.find(x=>x.id===equippedPetId);
  if(!p) return '';
  
  let effect = p.desc;
  const stars = S.petStars[equippedPetId] || 0;
  if(stars > 0){
    const mult = (1 + 0.05*stars);
    effect += ` (성급 +${Math.floor((mult-1)*100)}%)`;
  }
  return effect;
}

function totalPetStars(){
  return Object.values(S.petStars).reduce((a,b)=>a+b, 0);
}

function buyPet(id){
  const p = PETS.find(x=>x.id===id);
  if(!p) return;
  
  if(S.pets[id]){
    alert('이미 보유한 펫입니다!');
    return;
  }
  
  if(!S.inv[p.mat] || S.inv[p.mat] < p.need){
    alert(p.mat + ' ' + p.need + '개 필요');
    return;
  }
  
  S.inv[p.mat] -= p.need;
  S.pets[id] = true;
  S.petStars[id] = 0;
  
  playSound(0.5, 800, 0.1);
  alert(p.emoji + ' ' + p.name + ' 획득!');
  renderPetUI();
  renderShop();
  saveGame();
}

// 펫 뽑기 (가챠)
function petGacha(count=1){
  let cost = 1200;
  let actualCost = 0;
  let newPets = [];
  
  for(let i=0; i<count; i++){
    const unowned = PETS.filter(p=>!S.pets[p.id]);
    
    if(unowned.length === 0){
      // 모두 보유 시 환급
      actualCost += 600;
    } else {
      const p = unowned[Math.floor(Math.random()*unowned.length)];
      S.pets[p.id] = true;
      S.petStars[p.id] = 0;
      newPets.push(p);
      actualCost += cost;
    }
  }
  
  if(S.gold < actualCost){
    alert('골드 ' + actualCost + '개 필요');
    return;
  }
  
  S.gold -= actualCost;
  
  if(newPets.length > 0){
    let msg = '획득한 펫:\n';
    newPets.forEach(p=>msg += p.emoji + ' ' + p.name + '\n');
    alert(msg);
    playSound(0.5, 800, 0.1);
  } else {
    alert('모두 보유한 펫입니다! (600G 환급)');
  }
  
  renderPetUI();
  renderShop();
  saveGame();
}


// ============================================================================
// 🐾 펫 효과 시스템
// ============================================================================

function applyPetEffects(){
  let dmgMult = 1, goldMult = 1, defMult = 1, dodgeMult = 1;
  
  if(!equippedPetId) return {dmgMult, goldMult, defMult, dodgeMult};
  
  const p = PETS.find(x=>x.id===equippedPetId);
  if(!p) return {dmgMult, goldMult, defMult, dodgeMult};
  
  // 각 펫의 특별 효과
  switch(equippedPetId){
    case 'slimep':  // 미니 슬라임: 협공
      dmgMult *= 1.20;
      break;
    case 'batp':    // 아기 박쥐: 골드
      goldMult *= 1.15;
      break;
    case 'golemp':  // 꼬마 골렘: 방어
      defMult *= 1.20;
      break;
    case 'phoenix': // 불꽃새: 공격 + 크리
      dmgMult *= 1.15;
      break;
    case 'specter': // 유령: 회피 + 체력
      dodgeMult *= 1.20;
      break;
  }
  
  // 펫 성급에 따른 추가 효과
  const stars = S.petStars[equippedPetId] || 0;
  dmgMult *= (1 + 0.05*stars);
  goldMult *= (1 + 0.03*stars);
  defMult *= (1 + 0.05*stars);
  dodgeMult *= (1 + 0.02*stars);
  
  return {dmgMult, goldMult, defMult, dodgeMult};
}

// 펫 협공 (주기적 공격)
function petAttack(){
  if(!equippedPetId) return false;
  
  // 펫별 공격 주기
  const intervals = {
    'slimep': 1200,
    'batp': 1500,
    'golemp': 2000,
    'phoenix': 1000,
    'specter': 1800
  };
  
  const interval = intervals[equippedPetId];
  if(!interval) return false;
  
  const now = performance.now();
  if(now - tPet < interval) return false;
  
  tPet = now;
  
  // 펫 공격력 = 플레이어 공격력의 20%
  const petDmg = Math.floor(getHeroDmg() * 0.2);
  if(curMob && petDmg > 0){
    hitMob(petDmg, true);
    return true;
  }
  
  return false;
}


// ============================================================================
// 🌟 펫 성급 강화 시스템
// ============================================================================

function enhancePetStar(petId){
  const p = PETS.find(x=>x.id===petId);
  if(!p) return;
  
  if(!S.pets[petId]){
    alert('펫을 보유하지 않았습니다');
    return;
  }
  
  const currentStars = S.petStars[petId] || 0;
  if(currentStars >= 5){
    alert('최대 성급입니다!');
    return;
  }
  
  // 성급 강화 비용: 조각 3개
  const cost = 3;
  if(!S.shards || S.shards < cost){
    alert('환생의 조각 ' + cost + '개 필요');
    return;
  }
  
  // 성공률 계산 (성급이 높을수록 낮음)
  const successRate = 100 - (currentStars * 15);
  const isSuccess = Math.random() * 100 < successRate;
  
  S.shards -= cost;
  
  if(isSuccess){
    S.petStars[petId] = (S.petStars[petId] || 0) + 1;
    const newStars = S.petStars[petId];
    playSound(0.5, 1000, 0.1);
    alert(p.emoji + ' ' + p.name + ' ⭐ ' + newStars + '성으로 강화됨!');
  } else {
    playSound(0.3, 300, 0.1);
    alert('펫 강화 실패...');
  }
  
  renderPetUI();
  renderArtifacts();
  saveGame();
}



// ============================================================================
// 💾 향상된 영구 저장 시스템
// ============================================================================

// 자동 저장 타이머
let autoSaveTimer = null;

function startAutoSave(){
  // 15초마다 자동 저장
  autoSaveTimer = setInterval(()=>saveGame(true), 15000);
  
  // 페이지 닫을 때 저장
  window.addEventListener('beforeunload', ()=>saveGame(true));
  
  // 모바일 백그라운드로 전환할 때 저장
  if('onpagehide' in window){
    window.addEventListener('pagehide', ()=>saveGame(true));
  }
  if('onvisibilitychange' in document){
    document.addEventListener('visibilitychange', ()=>{
      if(document.hidden) saveGame(true);
    });
  }
  
  console.log('✅ 자동 저장 활성화 (15초 주기)');
}

async function saveGame(silent){
  if(!S) return;
  updateRanking();
  
  try {
    S.savedAt = Date.now();          // ★ 저장 시각 갱신 (오프라인 보상 계산 기준)
    // 1. 주 저장소 (localStorage)
    const json = JSON.stringify(S);
    storage.setItem(SAVE_KEY, json);
    
    // 2. 백업 저장소 (혹시 모를 손상 대비)
    storage.setItem(BACKUP_KEY, json);
    
    // 3. 동기화 시간 기록
    storage.setItem(SYNC_KEY, Date.now().toString());
    
    if(!silent) alert('저장 완료!');
    console.log('💾 게임 저장됨:', new Date().toLocaleTimeString('ko-KR'));
  } catch(e) {
    console.error('저장 실패:', e);
    if(!silent) alert('저장 실패: ' + e.message);
  }
}

async function loadGame(){
  // 반환값: 저장 데이터 객체(있으면) / null(없거나 손상)
  const tryParse = (json, label) => {
    if(!json) return null;
    try {
      const obj = JSON.parse(json);
      // 유효성 검사 — 게임 데이터가 맞는지 확인
      if(!obj || typeof obj !== 'object') return null;
      if(typeof obj.level !== 'number' || typeof obj.stage !== 'number') return null;
      return reviveDevItems(obj);
    } catch(e) {
      console.warn('저장 손상(' + label + '):', e);
      return null;
    }
  };

  try {
    // 1. 주 저장소
    let data = tryParse(storage.getItem(SAVE_KEY), 'main');

    // 2. 실패 시 백업 저장소
    if(!data) {
      data = tryParse(storage.getItem(BACKUP_KEY), 'backup');
      if(data) {
        console.log('✅ 백업 데이터에서 복구됨');
        storage.setItem(SAVE_KEY, JSON.stringify(data));
      }
    }

    if(data) {
      S = data;
      const syncTime = storage.getItem(SYNC_KEY);
      if(syncTime) {
        console.log('✅ 저장된 게임 로드됨:', new Date(parseInt(syncTime)).toLocaleTimeString('ko-KR'));
      }
      return data;   // ★ init의 if(loaded) 판정을 위해 반드시 반환
    }

    console.log('ℹ️ 저장 데이터 없음 — 새 게임 시작');
    return null;
  } catch(e) {
    console.error('로드 실패:', e);
    return null;
  }
}

function exportGameData(){
  if(!S) { alert('게임 데이터가 없습니다'); return; }
  
  const data = JSON.stringify(S, null, 2);
  const blob = new Blob([data], {type: 'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = '차원균열_백업_' + new Date().toISOString().split('T')[0] + '.json';
  a.click();
  URL.revokeObjectURL(url);
  
  alert('백업 다운로드 완료!');
}

function importGameData(file){
  const reader = new FileReader();
  reader.onload = (e)=>{
    try {
      const data = JSON.parse(e.target.result);
      
      // 유효성 검사
      if(!data.level || !data.stage) {
        alert('유효하지 않은 게임 데이터입니다');
        return;
      }
      
      S = reviveDevItems(data);
      saveGame(true);
      alert('백업 복구 완료! 페이지를 새로고침하세요.');
      location.reload();
    } catch(err) {
      alert('백업 파일 읽기 실패: ' + err.message);
    }
  };
  reader.readAsText(file);
}

function clearAllData(){
  if(!confirm('정말로 모든 저장 데이터를 삭제하시겠습니까?')) return;
  
  try {
    storage.removeItem(SAVE_KEY);
    storage.removeItem(BACKUP_KEY);
    storage.removeItem(SYNC_KEY);
    storage.removeItem('rift-chat');
    alert('모든 데이터 삭제 완료');
    location.reload();
  } catch(e) {
    alert('삭제 실패: ' + e.message);
  }
}





// IndexedDB 폴백 (큰 데이터 대비)
const useIndexedDB = (() => {
  const dbName = 'RiftShop';
  const storeName = 'saves';
  
  return {
    async save(key, value){
      try {
        const db = await this.getDB();
        const tx = db.transaction(storeName, 'readwrite');
        tx.objectStore(storeName).put({key, value, time: Date.now()});
        await tx.done;
        console.log('IndexedDB 저장됨:', key);
        return true;
      } catch(e) {
        console.log('IndexedDB 저장 실패:', e.message);
        return false;
      }
    },
    
    async load(key){
      try {
        const db = await this.getDB();
        const tx = db.transaction(storeName, 'readonly');
        const result = await tx.objectStore(storeName).get(key);
        return result?.value || null;
      } catch(e) {
        return null;
      }
    },
    
    getDB(){
      return new Promise((resolve, reject)=>{
        const req = indexedDB.open('RiftShop', 1);
        req.onerror = ()=>reject(req.error);
        req.onsuccess = ()=>resolve(req.result);
        req.onupgradeneeded = (e)=>{
          const db = e.target.result;
          if(!db.objectStoreNames.contains(storeName)){
            db.createObjectStore(storeName, {keyPath: 'key'});
          }
        };
      });
    }
  };
})();


// ============================================================================
// ☁️ Firebase 클라우드 동기화 (선택 옵션)
// ============================================================================

let firebaseEnabled = false;
let firebaseUser = null;

function initFirebase(){
  // Firebase 설정 예시 (사용자가 직접 설정 필요)
  // const firebaseConfig = {
  //   apiKey: "YOUR_API_KEY",
  //   authDomain: "your-app.firebaseapp.com",
  //   projectId: "your-project-id",
  //   storageBucket: "your-app.appspot.com",
  //   messagingSenderId: "YOUR_SENDER_ID",
  //   appId: "YOUR_APP_ID"
  // };
  
  // Firebase 미설정 시 로컬 저장만 사용
  console.log('💡 Firebase 미설정. 로컬 저장만 사용합니다.');
  firebaseEnabled = false;
}

async function syncToCloud(){
  if(!firebaseEnabled || !S) return;
  
  try {
    // Firebase Realtime Database에 저장
    // await firebase.database().ref('users/' + firebaseUser.uid + '/save').set(S);
    console.log('☁️ 클라우드 동기화 완료');
  } catch(e) {
    console.log('클라우드 동기화 실패:', e);
  }
}

async function syncFromCloud(){
  if(!firebaseEnabled) return;
  
  try {
    // Firebase에서 로드
    // const snapshot = await firebase.database().ref('users/' + firebaseUser.uid + '/save').get();
    // if(snapshot.exists()) S = snapshot.val();
    console.log('☁️ 클라우드에서 로드 완료');
  } catch(e) {
    console.log('클라우드 로드 실패:', e);
  }
}

// 클라우드 동기화는 수동 호출
function toggleCloudSync(){
  if(!firebaseEnabled){
    alert('Firebase를 설정한 후 사용할 수 있습니다.');
    return;
  }
  // syncToCloud();
}


// null 안전 DOM 접근
function safeSetHTML(id, html){
  const el = document.getElementById(id);
  if(!el) {
    console.log('⚠️ 요소 미발견:', id);
    return false;
  }
  try {
    el.innerHTML = html;
    return true;
  } catch(e) {
    console.error('HTML 설정 실패:', id, e);
    return false;
  }
}

function safeGetElement(id){
  const el = document.getElementById(id);
  if(!el) {
    console.log('⚠️ 요소 미발견:', id);
  }
  return el;
}


// ============================================================================
// 🐛 전역 에러 핸들러 (디버깅용)
// ============================================================================

window.addEventListener('error', (event)=>{
  console.error('🐛 JavaScript 에러:', event.error);
  console.error('파일:', event.filename, '줄:', event.lineno);
});

window.addEventListener('unhandledrejection', (event)=>{
  console.error('🐛 Promise 에러:', event.reason);
});

// 렌더링 함수 보호
const renderFunctions = [
  'renderAll', 'renderStats', 'renderEquip', 'renderArts', 
  'renderShop', 'renderContent', 'renderTalents', 'renderSettings',
  'renderSocial', 'renderPetUI'
];

renderFunctions.forEach(funcName=>{
  const originalFunc = window[funcName];
  if(typeof originalFunc === 'function'){
    window[funcName] = function(...args){
      try {
        return originalFunc.apply(this, args);
      } catch(e) {
        console.error(`❌ ${funcName} 에러:`, e.message);
      }
    };
  }
});

console.log('✅ 에러 핸들러 활성화');
// 실제 게임 초기화는 위쪽의 메인 (async function init(){...})() 에서 한 번만 수행됩니다.



// ============================================================================
// 🎮 고유이름(닉네임) 시스템 — 중복 방지 + "개발자" 이름 보호
// ============================================================================

const usedNicknames = (() => {
  const key = 'rift-used-nicknames';
  return {
    add(nick) {
      try {
        const list = JSON.parse(storage.getItem(key) || '[]');
        if(!list.includes(nick)) {
          list.push(nick);
          storage.setItem(key, JSON.stringify(list));
        }
      } catch(e) {}
    },
    check(nick) {
      try {
        const list = JSON.parse(storage.getItem(key) || '[]');
        return list.includes(nick);
      } catch(e) {
        return false;
      }
    },
    getAll() {
      try {
        return JSON.parse(storage.getItem(key) || '[]');
      } catch(e) {
        return [];
      }
    }
  };
})();

function isAdmin(nick){ return nick === ADMIN_NICK; }
function checkAdminAccess(){ return !!(S && S.nickname === ADMIN_NICK); }

// 고유이름 변경 (누구나 언제든 변경 가능 · "개발자"는 비밀번호를 아는 사람만 사용 가능)
function setNickname(){
  const inp = document.getElementById('nickInput');
  if(!inp || !inp.value.trim()){
    alert('닉네임을 입력하세요');
    return;
  }
  const nick = inp.value.trim();

  if(nick.length < 2 || nick.length > 15){
    alert('닉네임은 2~15글자입니다');
    return;
  }
  if(S.nickname === nick){
    alert('현재 닉네임과 같습니다');
    return;
  }

  // "개발자" 닉네임은 비밀번호를 아는 사람만 사용 가능 (그 외 닉네임과 중복 체크 로직 분리)
  if(nick === ADMIN_NICK){
    const pass = prompt('"' + ADMIN_NICK + '"은(는) 예약된 이름입니다. 관리자 비밀번호를 입력하세요:', '');
    if(pass !== ADMIN_PASSWORD){
      alert('비밀번호가 틀렸습니다. 다른 닉네임을 사용해주세요.');
      return;
    }
  } else if(usedNicknames.check(nick)){
    // 일반 닉네임은 중복 체크
    alert('이미 사용 중인 닉네임입니다!');
    inp.focus();
    return;
  }

  // 이전 닉네임 정리 (랭킹에서도 이전 이름 제거)
  const oldNick = S.nickname;
  if(oldNick){
    usedNicknames.add(oldNick);
    rankingSystem.remove(oldNick);
  }

  S.nickname = nick;
  saveGame(true);

  alert(nick + ' 닉네임으로 설정되었습니다!' + (nick===ADMIN_NICK ? ' 👑' : ''));
  initIdentity();
  updateRanking();
  renderAll();
}

// Enter 키로도 닉네임 변경 가능
document.addEventListener('DOMContentLoaded', ()=>{
  const nickInput = document.getElementById('nickInput');
  if(nickInput){
    nickInput.addEventListener('keypress', (e)=>{
      if(e.key === 'Enter') setNickname();
    });
  }
});

// 보스 전 제한 시간 (스테이지에 따라 증가)
function getBossTimeLimit(){
  const stage = S.stage || 1;
  return 30 + Math.floor((stage-1) / 10);  // 10스테이지마다 +1초
}

// ============================================================================
// 🏆 전투력 & 랭킹 시스템
// ============================================================================

const RANKING_KEY = 'rift-rankings';
const MAX_RANKINGS = 100;

const rankingSystem = (() => {
  return {
    add(nickname, power, stage, level) {
      try {
        const rankings = JSON.parse(storage.getItem(RANKING_KEY) || '[]');
        const idx = rankings.findIndex(r => r.nick === nickname);
        if(idx >= 0){
          rankings[idx] = {nick: nickname, power, stage, level, time: Date.now()};
        } else {
          rankings.push({nick: nickname, power, stage, level, time: Date.now()});
        }
        rankings.sort((a, b) => b.power - a.power);
        rankings.splice(MAX_RANKINGS);
        storage.setItem(RANKING_KEY, JSON.stringify(rankings));
        return true;
      } catch(e) {
        console.error('랭킹 저장 실패:', e);
        return false;
      }
    },
    remove(nickname) {
      try {
        const rankings = JSON.parse(storage.getItem(RANKING_KEY) || '[]');
        const filtered = rankings.filter(r => r.nick !== nickname);
        storage.setItem(RANKING_KEY, JSON.stringify(filtered));
      } catch(e) {}
    },
    getAll() {
      try {
        return JSON.parse(storage.getItem(RANKING_KEY) || '[]');
      } catch(e) {
        return [];
      }
    },
    getRank(nickname) {
      const rankings = this.getAll();
      const rank = rankings.findIndex(r => r.nick === nickname) + 1;
      return rank > 0 ? rank : '미기록';
    }
  };
})();

// 전투력 계산
function calcPower(){
  return Math.round(playerATK()*3 + playerDEF()*2 + playerMaxHP()*0.5 + (S.level||1)*10);
}
function getPowerColor(power){
  if(power >= 100000) return '#ff5470';
  if(power >= 30000)  return '#ffd23f';
  if(power >= 10000)  return '#a06bff';
  if(power >= 3000)   return '#43e6cf';
  return '#eae6ff';
}

// 매 저장 시 랭킹 업데이트
function updateRanking(){
  if(!S || !S.nickname) return;
  rankingSystem.add(S.nickname, calcPower(), S.stage, S.level);
}

// 전투력 / 순위 표시 업데이트
function updatePowerDisplay(){
  const power = calcPower();
  const powerEl = document.getElementById('powerDisplay');
  const rankEl = document.getElementById('rankDisplay');

  if(powerEl){
    powerEl.innerHTML = power.toLocaleString();
    powerEl.style.color = getPowerColor(power);
  }
  if(rankEl && S && S.nickname){
    const rank = rankingSystem.getRank(S.nickname);
    rankEl.innerHTML = '랭킹: ' + rank + ' / ' + rankingSystem.getAll().length;
  }
}

// 랭킹 팝업 표시



// ============================================================================
// 🤖 자동 판매/분해 시스템
// ============================================================================
let autoSellSettings = { enabled: false, sellNormal: true, sellRare: true, dismantleRare: true };
function saveAutoSellSettings(){ storage.setItem('rift-autosell', JSON.stringify(autoSellSettings)); }
function loadAutoSellSettings(){ try { const s = storage.getItem('rift-autosell'); if(s) autoSellSettings = JSON.parse(s); } catch(e){} }

// ============================================================================
// ⚡ 피버 모드 + 액티브 스킬
// ============================================================================
let skillCooldowns = { shatter: 0, heal: 0 };
const SKILLS = { shatter: { name: '균열의 일격', cooldown: 30 }, heal: { name: '치유의 성수', cooldown: 45 } };



function activateSkill(skillName){
  if(skillName !== 'heal') return;
  
  if(Date.now() < skillCooldowns.heal) {
    const remaining = Math.ceil((skillCooldowns.heal - Date.now()) / 1000);
    if(typeof log === 'function') {
      log('<span class="c">⏳ 치유의 성수 - ' + remaining + '초 후 사용 가능</span>');
    }
    return;
  }
  
  const oldHp = S.hp || 0;
  const heal = Math.floor((S.maxHp || 100) * 0.5);
  S.hp = Math.min(S.maxHp || 100, oldHp + heal);
  if(typeof log === 'function') {
    log('<span class="green">💚 치유의 성수! ' + heal + ' 회복!</span>');
  }
  skillCooldowns.heal = Date.now() + 45000;
  updateSkillUI();
}



function combinePets(petId){
  const p = PETS.find(x=>x.id===petId);
  if(!p || !S.pets[petId]) return;
  if(!S.shards || S.shards < 10) { alert('조각 10개 필요'); return; }
  S.shards -= 10;
  if(!S.petStars) S.petStars = {};
  S.petStars[petId] = (S.petStars[petId]||0) + 1;
  if(typeof log === 'function') log('<span class="gold">✨ ' + p.name + ' 진화!</span>');
  saveGame(true);
  renderPetUI();
}

// ============================================================================
// 🎰 미니게임 (룰렛 + 포커)
// ============================================================================
function openRoulette(){
  if(!confirm('룰렛? (조각 1개)')) return;
  if(!S.shards || S.shards < 1) { alert('조각 부족'); return; }
  S.shards -= 1;
  const rewards = ['💰 500G', '✨ 조각 2', '💎 강화석 3'];
  const idx = Math.floor(Math.random() * rewards.length);
  alert('🎰 ' + rewards[idx]);
  if(idx === 0) S.gold += 500;
  else if(idx === 1) S.shards += 2;
  else if(idx === 2) S.stones += 3;
  renderAll();
}



function updateSkillUI(){
  const skillDiv = document.getElementById('skillButtons');
  if(!skillDiv) return;
  
  const cd = Math.max(0, Math.ceil((skillCooldowns.heal - Date.now())/1000));
  
  skillDiv.innerHTML = `
    <button onclick="activateSkill('heal')" style="padding:12px;background:${cd>0?'var(--panel2)':'var(--rift)'};opacity:${cd>0?'0.5':'1'};color:white;border:2px solid var(--line);border-radius:4px;cursor:pointer;font-weight:bold;width:100%;">
      💚 치유의 성수${cd>0?' ('+cd+'초)':''}
    </button>
  `;
}


setInterval(updateSkillUI, 500);


function updateAutoSellUI(){
  const div = document.getElementById('autoSellSection');
  if(!div) return;
  
  div.innerHTML = `
    <div style="margin:15px 0; border:2px solid var(--rift); padding:10px; border-radius:4px;">
      <div style="color:var(--cyan); margin-bottom:8px; font-weight:bold;">🤖 자동 판매/분해</div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:12px;">
        <label style="display:flex; gap:6px;"><input type="checkbox" ${autoSellSettings.enabled?'checked':''} onchange="autoSellSettings.enabled=this.checked;saveAutoSellSettings();"><span>활성화</span></label>
        <label style="display:flex; gap:6px;"><input type="checkbox" ${autoSellSettings.sellNormal?'checked':''} onchange="autoSellSettings.sellNormal=this.checked;saveAutoSellSettings();"><span>일반판매</span></label>
        <label style="display:flex; gap:6px;"><input type="checkbox" ${autoSellSettings.sellRare?'checked':''} onchange="autoSellSettings.sellRare=this.checked;saveAutoSellSettings();"><span>희귀판매</span></label>
        <label style="display:flex; gap:6px;"><input type="checkbox" ${autoSellSettings.dismantleRare?'checked':''} onchange="autoSellSettings.dismantleRare=this.checked;saveAutoSellSettings();"><span>희귀분해</span></label>
      </div>
    </div>
  `;
}



function updateLanguageUI(){
  const btnKo = document.getElementById('btnKo');
  const btnEn = document.getElementById('btnEn');
  if(btnKo) btnKo.style.background = currentLanguage==='ko' ? 'var(--gold)' : '';
  if(btnEn) btnEn.style.background = currentLanguage==='en' ? 'var(--gold)' : '';
}


// 페이지 이탈/숨김 시 즉시 저장 (새로고침·탭 닫기 대비)
window.addEventListener('beforeunload', () => {
  try { if(typeof S !== 'undefined' && S) saveGame(true); } catch(e) {}
});
document.addEventListener('visibilitychange', () => {
  if(document.hidden){
    try { if(typeof S !== 'undefined' && S) saveGame(true); } catch(e) {}
  }
});

// 인라인 onclick/onkeydown에서 확실히 호출되도록 전역 노출
window.runDevCommand   = runDevCommand;
window.devGiveGear     = devGiveGear;
window.devSkipStage    = devSkipStage;
window.devGotoStage    = devGotoStage;
window.devLevelUp      = devLevelUp;
window.devMaxStats     = devMaxStats;
window.devGiveGold     = devGiveGold;
window.devGiveAllPets  = devGiveAllPets;

function toggleBGM(){
  if(!S.settings) S.settings = {};
  S.settings.bgm = !S.settings.bgm;
  BGM.toggle(S.settings.bgm);
  sfx('ui');
  log('<span class="c">🎵 배경음 ' + (S.settings.bgm ? '켜짐' : '꺼짐') + '</span>');
  saveGame(true);
}
window.toggleBGM = toggleBGM;
window.showSkinGUI = showSkinGUI;
window.gachaSkin = gachaSkin;
window.equipSkin = equipSkin;
window.showRankings = showRankings;
window.showOnlineGUI = showOnlineGUI;
window.showGuildGUI = showGuildGUI;
window.showMailGUI = showMailGUI;
window.showBossGUI = showBossGUI;
window.showMarketGUI = showMarketGUI;
window.closeGUI = closeGUI;
window.Audio8 = Audio8;
window.BGM = BGM;
</script>

<!-- 난이도 선택 모달 -->

<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/v4513226cdae34746b4dedf0b4dfa099e1781791509496" integrity="sha512-ZE9pZaUXND66v380QUtch/5sE9tPFh2zg45pR2PB0CVkCtOREv2AJKkSidISWkysEuQ0EH8faUU5du78bx87UQ==" data-cf-beacon='{"version":"2024.11.0","token":"4edd5f8ec12a48cfa682ab8261b80a79","server_timing":{"name":{"cfCacheStatus":true,"cfEdge":true,"cfExtPri":true,"cfL4":true,"cfOrigin":true,"cfSpeedBrain":true},"location_startswith":null}}' crossorigin="anonymous"></script>
</body>
</html>

<!-- Auto-save on page leave -->

