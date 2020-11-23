SELECT U.username , tmp.total_money
FROM user U , 
	(SELECT M.did , sum(T.amount) as total_money 
	FROM transaction T , matchs M
    WHERE T.tid = M.tid
	GROUP BY M.did) tmp
WHERE tmp.did = U.uid
ORDER BY tmp.total_money DESC
LIMIT 5