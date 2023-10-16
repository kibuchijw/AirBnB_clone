#!/usr/bin/python3
"""Test module for the class Place
"""

import os
import unittest
from time import sleep
from models import storage
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Place(unittest.TestCase):
    """Unittest testsuite for AirBnB place class which inherits
    from the BaseModel"""

    def test_place_instantation(self):
        """checking the instances of the class state"""
        p1 = Place()
        self.assertIsInstance(p1, Place)
        self.assertTrue(issubclass(type(p1), BaseModel))
        self.assertEqual(str(type(p1)), "<class 'models.place.Place'>")

    def test_unique_place_id(self):
        """Method that ascertains the state have unique ids"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_id_type(self):
        """checking that the state id is a string"""
        self.assertEqual(str, type(Place().id))

    def test_create_update_types(self):
        """checking that both created and updated at are type datetime"""
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))

    def test_diff_placeclass_creation(self):
        """Framework for checking two states created at different time"""
        p1 = Place()
        sleep(1)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_diff_place_updated_at(self):
        """Checking two states updated at different times"""
        p1 = Place()
        sleep(1)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)


if __name__ == "__main__":
    unittest.main()
