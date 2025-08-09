#!/usr/bin/env python3
"""Task 7 manual test script for POST /users"""
import json

URL = "http://127.0.0.1:5000/users"
DATA = {"email": "bob@me.com", "password": "mySuperPwd"}

def post_with_requests():
    import requests
    r1 = requests.post(URL, data=DATA)
    print("1) status:", r1.status_code, "->", r1.text)

    r2 = requests.post(URL, data=DATA)
    print("2) status:", r2.status_code, "->", r2.text)

def post_with_urllib():
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    import urllib.error

    body = urlencode(DATA).encode()
    for i in (1, 2):
        try:
            req = Request(URL, data=body, method="POST")
            with urlopen(req) as resp:
                raw = resp.read().decode()
                print(f"{i}) status:", resp.status, "->", raw)
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            print(f"{i}) status:", e.code, "->", raw)

if __name__ == "__main__":
    try:
        post_with_requests()
    except Exception:
        post_with_urllib()
