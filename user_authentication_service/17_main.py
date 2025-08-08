#!/usr/bin/env python3
from app import app, AUTH

def main():
    # email = "reset17@example.com"
    # password = "pwd12345"
    email = "bob@bob.com"
    password = "MyPwdOfBob"

    # Register user (idempotent)
    try:
        AUTH.register_user(email, password)
        print("[OK] Registered")
    except ValueError:
        print("[i] Already registered")

    with app.test_client() as client:
        # 1) Manque email -> 403
        r = client.post("/reset_password", data={})
        assert r.status_code == 403
        print("[OK] POST /reset_password without email -> 403")

        # 2) Email inconnu -> 403
        r = client.post("/reset_password", data={"email": "unknown@example.com"})
        assert r.status_code == 403
        print("[OK] POST /reset_password unknown email -> 403")

        # 3) Email existant -> 200 + reset_token
        r = client.post("/reset_password", data={"email": email})
        assert r.status_code == 200, r.data
        j = r.get_json()
        assert j["email"] == email and "reset_token" in j and j["reset_token"]
        print(f"[OK] Token generated: {j['reset_token']}")

if __name__ == "__main__":
    main()
