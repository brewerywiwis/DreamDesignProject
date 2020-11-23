SELECT d.uid
FROM designer d
INNER JOIN jobposting j ON d.uid = j.did;

SELECT j.did
FROM designer d, jobposting j
WHERE d.uid = j.did;

SELECT a.aid 
FROM advertisement a
WHERE startDate < NOW() 
	AND endDate > NOW() 
LIMIT 2;

SELECT a.aid 
FROM advertisement a
WHERE NOW() BETWEEN startDate AND endDate
LIMIT 2;