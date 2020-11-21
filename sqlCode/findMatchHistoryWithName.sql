select mid,designer_name,username as customer_name,tid
from (SELECT mid,username as designer_name,cid,tid
FROM dreamdesignDB.matchs
join dreamdesignDB.user on dreamdesignDB.user.uid = matchs.did
) as T1
join dreamdesignDB.user on dreamdesignDB.user.uid = T1.cid