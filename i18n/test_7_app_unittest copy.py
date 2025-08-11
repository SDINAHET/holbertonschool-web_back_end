# i18n/test_7_app_unittest.py
import unittest
import importlib.util
from pathlib import Path

# Charge dynamiquement le module 7-app.py sous le nom "app7"
APP_PATH = Path(__file__).with_name("7-app.py")
spec = importlib.util.spec_from_file_location("app7", APP_PATH)
app7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app7)  # type: ignore[attr-defined]

app = app7.app  # instance Flask


class LocaleTimezoneTestCase(unittest.TestCase):
    """Vérifie l'ordre de priorité: URL > user > header > default, et la timezone."""

    def run_case(self, query_string, expected_locale, expected_tz):
        """Crée un contexte de requête, exécute before_request, puis vérifie locale/tz."""
        with app.test_request_context(path="/", query_string=query_string):
            # Déclenche les before_request (ex: g.user)
            app.preprocess_request()
            loc = app7.get_locale()
            tz = app7.get_timezone()
            self.assertEqual(
                loc, expected_locale,
                f"Locale: got {loc!r}, expected {expected_locale!r} for {query_string}"
            )
            self.assertEqual(
                tz, expected_tz,
                f"Timezone: got {tz!r}, expected {expected_tz!r} for {query_string}"
            )

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
