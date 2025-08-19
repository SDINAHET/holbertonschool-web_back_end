# 0x0B_redis_basic

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
service redis-server start
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d# cd 0x0B_redis_basic/
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# sudo apt-get -y install redis-server
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libarchive13 libdvdnav4 libdvdread8 libmujs1 libplacebo192 libsixel1
  libva-wayland2 mpv python3-brotli python3-mutagen python3-pycryptodome
  python3-pyxattr python3-websockets rtmpdump
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libjemalloc2 liblua5.1-0 liblzf1 lua-bitop lua-cjson redis-tools
Suggested packages:
  ruby-redis
The following NEW packages will be installed:
  libjemalloc2 liblua5.1-0 liblzf1 lua-bitop lua-cjson redis-server redis-tools
0 upgraded, 7 newly installed, 0 to remove and 56 not upgraded.
1 not fully installed or removed.
Need to get 1273 kB of archives.
After this operation, 5725 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjemalloc2 amd64 5.2.1-4ubuntu1 [240 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/universe amd64 liblua5.1-0 amd64 5.1.5-8.1build4 [99.9 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/universe amd64 liblzf1 amd64 3.6-3 [7444 B]
Get:4 http://archive.ubuntu.com/ubuntu jammy/universe amd64 lua-bitop amd64 1.0.2-5 [6680 B]
Get:5 http://archive.ubuntu.com/ubuntu jammy/universe amd64 lua-cjson amd64 2.1.0+dfsg-2.1 [17.4 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/universe amd64 redis-tools amd64 5:6.0.16-1ubuntu1 [856 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy/universe amd64 redis-server amd64 5:6.0.16-1ubuntu1 [45.9 kB]
Fetched 1273 kB in 2s (783 kB/s)
Selecting previously unselected package libjemalloc2:amd64.
(Reading database ... 114661 files and directories currently installed.)
Preparing to unpack .../0-libjemalloc2_5.2.1-4ubuntu1_amd64.deb ...
Unpacking libjemalloc2:amd64 (5.2.1-4ubuntu1) ...
Selecting previously unselected package liblua5.1-0:amd64.
Preparing to unpack .../1-liblua5.1-0_5.1.5-8.1build4_amd64.deb ...
Unpacking liblua5.1-0:amd64 (5.1.5-8.1build4) ...
Selecting previously unselected package liblzf1:amd64.
Preparing to unpack .../2-liblzf1_3.6-3_amd64.deb ...
Unpacking liblzf1:amd64 (3.6-3) ...
Selecting previously unselected package lua-bitop:amd64.
Preparing to unpack .../3-lua-bitop_1.0.2-5_amd64.deb ...
Unpacking lua-bitop:amd64 (1.0.2-5) ...
Selecting previously unselected package lua-cjson:amd64.
Preparing to unpack .../4-lua-cjson_2.1.0+dfsg-2.1_amd64.deb ...
Unpacking lua-cjson:amd64 (2.1.0+dfsg-2.1) ...
Selecting previously unselected package redis-tools.
Preparing to unpack .../5-redis-tools_5%3a6.0.16-1ubuntu1_amd64.deb ...
Unpacking redis-tools (5:6.0.16-1ubuntu1) ...
Selecting previously unselected package redis-server.
Preparing to unpack .../6-redis-server_5%3a6.0.16-1ubuntu1_amd64.deb ...
Unpacking redis-server (5:6.0.16-1ubuntu1) ...
Setting up libjemalloc2:amd64 (5.2.1-4ubuntu1) ...
Setting up lua-cjson:amd64 (2.1.0+dfsg-2.1) ...
Setting up liblzf1:amd64 (3.6-3) ...
Setting up lua-bitop:amd64 (1.0.2-5) ...
Setting up postfix (3.6.4-1ubuntu1.3) ...

Postfix (main.cf) configuration was not changed.  If you need to make changes,
edit /etc/postfix/main.cf (and others) as needed.  To view Postfix
configuration values, see postconf(1).

After modifying main.cf, be sure to run 'systemctl reload postfix'.

Running newaliases
newaliases: fatal: bad string length 0 < 1: mydomain =
dpkg: error processing package postfix (--configure):
 installed postfix package post-installation script subprocess returned error exit status 75
Setting up liblua5.1-0:amd64 (5.1.5-8.1build4) ...
Setting up redis-tools (5:6.0.16-1ubuntu1) ...
Setting up redis-server (5:6.0.16-1ubuntu1) ...
Created symlink /etc/systemd/system/redis.service → /lib/systemd/system/redis-server.service.
Created symlink /etc/systemd/system/multi-user.target.wants/redis-server.service → /lib/systemd/system/redis-server.service.
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.10) ...
Errors were encountered while processing:
 postfix
E: Sub-process /usr/bin/dpkg returned an error code (1)
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# pip3 install redis
Collecting redis
  Downloading redis-6.4.0-py3-none-any.whl (279 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 279.8/279.8 KB 1.3 MB/s eta 0:00:00
Collecting async-timeout>=4.0.3
  Downloading async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Installing collected packages: async-timeout, redis
Successfully installed async-timeout-5.0.1 redis-6.4.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# service redis-server start
```

## Task0

exercise.py
```python
#!/usr/bin/env python3
"""Basic Redis cache module.

Provides a `Cache` class that wraps a Redis client and exposes a `store`
method to persist primitive values (str, bytes, int, float) under a
randomly generated UUID key.
"""

from typing import Union
import uuid
import redis


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis under a random UUID key.

        Args:
            data: Value to store (str, bytes, int, or float).

        Returns:
            The UUID key (as a string) used to store the value.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 0_main.py
a15f6096-cf21-4da7-9264-a9a3fac8c3c7
b'hello'
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 -m unittest test0_exercise.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.013s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#
```

## Task1

exercise.py
```python
#!/usr/bin/env python3
"""Basic Redis cache module.

Task0
Provides a `Cache` class that wraps a Redis client and exposes a `store`
method to persist primitive values (str, bytes, int, float) under a
randomly generated UUID key.

Task1
Defines a Cache class to store values in Redis with random UUID keys and
retrieve them with optional conversion back to the original type.
"""

from typing import Union, Optional, Callable, TypeVar
import uuid
import redis

T = TypeVar("T")


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis under a random UUID key.

        Args:
            data: Value to store (str, bytes, int, or float).

        Returns:
            The UUID key (as a string) used to store the value.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[Union[bytes, T]]:
        """Retrieve a value from Redis and optionally convert it.

        Args:
            key: Redis key to fetch.
            fn: Optional callable that converts the raw bytes into the desired
                type (e.g., int, float, lambda d: d.decode("utf-8"), etc.).

        Returns:
            - None if the key does not exist (mirrors Redis.get behavior).
            - Raw bytes if `fn` is None and the key exists.
            - Converted value of type T if `fn` is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a value as UTF-8 string (or None if missing)."""
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data  # type: ignore[return-value]

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a value converted to int (or None if missing)."""
        data = self.get(key, fn=int)
        return data  # type: ignore[return-value]
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 1_main.py
Traceback (most recent call last):
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/0x0B_redis_basic/1_main.py", line 7, in <module>
    Cache = __import__('exercise').Cache
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/0x0B_redis_basic/exercise.py", line 18, in <module>
    T = TypeVar("T")
NameError: name 'TypeVar' is not defined
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 1_main.py
4d0d741f-db7b-414f-8f23-596a16253e45
b'hello'
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 -m unittest test1_exercise.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 1b_main.py
IN: b'foo' KEY: 66b554a6-3c16-47ea-80cf-a3702b14feca OUT: b'foo'
IN: 123 KEY: 7e9f4306-8fbc-4e85-b71d-4a2bbc2297ca OUT: 123
IN: bar KEY: d16f97a6-2915-413b-80a4-8d301c361096 OUT: bar
✅ Task 1 OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#
```

## Task2

exercise.py
```python
#!/usr/bin/env python3
"""Basic Redis cache module.

Task 0: store values under random UUID keys.
Task 1: retrieve values with optional conversion back to original types.
Task 2: count how many times Cache.store is called.
"""

from typing import Union, Optional, Callable, TypeVar
from functools import wraps
import uuid
import redis

T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called.

    Stores the count in Redis using the method's qualified name as key.
    """
    key = method.__qualname__  # <-- explicit binding for the checker

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # increment call count in Redis
        self._redis.incr(key)
        # call the original method
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls  # add task 2
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis under a random UUID key.

        Args:
            data: Value to store (str, bytes, int, or float).

        Returns:
            The UUID key (as a string) used to store the value.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[Union[bytes, T]]:
        """Retrieve a value from Redis and optionally convert it.

        Args:
            key: Redis key to fetch.
            fn: Optional callable that converts the raw bytes into the desired
                type (e.g., int, float, lambda d: d.decode("utf-8"), etc.).

        Returns:
            - None if the key does not exist (mirrors Redis.get behavior).
            - Raw bytes if `fn` is None and the key exists.
            - Converted value of type T if `fn` is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a value as UTF-8 string (or None if missing)."""
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data  # type: ignore[return-value]

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a value converted to int (or None if missing)."""
        data = self.get(key, fn=int)
        return data  # type: ignore[return-value]
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 2_main.py
b'1'
b'3'
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 -m unittest test2_exercise.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.011s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 -m unittest test2_exercise.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.017s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#
```

Ton décorateur count_calls fonctionne correctement :

- il incrémente à chaque appel,
- il redémarre bien à zéro après un flushdb,
- la valeur stockée est correcte,
- et la clé utilisée est bien Cache.store (via __qualname__).


## Task3

exercise.py
```python
#!/usr/bin/env python3
"""Basic Redis cache module.

Task 0: store values under random UUID keys.
Task 1: retrieve values with optional conversion back to original types.
Task 2: count how many times Cache.store is called.
"""

from typing import Union, Optional, Callable, TypeVar
from functools import wraps
import uuid
import redis

T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called.

    Stores the count in Redis using the method's qualified name as key.
    """
    key = method.__qualname__  # <-- explicit binding for the checker

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # increment call count in Redis
        self._redis.incr(key)
        # call the original method
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to record call history: inputs and outputs in Redis lists.

    Uses two keys:
      <qualname>:inputs  -> RPUSH of str(args)
      <qualname>:outputs -> RPUSH of the returned value (as bytes/str/number)
    """
    in_key = f"{method.__qualname__}:inputs"
    out_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # store inputs (normalize to string)
        self._redis.rpush(in_key, str(args))
        # call original method
        result = method(self, *args, **kwargs)
        # store output (Redis can store str/bytes/int/float directly)
        self._redis.rpush(out_key, result)
        return result

    return wrapper


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history  # Task 3
    @count_calls  # Task 2
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis under a random UUID key.

        Args:
            data: Value to store (str, bytes, int, or float).

        Returns:
            The UUID key (as a string) used to store the value.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[Union[bytes, T]]:
        """Retrieve a value from Redis and optionally convert it.

        Args:
            key: Redis key to fetch.
            fn: Optional callable that converts the raw bytes into the desired
                type (e.g., int, float, lambda d: d.decode("utf-8"), etc.).

        Returns:
            - None if the key does not exist (mirrors Redis.get behavior).
            - Raw bytes if `fn` is None and the key exists.
            - Converted value of type T if `fn` is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a value as UTF-8 string (or None if missing)."""
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data  # type: ignore[return-value]

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a value converted to int (or None if missing)."""
        data = self.get(key, fn=int)
        return data  # type: ignore[return-value]
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 3_main.py
ad8c7cab-5b57-4ff9-a771-996b2d65e6dc
457f5afa-0d03-4ae2-a64d-69b010d7b6e3
3ed443e0-9e3c-4475-9c89-f416fb6db363
inputs: [b"('first',)", b"('secont',)", b"('third',)"]
outputs: [b'ad8c7cab-5b57-4ff9-a771-996b2d65e6dc', b'457f5afa-0d03-4ae2-a64d-69b010d7b6e3', b'3ed443e0-9e3c-4475-9c89-f416fb6db363']
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 -m unittest test3_exercise.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.017s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#


d/0x0B_redis_basic# python3 -m unittest -v test3_exercise.py
test_count_calls_still_increments (test3_exercise.TestCallHistoryTask3) ... ok
test_history_is_empty_initially (test3_exercise.TestCallHistoryTask3) ... ok
test_inputs_and_outputs_recorded (test3_exercise.TestCallHistoryTask3) ... ok
test_mixed_types (test3_exercise.TestCallHistoryTask3) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.022s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#
```

## Task4

exercise.py
```python
#!/usr/bin/env python3
"""Basic Redis cache module.

Task 0: store values under random UUID keys.
Task 1: retrieve values with optional conversion back to original types.
Task 2: count how many times Cache.store is called.
"""

from typing import Union, Optional, Callable, TypeVar
from functools import wraps
import uuid
import redis

T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called.

    Stores the count in Redis using the method's qualified name as key.
    """
    key = method.__qualname__  # <-- explicit binding for the checker

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # increment call count in Redis
        self._redis.incr(key)
        # call the original method
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to record call history: inputs and outputs in Redis lists.

    Uses two keys:
      <qualname>:inputs  -> RPUSH of str(args)
      <qualname>:outputs -> RPUSH of the returned value (as bytes/str/number)
    """
    in_key = f"{method.__qualname__}:inputs"
    out_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # store inputs (normalize to string)
        self._redis.rpush(in_key, str(args))
        # call original method
        result = method(self, *args, **kwargs)
        # store output (Redis can store str/bytes/int/float directly)
        self._redis.rpush(out_key, result)
        return result

    return wrapper


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis under a random UUID key.

        Args:
            data: Value to store (str, bytes, int, or float).

        Returns:
            The UUID key (as a string) used to store the value.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[Union[bytes, T]]:
        """Retrieve a value from Redis and optionally convert it.

        Args:
            key: Redis key to fetch.
            fn: Optional callable that converts the raw bytes into the desired
                type (e.g., int, float, lambda d: d.decode("utf-8"), etc.).

        Returns:
            - None if the key does not exist (mirrors Redis.get behavior).
            - Raw bytes if `fn` is None and the key exists.
            - Converted value of type T if `fn` is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a value as UTF-8 string (or None if missing)."""
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data  # type: ignore[return-value]

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a value converted to int (or None if missing)."""
        data = self.get(key, fn=int)
        return data  # type: ignore[return-value]

def replay(method: Callable) -> None:
    """Print the call history of a bound method (inputs and outputs).

    Format:
        <qualname> was called N times:
        <qualname>(*<args>) -> <return>

    Uses the keys populated by `call_history` and the counter from `count_calls`.
    """
    # Méthode liée => accès au Redis de l'instance
    r = method.__self__._redis
    qual = method.__qualname__
    in_key = f"{qual}:inputs"
    out_key = f"{qual}:outputs"

    # Nombre d'appels (clé du compteur = qualname)
    n_calls = int(r.get(qual) or 0)
    print(f"{qual} was called {n_calls} times:")

    # Récupère les listes d’entrées/sorties et les affiche appariées
    inputs = r.lrange(in_key, 0, -1)
    outputs = r.lrange(out_key, 0, -1)

    for raw_in, raw_out in zip(inputs, outputs):
        in_txt = raw_in.decode("utf-8")
        out_txt = raw_out.decode("utf-8")
        print(f"{qual}(*{in_txt}) -> {out_txt}")

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 4_main.py
Traceback (most recent call last):
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/0x0B_redis_basic/4_main.py", line 2, in <module>
    from exercise import Cache, replay
ImportError: cannot import name 'replay' from 'exercise' (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/0x0B_redis_basic/exercise.py)
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 4_main.py
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 5e488947-87d2-4025-91c3-861631d737d9
Cache.store(*('bar',)) -> c85b5631-1fb0-4aa9-abfc-63fa4c4d3ba9
Cache.store(*(42,)) -> 03368470-395d-4509-902b-6c48f943cfb2
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic# python3 -m unittest -v test4_exercise.py
test_replay_output_format_and_values (test4_exercise.TestReplayTask4) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.010s

OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/0x0B_redis_basic#
```

## Task5

exercise.py
```python

```

```bash

```

## Task6

web.py
```python

```

```bash

```
