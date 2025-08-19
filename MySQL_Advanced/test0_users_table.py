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
