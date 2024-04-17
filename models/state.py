#!/usr/bin/python3
"""This module describes the State class"""
from models.base_model import BaseModel

class State(BaseModel):
    """ State class """
    name = ""

    @classmethod
    def all(cls):
        """Return a list of all User instances."""
        from models import stroage
        return list(storage.all(cls).values())
