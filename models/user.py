#!/usr/bin/python3
""" This module defines the User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all User instances."""
        from models import storage
        return list(storage.all(cls).values())
