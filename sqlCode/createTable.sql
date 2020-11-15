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
   PRIMARY KEY (uid),
   FOREIGN KEY (uid) REFERENCES user(uid)
);

CREATE TABLE IF NOT EXISTS customer(
   uid BIGINT,
   PRIMARY KEY (uid),
   FOREIGN KEY (uid) REFERENCES user(uid)
);

CREATE TABLE IF NOT EXISTS admin(
   uid BIGINT,
   PRIMARY KEY (uid),
   FOREIGN KEY (uid) REFERENCES user(uid)
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
    uid BIGINT,
    startDate DATE,
    endDate DATE,
    advertiserEmail VARCHAR(100),
    adPicture BLOB,
    PRIMARY KEY (aid),
    FOREIGN KEY (uid) REFERENCES admin(uid)
);

CREATE TABLE IF NOT EXISTS jobposting(
    jid BIGINT NOT NULL AUTO_INCREMENT,
    did BIGINT,
    sampleWorks BLOB,
    description VARCHAR(500),
    PRIMARY KEY (jid),
    FOREIGN KEY (did) REFERENCES designer(uid)
);

CREATE TABLE IF NOT EXISTS matchs(
    mid BIGINT NOT NULL AUTO_INCREMENT,
    did BIGINT,
    cid BIGINT,
    tid BIGINT,
    score FLOAT,
    PRIMARY KEY (mid),
    FOREIGN KEY (did) REFERENCES designer(uid),
    FOREIGN KEY (cid) REFERENCES customer(uid),
    FOREIGN KEY (tid) REFERENCES transaction(tid)
);

CREATE TABLE IF NOT EXISTS contract(
    ctid BIGINT NOT NULL AUTO_INCREMENT,
    detail VARCHAR(300),
    mid BIGINT,
    PRIMARY KEY (ctid),
    FOREIGN KEY (mid) REFERENCES matchs(mid)
);