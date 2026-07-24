# -*- coding: utf-8 -*-
"""
🌐 차원 균열의 만물상 — 온라인 서버
표준 라이브러리만 사용 (설치 불필요)

실행: python server.py
기본 포트: 8777

기능: 채팅 / 랭킹 / 길드 / 접속자 / 월드보스 / 거래소 / 우편
"""
import json, os, sys, time, threading, sqlite3, hashlib
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from socketserver import ThreadingMixIn

# 한국어 Windows(cp949) 콘솔에서 이모지 출력 시 크래시 방지
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='ignore')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='ignore')
except Exception:
    pass


def _p(*args):
    try:
        print(*args)
    except Exception:
        try:
            enc = getattr(sys.stdout, 'encoding', None) or 'utf-8'
            sys.stdout.write(' '.join(str(a) for a in args).encode(enc, 'ignore').decode(enc, 'ignore') + '\n')
        except Exception:
            pass


PORT = int(os.environ.get('RIFT_PORT', 8777))
HOST = os.environ.get('RIFT_HOST', '0.0.0.0')
DB_PATH = os.environ.get('RIFT_DB') or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'rift_server.db')
_lock = threading.Lock()

# ---- 요청 속도 제한 (도배/스팸 방지) ----
RATE_LIMIT = int(os.environ.get('RIFT_RATE', 30))   # IP당 10초에 허용 요청 수
_rate = {}
_rate_lock = threading.Lock()

def rate_ok(ip):
    if RATE_LIMIT <= 0:
        return True
    now_t = time.time()
    with _rate_lock:
        q = _rate.setdefault(ip, [])
        while q and now_t - q[0] > 10:
            q.pop(0)
        if len(q) >= RATE_LIMIT:
            return False
        q.append(now_t)
        if len(_rate) > 5000:
            for k in [k for k, v in _rate.items() if not v or now_t - v[-1] > 60]:
                _rate.pop(k, None)
        return True


def db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS chat(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room TEXT NOT NULL DEFAULT 'global',
            nick TEXT NOT NULL, msg TEXT NOT NULL, ts INTEGER NOT NULL);
        CREATE INDEX IF NOT EXISTS idx_chat ON chat(room, id);

        CREATE TABLE IF NOT EXISTS ranking(
            nick TEXT PRIMARY KEY, power REAL DEFAULT 0, stage INTEGER DEFAULT 1,
            level INTEGER DEFAULT 1, tier TEXT DEFAULT '', ts INTEGER NOT NULL);

        CREATE TABLE IF NOT EXISTS players(
            nick TEXT PRIMARY KEY, last_seen INTEGER NOT NULL,
            stage INTEGER DEFAULT 1, level INTEGER DEFAULT 1, guild TEXT DEFAULT '');

        CREATE TABLE IF NOT EXISTS guilds(
            name TEXT PRIMARY KEY, owner TEXT NOT NULL, notice TEXT DEFAULT '',
            score REAL DEFAULT 0, ts INTEGER NOT NULL);

        CREATE TABLE IF NOT EXISTS guild_members(
            guild TEXT NOT NULL, nick TEXT NOT NULL, ts INTEGER NOT NULL,
            PRIMARY KEY(guild, nick));

        CREATE TABLE IF NOT EXISTS worldboss(
            id INTEGER PRIMARY KEY CHECK(id=1), name TEXT, hp REAL, max_hp REAL,
            season INTEGER DEFAULT 1, ts INTEGER);

        CREATE TABLE IF NOT EXISTS boss_damage(
            season INTEGER NOT NULL, nick TEXT NOT NULL, dmg REAL DEFAULT 0,
            PRIMARY KEY(season, nick));

        CREATE TABLE IF NOT EXISTS market(
            id INTEGER PRIMARY KEY AUTOINCREMENT, seller TEXT NOT NULL,
            item TEXT NOT NULL, grade TEXT, price INTEGER NOT NULL,
            sold INTEGER DEFAULT 0, buyer TEXT DEFAULT '', ts INTEGER NOT NULL);

        -- 경매 시스템
        CREATE TABLE IF NOT EXISTS auction(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seller TEXT NOT NULL,
            item TEXT NOT NULL,
            grade TEXT DEFAULT '',
            item_json TEXT DEFAULT '',      -- 장비 원본(구매자에게 그대로 전달)
            start_price INTEGER NOT NULL,   -- 시작가
            buyout INTEGER DEFAULT 0,       -- 즉시구매가 (0이면 없음)
            cur_bid INTEGER DEFAULT 0,      -- 현재 최고 입찰가
            cur_bidder TEXT DEFAULT '',     -- 현재 최고 입찰자
            is_private INTEGER DEFAULT 0,   -- 1이면 비공개(코드 필요)
            code TEXT DEFAULT '',           -- 비공개 입장 코드
            end_ts INTEGER NOT NULL,        -- 종료 시각
            closed INTEGER DEFAULT 0,       -- 1이면 정산 완료
            ts INTEGER NOT NULL);
        CREATE INDEX IF NOT EXISTS idx_auc ON auction(closed, end_ts);

        CREATE TABLE IF NOT EXISTS auction_bids(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            auc_id INTEGER NOT NULL, nick TEXT NOT NULL,
            amount INTEGER NOT NULL, ts INTEGER NOT NULL);

        CREATE TABLE IF NOT EXISTS mail(
            id INTEGER PRIMARY KEY AUTOINCREMENT, receiver TEXT NOT NULL,
            sender TEXT NOT NULL, subject TEXT, body TEXT,
            gold INTEGER DEFAULT 0, item_json TEXT DEFAULT '',
            taken INTEGER DEFAULT 0, ts INTEGER NOT NULL);
        CREATE INDEX IF NOT EXISTS idx_mail ON mail(receiver, taken);
        ''')
        # 기존 DB 호환: 없는 컬럼 자동 추가
        for tbl, col, decl in [('mail', 'item_json', "TEXT DEFAULT ''")]:
            cols = [r[1] for r in c.execute('PRAGMA table_info(%s)' % tbl).fetchall()]
            if col not in cols:
                c.execute('ALTER TABLE %s ADD COLUMN %s %s' % (tbl, col, decl))

        row = c.execute('SELECT 1 FROM worldboss WHERE id=1').fetchone()
        if not row:
            c.execute('INSERT INTO worldboss(id,name,hp,max_hp,season,ts) VALUES(1,?,?,?,1,?)',
                      ('차원의 포식자', 1e12, 1e12, int(time.time())))


def now(): return int(time.time())



def close_auction(c, aid):
    """경매 1건 낙찰 처리: 판매자에겐 골드, 낙찰자에겐 아이템을 우편 발송"""
    row = c.execute('SELECT * FROM auction WHERE id=? AND closed=0', (aid,)).fetchone()
    if not row:
        return False
    c.execute('UPDATE auction SET closed=1 WHERE id=?', (aid,))
    if row['cur_bidder'] and row['cur_bid'] > 0:
        # 낙찰자 → 아이템
        c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,item_json,ts) '
                  'VALUES(?,?,?,?,0,?,?)',
                  (row['cur_bidder'], '경매장', '낙찰 상품',
                   '%s 낙찰 (%d G)' % (row['item'], row['cur_bid']),
                   row['item_json'] or '', now()))
        # 판매자 → 골드 (수수료 5%)
        fee = int(row['cur_bid'] * 0.05)
        c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,ts) '
                  'VALUES(?,?,?,?,?,?)',
                  (row['seller'], '경매장', '판매 대금',
                   '%s 낙찰 (수수료 5%%: %d G)' % (row['item'], fee),
                   row['cur_bid'] - fee, now()))
    else:
        # 유찰 → 판매자에게 반환
        c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,item_json,ts) '
                  'VALUES(?,?,?,?,0,?,?)',
                  (row['seller'], '경매장', '유찰 반환',
                   '%s 입찰자가 없어 반환됩니다.' % row['item'],
                   row['item_json'] or '', now()))
    return True


def settle_auctions(c):
    """종료 시각이 지난 경매를 일괄 정산"""
    rows = c.execute('SELECT id FROM auction WHERE closed=0 AND end_ts<=?',
                     (now(),)).fetchall()
    for r in rows:
        close_auction(c, r['id'])
    return len(rows)


# ============================== API ==============================
def api(path, q, body):
    # GET 쿼리와 POST 본문을 통합 (한글 파라미터는 POST 본문 권장)
    def P(key, default=''):
        if key in body and body[key] is not None:
            return body[key]
        v = q.get(key)
        return v[0] if v else default

    with _lock, db() as c:
        # ---------- 1. 채팅 ----------
        if path == '/chat/send':
            nick = (body.get('nick') or '익명')[:20]
            msg = (body.get('msg') or '')[:200]
            room = (body.get('room') or 'global')[:40]
            if not msg.strip():
                return {'ok': False, 'error': 'empty'}
            c.execute('INSERT INTO chat(room,nick,msg,ts) VALUES(?,?,?,?)',
                      (room, nick, msg, now()))
            c.execute('DELETE FROM chat WHERE room=? AND id NOT IN '
                      '(SELECT id FROM chat WHERE room=? ORDER BY id DESC LIMIT 200)', (room, room))
            return {'ok': True}

        if path == '/chat/list':
            room = str(P('room', 'global'))[:40]
            since = int(P('since', 0) or 0)
            rows = c.execute('SELECT id,nick,msg,ts FROM chat WHERE room=? AND id>? '
                             'ORDER BY id DESC LIMIT 60', (room, since)).fetchall()
            return {'ok': True, 'messages': [dict(r) for r in reversed(rows)]}

        # ---------- 2. 랭킹 ----------
        if path == '/rank/submit':
            nick = (body.get('nick') or '익명')[:20]
            c.execute('INSERT INTO ranking(nick,power,stage,level,tier,ts) VALUES(?,?,?,?,?,?) '
                      'ON CONFLICT(nick) DO UPDATE SET power=excluded.power, stage=excluded.stage,'
                      'level=excluded.level, tier=excluded.tier, ts=excluded.ts',
                      (nick, float(body.get('power') or 0), int(body.get('stage') or 1),
                       int(body.get('level') or 1), (body.get('tier') or '')[:20], now()))
            c.execute('INSERT INTO players(nick,last_seen,stage,level,guild) VALUES(?,?,?,?,?) '
                      'ON CONFLICT(nick) DO UPDATE SET last_seen=excluded.last_seen,'
                      'stage=excluded.stage, level=excluded.level, guild=excluded.guild',
                      (nick, now(), int(body.get('stage') or 1), int(body.get('level') or 1),
                       (body.get('guild') or '')[:30]))
            return {'ok': True}

        if path == '/rank/list':
            rows = c.execute('SELECT nick,power,stage,level,tier FROM ranking '
                             'ORDER BY power DESC LIMIT 100').fetchall()
            return {'ok': True, 'rankings': [dict(r) for r in rows]}

        # ---------- 3. 접속자 ----------
        if path == '/online':
            cut = now() - 90
            rows = c.execute('SELECT nick,stage,level,guild FROM players WHERE last_seen>? '
                             'ORDER BY stage DESC LIMIT 50', (cut,)).fetchall()
            cnt = c.execute('SELECT COUNT(*) n FROM players WHERE last_seen>?', (cut,)).fetchone()['n']
            return {'ok': True, 'count': cnt, 'players': [dict(r) for r in rows]}

        # ---------- 4. 길드 ----------
        if path == '/guild/create':
            name = (body.get('name') or '').strip()[:30]
            owner = (body.get('nick') or '')[:20]
            if not name: return {'ok': False, 'error': 'no_name'}
            if c.execute('SELECT 1 FROM guilds WHERE name=?', (name,)).fetchone():
                return {'ok': False, 'error': 'exists'}
            c.execute('INSERT INTO guilds(name,owner,ts) VALUES(?,?,?)', (name, owner, now()))
            c.execute('INSERT OR REPLACE INTO guild_members(guild,nick,ts) VALUES(?,?,?)',
                      (name, owner, now()))
            return {'ok': True}

        if path == '/guild/join':
            name = (body.get('name') or '')[:30]
            nick = (body.get('nick') or '')[:20]
            if not c.execute('SELECT 1 FROM guilds WHERE name=?', (name,)).fetchone():
                return {'ok': False, 'error': 'not_found'}
            c.execute('DELETE FROM guild_members WHERE nick=?', (nick,))
            c.execute('INSERT OR REPLACE INTO guild_members(guild,nick,ts) VALUES(?,?,?)',
                      (name, nick, now()))
            return {'ok': True}

        if path == '/guild/list':
            rows = c.execute(
                'SELECT g.name,g.owner,g.notice,'
                '(SELECT COUNT(*) FROM guild_members m WHERE m.guild=g.name) members,'
                '(SELECT IFNULL(SUM(r.power),0) FROM guild_members m JOIN ranking r ON r.nick=m.nick '
                ' WHERE m.guild=g.name) score '
                'FROM guilds g ORDER BY score DESC LIMIT 50').fetchall()
            return {'ok': True, 'guilds': [dict(r) for r in rows]}

        # ---------- 5. 월드보스 ----------
        if path == '/boss/state':
            b = dict(c.execute('SELECT * FROM worldboss WHERE id=1').fetchone())
            top = c.execute('SELECT nick,dmg FROM boss_damage WHERE season=? '
                            'ORDER BY dmg DESC LIMIT 10', (b['season'],)).fetchall()
            return {'ok': True, 'boss': b, 'top': [dict(r) for r in top]}

        if path == '/boss/hit':
            nick = (body.get('nick') or '익명')[:20]
            dmg = max(0.0, float(body.get('dmg') or 0))
            b = c.execute('SELECT * FROM worldboss WHERE id=1').fetchone()
            hp = max(0.0, b['hp'] - dmg)
            season = b['season']
            c.execute('INSERT INTO boss_damage(season,nick,dmg) VALUES(?,?,?) '
                      'ON CONFLICT(season,nick) DO UPDATE SET dmg=dmg+?',
                      (season, nick, dmg, dmg))
            killed = False
            if hp <= 0:
                killed = True
                season += 1
                new_hp = b['max_hp'] * 2.5
                c.execute('UPDATE worldboss SET hp=?,max_hp=?,season=?,ts=? WHERE id=1',
                          (new_hp, new_hp, season, now()))
                # 처치 보상 우편
                for r in c.execute('SELECT nick,dmg FROM boss_damage WHERE season=? '
                                   'ORDER BY dmg DESC LIMIT 20', (b['season'],)).fetchall():
                    c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,ts) '
                              'VALUES(?,?,?,?,?,?)',
                              (r['nick'], '월드보스', '토벌 보상',
                               f"{b['name']} 처치 기여 보상", int(1e7), now()))
            else:
                c.execute('UPDATE worldboss SET hp=?,ts=? WHERE id=1', (hp, now()))
            return {'ok': True, 'hp': hp, 'killed': killed, 'season': season}

        # ---------- 6. 거래소 ----------
        if path == '/market/sell':
            c.execute('INSERT INTO market(seller,item,grade,price,ts) VALUES(?,?,?,?,?)',
                      ((body.get('nick') or '')[:20], (body.get('item') or '')[:40],
                       (body.get('grade') or '')[:20], int(body.get('price') or 0), now()))
            return {'ok': True}

        if path == '/market/list':
            rows = c.execute('SELECT id,seller,item,grade,price FROM market '
                             'WHERE sold=0 ORDER BY id DESC LIMIT 50').fetchall()
            return {'ok': True, 'items': [dict(r) for r in rows]}

        if path == '/market/buy':
            iid = int(body.get('id') or 0)
            buyer = (body.get('nick') or '')[:20]
            row = c.execute('SELECT * FROM market WHERE id=? AND sold=0', (iid,)).fetchone()
            if not row: return {'ok': False, 'error': 'sold_out'}
            c.execute('UPDATE market SET sold=1, buyer=? WHERE id=?', (buyer, iid))
            c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,ts) VALUES(?,?,?,?,?,?)',
                      (row['seller'], '거래소', '판매 완료',
                       f"{row['item']} 판매 대금", row['price'], now()))
            return {'ok': True, 'item': dict(row)}

        # ---------- 7. 우편 ----------
        if path == '/mail/list':
            nick = str(P('nick', ''))[:20]
            rows = c.execute('SELECT id,sender,subject,body,gold,item_json FROM mail '
                             'WHERE receiver=? AND taken=0 ORDER BY id DESC LIMIT 30',
                             (nick,)).fetchall()
            return {'ok': True, 'mails': [dict(r) for r in rows]}

        if path == '/mail/take':
            mid = int(body.get('id') or 0)
            nick = (body.get('nick') or '')[:20]
            row = c.execute('SELECT * FROM mail WHERE id=? AND receiver=? AND taken=0',
                            (mid, nick)).fetchone()
            if not row: return {'ok': False, 'error': 'not_found'}
            c.execute('UPDATE mail SET taken=1 WHERE id=?', (mid,))
            return {'ok': True, 'gold': row['gold'], 'item_json': row['item_json'] or ''}

        if path == '/mail/send':
            c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,ts) VALUES(?,?,?,?,?,?)',
                      ((body.get('to') or '')[:20], (body.get('nick') or '')[:20],
                       (body.get('subject') or '쪽지')[:40], (body.get('body') or '')[:200],
                       int(body.get('gold') or 0), now()))
            return {'ok': True}


        # ---------- 8. 경매 ----------
        if path == '/auction/create':
            seller = str(P('nick', ''))[:20]
            item = str(P('item', ''))[:40]
            if not seller or not item:
                return {'ok': False, 'error': 'bad_request'}
            start_price = max(1, int(P('start_price', 1) or 1))
            buyout = max(0, int(P('buyout', 0) or 0))
            if buyout and buyout < start_price:
                return {'ok': False, 'error': 'buyout_too_low'}
            is_private = 1 if P('is_private', 0) in (1, '1', True, 'true') else 0
            code = str(P('code', ''))[:20]
            if is_private and not code:
                return {'ok': False, 'error': 'code_required'}
            minutes = max(1, min(1440, int(P('minutes', 30) or 30)))
            c.execute(
                'INSERT INTO auction(seller,item,grade,item_json,start_price,buyout,'
                'cur_bid,cur_bidder,is_private,code,end_ts,ts) '
                'VALUES(?,?,?,?,?,?,0,"",?,?,?,?)',
                (seller, item, str(P('grade', ''))[:20], str(P('item_json', ''))[:2000],
                 start_price, buyout, is_private, code, now() + minutes * 60, now()))
            return {'ok': True, 'id': c.execute('SELECT last_insert_rowid() i').fetchone()['i']}

        if path == '/auction/list':
            settle_auctions(c)
            code = str(P('code', ''))[:20]
            if code:
                # 비공개 방: 코드가 일치하는 경매만
                rows = c.execute(
                    'SELECT id,seller,item,grade,start_price,buyout,cur_bid,cur_bidder,'
                    'is_private,end_ts FROM auction '
                    'WHERE closed=0 AND is_private=1 AND code=? ORDER BY end_ts ASC LIMIT 50',
                    (code,)).fetchall()
                return {'ok': True, 'items': [dict(r) for r in rows], 'private': True}
            rows = c.execute(
                'SELECT id,seller,item,grade,start_price,buyout,cur_bid,cur_bidder,'
                'is_private,end_ts FROM auction '
                'WHERE closed=0 AND is_private=0 ORDER BY end_ts ASC LIMIT 50').fetchall()
            return {'ok': True, 'items': [dict(r) for r in rows], 'private': False,
                    'now': now()}

        if path == '/auction/bid':
            settle_auctions(c)
            aid = int(P('id', 0) or 0)
            nick = str(P('nick', ''))[:20]
            amount = int(P('amount', 0) or 0)
            row = c.execute('SELECT * FROM auction WHERE id=? AND closed=0', (aid,)).fetchone()
            if not row:
                return {'ok': False, 'error': 'not_found'}
            if row['end_ts'] <= now():
                return {'ok': False, 'error': 'ended'}
            if row['seller'] == nick:
                return {'ok': False, 'error': 'own_auction'}
            if row['is_private'] and str(P('code', '')) != row['code']:
                return {'ok': False, 'error': 'bad_code'}
            floor = max(row['cur_bid'], row['start_price'] - 1)
            if amount <= floor:
                return {'ok': False, 'error': 'low_bid', 'min': floor + 1}
            # 이전 입찰자에게 환불 우편
            if row['cur_bidder'] and row['cur_bid'] > 0:
                c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,ts) '
                          'VALUES(?,?,?,?,?,?)',
                          (row['cur_bidder'], '경매장', '입찰 환불',
                           row['item'] + ' 경매에서 상위 입찰이 발생했습니다.',
                           row['cur_bid'], now()))
            c.execute('UPDATE auction SET cur_bid=?, cur_bidder=? WHERE id=?',
                      (amount, nick, aid))
            c.execute('INSERT INTO auction_bids(auc_id,nick,amount,ts) VALUES(?,?,?,?)',
                      (aid, nick, amount, now()))
            # 즉시구매가 도달 시 즉시 낙찰
            if row['buyout'] and amount >= row['buyout']:
                close_auction(c, aid)
                return {'ok': True, 'won': True, 'amount': amount}
            return {'ok': True, 'won': False, 'amount': amount}

        if path == '/auction/buyout':
            settle_auctions(c)
            aid = int(P('id', 0) or 0)
            nick = str(P('nick', ''))[:20]
            row = c.execute('SELECT * FROM auction WHERE id=? AND closed=0', (aid,)).fetchone()
            if not row:
                return {'ok': False, 'error': 'not_found'}
            if not row['buyout']:
                return {'ok': False, 'error': 'no_buyout'}
            if row['seller'] == nick:
                return {'ok': False, 'error': 'own_auction'}
            if row['is_private'] and str(P('code', '')) != row['code']:
                return {'ok': False, 'error': 'bad_code'}
            if row['cur_bidder'] and row['cur_bid'] > 0:
                c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,ts) '
                          'VALUES(?,?,?,?,?,?)',
                          (row['cur_bidder'], '경매장', '입찰 환불',
                           row['item'] + ' 즉시구매로 종료되었습니다.', row['cur_bid'], now()))
            c.execute('UPDATE auction SET cur_bid=?, cur_bidder=? WHERE id=?',
                      (row['buyout'], nick, aid))
            close_auction(c, aid)
            return {'ok': True, 'amount': row['buyout']}

        if path == '/auction/mine':
            settle_auctions(c)
            nick = str(P('nick', ''))[:20]
            rows = c.execute(
                'SELECT id,item,grade,start_price,buyout,cur_bid,cur_bidder,is_private,'
                'code,end_ts,closed FROM auction WHERE seller=? ORDER BY id DESC LIMIT 30',
                (nick,)).fetchall()
            return {'ok': True, 'items': [dict(r) for r in rows], 'now': now()}

        if path == '/auction/cancel':
            aid = int(P('id', 0) or 0)
            nick = str(P('nick', ''))[:20]
            row = c.execute('SELECT * FROM auction WHERE id=? AND closed=0', (aid,)).fetchone()
            if not row:
                return {'ok': False, 'error': 'not_found'}
            if row['seller'] != nick:
                return {'ok': False, 'error': 'not_owner'}
            if row['cur_bidder']:
                return {'ok': False, 'error': 'has_bid'}   # 입찰이 있으면 취소 불가
            c.execute('UPDATE auction SET closed=1 WHERE id=?', (aid,))
            c.execute('INSERT INTO mail(receiver,sender,subject,body,gold,item_json,ts) '
                      'VALUES(?,?,?,?,0,?,?)',
                      (nick, '경매장', '경매 취소', row['item'] + ' 반환',
                       row['item_json'] or '', now()))
            return {'ok': True}

        if path == '/ping':
            return {'ok': True, 'server': 'rift', 'time': now()}

    return {'ok': False, 'error': 'unknown_endpoint'}


class Handler(BaseHTTPRequestHandler):
    def _send(self, obj, code=200):
        data = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        self.end_headers()

    def do_GET(self):
        u = urlparse(self.path)
        if not rate_ok(self.client_address[0]):
            return self._send({'ok': False, 'error': 'rate_limited'}, 429)
        try:
            self._send(api(u.path, parse_qs(u.query), {}))
        except Exception as e:
            self._send({'ok': False, 'error': str(e)}, 500)

    def do_POST(self):
        u = urlparse(self.path)
        if not rate_ok(self.client_address[0]):
            return self._send({'ok': False, 'error': 'rate_limited'}, 429)
        try:
            n = int(self.headers.get('Content-Length') or 0)
            body = json.loads(self.rfile.read(n) or b'{}') if n else {}
        except Exception:
            body = {}
        try:
            self._send(api(u.path, parse_qs(u.query), body))
        except Exception as e:
            self._send({'ok': False, 'error': str(e)}, 500)

    def log_message(self, *a):
        pass  # 콘솔 조용히


class ThreadedHTTP(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def start_background():
    """게임 런처에서 서버를 백그라운드로 띄울 때 사용"""
    init_db()
    srv = ThreadedHTTP((HOST, PORT), Handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    return srv


if __name__ == '__main__':
    init_db()
    _p('=' * 52)
    _p('[SERVER] 차원 균열의 만물상 - 온라인 서버')
    _p(f'   바인딩 : {HOST}:{PORT}')
    _p(f'   DB     : {DB_PATH}')
    _p(f'   속도제한: IP당 10초 {RATE_LIMIT}회')
    try:
        import socket as _sk
        s = _sk.socket(_sk.AF_INET, _sk.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        _p(f'   내부 IP : http://{s.getsockname()[0]}:{PORT}')
        s.close()
    except Exception:
        pass
    _p('   같은 PC : http://127.0.0.1:%d' % PORT)
    _p('=' * 52)
    _p('종료하려면 Ctrl+C')
    try:
        ThreadedHTTP((HOST, PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        _p('\n서버를 종료합니다.')
