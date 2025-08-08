#!/usr/bin/env python3
"""
Test get_user_from_session_id
"""
from auth import Auth

auth = Auth()

# Étape 1 : Créer un utilisateur
email = "bob@bob.com"
password = "MyPwdOfBob"
try:
    user = auth.register_user(email, password)
except ValueError:
    print("Utilisateur déjà créé")

# Étape 2 : Créer une session pour l'utilisateur
session_id = auth.create_session(email)
print(f"Session ID créé : {session_id}")

# Étape 3 : Tester avec un session_id valide
user_from_session = auth.get_user_from_session_id(session_id)
print(f"Utilisateur trouvé : {user_from_session.email if user_from_session else None}")

# Étape 4 : Tester avec un session_id inexistant
invalid_session = auth.get_user_from_session_id("1234-uuid-invalide")
print(f"Avec UUID invalide : {invalid_session}")

# Étape 5 : Tester avec None
none_session = auth.get_user_from_session_id(None)
print(f"Avec None : {none_session}")
