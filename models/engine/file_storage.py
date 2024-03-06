#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file
    to instance."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serializable_dict = {}
        for key, value in self.__objects.items():
            serializable_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(serializable_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key]['__class__'] = class_name
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
