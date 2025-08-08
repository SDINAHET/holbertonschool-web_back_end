#!/usr/bin/env python3
from app import app, AUTH

def main():
    email = "profile@example.com"
    password = "pwd12345"
    try:
        AUTH.register_user(email, password)
        print("[OK] Registered")
    except ValueError:
        print("[i] Already registered")

    assert AUTH.valid_login(email, password)
    sid = AUTH.create_session(email)
    assert sid
    print(f"[OK] Session created: {sid}")

    with app.test_client() as client:
        # 1) sans cookie -> 403
        r = client.get("/profile")
        assert r.status_code == 403
        print("[OK] GET /profile without cookie -> 403")

        # 2) avec cookie -> 200 + email
        client.set_cookie("session_id", sid)   # Flask 3.x signature
        r = client.get("/profile")
        assert r.status_code == 200, r.status_code
        assert r.json == {"email": email}, r.json
        print("[OK] GET /profile with cookie -> 200 + email")

if __name__ == "__main__":
    main()
