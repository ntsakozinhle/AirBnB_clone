#!/usr/bin/python3
"""This module initializes the application's storage system."""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
