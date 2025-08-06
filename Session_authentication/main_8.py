#!/usr/bin/env python3
""" Test script for SessionDBAuth """

from api.v1.auth.session_db_auth import SessionDBAuth
from models.user import User
from models.user_session import UserSession
import time
import os
os.environ['SESSION_NAME'] = '_my_session_id'

print("🔄 Rechargement des utilisateurs...")
User.load_from_file()

print("📦 Création d'une instance SessionDBAuth...")
sdb_auth = SessionDBAuth()

print("👤 Recherche de l'utilisateur bobsession@hbtn.io...")
users = User.search({"email": "bobsession@hbtn.io"})
if users:
    user = users[0]
    print(f"✅ Utilisateur trouvé : {user.id}")
else:
    print("❌ Utilisateur non trouvé. Vérifie que le fichier .db_User.json contient l'utilisateur.")
    exit()

print("🔐 Création d'une session pour cet utilisateur...")
session_id = sdb_auth.create_session(user.id)
print(f"✅ Session ID : {session_id}")

print("📂 Vérification de la session créée en base...")
user_sess = UserSession.search({"session_id": session_id})
if user_sess:
    print(f"✅ Session trouvée : user_id = {user_sess[0].user_id}")
else:
    print("❌ Aucune session trouvée pour cet ID !")
    exit()

print("🔎 Récupération de l'user_id depuis la session...")
user_id = sdb_auth.user_id_for_session_id(session_id)
print(f"✅ user_id récupéré : {user_id}")

print("⏳ Attente 3 secondes (durée de session courte recommandée pour test)...")
time.sleep(3)

print("❌ Suppression de la session...")
# mock_request = type("Request", (object,), {"cookies": {"_my_session_id": session_id}})
mock_request = type("Request", (object,), {
    "cookies": {os.getenv('SESSION_NAME', '_my_session_id'): session_id}
})

deleted = sdb_auth.destroy_session(mock_request)
print(f"✅ Session supprimée ? {deleted}")

print("🔍 Nouvelle tentative de récupération après suppression...")
user_id_after = sdb_auth.user_id_for_session_id(session_id)
print(f"Résultat attendu : None → Résultat réel : {user_id_after}")
