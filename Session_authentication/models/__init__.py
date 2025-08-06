# #!/usr/bin/env python3
# """
# Initializes the storage engine
# """

# from models.engine.file_storage import FileStorage

# storage = FileStorage()
# storage.reload()
from models.engine.file_storage import FileStorage
from models.user import User
from models.user_session import UserSession

storage = FileStorage()
storage.reload()
