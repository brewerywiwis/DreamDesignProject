-- set global log_bin_trust_function_creators=1;
DROP TRIGGER IF EXISTS updateReviewScoreInMatch;

DELIMITER $$
CREATE TRIGGER updateReviewScoreInMatch
AFTER UPDATE
ON matchs FOR EACH ROW
BEGIN
    UPDATE designer
    SET reviewScore = (
            SELECT AVG(score)
            FROM Matchs 
            WHERE did = NEW.did
        )
    WHERE uid = NEW.did;
END $$
DELIMITER ;