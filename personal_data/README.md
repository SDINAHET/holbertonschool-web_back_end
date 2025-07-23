Personal Data Logging and Security 🔒



📚 Description

Ce projet a pour but de protéger les données personnelles (PII) lors de leur traitement ou affichage, notamment dans les fichiers de log. Il démontre également comment connecter une base de données de manière sécurisée, hasher des mots de passe et valider leur authenticité, tout en respectant les bonnes pratiques de cybersécurité.

🎯 Objectifs pédagogiques

À l’issue de ce projet, vous serez capable de :

Identifier les informations personnelles sensibles (PII).

Masquer automatiquement les champs sensibles dans les logs (name=***; email=***;...).

Hacher des mots de passe avec bcrypt.

Vérifier la validité d’un mot de passe par rapport à son hash.

Sécuriser les connexions à la base de données à l’aide de variables d’environnement.

💪 Technologies utilisées

Python 3.10+

MySQL 8.x

mysql-connector-python

bcrypt

logging

re (expressions régulières)

Variables d’environnement (os.environ)

🧹 Structure des fichiers

personal_data/
├── filtered_logger.py       # Masquage des PII dans les logs
├── encrypt_password.py      # Fonctions de hash et validation de mots de passe
├── main.sql                 # Script SQL de création de la BDD `my_db`
├── user_data.csv            # Données d’exemple (non soumises)
├── main.py                  # Fichier de test des fonctions
└── README.md                # Ce fichier

✅ Fonctions implémentées

filtered_logger.py

filter_datum(...) : masque les valeurs des champs PII dans un message.

RedactingFormatter : formatteur de logs qui applique filter_datum.

get_logger() : configure un logger avec un format masqué.

get_db() : connecte à la BDD via des variables d’environnement (PERSONAL_DATA_DB_*).

main() : extrait les données de la table users et les logge de façon sécurisée.

encrypt_password.py

hash_password(password: str) -> bytes : retourne un hash sécurisé (salé) d’un mot de passe.

is_valid(hashed_password: bytes, password: str) -> bool : vérifie qu’un mot de passe correspond bien à un hash bcrypt.

🔐 Exemples de PII filtrées

Le format de log :

[HOLBERTON] user_data INFO 2025-07-23 15:00:00: name=***; email=***; phone=***; ssn=***; password=***;

🌐 Variables d’environnement requises

Avant de lancer filtered_logger.py, exportez :

export PERSONAL_DATA_DB_USERNAME=root
export PERSONAL_DATA_DB_PASSWORD=root
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=my_db

Ou utilisez directement dans la ligne de commande :

PERSONAL_DATA_DB_USERNAME=root \
PERSONAL_DATA_DB_PASSWORD=root \
PERSONAL_DATA_DB_HOST=localhost \
PERSONAL_DATA_DB_NAME=my_db \
./filtered_logger.py

🧪 Exécution de tests

Test du hash et validation de mot de passe :

$ ./main.py
b'$2b$12$....'
True

Test du logger :

$ ./filtered_logger.py
[HOLBERTON] user_data INFO ... name=***; email=***; ...

📁 Ressources

What is PII? (Personally Identifiable Information)

Python logging module

bcrypt package (PyPI)

📌 Contraintes respectées

Tous les fichiers commencent par #!/usr/bin/env python3

Respect de pycodestyle (PEP8)

Fonctions et classes documentées

Fonctions typées

Aucun mot de passe stocké en clair

Hash sécurisé avec bcrypt

Connexion à MySQL sécurisée par environnement

🚀 Auteur

Projet réalisé par Stéphane Dinahet dans le cadre du cursus Holberton School - Web BackendGitHub - @SDINAHET


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestr
e/holbertonschool-web_back_end/personal_data# cat main.sql | mysql -uroot -p
Enter password:
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestr
e/holbertonschool-web_back_end/personal_data# echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password:
COUNT(*)
2
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestr
e/holbertonschool-web_back_end/personal_data# PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
[HOLBERTON] user_data INFO 2025-07-23 20:05:33,887: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2025-07-23 20:05:33,887: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/personal_data#
```


```bash
root@UI:holbertonschool-web_back_end/personal_data# cat main.sql | mysql -uroot -p
Enter password:
root@UI:holbertonschool-web_back_end/personal_data# echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password:
COUNT(*)
2
root@UI:holbertonschool-web_back_end/personal_data# PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
[HOLBERTON] user_data INFO 2025-07-23 20:05:33,887: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2025-07-23 20:05:33,887: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
root@UI:/holbertonschool-web_back_end/personal_data#
```
