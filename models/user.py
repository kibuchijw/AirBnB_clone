#!/usr/bin/python3
"""module for a class user which is a subclass of Basemodel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User which inherits from BaseModel
    Contains attributes and features of a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
