# MySQL 8.x Practical Cheatsheet

Quick, production‑ready snippets you can copy/paste. Focused on schema design, indexing, queries, procedures, triggers, and views — with examples inspired by a ticket/results app.

---

## Handy References

* [MySQL cheatsheet](https://devhints.io/mysql)
* [Indexing for performance (Percona)](https://www.percona.com/blog/2019/02/27/mysql-performance-how-to-leverage-mysql-database-indexing/)
* [Stored routines (official docs)](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)
* [Triggers (official docs)](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
* [Views (official docs)](https://dev.mysql.com/doc/refman/8.0/en/views.html)
* [Functions & operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
* [Trigger syntax & examples](https://www.mysqltutorial.org/mysql-triggers/)
* [CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
* [CREATE PROCEDURE / FUNCTION](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
* [CREATE INDEX](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
* [CREATE VIEW](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

---

## Basics

```bash
# Connect (CLI)
mysql -u USER -p -h HOST -P 3306

# See DBs & tables
SHOW DATABASES; USE mydb; SHOW TABLES; DESCRIBE users; \G
```

### Create & Drop DB

```sql
CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
DROP DATABASE mydb;
```

---

## Data Types (practical picks)

* **Primary IDs**: `BIGINT UNSIGNED` (auto‑inc) or `BINARY(16)` for UUID (compact) or `CHAR(36)` (readable).
* **Money**: `DECIMAL(12,2)` (avoid FLOAT/DOUBLE for money).
* **Timestamps**: `TIMESTAMP` or `DATETIME`; use `DEFAULT CURRENT_TIMESTAMP` & `ON UPDATE CURRENT_TIMESTAMP`.
* **JSON**: `JSON` type for flexible attributes; index with generated columns.

---

## Example Schema (tickets)

```sql
CREATE TABLE users (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARBINARY(60) NOT NULL,
  role ENUM('user','admin') NOT NULL DEFAULT 'user',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE tickets (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT UNSIGNED NOT NULL,
  draw_date DATE NOT NULL,
  numbers JSON NOT NULL,
  amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_ticket_user FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Optional linking for many-to-many (if needed)
CREATE TABLE user_ticket (
  user_id BIGINT UNSIGNED NOT NULL,
  ticket_id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (user_id, ticket_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE TABLE ticket_gains (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  ticket_id BIGINT UNSIGNED NOT NULL,
  rank TINYINT NOT NULL,
  gain DECIMAL(12,2) NOT NULL,
  computed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uniq_ticket_rank (ticket_id, rank),
  FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);
```

---

## Indexing Essentials

> Goal: match **WHERE**/**JOIN** columns (leftmost rule for composites). Keep indexes lean.

```sql
-- Single & composite
CREATE INDEX idx_ticket_user_date ON tickets (user_id, draw_date);

-- Covering index (includes): use composite to cover common query
-- Example query: WHERE user_id=? AND draw_date BETWEEN ? AND ? ORDER BY draw_date DESC
-- Index above covers (user_id, draw_date), helping range + sort

-- Fulltext (MySQL 8.0, InnoDB)
ALTER TABLE tickets ADD FULLTEXT idx_tickets_numbers (numbers);
-- Tip: for JSON, create a generated column and index it.

-- Generated column + index (for JSON attribute)
ALTER TABLE tickets
  ADD COLUMN numbers_str VARCHAR(255) AS (JSON_UNQUOTE(JSON_EXTRACT(numbers,'$.n'))) STORED,
  ADD INDEX idx_numbers_str (numbers_str);
```

### Index Tips

* Put most selective column **first** in a composite (subject to query pattern).
* Don’t duplicate indexes (MySQL may create redundant ones via FKs).
* Avoid indexing low-cardinality columns alone (e.g., boolean) — combine.
* Consider **`EXPLAIN ANALYZE`** to validate plan & timing.

---

## CRUD Patterns

```sql
-- Insert
INSERT INTO users (email, password_hash) VALUES ('a@b.com', UNHEX('...'));

-- Upsert (MySQL 8)
INSERT INTO ticket_gains (ticket_id, rank, gain)
VALUES (123, 9, 2.50)
ON DUPLICATE KEY UPDATE gain = VALUES(gain), computed_at = CURRENT_TIMESTAMP;

-- Update
UPDATE tickets SET amount = amount + 2 WHERE id = 10;

-- Delete
DELETE FROM tickets WHERE id = 10;
```

### Query Examples

```sql
-- Range, sort, limit (use composite index user_id, draw_date)
SELECT id, draw_date, amount
FROM tickets
WHERE user_id = ? AND draw_date BETWEEN ? AND ?
ORDER BY draw_date DESC
LIMIT 50 OFFSET 0;

-- Join with aggregation
SELECT u.id, u.email, COUNT(t.id) AS ticket_count, COALESCE(SUM(g.gain),0) AS total_gain
FROM users u
LEFT JOIN tickets t ON t.user_id = u.id
LEFT JOIN ticket_gains g ON g.ticket_id = t.id
GROUP BY u.id, u.email
HAVING ticket_count > 0
ORDER BY total_gain DESC;
```

---

## Filtering & Joins Quickies

```sql
-- CTEs (WITH)
WITH recent AS (
  SELECT id, user_id, draw_date FROM tickets
  WHERE draw_date >= CURRENT_DATE - INTERVAL 30 DAY
)
SELECT * FROM recent r JOIN users u ON u.id = r.user_id;

-- Window functions
SELECT ticket_id, gain,
       RANK() OVER (PARTITION BY ticket_id ORDER BY gain DESC) AS rnk
FROM ticket_gains;

-- JSON predicates
SELECT id FROM tickets
WHERE JSON_CONTAINS(numbers, '5', '$.n');
```

---

## Views

```sql
CREATE OR REPLACE VIEW v_user_totals AS
SELECT u.id AS user_id, u.email,
       COUNT(t.id) AS ticket_count,
       COALESCE(SUM(g.gain),0) AS total_gain
FROM users u
LEFT JOIN tickets t ON t.user_id = u.id
LEFT JOIN ticket_gains g ON g.ticket_id = t.id
GROUP BY u.id, u.email;

-- Use
SELECT * FROM v_user_totals WHERE total_gain > 0 ORDER BY total_gain DESC;

-- Drop
DROP VIEW IF EXISTS v_user_totals;
```

---

## Stored Procedures & Functions

```sql
DELIMITER $$
CREATE PROCEDURE p_add_ticket(
  IN p_user BIGINT UNSIGNED,
  IN p_draw DATE,
  IN p_numbers JSON,
  IN p_amount DECIMAL(10,2)
)
BEGIN
  INSERT INTO tickets (user_id, draw_date, numbers, amount)
  VALUES (p_user, p_draw, p_numbers, p_amount);
END $$
DELIMITER ;

-- Call
CALL p_add_ticket(1, '2025-08-15', JSON_OBJECT('n', '1,2,3,4,5+6'), 2.50);

-- Scalar function example
DELIMITER $$
CREATE FUNCTION f_is_weekend(p_date DATE)
RETURNS TINYINT DETERMINISTIC
BEGIN
  RETURN (DAYOFWEEK(p_date) IN (1,7)); -- 1=Sunday, 7=Saturday
END $$
DELIMITER ;
```

> Use **IN/OUT/INOUT** params, and mark functions **DETERMINISTIC** if they are.

---

## Triggers

```sql
-- BEFORE INSERT: normalize email
DELIMITER $$
CREATE TRIGGER trg_users_bi
BEFORE INSERT ON users FOR EACH ROW
BEGIN
  SET NEW.email = LOWER(TRIM(NEW.email));
END $$
DELIMITER ;

-- AFTER INSERT: initialize gain record (example)
DELIMITER $$
CREATE TRIGGER trg_ticket_ai
AFTER INSERT ON tickets FOR EACH ROW
BEGIN
  INSERT INTO ticket_gains(ticket_id, rank, gain)
  VALUES (NEW.id, 9, 0.00)
  ON DUPLICATE KEY UPDATE gain = VALUES(gain);
END $$
DELIMITER ;
```

> Prefer `BEFORE` to adjust values, `AFTER` to write dependent rows. Keep trigger logic short.

---

## Transactions & Concurrency

```sql
-- Start / commit / rollback
START TRANSACTION;
  UPDATE accounts SET balance = balance - 10 WHERE id = 1;
  UPDATE accounts SET balance = balance + 10 WHERE id = 2;
COMMIT; -- or ROLLBACK;

-- Isolation level (session)
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

Tips:

* Always use **InnoDB**.
* Wrap multi‑statement business ops in a transaction.
* Use **`SELECT ... FOR UPDATE`** to lock rows you will modify.

---

## Analyzing Queries

```sql
EXPLAIN SELECT * FROM tickets WHERE user_id = 42 AND draw_date >= '2025-01-01';
EXPLAIN ANALYZE SELECT * FROM tickets WHERE user_id = 42 AND draw_date >= '2025-01-01';

SHOW INDEX FROM tickets;  -- existing indexes
SHOW STATUS LIKE 'Handler%'; -- low-level counters (optional)
```

---

## Users & Privileges

```sql
CREATE USER 'api'@'%' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'api'@'%';
FLUSH PRIVILEGES;

-- Roles (8.0+)
CREATE ROLE 'app_readwrite';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_readwrite';
GRANT 'app_readwrite' TO 'api'@'%';
SET DEFAULT ROLE 'app_readwrite' TO 'api'@'%';
```

---

## Dump & Restore

```bash
# Dump schema + data
mysqldump -u USER -p --routines --triggers mydb > mydb.sql

# Restore
mysql -u USER -p mydb < mydb.sql
```

---

## Performance Quick Wins

* Add composite indexes to match **(WHERE + JOIN + ORDER BY)**, follow leftmost rule.
* Avoid `SELECT *` in hot paths; select needed columns (enables covering).
* Normalize first; denormalize selectively with **generated columns** or materialized summary tables.
* Audit with `EXPLAIN ANALYZE`; compare before/after.
* Keep transactions short; avoid long‑running locks.
* Use `LIMIT` with an indexed pagination key (`WHERE (user_id, id) > (?, ?) ORDER BY user_id, id`).

---

## Extras

```sql
-- UUIDs as BINARY(16) (compact); store UUID_TO_BIN(uuid, true) for time‑ordered
ALTER TABLE users ADD COLUMN uid BINARY(16) NULL,
  ADD UNIQUE KEY uq_users_uid (uid);

-- Inserting UUID (ordered)
INSERT INTO users (email, password_hash, uid)
VALUES ('x@y.com', UNHEX('...'), UUID_TO_BIN(UUID(), TRUE));

-- JSON validation
ALTER TABLE tickets ADD CONSTRAINT chk_numbers_json CHECK (JSON_VALID(numbers));

-- Partial-like indexing via generated columns
ALTER TABLE tickets
  ADD COLUMN draw_year SMALLINT AS (YEAR(draw_date)) STORED,
  ADD INDEX idx_draw_year_user (draw_year, user_id);
```

---

## Cheat Ready: Copy Blocks

**Create table with timestamps**

```sql
CREATE TABLE t (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;
```

**Covering index for range + sort**

```sql
CREATE INDEX idx_u_date ON tickets (user_id, draw_date);
SELECT id, draw_date, amount
FROM tickets
WHERE user_id=? AND draw_date BETWEEN ? AND ?
ORDER BY draw_date DESC
LIMIT 50;
```

**EXPLAIN ANALYZE**

```sql
EXPLAIN ANALYZE SELECT ...;
```

---

*End of cheatsheet — update as your schema evolves.*
