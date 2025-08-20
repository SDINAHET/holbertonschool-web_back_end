-- 5-valid_email.sql
-- Reset users.valid_email only when the email value changes

DROP TRIGGER IF EXISTS reset_valid_email_on_update;

DELIMITER $$

CREATE TRIGGER reset_valid_email_on_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END$$

DELIMITER ;
