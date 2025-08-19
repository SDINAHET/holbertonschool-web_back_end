MySQL_Advanced

Resources

Read or watch:

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.percona.com/blog/2019/02/27/mysql-performance-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://www.mysqltutorial.org/mysql-triggers/)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## More info
Comments for your SQL file:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

How to import a SQL dump
```sql
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/MySQL_Advanced# echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/MySQL_Advanced# curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/MySQL_Advanced# echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id      name
1       Drama
2       Mystery
3       Adventure
4       Fantasy
5       Comedy
6       Crime
7       Suspense
8       Thriller
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_en
d/MySQL_Advanced#
```



## Task0
0-uniq_users.sql
```sql
-- Task0 - We are all unique!
-- Create a table 'users' with id, email (unique), and name

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

```

1) Tests manuels (MYSQL CLI)
Rapide pour vérifier le schéma, l’unicité et les index.
```bash
# 1) Créer une base jetable
echo "DROP DATABASE IF EXISTS test_sql;" | mysql -uroot -p
echo "CREATE DATABASE test_sql;" | mysql -uroot -p

# 2) Exécuter ton script
cat 0-uniq_users.sql | mysql -uroot -p test_sql

# 3) Vérifier la table
echo "SHOW TABLES;" | mysql -uroot -p test_sql
echo "DESCRIBE users;" | mysql -uroot -p test_sql
echo "SHOW CREATE TABLE users\G" | mysql -uroot -p test_sql

# 4) Vérifier l'index unique sur email
echo "SHOW INDEX FROM users;" | mysql -uroot -p test_sql
# → La colonne 'email' doit avoir Non_unique = 0

# 5) Tester l’unicité
echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p test_sql
echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p test_sql
# ↑ Doit échouer avec ERROR 1062 (Duplicate entry)
```

2) Test automatisé en Bash (façon “unittest” minimal)

Script qui crée une DB jetable, lance le SQL, assert le schéma et l’unicité :
```bash
#!/usr/bin/env bash
set -euo pipefail

DB="test_sql_uniq_$$"
PASS="root"   # adapte si besoin
mysql -uroot -p"$PASS" -e "CREATE DATABASE ${DB};"

cleanup() {
  mysql -uroot -p"$PASS" -e "DROP DATABASE IF EXISTS ${DB};"
}
trap cleanup EXIT

# Exécuter le script
mysql -uroot -p"$PASS" "${DB}" < 0-uniq_users.sql

# 1) Table existe ?
mysql -uroot -p"$PASS" -e "USE ${DB}; SHOW TABLES LIKE 'users';" | grep -q users

# 2) Colonnes attendues ?
COLS=$(mysql -N -uroot -p"$PASS" -e "USE ${DB}; SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='${DB}' AND TABLE_NAME='users' ORDER BY ORDINAL_POSITION;")
echo "$COLS" | grep -qx "id"$'\n'"email"$'\n'"name"

# 3) Index UNIQUE sur email ?
mysql -uroot -p"$PASS" -e "USE ${DB}; SHOW INDEX FROM users;" | awk '{print $3,$2,$6,$7,$8,$10,$11}'

UNIQ=$(mysql -N -uroot -p"$PASS" -e "USE ${DB};
SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA='${DB}' AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;")
test "$UNIQ" = "0"

# 4) Test d’unicité (doit lever 1062)
mysql -uroot -p"$PASS" -e "USE ${DB}; INSERT INTO users (email,name) VALUES ('a@a.com','A');"
if mysql -uroot -p"$PASS" -e "USE ${DB}; INSERT INTO users (email,name) VALUES ('a@a.com','B');"; then
  echo "❌ Unicité non respectée"; exit 1
else
  echo "✅ Erreur attendue sur doublon (OK)"
fi

echo "✅ Tous les checks sont OK"
```

3) Tests Python (pytest) pour aller plus loin
Idéal si tu veux une vraie suite de tests.
test0_users_table.py
```python
import pytest
import mysql.connector

@pytest.fixture(scope="module")
def conn():
    cx = mysql.connector.connect(user="root", password="root", host="127.0.0.1")
    cx.autocommit = True
    cur = cx.cursor()
    cur.execute("DROP DATABASE IF EXISTS test_sql_py;")
    cur.execute("CREATE DATABASE test_sql_py;")
    cur.close()
    yield cx
    cur = cx.cursor()
    cur.execute("DROP DATABASE IF EXISTS test_sql_py;")
    cur.close()
    cx.close()

def run_sql(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()

def test_schema_and_unique(conn):
    run_sql(conn, "USE test_sql_py;")
    # Charger le script
    with open("0-uniq_users.sql", "r", encoding="utf-8") as f:
        sql = f.read()
    cur = conn.cursor()
    for stmt in filter(None, [s.strip() for s in sql.split(';')]):
        cur.execute(stmt)
    # Vérifications
    cur.execute("SHOW TABLES LIKE 'users';")
    assert cur.fetchone() is not None

    cur.execute("""
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA='test_sql_py' AND TABLE_NAME='users'
        ORDER BY ORDINAL_POSITION;
    """)
    cols = [r[0] for r in cur.fetchall()]
    assert cols == ["id", "email", "name"]

    cur.execute("""
        SELECT Non_unique FROM INFORMATION_SCHEMA.STATISTICS
        WHERE TABLE_SCHEMA='test_sql_py' AND TABLE_NAME='users' AND COLUMN_NAME='email' LIMIT 1;
    """)
    non_unique = cur.fetchone()[0]
    assert non_unique == 0  # 0 => UNIQUE

def test_uniqueness_violation(conn):
    run_sql(conn, "USE test_sql_py;")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email,name) VALUES ('x@x.com','X');")
    with pytest.raises(mysql.connector.errors.IntegrityError) as e:
        cur.execute("INSERT INTO users (email,name) VALUES ('x@x.com','Y');")
    # Code MySQL attendu : 1062
    assert e.value.errno == 1062
    cur.close()
```

Astuce : lance un MySQL 8 jetable en Docker pour isoler tes tests :
```bash
docker run --name mysql8 -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8
# Attendre qu’il soit prêt, puis exécuter les tests
pytest -q

```

```bash

```

## Task1
1-country_users.sql

```sql

```

```bash

```

## Task2
2-fans.sql
```sql

```

```bash

```


## Task3
3-glam_rock.sql
```sql

```

```bash

```


## Task4
4-store.sql
```sql

```

```bash

```


## Task5
5-valid_email.sql
```sql

```

```bash

```


## Task6
6-bonus.sql
```sql

```

```bash

```


## Task7
7-average_score.sql
```sql

```

```bash

```


## Task8
8-index_my_names.sql
```sql

```

```bash

```


## Task9
9-index_name_score.sql
```sql

```

```bash

```


## Task10
10-div.sql
```sql

```

```bash

```


## Task11
11-need_meeting.sql
```sql

```

```bash

```


## Task100
100-average_weighted_score.sql
```sql

```

```bash

```


## Task101
101-average_weighted_score.sql
```sql

```

```bash

```
