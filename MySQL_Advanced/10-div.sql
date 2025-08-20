-- 10-div.sql
-- Create function SafeDiv(a, b) -> a / b, or 0 if b = 0

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
  RETURN IF(b = 0, 0, a / b);
END$$

DELIMITER ;
