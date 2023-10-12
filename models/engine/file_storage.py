#!/usr/bin/python3
"""A module for the class Filestorage """

import json
import os


class FileStorage:
    """ A class that serializes instances to JSON and deserializes
    JSON files back to instances """

    __file_path = "file.json"
    __objects = {}
    # Add a classes dictionary to store valid class names
    classes = {}

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


    def reload(self):
        """Method that deserializes data from JSON file, reconstructs objects
        then store them back to __objects dictionary"""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    from models.base_model import BaseModel
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
                        # Update classes dictionary with valid class names
                        FileStorage.classes[class_name] = BaseModel
            except FileNotFoundError:
                pass
