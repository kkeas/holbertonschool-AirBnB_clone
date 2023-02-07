#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_state_inherits_from_base_model(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_state_has_name_attribute(self):
        self.assertTrue(hasattr(self.state, "name"))
        
    def test_state_name_attribute_has_correct_type(self):
        self.assertIsInstance(self.state.name, str)

if __name__ == '__main__':
    unittest.main()
