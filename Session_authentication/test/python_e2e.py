import requests
import time

BASE_URL = "http://0.0.0.0:5000/api/v1"
LOGIN_URL = f"{BASE_URL}/auth_session/login"
ME_URL = f"{BASE_URL}/users/me"
SESSION_NAME = "_my_session_id"

# Étape 1 - Login
login_data = {
    "email": "bobsession@hbtn.io",
    "password": "fake pwd"
}
res = requests.post(LOGIN_URL, data=login_data)
# assert res.status_code == 200
if res.status_code != 200:
    print("Login failed!")
    print("Status code:", res.status_code)
    print("Response:", res.text)
    exit(1)
cookie = res.cookies.get(SESSION_NAME)
print("Session ID:", cookie)

# Étape 2 - Vérif immédiate
res = requests.get(ME_URL, cookies={SESSION_NAME: cookie})
# assert res.status_code == 200
if res.status_code != 200:
    print("Login failed!")
    print("Status code:", res.status_code)
    print("Response:", res.text)
    exit(1)
print("User me (immédiat) OK")

# Étape 3 - Attendre 10s
time.sleep(10)
res = requests.get(ME_URL, cookies={SESSION_NAME: cookie})
# assert res.status_code == 200
if res.status_code != 200:
    print("Login failed!")
    print("Status code:", res.status_code)
    print("Response:", res.text)
    exit(1)
print("User me (10s) OK")

# Étape 4 - Attendre expiration (75s total)
print("Waiting for session to expire (65s)...")
time.sleep(65)
res = requests.get(ME_URL, cookies={SESSION_NAME: cookie})
# assert res.status_code == 403
# print("User me (session expirée) OK")
if res.status_code == 403:
    print("User me (session expirée) OK")
else:
    print("Session was expected to be expired but it wasn't!")
    print("Status code:", res.status_code)
    print("Response:", res.text)
    exit(1)
