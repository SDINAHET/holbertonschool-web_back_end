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
