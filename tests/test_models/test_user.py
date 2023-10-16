#!/usr/bin/python3
"""unittest module for AirBnB User's class
"""

import os
import unittest
from time import sleep
from models import storage
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """Testsuites for class User which inherits from
    BaseModel and rep all users of the AirBnB"""

    def test_user_instantation(self):
        """checking the instances of the class state"""
        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertTrue(issubclass(type(u1), BaseModel))
        self.assertEqual(str(type(u1)), "<class 'models.user.User'>")

    def test_user_unique_id(self):
        """Method that checks that users have unique ids"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_id_type(self):
        """checking that user's id is a string"""
        self.assertEqual(str, type(User().id))

    def test_create_update_types(self):
        """checks that created and updated at are type datetime"""
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))

    def test_different_user_creation(self):
        """Framework for checking 2 users created at different time"""
        u1 = User()
        sleep(1)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_diff_updated_at(self):
        """Checking two states updated at different times"""
        u1 = User()
        sleep(1)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_email_is_public_str(self):
        """Framework to check the type of users email"""
        self.assertEqual(str, type(User.email))

    def test_password_str(self):
        """checking the users passwors of of type string"""
        self.assertEqual(str, type(User.password))

    def test_firstname_str(self):
        """checking the users f. name is public"""
        self.assertEqual(str, type(User.first_name))

    def test_lastname_str(self):
        """Method that checks the user's last name is public"""
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
