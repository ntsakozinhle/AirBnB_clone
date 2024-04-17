#!/usr/bin/python3
""" This module describes Amenity class """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity class """
    name = ""

    @classmethod
    def all(cls):
        """Return a list of all User instances."""
        from models import stroage
        return list(storage.all(cls).values())
