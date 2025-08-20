-- 4-store.sql
-- Create a trigger that decreases items.quantity after inserting a new order

DROP TRIGGER IF EXISTS decrease_quantity_after_insert;

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
     SET quantity = quantity - NEW.number
   WHERE name = NEW.item_name;
END$$

DELIMITER ;
