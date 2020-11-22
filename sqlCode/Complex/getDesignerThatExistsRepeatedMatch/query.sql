-- Get Top N (=5) designer that exists repeated match from customer order by designer reviewScore --

SELECT D2.uid , D2.reviewScore
FROM designer D2
WHERE EXISTS
	(SELECT M.did
	FROM matchs M 
	WHERE D2.uid = M.did
	GROUP BY M.cid , M.did
	HAVING count(M.mid) > 1)
ORDER BY D2.reviewScore DESC
LIMIT 5;