#!/usr/bin/python3
"""module for a review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """A class that represent AirBnB reviews"""

        place_id = ""
        user_id = ""
        text = ""
