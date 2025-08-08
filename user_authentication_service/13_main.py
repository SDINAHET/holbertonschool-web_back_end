#!/usr/bin/env python3
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

def safe_register(auth: Auth, email: str, password: str):
    try:
        auth.register_user(email, password)
        print(f"[OK] Registered {email}")
    except ValueError:
        print(f"[i] {email} already registered")

def main():
    auth = Auth()

    email = "bob@example.com"
    password = "correcthorsebatterystaple"

    # 1) Register (idempotent)
    safe_register(auth, email, password)

    # 2) Login -> create session
    if not auth.valid_login(email, password):
        print("[ERR] valid_login failed")
        return

    session_id = auth.create_session(email)
    print(f"[OK] session created: {session_id!r}")

    # 3) get_user_from_session_id works
    user = auth.get_user_from_session_id(session_id)
    if user is None:
        print("[ERR] get_user_from_session_id returned None")
        return
    print(f"[OK] user fetched by session: id={user.id}, email={user.email}")

    # 4) destroy_session(user.id)
    auth.destroy_session(user.id)
    print("[OK] destroy_session called")

    # 5) old session should no longer resolve to a user
    user_after = auth.get_user_from_session_id(session_id)
    if user_after is None:
        print("[OK] session invalidated ✅")
    else:
        print("[ERR] session still valid after destroy_session ❌")

    # 6) calling with None should be a no-op (and not crash)
    auth.destroy_session(None)
    print("[OK] destroy_session(None) did not crash")

if __name__ == "__main__":
    main()
