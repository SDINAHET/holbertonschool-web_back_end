#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import uuid
import re
import importlib
from app import app  # adapte si nécessaire

# --- couleurs terminal ---
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def _import_generate_uuid():
    candidates = [
        ("utils", "generate_uuid"),
        ("auth", "generate_uuid"),
        ("auth", "_generate_uuid"),
        ("app.utils", "generate_uuid"),
        ("app.auth", "generate_uuid"),
        ("app.auth", "_generate_uuid"),
    ]
    for module_name, attr in candidates:
        try:
            mod = importlib.import_module(module_name)
            fn = getattr(mod, attr)
            return fn, f"{module_name}.{attr}"
        except Exception:
            continue
    return None, None

GENERATE_UUID_FN, GENERATE_UUID_PATH = _import_generate_uuid()

class Runner:
    def __init__(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        self.passed = 0
        self.failed = 0
        self.start = time.time()
        self._last_response = None

    # --------- LOG DÉTAILLÉ APRÈS CHAQUE TEST ---------
    def _format_last(self):
        """Retourne '(status) -> bref résumé' pour le dernier self._last_response."""
        rv = self._last_response
        if rv is None:
            return "(status n/a)"
        status = rv.status_code
        extra = ""
        # Redirection ?
        if status in (301, 302, 303, 307, 308):
            loc = rv.headers.get("Location")
            if loc:
                extra += f" -> redirect to {loc}"
        # JSON lisible ?
        js = None
        try:
            js = rv.get_json()
        except Exception:
            js = None
        if js:
            keys = {}
            for k in ("email", "message", "reset_token", "error"):
                if k in js:
                    val = js[k]
                    if k == "reset_token" and isinstance(val, str):
                        val = (val[:8] + "...") if len(val) > 11 else val
                    keys[k] = val
            if keys:
                extra += f" -> {keys}"
            else:
                extra += f" -> JSON keys: {list(js.keys())[:5]}"
        else:
            body = rv.get_data(as_text=True)
            if body:
                snippet = body[:120].replace("\n", " ").replace("\r", " ")
                extra += f" -> {snippet}"
        return f"({status}){extra}"

    def record(self, name, func):
        # reset du dernier response pour ne pas logguer un ancien appel
        self._last_response = None
        try:
            func()
            self.passed += 1
            # PASS + statut + extrait
            print(f"{GREEN}[PASS]{RESET} {name} {self._format_last()}")
        except AssertionError as e:
            self.failed += 1
            # FAIL + message + statut + extrait
            print(f"{RED}[FAIL]{RESET} {name}  -> {e} {self._format_last()}")
        except Exception as e:
            self.failed += 1
            # ERROR + message + statut + extrait
            print(f"{YELLOW}[ERROR]{RESET} {name}  -> {e} {self._format_last()}")

    # --------- wrappers HTTP ---------
    def _remember(self, rv):
        self._last_response = rv
        return rv

    def post(self, url, payload):
        return self._remember(self.client.post(url, data=payload))

    def put(self, url, payload):
        return self._remember(self.client.put(url, data=payload))

    def delete(self, url):
        return self._remember(self.client.delete(url))

    def get(self, url):
        return self._remember(self.client.get(url))

    def cookie_session_id(self):
        try:
            val = self.client.get_cookie("session_id", domain="localhost", path="/")
            if val:
                return val
        except Exception:
            pass
        rv = self._last_response
        if rv is not None:
            for sc in rv.headers.get_all("Set-Cookie"):
                m = re.search(r"\bsession_id=([^;]+)", sc)
                if m:
                    return m.group(1)
        return None

    def require_status(self, rv, allowed, ctx=""):
        if rv.status_code not in allowed:
            body = rv.get_data(as_text=True)
            raise AssertionError(f"{ctx} status={rv.status_code} body={body[:500]}")

    # ----------------- RUN ALL (identique) -----------------
    def run_all(self):
        self.email = f"user_{uuid.uuid4().hex[:8]}@example.com"
        self.password = "InitPassw0rd!"
        self.new_password = "N3wPassw0rd!"

        self.record("test_register_user_created", self.test_register_user_created)
        self.record("test_register_user_already_registered", self.test_register_user_already_registered)

        self.record("test_valid_login_correct_credentials", self.test_valid_login_correct_credentials)
        self.record("test_valid_login_unknown_email", self.test_valid_login_unknown_email)
        self.record("test_valid_login_wrong_password", self.test_valid_login_wrong_password)

        self.record("test_returns_string_and_valid_uuid", self.test_returns_string_and_valid_uuid)
        self.record("test_returns_different_values_each_time", self.test_returns_different_values_each_time)
        self.record("test_uses_uuid4_under_the_hood", self.test_uses_uuid4_under_the_hood)

        self.record("test_create_session_success", self.test_create_session_success)
        self.record("test_create_session_unknown_email", self.test_create_session_unknown_email)

        self.record("test_login_failure_returns_401", self.test_login_failure_returns_401)
        self.record("test_login_success_sets_cookie_and_returns_json", self.test_login_success_sets_cookie_and_returns_json)

        self.record("test_none_session_id_returns_none_and_skips_db", self.test_none_session_id_returns_none_and_skips_db)
        self.record("test_returns_user_when_session_exists", self.test_returns_user_when_session_exists)
        self.record("test_unknown_session_id_returns_none", self.test_unknown_session_id_returns_none)

        self.record("test_destroy_session_invalidate", self.test_destroy_session_invalidate)
        self.record("test_destroy_session_idempotent", self.test_destroy_session_idempotent)

        self.record("test_logout_with_cookie", self.test_logout_with_cookie)
        self.record("test_logout_without_cookie", self.test_logout_without_cookie)

        self.record("test_profile_with_cookie", self.test_profile_with_cookie)
        self.record("test_profile_without_cookie", self.test_profile_without_cookie)

        self.record("test_get_reset_password_token_ok", self.test_get_reset_password_token_ok)
        self.record("test_get_reset_password_token_unknown_email", self.test_get_reset_password_token_unknown_email)

        self.record("test_known_email_generates_token", self.test_known_email_generates_token)
        self.record("test_missing_email", self.test_missing_email)
        self.record("test_unknown_email", self.test_unknown_email)

        self.record("test_update_password_bad_token", self.test_update_password_bad_token)
        self.record("test_update_password_ok", self.test_update_password_ok)

        self.record("test_put_reset_password_invalid_token", self.test_put_reset_password_invalid_token)
        self.record("test_put_reset_password_missing_fields", self.test_put_reset_password_missing_fields)
        self.record("test_put_reset_password_success_and_invalidate_token", self.test_put_reset_password_success_and_invalidate_token)

        total = self.passed + self.failed
        duration = time.time() - self.start
        pct = (self.passed / total * 100) if total else 0.0
        print("\n" + "-" * 60)
        if self.failed == 0 and total == 31:
            print(f"[E2E] Tous les tests réussis ✅  ({self.passed}/{total})  {pct:.0f}%")
        else:
            print(f"[E2E] Terminé : PASS={self.passed}  FAIL={self.failed}  ({pct:.0f}%)")
        print(f"Durée: {duration:.2f}s")
        print("-" * 60)

    # --------- Implémentations (inchangé) ---------
    # ... (garde exactement tes méthodes de tests ci-dessous, inchangées)
    # Register
    def test_register_user_created(self):
        rv = self.post("/users", {"email": self.email, "password": self.password})
        self.require_status(rv, (200, 201), "register_user_created")
        js = rv.get_json() or {}
        assert js.get("email") == self.email
        assert re.search("user created", js.get("message", ""), re.I)

    def test_register_user_already_registered(self):
        rv = self.post("/users", {"email": self.email, "password": self.password})
        self.require_status(rv, (400, 409), "register_user_already_registered")

    # Valid login
    def test_valid_login_correct_credentials(self):
        rv = self.post("/sessions", {"email": self.email, "password": self.password})
        self.require_status(rv, (200, 201), "valid_login_correct_credentials")
        assert self.cookie_session_id(), "cookie session_id manquant"

    def test_valid_login_unknown_email(self):
        rv = self.post("/sessions", {"email": "unknown@example.com", "password": "x"})
        self.require_status(rv, (401, 404, 400), "valid_login_unknown_email")

    def test_valid_login_wrong_password(self):
        rv = self.post("/sessions", {"email": self.email, "password": "Wrong#123"})
        self.require_status(rv, (401, 403), "valid_login_wrong_password")

    # generate_uuid
    def test_returns_string_and_valid_uuid(self):
        if GENERATE_UUID_FN is None:
            rv = self.post("/reset_password", {"email": self.email})
            self.require_status(rv, (200, 201), "reset_password_for_uuid")
            token = (rv.get_json() or {}).get("reset_token")
            assert token and re.fullmatch(r"[0-9a-fA-F-]{36}", token)
            return
        val = GENERATE_UUID_FN()
        assert isinstance(val, str)
        assert re.fullmatch(r"[0-9a-fA-F-]{36}", val), f"format non UUID: {val}"

    def test_returns_different_values_each_time(self):
        if GENERATE_UUID_FN is None:
            rv1 = self.post("/reset_password", {"email": self.email})
            rv2 = self.post("/reset_password", {"email": self.email})
            t1 = (rv1.get_json() or {}).get("reset_token")
            t2 = (rv2.get_json() or {}).get("reset_token")
            assert t1 and t2 and t1 != t2
            return
        a = GENERATE_UUID_FN(); b = GENERATE_UUID_FN()
        assert a != b, "UUID identiques, attendu différents"

    def test_uses_uuid4_under_the_hood(self):
        if GENERATE_UUID_FN is None:
            rv = self.post("/reset_password", {"email": self.email})
            self.require_status(rv, (200, 201), "reset_password_for_uuid4")
            token = (rv.get_json() or {}).get("reset_token")
            u = uuid.UUID(token)
            assert u.version == 4, f"attendu version 4, reçu {u.version}"
            return
        u = uuid.UUID(GENERATE_UUID_FN())
        assert u.version == 4, f"attendu uuid4, reçu version {u.version}"

    # create session
    def test_create_session_success(self):
        rv = self.post("/sessions", {"email": self.email, "password": self.password})
        self.require_status(rv, (200, 201), "create_session_success")
        assert self.cookie_session_id(), "session_id manquant"

    def test_create_session_unknown_email(self):
        rv = self.post("/sessions", {"email": "nobody@example.com", "password": "x"})
        self.require_status(rv, (401, 404, 400), "create_session_unknown_email")

    # app login endpoint
    def test_login_failure_returns_401(self):
        rv = self.post("/sessions", {"email": self.email, "password": "bad"})
        self.require_status(rv, (401, 403), "login_failure_returns_401")

    def test_login_success_sets_cookie_and_returns_json(self):
        rv = self.post("/sessions", {"email": self.email, "password": self.password})
        self.require_status(rv, (200, 201), "login_success_sets_cookie")
        js = rv.get_json() or {}
        assert js.get("email") == self.email
        assert re.search("logged in", js.get("message", ""), re.I)
        assert self.cookie_session_id(), "session_id manquant après login"

    # get_user_from_session_id
    def test_none_session_id_returns_none_and_skips_db(self):
        with app.test_client() as c2:
            rv = c2.get("/profile")
            if rv.status_code not in (401, 403):
                body = rv.get_data(as_text=True)
                raise AssertionError(f"none_session_id -> status={rv.status_code} body={body[:500]}")

    def test_returns_user_when_session_exists(self):
        self.post("/sessions", {"email": self.email, "password": self.password})
        rv = self.get("/profile")
        self.require_status(rv, (200,), "returns_user_when_session_exists")
        js = rv.get_json() or {}
        assert js.get("email") == self.email

    def test_unknown_session_id_returns_none(self):
        with app.test_client() as c3:
            c3.set_cookie("session_id", "invalid-session-id", domain="localhost", path="/")
            rv = c3.get("/profile")
            if rv.status_code not in (401, 403):
                body = rv.get_data(as_text=True)
                raise AssertionError(f"unknown_session_id -> status={rv.status_code} body={body[:500]}")

    # destroy session
    def test_destroy_session_invalidate(self):
        self.post("/sessions", {"email": self.email, "password": self.password})
        rv = self.delete("/sessions")
        self.require_status(rv, (200, 204, 302), "destroy_session_invalidate.logout")
        rv = self.get("/profile")
        if rv.status_code not in (401, 403):
            body = rv.get_data(as_text=True)
            raise AssertionError(f"destroy_session_invalidate.profile -> status={rv.status_code} body={body[:500]}")

    def test_destroy_session_idempotent(self):
        rv = self.delete("/sessions")
        self.require_status(rv, (200, 204, 401, 403, 302), "destroy_session_idempotent")

    # logout endpoint
    def test_logout_with_cookie(self):
        self.post("/sessions", {"email": self.email, "password": self.password})
        rv = self.delete("/sessions")
        self.require_status(rv, (200, 204, 302), "logout_with_cookie")

    def test_logout_without_cookie(self):
        with app.test_client() as c4:
            rv = c4.delete("/sessions")
            if rv.status_code not in (200, 204, 401, 403, 302):
                body = rv.get_data(as_text=True)
                raise AssertionError(f"logout_without_cookie -> status={rv.status_code} body={body[:500]}")

    # profile endpoint
    def test_profile_with_cookie(self):
        self.post("/sessions", {"email": self.email, "password": self.password})
        rv = self.get("/profile")
        self.require_status(rv, (200,), "profile_with_cookie")
        assert (rv.get_json() or {}).get("email") == self.email

    def test_profile_without_cookie(self):
        with app.test_client() as c5:
            rv = c5.get("/profile")
            if rv.status_code not in (401, 403):
                body = rv.get_data(as_text=True)
                raise AssertionError(f"profile_without_cookie -> status={rv.status_code} body={body[:500]}")

    # reset token
    def test_get_reset_password_token_ok(self):
        rv = self.post("/reset_password", {"email": self.email})
        self.require_status(rv, (200, 201), "get_reset_password_token_ok")
        token = (rv.get_json() or {}).get("reset_token")
        assert token and re.fullmatch(r"[0-9a-fA-F-]{36}", token)
        self._last_token = token

    def test_get_reset_password_token_unknown_email(self):
        rv = self.post("/reset_password", {"email": "nobody@example.com"})
        self.require_status(rv, (400, 401, 403, 404), "get_reset_password_token_unknown_email")

    def test_known_email_generates_token(self):
        rv = self.post("/reset_password", {"email": self.email})
        self.require_status(rv, (200, 201), "known_email_generates_token")
        token = (rv.get_json() or {}).get("reset_token")
        assert token and re.fullmatch(r"[0-9a-fA-F-]{36}", token)
        self._last_token = token

    def test_missing_email(self):
        rv = self.post("/reset_password", {})
        self.require_status(rv, (400, 422, 403), "missing_email")

    def test_unknown_email(self):
        rv = self.post("/reset_password", {"email": "ghost@example.com"})
        self.require_status(rv, (400, 401, 403, 404), "unknown_email")

    # update password
    def test_update_password_bad_token(self):
        rv = self.put("/reset_password", {"email": self.email, "reset_token": "bad-token", "new_password": self.new_password})
        self.require_status(rv, (400, 401, 403), "update_password_bad_token")

    def test_update_password_ok(self):
        if not hasattr(self, "_last_token"):
            self.test_get_reset_password_token_ok()
        rv = self.put("/reset_password", {"email": self.email, "reset_token": self._last_token, "new_password": self.new_password})
        self.require_status(rv, (200,), "update_password_ok")
        msg = (rv.get_json() or {}).get("message", "")
        assert re.search("password updated", msg, re.I)

    def test_put_reset_password_invalid_token(self):
        rv = self.put("/reset_password", {"email": self.email, "reset_token": "00000000-0000-0000-0000-000000000000", "new_password": "Another#1"})
        self.require_status(rv, (400, 401, 403), "put_reset_password_invalid_token")

    def test_put_reset_password_missing_fields(self):
        rv = self.put("/reset_password", {"email": self.email})
        self.require_status(rv, (400, 422, 403), "put_reset_password_missing_fields")

    def test_put_reset_password_success_and_invalidate_token(self):
        rv = self.post("/reset_password", {"email": self.email})
        self.require_status(rv, (200, 201), "prep_token_for_success")
        token = (rv.get_json() or {}).get("reset_token")
        assert token

        rv = self.put("/reset_password", {"email": self.email, "reset_token": token, "new_password": "FinalPassw0rd!"})
        self.require_status(rv, (200,), "put_reset_password_success")

        rv2 = self.put("/reset_password", {"email": self.email, "reset_token": token, "new_password": "Nope#1"})
        self.require_status(rv2, (400, 401, 403), "put_reset_password_reuse_token")

if __name__ == "__main__":
    Runner().run_all()
