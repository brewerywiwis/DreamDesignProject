\! clear
\! echo "Begin test usernameToLower"

\! echo "Show user table"
SELECT * FROM user WHERE uid > 2000000000000;

\! echo "Insert somsak"
\! echo "Insert SomChAi"
\! echo "Insert SOMYING"
\! echo "Insert SoM_$$!&#"
INSERT INTO user
VALUES (2234567892234, 'somsak', 's1223ssd', NULL),
    (2234567892235, 'SomChAi', 'g9ad6fah2es8', NULL),
    (2234567892236, 'SOMYING', 'd3k4a34ssda', NULL),
    (2234567893236, 'SoM_$$!&#', 'd3k4a34ssda', NULL);

\! echo "Result"
SELECT * FROM user WHERE uid > 2000000000000;