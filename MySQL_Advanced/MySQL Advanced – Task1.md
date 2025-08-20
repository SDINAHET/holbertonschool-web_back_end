Task1 — 1-country_users.sql
✅ Script SQL
-- 1-country_users.sql
-- Create table `users` if it doesn't already exist.
-- Requirements:
-- - id: INT, NOT NULL, AUTO_INCREMENT, PRIMARY KEY
-- - email: VARCHAR(255), NOT NULL, UNIQUE
-- - name: VARCHAR(255)
-- - country: ENUM('US','CO','TN'), NOT NULL, default 'US'


CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US','CO','TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (id),
  UNIQUE KEY unique_email (email)
);
1) Tests manuels (MySQL CLI – Docker sur 3307)
# Base jetable
echo "DROP DATABASE IF EXISTS test_sql1;" | mysql -h 127.0.0.1 -P 3307 -uroot -p
echo "CREATE DATABASE test_sql1;" | mysql -h 127.0.0.1 -P 3307 -uroot -p


# Exécuter le script
cat 1-country_users.sql | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1


# Vérifs de schéma
echo "SHOW TABLES;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1
echo "DESCRIBE users;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1
echo "SHOW CREATE TABLE users\G" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1


# Vérifier l'UNIQUE sur email
echo "SHOW INDEX FROM users;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1
# → email doit avoir Non_unique = 0


# Vérifier NOT NULL + DEFAULT de country
mysql -h 127.0.0.1 -P 3307 -uroot -p -e "\
SELECT COLUMN_NAME, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_TYPE \
FROM INFORMATION_SCHEMA.COLUMNS \
WHERE TABLE_SCHEMA='test_sql1' AND TABLE_NAME='users' AND COLUMN_NAME='country';"
# → IS_NULLABLE = 'NO', COLUMN_DEFAULT = 'US', COLUMN_TYPE = enum('US','CO','TN')


# Insertion avec country omis → doit prendre 'US' par défaut
echo "INSERT INTO users (email, name) VALUES ('a@a.com','Alice');" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1


# Insertion avec country explicite
echo "INSERT INTO users (email, name, country) VALUES ('b@b.com','Bob','CO');" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1


# Insertion invalid enum → doit échouer en SQL_MODE strict (MySQL 8)
# On valide juste que la commande retourne une erreur (code non 0)
if echo "INSERT INTO users (email, name, country) VALUES ('bad@x.com','Bad','FR');" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1; then
  echo "❌ L'ENUM a accepté une valeur invalide";
else
  echo "✅ Insertion invalide rejetée (ENUM OK)";
fi


# Vérifier données
echo "SELECT id,email,name,country FROM users ORDER BY id;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql1
2) Test Bash automatisé – tests/test_task1.sh
#!/usr/bin/env bash
set -euo pipefail


DB_NAME="test_sql1_$$"
DB_HOST="${DB_HOST:-127.0.0.1}"
DB_PORT="${DB_PORT:-3307}"
DB_USER="${DB_USER:-root}"
DB_PASS="${DB_PASS:-root}"


mysql_cli() {
  mysql -h "$DB_HOST" -P "$DB_PORT" -u"$DB_USER" -p"$DB_PASS" "$@"
}


mysql_cli -e "CREATE DATABASE ${DB_NAME};"
cleanup() { mysql_cli -e "DROP DATABASE IF EXISTS ${DB_NAME};"; }
trap cleanup EXIT


# Exécuter le script
mysql_cli "${DB_NAME}" < 1-country_users.sql


# 1) Colonnes attendues
echo "[Schema]"
COLS=$(mysql_cli -N -e "USE ${DB_NAME}; SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='${DB_NAME}' AND TABLE_NAME='users' ORDER BY ORDINAL_POSITION;")
echo "$COLS" | grep -qx "id"$'
'"email"$'
'"name"$'
'"country"


# 2) UNIQUE sur email
UNIQ=$(mysql_cli -N -e "USE ${DB_NAME}; SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS WHERE TABLE_SCHEMA='${DB_NAME}' AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;")
[[ "$UNIQ" == "0" ]]


# 3) country NOT NULL + DEFAULT 'US' + type ENUM
read -r IS_NULLABLE COLUMN_DEFAULT COLUMN_TYPE < <(mysql_cli -N -e "\
SELECT IS_NULLABLE, COLUMN_DEFAULT, COLUMN_TYPE \
FROM INFORMATION_SCHEMA.COLUMNS \
WHERE TABLE_SCHEMA='${DB_NAME}' AND TABLE_NAME='users' AND COLUMN_NAME='country';")
[[ "$IS_NULLABLE" == "NO" ]]
[[ "$COLUMN_DEFAULT" == "US" ]]
[[ "$COLUMN_TYPE" == "enum('US','CO','TN')" ]]


# 4) Insertion par défaut (country omis)
mysql_cli -e "USE ${DB_NAME}; INSERT INTO users (email,name) VALUES ('a@a.com','Alice');"
VAL=$(mysql_cli -N -e "USE ${DB_NAME}; SELECT country FROM users WHERE email='a@a.com';")
[[ "$VAL" == "US" ]]


# 5) Insertion ENUM valide
mysql_cli -e "USE ${DB_NAME}; INSERT INTO users (email,name,country) VALUES ('b@b.com','Bob','CO');"
VAL2=$(mysql_cli -N -e "USE ${DB_NAME}; SELECT country FROM users WHERE email='b@b.com';")
[[ "$VAL2" == "CO" ]]


# 6) Insertion ENUM invalide → doit échouer (sql_mode strict par défaut sur MySQL 8)
if mysql_cli -e "USE ${DB_NAME}; INSERT INTO users (email,name,country) VALUES ('bad@x.com','Bad','FR');"; then
  echo "❌ ENUM a accepté une valeur invalide"; exit 1
else
  echo "✅ ENUM rejette les valeurs invalides"
fi


echo "✅ Task1 checks OK (Bash)"

Ajoute ce script puis exécute via make test-cli (il prendra automatiquement DB_HOST/PORT du Makefile).

3) Tests PyTest – tests/test1_country_users.py
import pytest
        cur.execute(stmt)
    cur.close()




def test_schema(conn):
    cur = conn.cursor()
    cur.execute(f"USE {DB};")
    run_sql_file(conn, "1-country_users.sql")


    cur.execute("SHOW TABLES LIKE 'users';")
    assert cur.fetchone() is not None


    cur.execute(
        """
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users'
        ORDER BY ORDINAL_POSITION;
        """,
        (DB,),
    )
    cols = [r[0] for r in cur.fetchall()]
    assert cols == ["id", "email", "name", "country"]


    # email UNIQUE
    cur.execute(
        """
        SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;
        """,
        (DB,),
    )
    non_unique = cur.fetchone()[0]
    assert non_unique == 0


    # country NOT NULL + DEFAULT + ENUM type
    cur.execute(
        """
        SELECT IS_NULLABLE, COLUMN_DEFAULT, COLUMN_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users' AND COLUMN_NAME='country';
        """,
        (DB,),
    )
    is_nullable, default, coltype = cur.fetchone()
    assert is_nullable == "NO"
    assert default == "US"
    assert coltype == "enum('US','CO','TN')"




def test_inserts_and_enum(conn):
    cur = conn.cursor()
    cur.execute(f"USE {DB};")


    # Default country
    cur.execute("INSERT INTO users (email,name) VALUES ('a@a.com','Alice');")
    cur.execute("SELECT country FROM users WHERE email='a@a.com';")
    assert cur.fetchone()[0] == "US"


    # Valid enum value
    cur.execute("INSERT INTO users (email,name,country) VALUES ('b@b.com','Bob','TN');")
    cur.execute("SELECT country FROM users WHERE email='b@b.com';")
    assert cur.fetchone()[0] == "TN"


    # Invalid enum value → doit lever une erreur en mode strict
    with pytest.raises(mysql.connector.Error):
        cur.execute("INSERT INTO users (email,name,country) VALUES ('bad@x.com','Bad','FR');")


    cur.close()
Utilisation rapide
# Bash (via Makefile)
make test-cli DB_PORT=3307 DB_USER=root DB_PASS=root DB_HOST=127.0.0.1


# PyTest
pytest -q tests/test1_country_users.py

C’est bon ! 🎉
J’ai ajouté à la fiche Canva :
Le script SQL complet pour Task1 (1-country_users.sql)
Les tests manuels (CLI MySQL sur Docker 3307)
Un test Bash automatisé (tests/test_task1.sh)
Un test PyTest (tests/test1_country_users.py)
Les commandes d’utilisation rapides

Tu peux copier-coller et lancer tout de suite :

make test-cli           # exécute le test Bash (si tu passes test_task1.sh à la cible ou le lances directement)
pytest -q tests/test1_country_users.py   # exécute le test PyTes
