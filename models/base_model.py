#!/usr/bin/python3
"""
This is the base class for other ensuing classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    A base class that other classes will inherit from
    Contains common attributes and methods that will
    be duely inherited
    """

    def __init__(self, *args, **kwargs):
        """instance attribute initialization

        Arguments:
            *args: tuple containing all arguments
            **kwargs: dict containing all arguments by key/value

        """

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Method that returns human-readable string
        representation of instances"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates the attribute 'updated_at' to
        the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method returning the dictionary representation of an instance"""

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
