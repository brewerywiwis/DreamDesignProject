DROP PROCEDURE IF EXISTS createUserWithEncryptedPassword;

DELIMITER $$
CREATE PROCEDURE createUserWithEncryptedPassword(
	IN _uid BIGINT ,
    IN _username VARCHAR(20) , 
    IN _password VARCHAR(20) 
    )
BEGIN
	DECLARE salt VARCHAR(50);
	DECLARE encryptedPassword VARCHAR(50);
	select md5(rand()) into salt;
	select passwordHashing(_password,salt) into encryptedPassword;
	
    IF _uid != NULL THEN
		INSERT INTO user (username, password , salt)
		VALUES (_username,encryptedPassword,salt);
	ELSE 
		INSERT INTO user (uid,username, password , salt)
		VALUES (_uid,_username,encryptedPassword,salt);
    END IF;
    
    COMMIT;
END $$
DELIMITER ;

-- note need to add salt field in users