-- set global log_bin_trust_function_creators=1;
DROP TRIGGER IF EXISTS usernameToLower;

CREATE TRIGGER usernameToLower
BEFORE INSERT
ON user FOR EACH ROW
SET NEW.username = LOWER(NEW.username);
\! echo "Create usernameToLower trigger"