#!/usr/bin/env python3
"""
End-to-end integration test for the authentication service
"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user"""
    payload = {"email": email, "password": password}
    resp = requests.post(f"{BASE_URL}/users", data=payload)
    assert resp.status_code == 200 or resp.status_code == 400
    if resp.status_code == 200:
        assert resp.json() == {"email": email, "message": "user created"}
    else:  # 400 if already registered
        assert resp.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt login with wrong password"""
    payload = {"email": email, "password": password}
    resp = requests.post(f"{BASE_URL}/sessions", data=payload)
    # print("wrong-pwd =>", resp.status_code, resp.headers.get("content-type"),
    #       resp.text)
    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    """Log in with correct credentials, return session_id"""
    payload = {"email": email, "password": password}
    resp = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("email") == email and body.get("message") == "logged in"
    return resp.cookies.get("session_id")


def profile_unlogged() -> None:
    """Profile access without login should be forbidden"""
    resp = requests.get(f"{BASE_URL}/profile")
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """Profile access with valid session"""
    cookies = {"session_id": session_id}
    resp = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert "email" in resp.json()


def log_out(session_id: str) -> None:
    """Log out user by deleting the session"""
    cookies = {"session_id": session_id}
    resp = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
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
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }
    resp = requests.put(
        f"{BASE_URL}/reset_password",
        data=data
    )
    assert resp.status_code == 200
    assert resp.json() == {"email": email, "message": "Password updated"}

def ok(msg: str) -> None:
    print(f"✅ {msg}")


# Variables fournies
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD); ok("Enregistrement OK / déjà inscrit")
    log_in_wrong_password(EMAIL, NEW_PASSWD); ok("Mauvais mot de passe → 401")
    profile_unlogged(); ok("Profil sans login → 403")
    session_id = log_in(EMAIL, PASSWD); ok("Login OK")
    profile_logged(session_id); ok("Profil connecté OK")
    log_out(session_id); ok("Déconnexion OK")
    reset_token = reset_password_token(EMAIL); ok("Token reset généré")
    update_password(EMAIL, reset_token, NEW_PASSWD); ok("Mot de passe màj")
    log_in(EMAIL, NEW_PASSWD); ok("Login avec nouveau mot de passe OK")

