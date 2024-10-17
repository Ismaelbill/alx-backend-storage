-- SQL script that creates a trigger that decreases the quantity of an item
CREATE trigger decrement
AFTER INSERT
    ON orders FOR each ROW
UPDATE
    items
SET
    quantity = quantity - NEW.number
WHERE
    NAME = NEW.item_name;