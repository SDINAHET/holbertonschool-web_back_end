#!/usr/bin/env python3
"""Setup test user for Session authentication"""

from models.user import User

user_email = "bobsession@hbtn.io"
user_password = "fake pwd"

# Create the user
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Session"
user.password = user_password
user.save()

print("User created:")
print(user.id)
