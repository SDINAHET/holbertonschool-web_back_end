#!/usr/bin/env python3
from app import app, AUTH

def main():
    email = "user19@example.com"
    old_pwd = "oldpass"
    new_pwd = "newpass"

    # Register (idempotent)
    try:
        AUTH.register_user(email, old_pwd)
        print("[OK] Registered")
    except ValueError:
        print("[i] Already registered")

    with app.test_client() as client:
        # 1) Générer un reset_token via l'endpoint POST /reset_password
        r = client.post("/reset_password", data={"email": email})
        assert r.status_code == 200, r.data
        token = r.get_json().get("reset_token")
        print(f"[OK] token: {token}")

        # 2) PUT /reset_password sans champs -> 403
        r = client.put("/reset_password", data={})
        assert r.status_code == 403
        print("[OK] PUT /reset_password without fields -> 403")

        # 3) PUT /reset_password avec mauvais token -> 403
        r = client.put("/reset_password", data={
            "email": email,
            "reset_token": "bad-token",
            "new_password": new_pwd
        })
        assert r.status_code == 403
        print("[OK] PUT /reset_password invalid token -> 403")

        # 4) PUT /reset_password avec bon token -> 200
        r = client.put("/reset_password", data={
            "email": email,
            "reset_token": token,
            "new_password": new_pwd
        })
        assert r.status_code == 200, r.data
        assert r.get_json() == {"email": email, "message": "Password updated"}
        print("[OK] PUT /reset_password valid token -> 200 + message")

        # 5) Vérifier que le mot de passe a bien changé
        assert not AUTH.valid_login(email, old_pwd)
        assert AUTH.valid_login(email, new_pwd)
        print("[OK] valid_login switches to new password")

        # 6) Token ne doit plus être réutilisable
        r = client.put("/reset_password", data={
            "email": email,
            "reset_token": token,
            "new_password": "another"
        })
        assert r.status_code == 403
        print("[OK] token cannot be reused")

if __name__ == "__main__":
    main()
