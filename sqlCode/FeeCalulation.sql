DROP FUNCTION IF EXISTS FeeCalculation;
DELIMITER $$
CREATE FUNCTION FeeCalculation(amount FLOAT)
	RETURNS FLOAT
	DETERMINISTIC
BEGIN
	RETURN (amount/10);
END $$
DELIMITER ;


-- test -> select amount, FeeCalculation(amount) from transaction;