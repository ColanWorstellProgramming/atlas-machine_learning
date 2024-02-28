-- SQL
delimiter //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT(10, 2)
BEGIN
    DECLARE result FLOAT(10, 2);

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END;//

delimiter ;