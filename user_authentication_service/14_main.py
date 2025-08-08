#!/usr/bin/env python3
from app import app, AUTH

def main():
    email = "logout@example.com"
    password = "pass1234"

    # Register user (idempotent)
    try:
        AUTH.register_user(email, password)
        print("[OK] Registered user")
    except ValueError:
        print("[i] User already registered")

    # Create session
    assert AUTH.valid_login(email, password)
    sid = AUTH.create_session(email)
    assert sid
    print(f"[OK] Session created: {sid}")

    # App test client
    with app.test_client() as client:
        # 1) Sans cookie -> 403 (ok)
        r = client.delete("/sessions")
        assert r.status_code == 403
        print("[OK] DELETE /sessions without cookie -> 403")

        # 2) Poser le cookie correctement
        client.set_cookie("session_id", sid)  # Flask 3.x
        print("[OK] Cookie set in client")

        # 3) Appeler l’endpoint -> doit rediriger vers /
        r = client.delete("/sessions")
        assert r.status_code in (301, 302), r.status_code
        loc = r.headers.get("Location")
        assert loc in ("/", "http://localhost/"), loc
        print("[OK] DELETE /sessions with cookie -> redirect /")

        # 4) Vérifier que la session est bien détruite
        assert AUTH.get_user_from_session_id(sid) is None
        print("[OK] Session destroyed")

if __name__ == "__main__":
    main()
