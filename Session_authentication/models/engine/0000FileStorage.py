# #!/usr/bin/env python3
# """
# FileStorage module
# Serializes instances to a JSON file and deserializes back.
# """

# import json
# import os
# from datetime import datetime


# class FileStorage:
#     """Class that serializes and deserializes objects to/from JSON files."""

#     __objects = {}
#     __file_path = "file.json"

#     def all(self, cls=None):
#         """Returns all objects, or objects of a specific class."""
#         if cls is None:
#             return FileStorage.__objects
#         return {
#             key: obj for key, obj in FileStorage.__objects.items()
#             if isinstance(obj, cls)
#         }

#     def new(self, obj):
#         """Adds a new object to storage dictionary."""
#         key = f"{obj.__class__.__name__}.{obj.id}"
#         FileStorage.__objects[key] = obj

#     def save(self):
#         """Serializes __objects to the JSON file."""
#         to_store = {
#             key: obj.to_dict() for key, obj in FileStorage.__objects.items()
#         }
#         with open(FileStorage.__file_path, 'w') as f:
#             json.dump(to_store, f)

#     def reload(self):
#         """Deserializes the JSON file to __objects (if exists)."""
#         from models.user import User
#         from models.user_session import UserSession

#         classes = {
#             'User': User,
#             'UserSession': UserSession
#         }

#         if not os.path.isfile(FileStorage.__file_path):
#             return

#         try:
#             with open(FileStorage.__file_path, 'r') as f:
#                 data = json.load(f)

#             for key, obj_dict in data.items():
#                 cls_name = key.split('.')[0]
#                 cls = classes.get(cls_name)
#                 if cls:
#                     FileStorage.__objects[key] = cls(**obj_dict)
#         except Exception:
#             pass  # silent failure if file corrupt

#     def delete(self, obj=None):
#         """Deletes obj from __objects if it's inside."""
#         if obj is None:
#             return
#         key = f"{obj.__class__.__name__}.{obj.id}"
#         if key in FileStorage.__objects:
#             del FileStorage.__objects[key]

#     def search(self, filters={}):
#         """
#         Returns list of objects matching all key/value pairs in filters.
#         Example: filters = {"session_id": "abc", "user_id": "123"}
#         """
#         results = []
#         for obj in FileStorage.__objects.values():
#             match = all(getattr(obj, k, None) == v for k, v in filters.items())
#             if match:
#                 results.append(obj)
#         return results
