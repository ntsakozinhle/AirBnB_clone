#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User

classes = {
        'BaseModel': BaseModel,
        'User': User,
}

class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file
    to instance."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serializable_objs = {}
        for key, value in FileStorage.__objects.items():
            serializable_objs[key] = value.to_dict()
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(serializable_objs, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = classes[class_name]
                    instance = cls(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
