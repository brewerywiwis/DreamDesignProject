SELECT U.username , tmp.total_money
FROM user U , 
	(SELECT M.did , sum(T.amount) as total_money
	FROM transaction T , matchs M
	GROUP BY M.did) tmp
WHERE tmp.did = U.uid
ORDER BY tmp.total_money DESC
LIMIT 5


-- ค้นหา designer ที่มั่งคั่งที่สุด N (= 5) คนแรกของเว็บไซต์