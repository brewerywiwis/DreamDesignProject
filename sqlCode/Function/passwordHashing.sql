DROP FUNCTION IF EXISTS passwordHashing;
DELIMITER $$
CREATE FUNCTION passwordHashing(plainPassword VARCHAR(50) , salt VARCHAR(50))
	RETURNS VARCHAR(50)
	DETERMINISTIC
BEGIN
	RETURN sha1(CONCAT( plainPassword , salt));
END $$
DELIMITER ;


-- test -> select passwordHashing('123456','kr34g');