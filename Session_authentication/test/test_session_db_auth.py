#!/usr/bin/env python3
"""
E2E test for SessionDBAuth using requests
"""

import requests

BASE_URL = "http://localhost:5000/api/v1"
LOGIN_URL = f"{BASE_URL}/auth_session/login/"
ME_URL = f"{BASE_URL}/users/me"
LOGOUT_URL = f"{BASE_URL}/auth_session/logout/"

# User credentials
email = "bobsession@hbtn.io"
password = "fake pwd"

print("1. Logging in...")

# 1. Login and get session cookie
res = requests.post(LOGIN_URL, data={"email": email, "password": password})
assert res.status_code == 200, f"Login failed: {res.text}"
print("✅ Login OK")

# 2. Extract session cookie
session_id = res.cookies.get('_my_session_id')
assert session_id is not None, "No session ID returned"
print(f"🔐 Session ID: {session_id}")

# 3. Get current user using session
cookies = {'_my_session_id': session_id}
res = requests.get(ME_URL, cookies=cookies)
assert res.status_code == 200, f"/users/me failed: {res.text}"
print("✅ /users/me OK")
print("User:", res.json())

# 4. Logout
res = requests.delete(LOGOUT_URL, cookies=cookies)
assert res.status_code == 200, f"Logout failed: {res.text}"
print("✅ Logout OK")

# 5. Verify session invalid
res = requests.get(ME_URL, cookies=cookies)
assert res.status_code == 401, "Session should be invalid after logout"
print("✅ Session properly invalidated")
