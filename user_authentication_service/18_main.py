#!/usr/bin/env python3
from auth import Auth

def main():
    auth = Auth()
    email = "update18@example.com"
    old_pwd = "oldpass"
    new_pwd = "newpass"

    try:
        auth.register_user(email, old_pwd)
        print("[OK] Registered")
    except ValueError:
        print("[i] Already registered")

    # Générer un token
    token = auth.get_reset_password_token(email)
    print(f"[OK] token: {token}")

    # Mettre à jour le mot de passe
    auth.update_password(token, new_pwd)
    print("[OK] password updated")

    # L'ancien mot de passe ne marche plus
    assert not auth.valid_login(email, old_pwd)
    # Le nouveau marche
    assert auth.valid_login(email, new_pwd)
    print("[OK] valid_login with new password")

    # Le token doit être invalidé (réutilisation impossible)
    try:
        auth.update_password(token, "anotherpass")
        print("[ERR] token should not be reusable")
    except ValueError:
        print("[OK] token cannot be reused")

if __name__ == "__main__":
    main()
