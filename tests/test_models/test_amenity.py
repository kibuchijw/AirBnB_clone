#!/usr/bin/python3
"""unittest module for the class Amenity
"""

import os
import unittest
from time import sleep
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Amenity(unittest.TestCase):
    """Testsuite for the state class which inherits
    from the BaseModel class"""

    def test_amenity_unique_id(self):
        """Checking the different id of two amenity classess"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_id_type(self):
        """Framework checking that the Amenity id is a string"""
        self.assertEqual(str, type(Amenity().id))

    def test_create_update_types(self):
        """checking that both created_at and updated_at
        are of type datetime"""
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_diff_amenityclass_creation(self):
        """Checks that two Amenity classes created at different time"""
        a1 = Amenity()
        sleep(1)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_diff_updated_at_times(self):
        """Amenity class updated at different times"""
        a1 = Amenity()
        sleep(1)
        a2 = Amenity()
        self.assertLess(a1.updated_at, a2.updated_at)

    def test_Amenity_instance(self):
        """checking the instances of the class state"""
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)
        self.assertTrue(issubclass(type(a1), BaseModel))
        self.assertEqual(str(type(a1)), "<class 'models.amenity.Amenity'>")


if __name__ == "__main__":
    unittest.main()
