user_authentication_service

```python
python3 -m venv venv
```

```python
pip3 install bcrypt
pip3 install sqlalchemy

```

```bash
source venv/bin/activate
pip install -r requirements.txt

pip install sqlalchemy bcrypt
deactivate
```

Task0
user.py
```python
#!/usr/bin/env python3
"""
This module defines the User model for authentication.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
```

main.py
```python
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
```


```bash
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service# python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
```

Task1
db.py
```python
#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User  # 👈 N'oublie pas d'importer User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user
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
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service# python3 main.py
2025-08-07 15:45:01,878 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 15:45:01,879 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("users")
2025-08-07 15:45:01,879 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-08-07 15:45:01,885 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("users")
2025-08-07 15:45:01,885 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-08-07 15:45:01,886 INFO sqlalchemy.engine.Engine COMMIT
2025-08-07 15:45:01,886 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 15:45:01,886 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("users")
2025-08-07 15:45:01,886 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-08-07 15:45:01,890 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("users")
2025-08-07 15:45:01,890 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-08-07 15:45:01,891 INFO sqlalchemy.engine.Engine
CREATE TABLE users (
        id INTEGER NOT NULL,
        email VARCHAR(250) NOT NULL,
        hashed_password VARCHAR(250) NOT NULL,
        session_id VARCHAR(250),
        reset_token VARCHAR(250),
        PRIMARY KEY (id)
)


2025-08-07 15:45:01,892 INFO sqlalchemy.engine.Engine [no key 0.00028s] ()
2025-08-07 15:45:01,923 INFO sqlalchemy.engine.Engine COMMIT
2025-08-07 15:45:01,928 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 15:45:01,930 INFO sqlalchemy.engine.Engine INSERT INTO users (email, hashed_password, session_id, reset_token) VALUES (?, ?, ?, ?)
2025-08-07 15:45:01,931 INFO sqlalchemy.engine.Engine [generated in 0.00039s] ('test@test.com', 'SuperHashedPwd', None, None)
2025-08-07 15:45:01,940 INFO sqlalchemy.engine.Engine COMMIT
2025-08-07 15:45:01,957 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 15:45:01,961 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.email AS users_email, users.hashed_password AS users_hashed_password, users.session_id AS users_session_id, users.reset_token AS users_reset_token
FROM users
WHERE users.id = ?
2025-08-07 15:45:01,961 INFO sqlalchemy.engine.Engine [generated in 0.00042s] (1,)
1
2025-08-07 15:45:01,965 INFO sqlalchemy.engine.Engine INSERT INTO users (email, hashed_password, session_id, reset_token) VALUES (?, ?, ?, ?)
2025-08-07 15:45:01,965 INFO sqlalchemy.engine.Engine [cached since 0.0352s ago] ('test1@test.com', 'SuperHashedPwd1', None, None)
2025-08-07 15:45:01,975 INFO sqlalchemy.engine.Engine COMMIT
2025-08-07 15:45:01,991 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 15:45:01,991 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.email AS users_email, users.hashed_password AS users_hashed_password, users.session_id AS users_session_id, users.reset_token AS users_reset_token
FROM users
WHERE users.id = ?
2025-08-07 15:45:01,992 INFO sqlalchemy.engine.Engine [cached since 0.03122s ago] (2,)
2
```

db.py
```python
#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User  # 👈 N'oublie pas d'importer User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user
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
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service# python3 main.py
1
2
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service#
```

Task2
db.py
```python
#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound  # ✅ CORRECT
from sqlalchemy.exc import InvalidRequestError  # ✅ Déjà utilisé


from user import Base, User  # 👈 N'oublie pas d'importer User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the given filters.

        Args:
            **kwargs: fields to filter by.

        Returns:
            User: the user found.

        Raises:
            NoResultFound: if no user matches.
            InvalidRequestError: if an invalid field is provided.
        """
        if not kwargs:
            raise InvalidRequestError

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except Exception as e:
            raise InvalidRequestError from e

        if user is None:
            raise NoResultFound

        return user
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
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service# python3 main.py
1
1
Not found
Invalid
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service#
```

Task3
db.py
```python
#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound  # ✅ CORRECT
from sqlalchemy.exc import InvalidRequestError  # ✅ Déjà utilisé


from user import Base, User  # 👈 N'oublie pas d'importer User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the given filters.

        Args:
            **kwargs: fields to filter by.

        Returns:
            User: the user found.

        Raises:
            NoResultFound: if no user matches.
            InvalidRequestError: if an invalid field is provided.
        """
        if not kwargs:
            raise InvalidRequestError

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except Exception as e:
            raise InvalidRequestError from e

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Met à jour un utilisateur puis commit.
        Lève ValueError si un champ est invalide.
        """
        # récupère l'utilisateur (lèvera NoResultFound si introuvable)
        user = self.find_user_by(id=user_id)

        # applique les mises à jour demandées
        for field, value in kwargs.items():
            if not hasattr(user, field):
                raise ValueError(f"Invalid field: {field}")
            setattr(user, field, value)

        # enregistre en base
        self._session.commit()
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
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service# python3 main.py
1
Password updated
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service#
```

Task4
auth.py
```python
#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Retourne un hash bcrypt (bytes) du mot de passe fourni."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

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
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service# python3 main.py
b'$2b$12$DyuwYcoqvO5c9D9V8rmFS.IYKIuQtuaWgJwhsBZIWmJEbM/2l.Lti'
(venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbe
rtonschool-web_back_end/user_authentication_service#
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
