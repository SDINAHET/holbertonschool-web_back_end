# MySQL Advanced – Task0 (We are all unique!)

Guide **README (Markdown)** pour lancer **MySQL 8 sous Docker** (isolé du PC) et réaliser **tous les tests** de la Task0, avec résultats attendus.

---

## 🚀 Démarrer MySQL 8 en Docker (isolé)

```bash
# 1) (Optionnel) Nettoyer un ancien conteneur
docker stop mysql8 || true && docker rm mysql8 || true

# 2) Lancer MySQL 8 sur le port hôte 3307
docker run --name mysql8 \
  -e MYSQL_ROOT_PASSWORD=root \
  -p 3307:3306 \
  -d mysql:8

# 3) Attendre que MySQL soit prêt
docker logs -f mysql8 | grep -m1 "ready for connections"
```

> Connexion au serveur Docker : `mysql -h 127.0.0.1 -P 3307 -uroot -p`

---

## 📁 Fichier à tester

### `0-uniq_users.sql`

```sql
-- Task0 - We are all unique!
-- Create a table 'users' with id, email (unique), and name

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
```

---

## 🧪 Tests (dans le MySQL Docker)

### 1) Tests manuels (MYSQL CLI)

Rapide pour vérifier le schéma, l’unicité et les index.

```bash
# 1) Créer une base jetable
echo "DROP DATABASE IF EXISTS test_sql;" | mysql -h 127.0.0.1 -P 3307 -uroot -p
echo "CREATE DATABASE test_sql;" | mysql -h 127.0.0.1 -P 3307 -uroot -p

# 2) Exécuter ton script
cat 0-uniq_users.sql | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql

# 3) Vérifier la table
echo "SHOW TABLES;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql
echo "DESCRIBE users;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql
echo "SHOW CREATE TABLE users\G" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql

# 4) Vérifier l'index unique sur email
echo "SHOW INDEX FROM users;" | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql
# → La colonne 'email' doit avoir Non_unique = 0

# 5) Tester l’unicité
echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql
echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -h 127.0.0.1 -P 3307 -uroot -p test_sql
# ↑ Doit échouer avec ERROR 1062 (Duplicate entry)
```

> 💡 Si tu préfères tester sur ton MySQL local (3306), supprime `-h 127.0.0.1 -P 3307` ou adapte le port.

---

### 2) Test automatisé en Bash (façon “unittest” minimal)

Script qui crée une DB jetable, lance le SQL, **assert** le schéma et l’unicité :

```bash
#!/usr/bin/env bash
set -euo pipefail

DB="test_sql_uniq_$$"
PASS="root"   # adapte si besoin

# Cible le MySQL en Docker (port 3307)
mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "CREATE DATABASE ${DB};"

cleanup() {
  mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "DROP DATABASE IF EXISTS ${DB};"
}
trap cleanup EXIT

# Exécuter le script
mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" "${DB}" < 0-uniq_users.sql

# 1) Table existe ?
mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "USE ${DB}; SHOW TABLES LIKE 'users';" | grep -q users

# 2) Colonnes attendues ?
COLS=$(mysql -N -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "USE ${DB}; SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='${DB}' AND TABLE_NAME='users' ORDER BY ORDINAL_POSITION;")
echo "$COLS" | grep -qx "id"$'
'"email"$'
'"name"

# 3) Index UNIQUE sur email ?
mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "USE ${DB}; SHOW INDEX FROM users;" | awk '{print $3,$2,$6,$7,$8,$10,$11}'

UNIQ=$(mysql -N -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "USE ${DB};
SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA='${DB}' AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;")
[[ "$UNIQ" == "0" ]]

# 4) Test d’unicité (doit lever 1062)
mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "USE ${DB}; INSERT INTO users (email,name) VALUES ('a@a.com','A');"
if mysql -h 127.0.0.1 -P 3307 -uroot -p"$PASS" -e "USE ${DB}; INSERT INTO users (email,name) VALUES ('a@a.com','B');"; then
  echo "❌ Unicité non respectée"; exit 1
else
  echo "✅ Erreur attendue sur doublon (OK)"
fi

echo "✅ Tous les checks sont OK"
```

> Sauvegarde ce script en `tests/test_task0.sh`, rends-le exécutable (`chmod +x tests/test_task0.sh`) puis lance-le.

---

### 3) Tests Python (pytest) – suite de tests

Idéal si tu veux une vraie suite de tests.

Créer `tests/test0_users_table.py` :

```python
import pytest
import mysql.connector

DB = "test_sql_py"
HOST = "127.0.0.1"
PORT = 3307  # cible le Docker mysql8 lancé ci-dessus
USER = "root"
PASS = "root"

@pytest.fixture(scope="module")
def conn():
    cx = mysql.connector.connect(user=USER, password=PASS, host=HOST, port=PORT)
    cx.autocommit = True
    cur = cx.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB};")
    cur.execute(f"CREATE DATABASE {DB};")
    cur.close()
    yield cx
    cur = cx.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB};")
    cur.close()
    cx.close()

def run_sql(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()

def test_schema_and_unique(conn):
    run_sql(conn, f"USE {DB};")
    # Charger le script
    with open("0-uniq_users.sql", "r", encoding="utf-8") as f:
        sql = f.read()
    cur = conn.cursor()
    for stmt in filter(None, [s.strip() for s in sql.split(';')]):
        cur.execute(stmt)
    # Vérifications
    cur.execute("SHOW TABLES LIKE 'users';")
    assert cur.fetchone() is not None

    cur.execute(
        """
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users'
        ORDER BY ORDINAL_POSITION;
        """,
        (DB,)
    )
    cols = [r[0] for r in cur.fetchall()]
    assert cols == ["id", "email", "name"]

    cur.execute(
        """
        SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;
        """,
        (DB,)
    )
    non_unique = cur.fetchone()[0]
    assert non_unique == 0  # 0 => UNIQUE


def test_uniqueness_violation(conn):
    run_sql(conn, f"USE {DB};")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email,name) VALUES ('x@x.com','X');")
    with pytest.raises(mysql.connector.errors.IntegrityError) as e:
        cur.execute("INSERT INTO users (email,name) VALUES ('x@x.com','Y');")
    # Code MySQL attendu : 1062
    assert e.value.errno == 1062
    cur.close()
```

Installer les dépendances (si besoin) puis lancer :

```bash
pip install -q mysql-connector-python pytest
pytest -q
```

---

## ✅ Résultats attendus

* **Création** d’une table `users` avec :

  * `id` INT NOT NULL AUTO\_INCREMENT PRIMARY KEY
  * `email` VARCHAR(255) NOT NULL **UNIQUE**
  * `name` VARCHAR(255)
* Le script peut être relancé **sans erreur** (grâce à `IF NOT EXISTS`).
* Une seconde insertion avec le **même** `email` produit l’erreur `ERROR 1062 (23000) Duplicate entry`.

---

## 🆘 Dépannage rapide

* **Port déjà utilisé** : change le mapping Docker (`-p 3308:3306`) ou stoppe MySQL local.
* **Login root échoue** : vérifie `MYSQL_ROOT_PASSWORD` et le port ciblé (`-P 3307`).
* **pytest: no tests ran** : assure-toi d’avoir `tests/test0_users_table.py` et lance `pytest -q` depuis la racine.

---

## 📌 Notes

* Ce setup **n’altère pas** ton MySQL local : tout est contenu dans le conteneur.
* Tu peux réutiliser la même structure pour les autres Tasks (1 → 101).

---

## 🧰 Option « une seule commande » : docker-compose + Makefile

Voici une config **clé en main** pour lancer MySQL en Docker, attendre qu’il soit prêt et exécuter **tous les tests** (Bash + Pytest) via `make`.

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  mysql8:
    image: mysql:8
    container_name: mysql8
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:-root}
    ports:
      - "${DB_PORT:-3307}:3306"
    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -proot || exit 1"]
      interval: 2s
      timeout: 2s
      retries: 30
      start_period: 5s
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

### (Optionnel) `.env`

```dotenv
# Ports et credentials (peuvent être surchargés dans l'environnement)
DB_PORT=3307
MYSQL_ROOT_PASSWORD=root
```

### `Makefile`

```make
SHELL := /bin/bash
DB_HOST ?= 127.0.0.1
DB_PORT ?= 3307
DB_USER ?= root
DB_PASS ?= root
SERVICE := mysql8
COMPOSE := docker compose -f docker-compose.yml

.PHONY: up down logs mysql wait test-cli test-py test-all clean

up:
	$(COMPOSE) up -d

wait:
	@echo "⏳ Waiting for MySQL healthcheck to be healthy..."
	@until [ "$$(docker inspect -f {{.State.Health.Status}} $(SERVICE))" = "healthy" ]; do \
	  sleep 1; echo -n "."; \
	done; echo "
✅ MySQL is healthy."

logs:
	$(COMPOSE) logs -f $(SERVICE)

mysql:
	docker exec -it $(SERVICE) mysql -u$(DB_USER) -p$(DB_PASS)

# Tests Bash (nécessite tests/test_task0.sh)
test-cli:
	@chmod +x tests/test_task0.sh
	DB_HOST=$(DB_HOST) DB_PORT=$(DB_PORT) DB_USER=$(DB_USER) DB_PASS=$(DB_PASS) tests/test_task0.sh

# Tests PyTest (exécutés sur l'hôte)
test-py:
	pytest -q

# Pipeline complet : démarre, attend et lance tous les tests
test-all: up wait test-cli test-py
	@echo "
🎉 All tests done."

down:
	$(COMPOSE) down -v

clean: down
	@echo "🧹 Cleaned containers & volumes."
```

### `tests/test_task0.sh`

> Version compatible avec le **Makefile** (utilise les variables d’environnement DB\_\*)

```bash
#!/usr/bin/env bash
set -euo pipefail

DB_NAME="test_sql_uniq_$$"
DB_HOST="${DB_HOST:-127.0.0.1}"
DB_PORT="${DB_PORT:-3307}"
DB_USER="${DB_USER:-root}"
DB_PASS="${DB_PASS:-root}"

mysql_cli() {
  mysql -h "$DB_HOST" -P "$DB_PORT" -u"$DB_USER" -p"$DB_PASS" "$@"
}

mysql_cli -e "CREATE DATABASE ${DB_NAME};"

cleanup() {
  mysql_cli -e "DROP DATABASE IF EXISTS ${DB_NAME};"
}
trap cleanup EXIT

# Exécuter le script
mysql_cli "${DB_NAME}" < 0-uniq_users.sql

# 1) Table existe ?
mysql_cli -e "USE ${DB_NAME}; SHOW TABLES LIKE 'users';" | grep -q users

# 2) Colonnes attendues ?
COLS=$(mysql_cli -N -e "USE ${DB_NAME}; SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='${DB_NAME}' AND TABLE_NAME='users' ORDER BY ORDINAL_POSITION;")
echo "$COLS" | grep -qx "id"$'
'"email"$'
'"name"

# 3) Index UNIQUE sur email ?
UNIQ=$(mysql_cli -N -e "USE ${DB_NAME}; SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS WHERE TABLE_SCHEMA='${DB_NAME}' AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;")
[[ "$UNIQ" == "0" ]]

# 4) Test d’unicité (doit lever 1062)
mysql_cli -e "USE ${DB_NAME}; INSERT INTO users (email,name) VALUES ('a@a.com','A');"
if mysql_cli -e "USE ${DB_NAME}; INSERT INTO users (email,name) VALUES ('a@a.com','B');"; then
  echo "❌ Unicité non respectée"; exit 1
else
  echo "✅ Erreur attendue sur doublon (OK)"
fi

echo "✅ Tous les checks sont OK (Bash)"
```

### `tests/test0_users_table.py`

> Identique à la section précédente, mais paramétré sur le **port 3307** (Docker)

```python
import pytest
import mysql.connector

DB = "test_sql_py"
HOST = "127.0.0.1"
PORT = 3307
USER = "root"
PASS = "root"

@pytest.fixture(scope="module")
def conn():
    cx = mysql.connector.connect(user=USER, password=PASS, host=HOST, port=PORT)
    cx.autocommit = True
    cur = cx.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB};")
    cur.execute(f"CREATE DATABASE {DB};")
    cur.close()
    yield cx
    cur = cx.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DB};")
    cur.close()
    cx.close()


def run_sql(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()


def test_schema_and_unique(conn):
    run_sql(conn, f"USE {DB};")
    with open("0-uniq_users.sql", "r", encoding="utf-8") as f:
        sql = f.read()
    cur = conn.cursor()
    for stmt in filter(None, [s.strip() for s in sql.split(';')]):
        cur.execute(stmt)

    cur.execute("SHOW TABLES LIKE 'users';")
    assert cur.fetchone() is not None

    cur.execute(
        """
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users'
        ORDER BY ORDINAL_POSITION;
        """,
        (DB,)
    )
    cols = [r[0] for r in cur.fetchall()]
    assert cols == ["id", "email", "name"]

    cur.execute(
        """
        SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS
        WHERE TABLE_SCHEMA=%s AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;
        """,
        (DB,)
    )
    non_unique = cur.fetchone()[0]
    assert non_unique == 0


def test_uniqueness_violation(conn):
    run_sql(conn, f"USE {DB};")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email,name) VALUES ('x@x.com','X');")
    with pytest.raises(mysql.connector.errors.IntegrityError) as e:
        cur.execute("INSERT INTO users (email,name) VALUES ('x@x.com','Y');")
    assert e.value.errno == 1062
    cur.close()
```

### Utilisation

```bash
# 1) Lancer MySQL + attendre + exécuter tous les tests
make test-all

# 2) Voir les logs temps réel
make logs

# 3) Ouvrir un client MySQL dans le conteneur
make mysql

# 4) Stopper et nettoyer
make clean
```

> Place `docker-compose.yml`, `Makefile`, `.env` (optionnel), `tests/test_task0.sh`, `tests/test0_users_table.py` à la **racine du dossier MySQL\_Advanced** avec `0-uniq_users.sql`.
