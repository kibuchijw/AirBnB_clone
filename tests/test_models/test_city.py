#!/usr/bin/python3
"""A unittest python module for the class City"""

import os
import json
import unittest
import models
from time import sleep
from models import storage
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """A class with test suites for city.py"""

    def test_city_instance(self):
        """Framework for testing instatation of the class city"""
        c1 = City()
        self.assertIsInstance(c1, City)
        self.assertTrue(issubclass(type(c1), BaseModel))
        self.assertEqual(str(type(c1)), "<class 'models.city.City'>")

    def test_newinstance_stored(self):
        """checking that values of city instance are stored well"""
        self.assertIn(City(), models.storage.all().values())

    def test_storing_city(self):
        """putting city into a dictionary"""
        self.assertTrue(dict, type(City().to_dict()))

    def test_twodiff_cities(self):
        """checking two different cities with diff id"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)


if __name__ == "__main__":
    unittest.main()
