#!/usr/bin/python3
"""Unittest module for the class amenity"""

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Test suites for the class amenity"""

    def test_amenity_instance(self):
        """checking the instantation of the class amenity"""
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)
        self.assertTrue(issubclass(type(a1), BaseModel))
        self.assertEqual(str(type(a1)), "<class 'models.amenity.Amenity'>")

    def test_id_type(self):
        """checking that the state id is a string"""
        self.assertEqual(str, type(Amenity().id))

    def test_unique_id(self):
        """Method that ascertains the state have unique ids"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_diff_state_creation(self):
        """Framework for checking two states created at different time"""
        a1 = Amenity()
        sleep(1)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_diff_updated_at(self):
        """Checking two states updated at different times"""
        a1 = Amenity()
        sleep(1)
        a2 = Amenity()
        self.assertLess(a1.updated_at, a2.updated_at)

    def test_create_update_types(self):
        """Framework to check that both created_at and updated_at
        are type datetime"""
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))


if __name__ == "__main__":
    unittest.main()
