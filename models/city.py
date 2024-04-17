#!/usr/bin/python3
""" This module describes City class """
from models.base_model import BaseModel

class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""

    @classmethod
    def all(cls):
        """Return a list of all User instances."""
        from models import stroage
        return list(storage.all(cls).values())
