#!/usr/bin/python3
"""A module for the class Filestorage """

import json
import os


class FileStorage:
    """ A class that serializes instances to JSON and deserializes
    JSON files back to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that returns __object dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Method that adds new objects to the __objects dictionary
        objects are stored by their class name and ID"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Method that serializes the contents of FileStorage.__objects dict
        into JSON file specified by FileStorage.__file_path """
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def classes(self):
        """Methd that Returns a dictionary of valid classes and their
        appropriate references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Method that deserializes data from JSON file, reconstructs objects
        then store them back to __objects dictionary"""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
                        # Update classes dictionary with valid class names
                        FileStorage.classes[class_name] = BaseModel
            except FileNotFoundError:
                pass
