i18n

```bash
mkdir -p templates translations/en/LC_MESSAGES translations/fr/LC_MESSAGES
touch 0-app.py templates/0-index.html \
1-app.py templates/1-index.html \
2-app.py templates/2-index.html \
3-app.py babel.cfg templates/3-index.html \
translations/en/LC_MESSAGES/messages.po \
translations/fr/LC_MESSAGES/messages.po \
translations/en/LC_MESSAGES/messages.mo \
translations/fr/LC_MESSAGES/messages.mo \
4-app.py templates/4-index.html \
5-app.py templates/5-index.html \
6-app.py templates/6-index.html \
7-app.py templates/7-index.html \
app.py templates/index.html \
translations/en/LC_MESSAGES/messages.po \
translations/fr/LC_MESSAGES/messages.po
```
```bash
python3 -m venv .venv
source .venv/bin/activate
deactivate
pip freeze > requirements.txt
```

# Task0
## 0. Basic Flask app

0-app.py
```python
#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render the index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

templates/0-index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Holberton</title>
</head>
<body>
    <h1>Hello world</h1>
</body>
</html>
```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n# python3 0-app.py
 * Serving Flask app '0-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Aug/2025 22:00:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Aug/2025 22:00:16] "GET /favicon.ico HTTP/1.1" 404 -

```

# Task1
## 1. Basic Babel setup

1-app.py
```python

```

templates/1-index.html
```html

```

```bash

```


# Task2
## 2. Get locale from request

2-app.py
```python

```

templates/2-index.html
```html

```

```bash

```

# Task3
## 3. Parametrize templates

3-app.py
```python

```

templates/3-index.html
```html

```

```bash

```

# Task4
## 4. Force locale with URL parameter

4-app.py
```python

```

templates/4-index.html
```html

```

```bash

```


# Task5
## 5. Mock logging in

5-app.py
```python

```

templates/5-index.html
```html

```

```bash

```


# Task6
## 6. Use user locale

6-app.py
```python

```

templates/6-index.html
```html

```

```bash

```


# Task7
## 7. Infer appropriate time zone

7-app.py
```python

```

templates/7-index.html
```html

```

```bash

```

# Task8
## 8. Display the current time

8-app.py
```python

```

templates/8-index.html
```html

```

```bash

```



