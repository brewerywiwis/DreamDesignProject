DELETE FROM Advertisement;

INSERT INTO Advertisement VALUES
(NULL, 1234567891244, '2020/10/10', '2020/11/11', 'lazada@gmail.com', 'BLOB of lazada0.png'), 
(NULL, 1234567891244, '2020/10/11', '2020/12/11', 'lazada@gmail.com', 'BLOB of lazada1.png'), 
(NULL, 1234567891244, '2020/10/10', '2020/11/12', 'lazada@gmail.com', 'BLOB of lazada2.png'), 
(NULL, 1234567891244, '2020/10/11', '2020/12/11', 'lazada@gmail.com', 'BLOB of lazada3.png'), 
(NULL, 1234567891244, '2020/10/10', '2020/11/13', 'lazada@gmail.com', 'BLOB of lazada4.png'), 
(NULL, 1234567891244, '2020/10/11', '2020/12/11', 'lazada@gmail.com', 'BLOB of lazada5.png'), 
(NULL, 1234567891244, '2020/10/10', '2020/11/14', 'lazada@gmail.com', 'BLOB of lazada6.png'), 
(NULL, 1234567891244, '2020/10/11', '2020/12/11', 'lazada@gmail.com', 'BLOB of lazada7.png'), 
(NULL, 1234567891245, '2020/10/12', '2020/12/12', 'shoppee@hotmail.com', 'BLOB of shopee0.png'), 
(NULL, 1234567891245, '2020/10/13', '2020/11/13', 'shoppee@hotmail.com', 'BLOB of shopee1.png'), 
(NULL, 1234567891245, '2020/10/12', '2020/12/12', 'shoppee@hotmail.com', 'BLOB of shopee2.png'), 
(NULL, 1234567891245, '2020/10/13', '2020/11/13', 'shoppee@hotmail.com', 'BLOB of shopee3.png'),
(NULL, 1234567891245, '2020/10/12', '2020/12/12', 'shoppee@hotmail.com', 'BLOB of shopee4.png'), 
(NULL, 1234567891245, '2020/10/13', '2020/11/13', 'shoppee@hotmail.com', 'BLOB of shopee5.png'),
(NULL, 1234567891245, '2020/10/12', '2020/12/12', 'shoppee@hotmail.com', 'BLOB of shopee6.png'), 
(NULL, 1234567891245, '2020/10/13', '2020/11/13', 'shoppee@hotmail.com', 'BLOB of shopee7.png'), 
(NULL, 1234567891245, '2020/10/14', '2020/11/14', 'adthailand@gmail.com', 'BLOB of adthailand0.png'),
(NULL, 1234567891245, '2020/10/14', '2020/12/14', 'adthailand@gmail.com', 'BLOB of adthailand1.png'), 
(NULL, 1234567891245, '2020/10/14', '2020/11/14', 'adthailand@gmail.com', 'BLOB of adthailand2.png'),
(NULL, 1234567891245, '2020/10/14', '2020/12/14', 'adthailand@gmail.com', 'BLOB of adthailand3.png');

SELECT advertiserEmail, GROUP_CONCAT(aid) AS aidList
FROM Advertisement
WHERE endDate > NOW()
GROUP BY advertiserEmail;

-- CALL Function to test
CALL getRandomAds(2);
CALL getRandomAds(2);
CALL getRandomAds(8);