#!/usr/bin/env python3
"""
End-to-end integration test for the authentication service
"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user"""
    resp = requests.post(f"{BASE_URL}/users", data={"email": email, "password": password})
    assert resp.status_code == 200 or resp.status_code == 400
    if resp.status_code == 200:
        assert resp.json() == {"email": email, "message": "user created"}
    else:  # 400 if already registered
        assert resp.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt login with wrong password"""
    resp = requests.post(f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    """Log in with correct credentials, return session_id"""
    resp = requests.post(f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert resp.status_code == 200
    assert resp.json().get("email") == email and resp.json().get("message") == "logged in"
    return resp.cookies.get("session_id")


def profile_unlogged() -> None:
    """Profile access without login should be forbidden"""
    resp = requests.get(f"{BASE_URL}/profile")
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """Profile access with valid session"""
    resp = requests.get(f"{BASE_URL}/profile", cookies={"session_id": session_id})
    assert resp.status_code == 200
    assert "email" in resp.json()


def log_out(session_id: str) -> None:
    """Log out user by deleting the session"""
    resp = requests.delete(f"{BASE_URL}/sessions", cookies={"session_id": session_id})
    assert resp.status_code == 200
    assert resp.json().get("message") == "Bienvenue"


def reset_password_token(email: str) -> str:
    """Request a password reset token"""
    resp = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    assert resp.status_code == 200
    assert resp.json().get("email") == email
    return resp.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password with the reset token"""
    resp = requests.put(
        f"{BASE_URL}/reset_password",
        data={"email": email, "reset_token": reset_token, "new_password": new_password}
    )
    assert resp.status_code == 200
    assert resp.json() == {"email": email, "message": "Password updated"}


# Variables fournies
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
