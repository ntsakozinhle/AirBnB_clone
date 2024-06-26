#!/usr/bin/python3
""" This module describes Review class """
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""


    @classmethod
    def all(cls):
        """Return a list of all User instances."""
        from models import stroage
        return list(storage.all(cls).values())
