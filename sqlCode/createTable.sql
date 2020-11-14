CREATE TABLE IF NOT EXISTS user(
   uid BIGINT,
   username VARCHAR(20),
   password VARCHAR(20),
   PRIMARY KEY (uid)
);

CREATE TABLE IF NOT EXISTS designer(
   uid BIGINT,
   bio VARCHAR(100),
   reviewScore FLOAT,
   PRIMARY KEY (uid)
);

CREATE TABLE IF NOT EXISTS customer(
   uid BIGINT,
   PRIMARY KEY (uid)
);

CREATE TABLE IF NOT EXISTS admin(
   uid BIGINT,
   PRIMARY KEY (uid)
);

CREATE TABLE IF NOT EXISTS contract(
    ctid BIGINT NOT NULL AUTO_INCREMENT,
    detail VARCHAR(300),
    mid VARCHAR(15),
    PRIMARY KEY (ctid)
);

CREATE TABLE IF NOT EXISTS jobposting(
    jid BIGINT NOT NULL AUTO_INCREMENT,
    did VARCHAR(15),
    sampleWorks BLOB,
    description VARCHAR(500),
    PRIMARY KEY (jid)
);

CREATE TABLE IF NOT EXISTS transaction(
    tid BIGINT NOT NULL AUTO_INCREMENT,
    bank VARCHAR(50),
    amount FLOAT,
    status BOOLEAN,
    paymentMethod VARCHAR(50),
    PRIMARY KEY (tid)
);

CREATE TABLE IF NOT EXISTS advertisement(
    aid BIGINT NOT NULL AUTO_INCREMENT,
    uid VARCHAR(15),
    startDate DATE,
    endDate DATE,
    advertiserEmail VARCHAR(100),
    adPicture BLOB,
    PRIMARY KEY (aid)
);

CREATE TABLE IF NOT EXISTS matchs(
    mid BIGINT NOT NULL AUTO_INCREMENT,
    did VARCHAR(15),
    cid VARCHAR(15),
    tid VARCHAR(15),
    score FLOAT,
    PRIMARY KEY (mid)
);