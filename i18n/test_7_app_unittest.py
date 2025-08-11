# i18n/test_7_app_unittest.py
import unittest
import importlib.util
from pathlib import Path
import re

# Charger dynamiquement le module 7-app.py sous le nom "app7"
APP_PATH = Path(__file__).with_name("7-app.py")
spec = importlib.util.spec_from_file_location("app7", APP_PATH)
app7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app7)  # type: ignore[attr-defined]

app = app7.app  # instance Flask

H1_BY_LOCALE = {
    "en": "Hello world!",
    "fr": "Bonjour monde!",
}


def extract_tag(text: str, tag: str) -> str | None:
    """
    Retourne le contenu du premier <tag>...</tag> trouvé, sans les balises.
    Insensible à la casse et tolérant aux espaces/nouvelles lignes.
    """
    pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
    m = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else None


class LocaleTimezoneTestCase(unittest.TestCase):
    """Vérifie l'ordre de priorité et logge statut + texte de la page."""

    def run_case(self, query_string, expected_locale, expected_tz):
        """
        1) Fait une vraie requête HTTP sur "/" (test_client) et logge:
           - status code
           - <title> et <h1>
        2) Dans un contexte de requête équivalent, exécute before_request,
           puis vérifie get_locale() et get_timezone().
        3) Vérifie aussi le <h1> attendu selon la locale.
        """
        # 1) Appel réel côté client
        with app.test_client() as client:
            resp = client.get("/", query_string=query_string)
            status = resp.status_code
            body = resp.data.decode("utf-8", errors="ignore")
            title = extract_tag(body, "title") or "(no <title>)"
            h1 = extract_tag(body, "h1") or "(no <h1>)"
            print(f"[CLIENT] GET /?{query_string} -> status={status}, title={title!r}, h1={h1!r}")

            self.assertEqual(status, 200, f"HTTP status should be 200, got {status}")

        # 2) Vérification locale/timezone via les sélecteurs de l'app
        with app.test_request_context(path="/", query_string=query_string):
            app.preprocess_request()  # pour renseigner g.user
            loc = app7.get_locale()
            tz = app7.get_timezone()
            print(f"[SELECTORS] query={query_string} -> locale={loc!r}, timezone={tz!r}")

            self.assertEqual(
                loc, expected_locale,
                f"Locale: got {loc!r}, expected {expected_locale!r} for {query_string}"
            )
            self.assertEqual(
                tz, expected_tz,
                f"Timezone: got {tz!r}, expected {expected_tz!r} for {query_string}"
            )

        # 3) Vérification du contenu <h1> attendu selon la locale
        expected_h1 = H1_BY_LOCALE.get(expected_locale, H1_BY_LOCALE["en"])
        with app.test_client() as client:
            resp = client.get("/", query_string=query_string)
            body = resp.data.decode("utf-8", errors="ignore")
            h1 = extract_tag(body, "h1") or ""
            print(f"[ASSERT HTML] expected_h1={expected_h1!r}, got_h1={h1!r}")
            self.assertEqual(h1, expected_h1, f"<h1> mismatch for {query_string}")

    def test_login_as_1_user_fr_paris(self):
        # /?login_as=1 → locale = fr, timezone = Europe/Paris
        self.run_case({"login_as": "1"}, expected_locale="fr", expected_tz="Europe/Paris")

    def test_login_as_3_invalid_tz_fallback_utc(self):
        # /?login_as=3 → Spock tz invalide → UTC ; locale user "kg" non supportée → default/header ("en")
        self.run_case({"login_as": "3"}, expected_locale="en", expected_tz="UTC")

    def test_force_tz_us_central(self):
        # /?timezone=US/Central → timezone forcée ; locale par défaut "en"
        self.run_case({"timezone": "US/Central"}, expected_locale="en", expected_tz="US/Central")

    def test_ignore_bad_timezone(self):
        # /?timezone=NotAZone → ignoré → fallback (user tz ou UTC) ; ici: pas de user → UTC
        self.run_case({"timezone": "NotAZone"}, expected_locale="en", expected_tz="UTC")

    def test_combo_login2_locale_fr_tz_paris(self):
        # /?login_as=2&locale=fr&timezone=Europe/Paris → URL gagne pour locale & tz
        self.run_case(
            {"login_as": "2", "locale": "fr", "timezone": "Europe/Paris"},
            expected_locale="fr",
            expected_tz="Europe/Paris",
        )


if __name__ == "__main__":
    unittest.main()
