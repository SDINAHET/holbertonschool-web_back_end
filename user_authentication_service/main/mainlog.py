import requests

BASE_URL = "http://127.0.0.1:5000"

def register_user(email: str, password: str) -> None:
    print(f"[INFO] Registering user: {email}")
    r = requests.post(f"{BASE_URL}/users", data={"email": email, "password": password})
    assert r.status_code == 200
    print("[OK] User registered successfully")

def log_in_wrong_password(email: str, password: str) -> None:
    print(f"[INFO] Trying to login with wrong password for: {email}")
    r = requests.post(f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert r.status_code == 401
    print("[OK] Wrong password rejected")

def log_in(email: str, password: str) -> str:
    print(f"[INFO] Logging in as: {email}")
    r = requests.post(f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert r.status_code == 200
    session_id = r.cookies.get("session_id")
    assert session_id is not None
    print(f"[OK] Logged in, session_id={session_id}")
    return session_id

def profile_unlogged() -> None:
    print("[INFO] Checking profile without login")
    r = requests.get(f"{BASE_URL}/profile")
    assert r.status_code == 403
    print("[OK] Profile access denied when not logged in")

def profile_logged(session_id: str) -> None:
    print("[INFO] Checking profile with login")
    r = requests.get(f"{BASE_URL}/profile", cookies={"session_id": session_id})
    assert r.status_code == 200
    print("[OK] Profile retrieved successfully")

def log_out(session_id: str) -> None:
    print("[INFO] Logging out")
    r = requests.delete(f"{BASE_URL}/sessions", cookies={"session_id": session_id})
    assert r.status_code == 200
    print("[OK] Logged out successfully")

def reset_password_token(email: str) -> str:
    print(f"[INFO] Requesting reset token for: {email}")
    r = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    assert r.status_code == 200
    token = r.json().get("reset_token")
    assert token is not None
    print(f"[OK] Reset token received: {token}")
    return token

def update_password(email: str, reset_token: str, new_password: str) -> None:
    print(f"[INFO] Updating password for: {email}")
    r = requests.put(f"{BASE_URL}/reset_password",
                     data={"email": email, "reset_token": reset_token, "new_password": new_password})
    assert r.status_code == 200
    print("[OK] Password updated successfully")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
