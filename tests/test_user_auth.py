import unittest
from patient_management.utils.user_auth import authenticate_user

class TestUserAuth(unittest.TestCase):
    def test_valid_user(self):
        self.assertTrue(authenticate_user('valid_username', 'valid_password'))

    def test_invalid_user(self):
        self.assertFalse(authenticate_user('invalid_username', 'invalid_password'))

if __name__ == "__main__":
    unittest.main()