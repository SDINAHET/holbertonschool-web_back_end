#!/usr/bin/env python3
"""
Defines FileStorage class for storing data in JSON file.
"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to objects"""
    __file_path = ".db_file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        json_dict = {
            k: v.__dict__ for k, v in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f, default=str)

    def reload(self):
        """Deserializes JSON file to __objects if it exists"""
        if not os.path.exists(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    FileStorage.__objects[key] = type('GenericObject', (), value)
        except Exception:
            pass

    def search(self, attr_dict={}):
        """Search for objects matching attributes in attr_dict"""
        result = []
        for obj in FileStorage.__objects.values():
            if all(getattr(obj, k, None) == v for k, v in attr_dict.items()):
                result.append(obj)
        return result
