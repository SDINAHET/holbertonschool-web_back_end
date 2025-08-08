import unittest
from app import app, AUTH

class TestGetResetPasswordToken(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # self.email = "unittest_reset17@example.com"
        # self.password = "pwd12345"
        self.email = "bob@bob.com"
        self.password = "MyPwdOfBob"
        try:
            AUTH.register_user(self.email, self.password)
        except ValueError:
            pass

    def test_missing_email(self):
        resp = self.client.post("/reset_password", data={})
        self.assertEqual(resp.status_code, 403)

    def test_unknown_email(self):
        resp = self.client.post("/reset_password", data={"email": "nope@example.com"})
        self.assertEqual(resp.status_code, 403)

    def test_known_email_generates_token(self):
        resp = self.client.post("/reset_password", data={"email": self.email})
        self.assertEqual(resp.status_code, 200)
        payload = resp.get_json()
        self.assertEqual(payload["email"], self.email)
        self.assertIn("reset_token", payload)
        self.assertTrue(payload["reset_token"])

        # (optionnel) vérifier la persistance du token
        user = AUTH._db.find_user_by(email=self.email)
        self.assertEqual(user.reset_token, payload["reset_token"])

if __name__ == "__main__":
    unittest.main()
