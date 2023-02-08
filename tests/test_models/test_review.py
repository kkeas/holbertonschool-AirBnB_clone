#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review



class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_review_inherits_from_base_model(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_review_has_attributes(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
         
    def test_review_attributes_have_correct_type(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        
    
    def test_init(self):
        self.assertEqual(Review, type(Review()))

    def test_review_pid(self):
        villager_noise = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", villager_noise.__dict__)

    def test_review_uid(self):
        villager_noise = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Review()))
        self.assertNotIn("user_id", villager_noise.__dict__)


if __name__ == '__main__':
    unittest.main()
