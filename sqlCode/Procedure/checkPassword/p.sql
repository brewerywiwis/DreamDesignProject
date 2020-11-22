DROP PROCEDURE IF EXISTS loginWithUsernamePassword;

DELIMITER $$
CREATE PROCEDURE loginWithUsernamePassword(
    IN _username VARCHAR(20) , 
    IN _password VARCHAR(20) ,
    OUT response BOOLEAN 
    )
BEGIN
    DECLARE salt VARCHAR(50);
    DECLARE encryptedPassword VARCHAR(50);
    
    SET response = FALSE;
    
	SELECT U.salt into salt
    FROM user U
    WHERE U.username = _username
    LIMIT 1;
    
    IF salt IS NULL THEN
		SET encryptedPassword = _password;
	ELSE
		SELECT passwordHashing(_password,salt) into encryptedPassword;
    END IF;
    
    IF EXISTS 
		(SELECT U.username
		FROM user U
		WHERE U.username = _username 
        AND U.password = encryptedPassword) 
	THEN
        SET response = TRUE;
	END IF;
    
END $$
DELIMITER ;