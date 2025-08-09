#!/usr/bin/env python3
import subprocess, threading, queue, time, re, json, os
from flask import Flask, Response, request, send_from_directory

app = Flask(__name__)
q = queue.Queue()

ORDER = [
    "test_users_7.py",
    "test_valid_login_8.py",
    "test_generate_uuid_9.py",
    "test_auth_create_session_10.py",
    "test_app_login_11.py",
    "test_auth_get_user_from_session_id_12.py",
    "test_auth_destroy_session_13.py",
    "test_app_logout_14.py",
    "test_app_profile_15.py",
    "test_auth_reset_token_16.py",
    "test_app_reset_password_token_17.py",
    "test_auth_update_password_18.py",
    "test_app_update_password_19.py",
]

def sse(event, data):
    # small helper to format SSE frames
    if isinstance(data, str):
        payload = data
    else:
        payload = json.dumps(data)
    return f"event: {event}\ndata: {payload}\n\n"

def collect_total():
    # still fine to use --collect-only
    p = subprocess.run(["pytest", "--collect-only", "-q"] + ORDER,
                       capture_output=True, text=True, check=False,
                       env=dict(os.environ, PYTHONUNBUFFERED="1"))
    return sum(1 for line in p.stdout.splitlines() if "::" in line)

def run_pytest():
    total = collect_total()
    q.put(("init", {"total": total}))

    cmd = ["pytest", "-vv", "-s", "--color=no"] + ORDER
    env = dict(os.environ, PYTHONUNBUFFERED="1")

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env
    )

    done = passed = failed = skipped = 0
    last_nodeid = None
    start_time = None

    for raw in proc.stdout:
        line = raw.rstrip("\n")
        q.put(("log", line))

        # Nouveau test détecté
        if "::" in line and not re.search(r"\b(PASSED|FAILED|ERROR|SKIPPED|XFAILED|XPASSED)\b", line):
            last_nodeid = line.strip()
            start_time = time.time()
            q.put(("case", {"nodeid": last_nodeid}))

        # Test terminé
        match = re.search(r"\b(PASSED|FAILED|ERROR|SKIPPED|XFAILED|XPASSED)\b", line)
        if match and last_nodeid:
            outcome = match.group(1).lower()
            duration_ms = int((time.time() - start_time) * 1000)

            # Normalisation des statuts
            if outcome in ["xfailed", "xpassed"]:
                outcome = "skipped"
            elif outcome == "error":
                outcome = "failed"

            # Mise à jour des compteurs
            if outcome == "passed":
                passed += 1
            elif outcome == "failed":
                failed += 1
            elif outcome == "skipped":
                skipped += 1
            done += 1

            # Événement individuel
            q.put(("result", {
                "nodeid": last_nodeid,
                "outcome": outcome,
                "duration_ms": duration_ms
            }))

            # Événement global
            q.put(("update", {
                "done": done,
                "passed": passed,
                "failed": failed,
                "skipped": skipped
            }))

            last_nodeid = None

    proc.wait()
    q.put(("end", {
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "total": total
    }))



@app.route("/run", methods=["POST"])
def run():
    # clear old queue so the next run starts clean
    try:
        while True: q.get_nowait()
    except queue.Empty:
        pass
    threading.Thread(target=run_pytest, daemon=True).start()
    return {"status": "started"}

@app.route("/events")
def events():
    def gen():
        last = time.time()
        # kick a first message to “open” the pipe in some proxies
        yield sse("log", "Flux SSE démarré")
        while True:
            try:
                event, data = q.get(timeout=1)
                yield sse(event, data)
                last = time.time()
            except queue.Empty:
                # heartbeat every 10s to keep connection warm
                if time.time() - last > 10:
                    yield ":\n\n"
                    last = time.time()
    return Response(
        gen(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"  # disable Nginx buffering if present
        }
    )

@app.route("/")
def root():
    return send_from_directory(os.getcwd(), "progress.html")

if __name__ == "__main__":
    # threaded=True helps SSE & POST /run coexist
    app.run(host="0.0.0.0", port=5057, debug=False, threaded=True)
