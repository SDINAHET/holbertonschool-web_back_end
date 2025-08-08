import unittest
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

class TestUpdatePassword(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()
        self.email = "unittest_update18@example.com"
        self.old_pwd = "oldpwd"
        self.new_pwd = "newpwd"
        try:
            self.auth.register_user(self.email, self.old_pwd)
        except ValueError:
            pass

    def test_update_password_ok(self):
        token = self.auth.get_reset_password_token(self.email)
        self.auth.update_password(token, self.new_pwd)
        self.assertTrue(self.auth.valid_login(self.email, self.new_pwd))
        self.assertFalse(self.auth.valid_login(self.email, self.old_pwd))
        # token cleared
        with self.assertRaises(ValueError):
            self.auth.update_password(token, "again")

    def test_update_password_bad_token(self):
        with self.assertRaises(ValueError):
            self.auth.update_password("not-a-real-token", self.new_pwd)

if __name__ == "__main__":
    unittest.main()
