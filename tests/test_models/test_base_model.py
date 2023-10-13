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

    def test_base_model_type(self):
        """Framework to test the type of the base model"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_updates_as(self):
        """Framework to check the different update time"""
        base4 = BaseModel()
        var1 = base4.updated_at
        sleep(1)
        base4.save()
        var2 = base4.updated_at
        self.assertNotEqual(var1, var2)

    def test_attributes(self):
        """Framework for testing default attributes of the class"""
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertIsNotNone(self.base.id)

    def test_kwargs(self):
        """Testing assignment of custom attributes"""

        base_model = BaseModel(name="New Model", value=50)
        self.assertEqual(base_model.name, "New Model")
        self.assertEqual(base_model.value, 50)

    def test_None_kwargs(self):
        """check to see the behavior when no kwargs are passed"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_stringrepresentation(self):
        """Testing str representation of instance"""
        b = self.base
        r = f"[{type(b).__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(str(self.base), r)

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

    def test_id(self):
        """Test to check that id is a valid UUID"""
        base3 = BaseModel()
        try:
            uuid.UUID(base3.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")


class Test_BaseModel_to_dict(unittest.TestCase):
    """Test suites on the to_dict method of the BaseModel class"""

    def setUp(self):
        """Frameworking creating a BaseModel instance for testing"""
        b1 = BaseModel()

    def test_type_to_dict(self):
        """checking the type of dictionary"""
        b1 = BaseModel()
        self.assertTrue(dict, type(b1.to_dict()))

    def test_dictionary_representation(self):
        """Framework for the dictionary output of the BaseModel"""
        b1 = BaseModel()
        my_dict = b1.to_dict()
        self.assertEqual(my_dict["id"], b1.id)
        self.assertEqual(my_dict["created_at"], b1.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], b1.updated_at.isoformat())
        self.assertEqual(my_dict["__class__"], type(b1).__name__)

    def test_to_dict_output(self):
        """Framework for testing the dictionary actual output"""
        b1 = BaseModel()
        time = datetime.today()
        b1.id = "45667"
        b1.created_at = b1.updated_at = time
        obj_dict = {
                "id": "45667",
                '__class__': 'BaseModel',
                'created_at': time.isoformat(),
                'updated_at': time.isoformat()
                }
        self.assertDictEqual(b1.to_dict(), obj_dict)

    def test_to_dict_empty(self):
        """Checking to_dict output with no args passed"""
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.to_dict(None)

    def test_addedattr_to_dict(self):
        """Framework to check added attributes"""
        b1 = BaseModel()
        b1.name = "Koech"
        b1.number = 2
        self.assertIn("name", b1.to_dict())
        self.assertIn("number", b1.to_dict())

    def test_to_dict(self):
        """check the return type of the to_dict method when
        called on an instance of the BaseModel class"""
        my_model = BaseModel()
        to_dict = my_model.to_dict
        self.assertNotEqual(type(my_model), type(to_dict))


if __name__ == "__main__":
    unittest.main()
