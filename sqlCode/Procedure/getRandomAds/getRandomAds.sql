-- show procedure status where Db = 'project';
DROP PROCEDURE IF EXISTS getRandomAds;

DELIMITER $$
CREATE PROCEDURE getRandomAds(IN N INT)
BEGIN
    SELECT a.advertiserEmail, 
        (SELECT b.aid 
        FROM Advertisement b 
        WHERE endDate > NOW() AND a.advertiserEmail = b.advertiserEmail 
        ORDER by rand() 
        LIMIT 1) AS random_aid
    FROM Advertisement a
    WHERE endDate > NOW() 
    GROUP BY a.advertiserEmail
    ORDER by rand()
    LIMIT N;
END $$
DELIMITER ;