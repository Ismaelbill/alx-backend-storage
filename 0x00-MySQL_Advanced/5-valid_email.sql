-- SQL script that creates a trigger that resets the attribute valid_email ONLY
-- WHEN the email has been CHANGED.
DELIMITER //
CREATE Trigger RESET BEFORE
UPDATE
    ON users FOR each ROW BEGIN IF NEW.email != old.email THEN
SET
    NEW.valid_email = 0;

END IF;

END //
DELIMITER;