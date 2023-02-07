#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_user_inherits_from_base_model(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_user_has_attributes(self):
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        
    def test_user_attributes_have_correct_type(self):
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

if __name__ == '__main__':
    unittest.main()
