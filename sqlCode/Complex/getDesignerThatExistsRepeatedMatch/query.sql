-- Get Top N (=5) designer that exists repeated match from customer order by designer reviewScore --

SELECT D2.uid , D2.reviewScore
FROM designer D2
WHERE EXISTS
	(SELECT D.uid
	FROM matchs M , designer D , customer C
	WHERE C.uid = M.cid AND D.uid = M.did AND D2.uid = D.uid
	GROUP BY D.uid , C.uid
	HAVING count(M.mid) >= 1)
ORDER BY D2.reviewScore DESC
LIMIT 5;