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
