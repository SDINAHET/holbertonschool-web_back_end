import re
import uuid
import pytest

# Adapte cet import à ta structure de projet :
from app import app  # doit exposer un Flask instance nommée "app"

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_e2e_full_flow(client):
    # 1) Register
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    password = "InitPassw0rd!"
    rv = client.post("/users", data={"email": email, "password": password})
    assert rv.status_code in (200, 201)
    data = rv.get_json()
    assert data and data.get("email") == email
    assert re.search("user created", data.get("message", ""), re.I)

    # 2) Login
    rv = client.post("/sessions", data={"email": email, "password": password})
    assert rv.status_code in (200, 201)
    data = rv.get_json()
    assert data and data.get("email") == email
    assert re.search("logged in", data.get("message", ""), re.I)
    # Récupère le cookie de session
    session_id = None
    for c in client.cookie_jar:
        if c.name == "session_id":
            session_id = c.value
            break
    assert session_id, "Cookie session_id non défini après login"

    # 3) Profile (protégé)
    rv = client.get("/profile")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data and data.get("email") == email

    # 4) Demande de reset token
    rv = client.post("/reset_password", data={"email": email})
    assert rv.status_code in (200, 201)
    data = rv.get_json()
    assert data and data.get("email") == email
    reset_token = data.get("reset_token")
    assert reset_token and re.fullmatch(
        r"[0-9a-fA-F-]{36}", reset_token
    ), "reset_token doit être un UUID"

    # 5) Update password (et invalidation du token)
    new_password = "N3wPassw0rd!"
    rv = client.put(
        "/reset_password",
        data={"email": email, "reset_token": reset_token, "new_password": new_password},
    )
    assert rv.status_code == 200
    data = rv.get_json()
    assert data and data.get("email") == email
    assert re.search("password updated", data.get("message", ""), re.I)

    # 5bis) Vérifie que le token est bien invalidé (optionnel si ton API le gère côté serveur)
    rv_bad = client.put(
        "/reset_password",
        data={"email": email, "reset_token": reset_token, "new_password": "Another#1"},
    )
    assert rv_bad.status_code in (400, 401, 403), "Le reset_token devrait être usage unique"

    # 6) Logout (déconnecte l’ancienne session)
    rv = client.delete("/sessions")
    assert rv.status_code in (200, 204)
    # (Selon ta spec, tu peux vérifier le message JSON)

    # 7) Login avec le NOUVEAU mot de passe
    rv = client.post("/sessions", data={"email": email, "password": new_password})
    assert rv.status_code in (200, 201)
    data = rv.get_json()
    assert data and data.get("email") == email
    assert re.search("logged in", data.get("message", ""), re.I)

    # 8) Profile à nouveau (doit réussir)
    rv = client.get("/profile")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data and data.get("email") == email

    # 9) Logout final
    rv = client.delete("/sessions")
    assert rv.status_code in (200, 204)
