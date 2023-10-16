#!/usr/bin/python3
"""unittest module for the classs state
"""

import os
import json
import unittest
from time import sleep
from models import storage
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_State(unittest.TestCase):
    """Testsuite for the state class which inherits
    from the BaseModel class"""

    def test_unique_id(self):
        """Method that ascertains the state have unique ids"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_id_type(self):
        """checking that the state id is a string"""
        self.assertEqual(str, type(State().id))

    def test_create_update_types(self):
        """checking that both created and updated at are type datetime"""
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

    def test_diff_state_creation(self):
        """Framework for checking two states created at different time"""
        s1 = State()
        sleep(1)
        s2 = State()
        self.assertLess(s1.created_at, s2.created_at)

    def test_diff_updated_at(self):
        """Checking two states updated at different times"""
        s1 = State()
        sleep(1)
        s2 = State()
        self.assertLess(s1.updated_at, s2.updated_at)

    def test_state_instance(self):
        """checking the instances of the class state"""
        s1 = State()
        self.assertIsInstance(s1, State)
        self.assertTrue(issubclass(type(s1), BaseModel))
        self.assertEqual(str(type(s1)), "<class 'models.state.State'>")


if __name__ == "__main__":
    unittest.main()
