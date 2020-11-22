\! clear
\! echo "Begin test updateReviewScoreInMatch"

INSERT INTO Matchs VALUES
(NULL, 1234567891237, 1234567891239, 5000000002, NULL),
(NULL, 1234567891237, 1234567891239, 5000000002, NULL),
(NULL, 1234567891237, 1234567891239, 5000000002, NULL),
(NULL, 1234567891237, 1234567891239, 5000000002, NULL);

\! echo "Show matchs data where did = 1234567891237"
SELECT mid, did, score
FROM matchs
WHERE did = 1234567891237;

\! echo "Show designer reviewScore where did = 1234567891237"
SELECT uid, reviewScore
FROM designer
WHERE uid = 1234567891237;
\! echo "========================================================================="

-- Update
\! echo "Update mid = 2000000005 score = 9"
UPDATE Matchs
SET score = 9
WHERE mid = 2000000005;

\! echo "Show matchs data where did = 1234567891237"
SELECT mid, did, score
FROM matchs
WHERE did = 1234567891237;

\! echo "Show designer reviewScore where did = 1234567891237"
SELECT uid, reviewScore
FROM designer
WHERE uid = 1234567891237;

\! echo "========================================================================="
-- Update
\! echo "Update mid = 2000000007 score = 3"
UPDATE Matchs
SET score = 3
WHERE mid = 2000000007;

\! echo "Show matchs data where did = 1234567891237"
SELECT mid, did, score
FROM matchs
WHERE did = 1234567891237;

\! echo "Show designer reviewScore where did = 1234567891237"
SELECT uid, reviewScore
FROM designer
WHERE uid = 1234567891237;

\! echo "========================================================================="
-- Update
\! echo "Update mid = 2000000008 score = 4"
UPDATE Matchs
SET score = 4
WHERE mid = 2000000008;

\! echo "Show matchs data where did = 1234567891237"
SELECT mid, did, score
FROM matchs
WHERE did = 1234567891237;

\! echo "Show designer reviewScore where did = 1234567891237"
SELECT uid, reviewScore
FROM designer
WHERE uid = 1234567891237;

\! echo "========================================================================="
-- Update
\! echo "Update mid = 2000000007 score = 7"
UPDATE Matchs
SET score = 7
WHERE mid = 2000000007;

\! echo "Show matchs data where did = 1234567891237"
SELECT mid, did, score
FROM matchs
WHERE did = 1234567891237;

\! echo "Show designer reviewScore where did = 1234567891237"
SELECT uid, reviewScore
FROM designer
WHERE uid = 1234567891237;