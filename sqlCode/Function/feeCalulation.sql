DROP FUNCTION IF EXISTS feeCalculation;
DELIMITER $$
CREATE FUNCTION feeCalculation(amount FLOAT)
	RETURNS FLOAT
	DETERMINISTIC
BEGIN
	RETURN (amount/10);
END $$
DELIMITER ;

-- test -> select amount, feeCalculation(amount) from transaction;
