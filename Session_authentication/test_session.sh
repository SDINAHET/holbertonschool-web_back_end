#!/bin/bash

# 1. LOGIN
echo "🟢 Login..."
curl -X POST "http://127.0.0.1:5000/api/v1/auth_session/login" \
  -d "email=bobsession@hbtn.io" -d "password=fake pwd" -c cookie.txt
echo -e "\n"

# 2. GET all users
echo "📄 Récupération des utilisateurs..."
curl -X GET "http://127.0.0.1:5000/api/v1/users" -b cookie.txt
echo -e "\n"

# 3. POST (créer un user)
echo "➕ Création d'un utilisateur..."
curl -X POST "http://127.0.0.1:5000/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{"email": "stef@hbnb.com", "password": "user1234"}' \
  -b cookie.txt
echo -e "\n"
