import unittest
from app import app, AUTH

class TestProfileEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.email = "bob@bob.com"
        self.password = "mySuperPwd"
        try:
            AUTH.register_user(self.email, self.password)
        except ValueError:
            pass
        self.assertTrue(AUTH.valid_login(self.email, self.password))
        self.sid = AUTH.create_session(self.email)
        self.assertIsNotNone(self.sid)

    def test_profile_without_cookie(self):
        resp = self.client.get("/profile")
        self.assertEqual(resp.status_code, 403)

    def test_profile_with_cookie(self):
        self.client.set_cookie("session_id", self.sid)  # Flask 3.x
        resp = self.client.get("/profile")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {"email": self.email})

if __name__ == "__main__":
    unittest.main()
