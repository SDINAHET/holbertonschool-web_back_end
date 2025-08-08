import unittest
from auth import Auth

class TestResetToken(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()
        self.email = "bob@bob.com"
        self.password = "MyPwdOfBob"
        try:
            self.auth.register_user(self.email, self.password)
        except ValueError:
            pass

    def test_get_reset_password_token_ok(self):
        token = self.auth.get_reset_password_token(self.email)
        self.assertIsInstance(token, str)
        self.assertTrue(len(token) > 0)
        # token should be persisted in DB
        user = self.auth._db.find_user_by(email=self.email)  # or via your public getter if you have one
        self.assertEqual(user.reset_token, token)

    def test_get_reset_password_token_unknown_email(self):
        with self.assertRaises(ValueError):
            self.auth.get_reset_password_token("unknown@example.com")

if __name__ == "__main__":
    unittest.main()
