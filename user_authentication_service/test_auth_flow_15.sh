#!/bin/bash
BASE_URL="http://localhost:5000"
EMAIL="bob@bob.com"
PASSWORD="mySuperPwd"

echo "=== 1) Login ==="
LOGIN_RESPONSE=$(curl -s -XPOST "$BASE_URL/sessions" \
  -d "email=$EMAIL" \
  -d "password=$PASSWORD" \
  -i)

echo "$LOGIN_RESPONSE"

# Extraire le session_id du cookie
SESSION_ID=$(echo "$LOGIN_RESPONSE" | grep -i "Set-Cookie:" | sed -E 's/.*session_id=([^;]+);.*/\1/')
if [ -z "$SESSION_ID" ]; then
  echo "[ERR] Impossible de récupérer le session_id"
  exit 1
fi
echo "[OK] Session ID: $SESSION_ID"

echo
echo "=== 2) GET /profile (avec cookie) ==="
curl -s -XGET "$BASE_URL/profile" -b "session_id=$SESSION_ID"
echo

echo
echo "=== 3) DELETE /sessions (logout) ==="
curl -i -XDELETE "$BASE_URL/sessions" -b "session_id=$SESSION_ID"
echo

echo
echo "=== 4) GET /profile (session invalide) ==="
curl -i -XGET "$BASE_URL/profile" -b "session_id=$SESSION_ID"
