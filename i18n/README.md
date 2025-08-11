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

Install the Babel Flask extension:
```bash
$ pip3 install flask_babel
```

1-app.py
```python
#!/usr/bin/env python3
"""
Basic Flask app with Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for Babel and available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """Render the index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

templates/1-index.html
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
b_back_end/i18n# python3 1-app.py
 * Serving Flask app '1-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Aug/2025 22:22:40] "GET / HTTP/1.1" 200 -

```


# Task2
## 2. Get locale from request

2-app.py
```python
#!/usr/bin/env python3
"""
Flask app: detect locale from request using Flask-Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Babel and available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()  # create Babel instance without binding


def get_locale():
    """Select the best match between client's Accept-Language and supported LANGUAGES."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Initialize Babel with our locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render the index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

templates/2-index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Welcome to Holberton</title>
</head>
<body>
  <h1>Hello world</h1>
</body>
</html>

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n# python3 2-app.py
 * Serving Flask app '2-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Aug/2025 22:26:24] "GET / HTTP/1.1" 200 -


```

# Task3
## 3. Parametrize templates

3-app.py
```python
#!/usr/bin/env python3
"""
Flask app: parametrized templates with Flask-Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def index():
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

templates/3-index.html
```html
<!DOCTYPE html>
<html lang="{{ get_locale() or 'en' }}">
<head>
  <meta charset="UTF-8" />
  <title>{{ _('home_title') }}</title>
</head>
<body>
  <h1>{{ _('home_header') }}</h1>
</body>
</html>

```

générer avec
```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
pybabel compile -d translations
```

translations/en/LC_MESSAGES/messages.po
```bash
# English translations for PROJECT.
# Copyright (C) 2025 ORGANIZATION
# This file is distributed under the same license as the PROJECT project.
# FIRST AUTHOR <EMAIL@ADDRESS>, 2025.
#
msgid ""
msgstr ""
"Project-Id-Version: PROJECT VERSION\n"
"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
"POT-Creation-Date: 2025-08-11 22:45+0200\n"
"PO-Revision-Date: 2025-08-11 22:37+0200\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language: en\n"
"Language-Team: en <LL@li.org>\n"
"Plural-Forms: nplurals=2; plural=(n != 1)\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: Babel 2.8.0\n"

#: templates/3-index.html:5
msgid "home_title"
msgstr "Welcome to Holberton"

#: templates/3-index.html:8
msgid "home_header"
msgstr "Hello world!"


```

translations/fr/LC_MESSAGES/messages.po
```bash
# French translations for PROJECT.
# Copyright (C) 2025 ORGANIZATION
# This file is distributed under the same license as the PROJECT project.
# FIRST AUTHOR <EMAIL@ADDRESS>, 2025.
#
msgid ""
msgstr ""
"Project-Id-Version: PROJECT VERSION\n"
"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
"POT-Creation-Date: 2025-08-11 22:45+0200\n"
"PO-Revision-Date: 2025-08-11 22:37+0200\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language: fr\n"
"Language-Team: fr <LL@li.org>\n"
"Plural-Forms: nplurals=2; plural=(n > 1)\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: Babel 2.8.0\n"

#: templates/3-index.html:5
msgid "home_title"
msgstr "Bienvenue chez Holberton"

#: templates/3-index.html:8
msgid "home_header"
msgstr "Bonjour monde!"


```

translations/en/LC_MESSAGES/messages.mo
```bash

```

translations/fr/LC_MESSAGES/messages.mo
```bash

```

Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

Create a babel.cfg file containing
```bash
[python: **.py]
[jinja2: **/templates/**.html]
```
Then initialize your translations with
```bash
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide the correct value for each message ID for each language. Use the following translations:

msgid	English	French
home_title	"Welcome to Holberton"	"Bienvenue chez Holberton"
home_header	"Hello world!"	"Bonjour monde!"
Then compile your dictionaries with

```bash
$ pybabel compile -d translations
```
Reload the home page of your app and make sure that the correct messages show up.


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel extract -F babel.cfg -o messages.pot .
extracting messages from 0-app.py
extracting messages from 1-app.py
extracting messages from 2-app.py
extracting messages from 3-app.py
extracting messages from 4-app.py
extracting messages from 5-app.py
extracting messages from 6-app.py
extracting messages from 7-app.py
extracting messages from app.py
extracting messages from templates/0-index.html
extracting messages from templates/1-index.html
extracting messages from templates/2-index.html
extracting messages from templates/3-index.html
extracting messages from templates/4-index.html
extracting messages from templates/5-index.html
extracting messages from templates/6-index.html
extracting messages from templates/7-index.html
extracting messages from templates/index.html
writing PO template file to messages.pot
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel init -i messages.pot -d translations -l en
creating catalog translations/en/LC_MESSAGES/messages.po based on messages.pot
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel init -i messages.pot -d translations -l fr
creating catalog translations/fr/LC_MESSAGES/messages.po based on messages.pot
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel compile -d translations
compiling catalog translations/en/LC_MESSAGES/messages.po to translations/en/LC_MESSAGES/messages.mo
compiling catalog translations/fr/LC_MESSAGES/messages.po to translations/fr/LC_MESSAGES/messages.mo
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n#
```


```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n# python3 3-app.py
 * Serving Flask app '3-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Aug/2025 22:44:59] "GET / HTTP/1.1" 200 -

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel extract -F babel.cfg -o messages.pot .
extracting messages from 0-app.py
extracting messages from 1-app.py
extracting messages from 2-app.py
extracting messages from 3-app.py
extracting messages from 4-app.py
extracting messages from 5-app.py
extracting messages from 6-app.py
extracting messages from 7-app.py
extracting messages from app.py
extracting messages from templates/0-index.html
extracting messages from templates/1-index.html
extracting messages from templates/2-index.html
extracting messages from templates/3-index.html
extracting messages from templates/4-index.html
extracting messages from templates/5-index.html
extracting messages from templates/6-index.html
extracting messages from templates/7-index.html
extracting messages from templates/index.html
writing PO template file to messages.pot
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel update -i messages.pot -d translations
updating catalog translations/en/LC_MESSAGES/messages.po based on messages.pot
updating catalog translations/fr/LC_MESSAGES/messages.po based on messages.pot
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n# pybabel compile -d translations
compiling catalog translations/en/LC_MESSAGES/messages.po to translations/en/LC_MESSAGES/messages.mo
compiling catalog translations/fr/LC_MESSAGES/messages.po to translations/fr/LC_MESSAGES/messages.mo
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_e
nd/i18n#

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n# python3 3-app.py
 * Serving Flask app '3-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Aug/2025 22:56:46] "GET / HTTP/1.1" 200 -


(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n# pybabel compile -d translations
compiling catalog translations/en/LC_MESSAGES/messages.po to translations/en/LC_MESSAGES/messages.mo
compiling catalog translations/fr/LC_MESSAGES/messages.po to translations/fr/LC_MESSAGES/messages.mo
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n#

(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-we
b_back_end/i18n# python3 3-app.py
 * Serving Flask app '3-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Aug/2025 22:56:46] "GET / HTTP/1.1" 200 -

```
![alt text](image.png)


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



