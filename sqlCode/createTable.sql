CREATE TABLE IF NOT EXISTS user(
   uid VARCHAR(15),
   username VARCHAR(20),
   password VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS designer(
   uid VARCHAR(15),
   bio VARCHAR(100),
   reviewScore FLOAT
);

CREATE TABLE IF NOT EXISTS customer(
   uid VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS admin(
   uid VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS contract(
    ctid VARCHAR(15),
    detail VARCHAR(300),
    mid VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS jobposting(
    jid VARCHAR(15),
    did VARCHAR(15),
    sampleWorks BLOB,
    description VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS transaction(
    tid VARCHAR(15),
    bank VARCHAR(50),
    amount FLOAT,
    status BOOLEAN,
    paymentMethod VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS advertisement(
    aid VARCHAR(15),
    uid VARCHAR(15),
    startDate DATE,
    endDate DATE,
    advertiserEmail VARCHAR(100),
    adPicture BLOB
);

CREATE TABLE IF NOT EXISTS matchs(
    mid VARCHAR(15),
    did VARCHAR(15),
    cid VARCHAR(15),
    tid VARCHAR(15),
    score FLOAT
);