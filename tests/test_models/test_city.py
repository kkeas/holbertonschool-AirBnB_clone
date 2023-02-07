#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_city_inherits_from_base_model(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_city_has_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        
    def test_city_attributes_have_correct_type(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

if __name__ == '__main__':
    unittest.main()
