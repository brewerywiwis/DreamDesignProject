/*INSERT INTO matchs VALUES
(2000000006, 1234567891243, 1234567891234, NULL , NULL),
(2000000007, 1234567891248, 1234567891240, NULL , NULL),
(2000000008, 1234567891245, 1234567891233, NULL , NULL),
(2000000009, 1234567891242, 1234567891237, NULL , NULL),
(2000000010, 1234567891243, 1234567891235, NULL , NULL),
(2000000011, 1234567891243, 1234567891230, NULL , NULL),
(2000000012, 1234567891242, 1234567891232, NULL , NULL);

INSERT INTO user VALUES
(1234567891243, 'aaaaaaaaa' ,'aaaaaaaaa' , NULL),
(1234567891238, 'bbbbbbbbb' ,'bbbbbbbbb' , NULL),
(1234567891245, 'ccccccccc' ,'ccccccccc', NULL),
(1234567891242, 'ddddddddd' ,'ddddddddd', NULL),
(1234567891249, 'eeeeeeeee' ,'eeeeeeeee', NULL),
(1234567891240, 'fffffffff' ,'fffffffff', NULL),
(1234567891247, 'ggggggggg' ,'ggggggggg', NULL);*/

select mid,designer_name,username as customer_name,tid
from (SELECT mid,username as designer_name,cid,tid
FROM dreamdesignDB.matchs
join dreamdesignDB.user on dreamdesignDB.user.uid = matchs.did
) as T1
join dreamdesignDB.user on dreamdesignDB.user.uid = T1.cid