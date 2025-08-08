import unittest
from app import app, AUTH

class TestLogoutEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.email = "unitlogout@example.com"
        self.password = "pwd12345"
        try:
            AUTH.register_user(self.email, self.password)
        except ValueError:
            pass
        # login + session
        self.assertTrue(AUTH.valid_login(self.email, self.password))
        self.sid = AUTH.create_session(self.email)
        self.assertIsNotNone(self.sid)

    def test_logout_without_cookie(self):
        resp = self.client.delete("/sessions")
        self.assertEqual(resp.status_code, 403)

    def test_logout_with_cookie(self):
        # Poser le cookie dans le client Flask 3.x
        self.client.set_cookie("session_id", self.sid)  # Flask 3.x

        # Appeler DELETE /sessions
        resp = self.client.delete("/sessions")
        self.assertIn(resp.status_code, (301, 302))
        self.assertIn(resp.headers.get("Location"), ("/", "http://localhost/"))

        # Vérifier que la session est détruite
        self.assertIsNone(AUTH.get_user_from_session_id(self.sid))


if __name__ == "__main__":
    unittest.main()
