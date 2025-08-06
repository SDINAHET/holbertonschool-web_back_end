#!/usr/bin/env python3
"""
Initializes the storage engine
"""

# from models.engine.file_storage import FileStorage

# storage = FileStorage()
# storage.reload()
from models.engine.file_storage import FileStorage
from models.user import User
from models.user_session import UserSession

classes = {
    "User": User,
    "UserSession": UserSession,
}

User.load_from_file()
UserSession.load_from_file()

storage = FileStorage()
storage.reload()
