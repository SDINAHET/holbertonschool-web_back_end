user_authentication_service

Task0
app.py
```python

```

```bash

```

Task1
db.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
```

```bash

```

Task2
db.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")
```

```bash

```

Task3
db.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")
```

```bash

```

Task4
auth.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from auth import _hash_password

print(_hash_password("Hello Holberton"))
```

```bash

```

Task5
auth.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from auth import _hash_password

print(_hash_password("Hello Holberton"))
```

```bash

```


Task6
app.py
```python

```



```bash

```

Task7
app.py
```python

```

```bash

```

```bash

```

Task8
auth.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))

```

```bash

```

Task9
auth.py
```python

```

```bash

```

Task10
auth.py
```python

```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))
```

```bash

```

Task11
app.py
```python

```

```bash

```

Task12
auth.py
```python

```

```bash

```

Task13
auth.py
```python

```

```bash

```

Task14
app.py
```python

```

```bash

```


Task15
app.py
```python

```

```bash

```

Task16
auth.py
```python

```

```bash

```


Task17
app.py
```python

```

```bash

```

Task18
auth.py
```python

```

```bash

```


Task19
main.py
```python

```

```bash

```




Taskx
app.py
```python

```

```bash

```
