\! clear
\! echo "Test 1 Cascade Update: User <- Designer <- Match"
\! echo "Designer table"
SELECT uid as 'Designer_uid' FROM Designer;
\! echo "User table WHERE uid = 1234567891238"
SELECT * FROM User WHERE uid = 1234567891238;
\! echo "User table WHERE uid = 2234567891238"
SELECT * FROM User WHERE uid = 2234567891238;
\! echo "User Matchs WHERE uid = 1234567891238"
SELECT * FROM Matchs WHERE did = 1234567891238;
\! echo "User Matchs WHERE uid = 2234567891238"
SELECT * FROM Matchs WHERE did = 2234567891238;
\! echo ""
\! echo "=========== UPDATE User SET uid = 2234567891238 WHERE uid = 1234567891238"
\! echo ""
\! echo ""
UPDATE User SET uid = 2234567891238 WHERE uid = 1234567891238;
\! echo "FOREIGN KEY (uid) REFERENCES user(uid) ON UPDATE CASCADE ON DELETE CASCADE"
\! echo "Designer table"
SELECT uid as 'Designer_uid' FROM Designer;
\! echo "User table WHERE uid = 1234567891238"
SELECT * FROM User WHERE uid = 1234567891238;
\! echo "User table WHERE uid = 2234567891238"
SELECT * FROM User WHERE uid = 2234567891238;
\! echo "User Matchs WHERE uid = 1234567891238"
SELECT * FROM Matchs WHERE did = 1234567891238;
\! echo "User Matchs WHERE uid = 2234567891238"
SELECT * FROM Matchs WHERE did = 2234567891238;
\! echo "========================================================================="
\! echo "========================================================================="
\! echo "========================================================================="
\! echo "Test 2 Cascade Remove: User <- Designer <- Match <- Contract"
\! echo "User table WHERE uid = 2234567891238"
SELECT * FROM User WHERE uid = 2234567891238;
\! echo "Designer table"
SELECT uid as 'Designer_uid' FROM Designer;
\! echo "User Matchs WHERE uid = 2234567891238"
SELECT * FROM Matchs WHERE did = 2234567891238;
\! echo "User contract WHERE mid = 2000000002"
SELECT ctid, mid FROM Contract WHERE mid = 2000000002;
\! echo ""
\! echo "=========== DELETE FROM User WHERE uid = 2234567891238"
\! echo ""
\! echo ""
DELETE FROM User WHERE uid = 2234567891238;
\! echo "User table WHERE uid = 2234567891238"
SELECT * FROM User WHERE uid = 2234567891238;
\! echo "Designer table"
SELECT uid as 'Designer_uid' FROM Designer;
\! echo "User Matchs WHERE uid = 2234567891238"
SELECT * FROM Matchs WHERE did = 2234567891238;
\! echo "User contract WHERE mid = 2000000002"
SELECT ctid, mid FROM Contract WHERE mid = 2000000002;
\! echo "========================================================================="
\! echo "========================================================================="
\! echo "========================================================================="
\! echo "Test 3 Cascade Remove: User <- Admin then SET NULL Admin <- advertisement"
\! echo "Admin table"
SELECT * FROM Admin;
\! echo "User table WHERE uid = 1234567891244"
SELECT * FROM User WHERE uid = 1234567891244;
\! echo "Advertisement table where uid = 1234567891244"
SELECT aid, uid, startDate, endDate, advertiserEmail FROM Advertisement WHERE uid = 1234567891244;
\! echo ""
\! echo "=========== DELETE FROM User WHERE uid = 1234567891244"
\! echo ""
\! echo ""
DELETE FROM User WHERE uid = 1234567891244;
\! echo "Admin table"
SELECT * FROM Admin;
\! echo "User table WHERE uid = 1234567891244"
SELECT * FROM User WHERE uid = 1234567891244;
\! echo "Advertisement table where uid = 1234567891244"
SELECT aid, uid, startDate, endDate, advertiserEmail FROM Advertisement WHERE uid = 1234567891244;
\! echo "Advertisement table where uid = 1234567891244"
SELECT aid, uid, startDate, endDate, advertiserEmail FROM Advertisement WHERE aid IN (4000000001, 4000000002);
