import unittest
from app.services import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()

    def test_create_user(self):
        user = self.user_service.create_user("john_doe", "password123", True)
        self.assertEqual(user.username, "john_doe")
        self.assertTrue(user.check_password("password123"))

    def test_update_user_password(self):
        self.user_service.create_user("john_doe", "password123", True)
        self.user_service.update_user("john_doe", password="new_password456")
        user = self.user_service.read_user("john_doe")
        self.assertTrue(user.check_password("new_password456"))

    def test_create_user_empty_username(self):
        with self.assertRaises(ValueError):
            self.user_service.create_user("", "password123", True)

    def test_create_user_empty_password(self):
        with self.assertRaises(ValueError):
            self.user_service.create_user("john_doe", "", True)

    def test_create_user_short_password(self):
        with self.assertRaises(ValueError):
            self.user_service.create_user("john_doe", "short", True)

    def test_read_user_empty_username(self):
        with self.assertRaises(ValueError):
            self.user_service.read_user("")

    def test_update_user_nonexistent(self):
        with self.assertRaises(ValueError):
            self.user_service.update_user("nonexistent_user", active=False)

    def test_delete_user_empty_username(self):
        with self.assertRaises(ValueError):
            self.user_service.delete_user("")

    def test_delete_user_nonexistent(self):
        with self.assertRaises(ValueError):
            self.user_service.delete_user("nonexistent_user")

if __name__ == "__main__":
    unittest.main()
