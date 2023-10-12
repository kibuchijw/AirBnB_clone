#!/usr/bin/python
"""A unittest module for the class BaseModel"""

import uuid
import json
import unittest
from time import sleep
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_BaseModel(unittest.TestCase):
    """Test suites for the base class BaseModel"""

    def setUp(self):
        """Frameworking creating a BaseModel instance for testing"""
        self.base = BaseModel()

    def test_attributes(self):
        """Framework for testing default attributes of the class"""

        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertIsNotNone(self.base.id)

    def test_kwargs(self):
        """Testing assignment of custom attributes"""

        base_model = BaseModel(name= "New Model", value=50)
        self.assertEqual(base_model.name, "New Model")
        self.assertEqual(base_model.value, 50)

    def test_stringrepresentation(self):
        """Testing str representation of instance"""
        resul = f"[{type(self.base).__name__}] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(str(self.base), resul)

    def test_dictionary_representation(self):
        """Framework for the dictionary output of the BaseModel"""
        my_dict = self.base.to_dict()
        self.assertEqual(my_dict["id"], self.base.id)
        self.assertEqual(my_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], self.base.updated_at.isoformat())
        self.assertEqual(my_dict["__class__"], type(self.base).__name__)


    def test_id_is_string(self):
        """Framework to check that id is string based on the uuid"""
        self.assertEqual(str, type(BaseModel().id))

    def test_create_at_type(self):
        """Framework to check that create of datetime format"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        """Testing to see if updated at is datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_id(self):
        """Framework to test that each instance has unique id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_createtimes(self):
        """Test earlier and later class creations"""
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_updatetimes(self):
        """Test order of updates"""
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)











if __name__ == "__main__":
    unittest.main()





