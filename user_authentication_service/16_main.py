#!/usr/bin/env python3
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

def main():
    auth = Auth()
    email = "bob@bob.com"
    password = "MyPwdOfBob"

    # register (idempotent)
    try:
        auth.register_user(email, password)
        print("[OK] Registered user")
    except ValueError:
        print("[i] Already registered")

    # generate token
    token = auth.get_reset_password_token(email)
    assert isinstance(token, str) and len(token) > 0
    print(f"[OK] reset token: {token}")

    # non-existing email -> ValueError
    try:
        auth.get_reset_password_token("nope@example.com")
        print("[ERR] expected ValueError for unknown email")
    except ValueError:
        print("[OK] ValueError raised for unknown email")

if __name__ == "__main__":
    main()
