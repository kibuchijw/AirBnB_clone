#!/usr/bin/python3
"""Python unittest module for AirBnB review class
"""

import os
import unittest
from time import sleep
from models import storage
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Review(unittest.TestCase):
    """Testsuites for the instance of Review class"""

    def test_review_id(self):
        """Method for checking that each Review class is unique"""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_review_instance(self):
        """Framework for outlining the review instance"""
        r1 = Review()
        self.assertIsInstance(r1, Review)
        self.assertTrue(issubclass(type(r1), BaseModel))
        self.assertEqual(str(type(r1)), "<class 'models.review.Review'>")

    def test_review_id_type(self):
        """checks that review id is a string"""
        self.assertEqual(str, type(Review().id))

    def test_create_update_types(self):
        """checking that created and updated review classes
        are type datetime"""
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))

    def test_diff_review_creation(self):
        """Method that checks two review created at different time"""
        r1 = Review()
        sleep(1)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_diff_updated_at(self):
        """Method Checking two review updated at different times"""
        r1 = Review()
        sleep(1)
        r2 = Review()
        self.assertLess(r1.updated_at, r2.updated_at)

    def test_unused_args(self):
        """Framework used when no arguments are passed to review class"""
        r1 = Review(None)
        self.assertNotIn(None, r1.__dict__.values())


if __name__ == "__main__":
    unittest.main()
