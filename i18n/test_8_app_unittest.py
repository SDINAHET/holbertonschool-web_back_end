# i18n/test_8_app_unittest.py
import unittest
import importlib.util
from pathlib import Path
import re

# Charge dynamiquement app.py (étape 8)
APP_PATH = Path(__file__).with_name("app.py")
spec = importlib.util.spec_from_file_location("app8", APP_PATH)
app8 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app8)  # type: ignore[attr-defined]

app = app8.app  # instance Flask


def contains(text: str, needle: str) -> bool:
    return needle in text


class Step8CurrentTimeTestCase(unittest.TestCase):
    """Vérifie l'affichage de l'heure localisée et la sélection locale/timezone."""

    def run_case(self, query_string, expect_locale, expect_tz, expect_phrase):
        """
        1) Fait une requête GET / avec query_string et vérifie la phrase attendue.
        2) Vérifie locale/timezone via les sélecteurs de l'app.
        """
        # 1) Requête réelle côté client
        with app.test_client() as client:
            resp = client.get("/", query_string=query_string)
            self.assertEqual(resp.status_code, 200)
            body = resp.data.decode("utf-8", errors="ignore")
            # On vérifie la phrase de traduction (FR/EN)
            self.assertTrue(
                contains(body, expect_phrase),
                f"Corps ne contient pas la phrase attendue '{expect_phrase}'. Body: {body[:200]}..."
            )

        # 2) Vérification via sélecteurs (locale & timezone)
        with app.test_request_context(path="/", query_string=query_string):
            app.preprocess_request()  # pour g.user
            loc = app8.get_locale()
            tz = app8.get_timezone()
            # Logs console utiles
            print(f"[SELECTORS] query={query_string} -> locale={loc!r}, timezone={tz!r}")
            self.assertEqual(loc, expect_locale, f"Locale attendue {expect_locale}, obtenu {loc}")
            self.assertEqual(tz, expect_tz, f"Timezone attendue {expect_tz}, obtenu {tz}")

    # 1) http://127.0.0.1:5000/?login_as=1 → FR + Europe/Paris → “Nous sommes le …”
    def test_login_as_1_fr_paris(self):
        self.run_case(
            {"login_as": "1"},
            expect_locale="fr",
            expect_tz="Europe/Paris",
            expect_phrase="Nous sommes le"
        )

    # 2) http://127.0.0.1:5000/?login_as=2 → EN + US/Central → “The current time is …”
    def test_login_as_2_en_us_central(self):
        self.run_case(
            {"login_as": "2"},
            expect_locale="en",
            expect_tz="US/Central",
            expect_phrase="The current time is"
        )

    # 3) http://127.0.0.1:5000/?locale=fr&timezone=Europe/Paris → FR + Paris.
    def test_force_fr_paris(self):
        self.run_case(
            {"locale": "fr", "timezone": "Europe/Paris"},
            expect_locale="fr",
            expect_tz="Europe/Paris",
            expect_phrase="Nous sommes le"
        )

    # 4) http://127.0.0.1:5000/?timezone=NotAZone → timezone ignorée → défaut UTC.
    # (locale: défaut "en" si pas de user ni param)
    def test_bad_timezone_fallback_utc(self):
        self.run_case(
            {"timezone": "NotAZone"},
            expect_locale="en",
            expect_tz="UTC",
            expect_phrase="The current time is"
        )


if __name__ == "__main__":
    unittest.main()
