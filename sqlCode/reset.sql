DROP TABLE IF EXISTS contract;
DROP TABLE IF EXISTS matchs;
DROP TABLE IF EXISTS jobposting;
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS advertisement;
DROP TABLE IF EXISTS designer;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user(
    uid BIGINT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20),
    password VARCHAR(50),
    salt VARCHAR(50),
    PRIMARY KEY (uid),
    UNIQUE KEY(uid)
    -- ADD UNIQUE INDEX `uid_UNIQUE` (`uid` ASC);
);
CREATE TABLE IF NOT EXISTS designer(
    uid BIGINT NOT NULL AUTO_INCREMENT,
    bio VARCHAR(100),
    reviewScore FLOAT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES user(uid) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE KEY(uid)
    -- ADD UNIQUE INDEX `uid_UNIQUE` (`uid` ASC);
);
CREATE TABLE IF NOT EXISTS customer(
    uid BIGINT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES user(uid) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE KEY(uid)
    -- ADD UNIQUE INDEX `uid_UNIQUE` (`uid` ASC);
);
CREATE TABLE IF NOT EXISTS admin(
    uid BIGINT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES user(uid) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE KEY(uid)
    -- ADD UNIQUE INDEX `uid_UNIQUE` (`uid` ASC);
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
    FOREIGN KEY (uid) REFERENCES admin(uid) ON UPDATE CASCADE ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS jobposting(
    jid BIGINT NOT NULL AUTO_INCREMENT,
    did BIGINT,
    sampleWorks BLOB,
    description VARCHAR(500),
    PRIMARY KEY (jid),
    FOREIGN KEY (did) REFERENCES designer(uid) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS matchs(
    mid BIGINT NOT NULL AUTO_INCREMENT,
    did BIGINT,
    cid BIGINT,
    tid BIGINT,
    score INT,
    PRIMARY KEY (mid),
    FOREIGN KEY (did) REFERENCES designer(uid) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES customer(uid) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (tid) REFERENCES transaction(tid) ON UPDATE CASCADE ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS contract(
    ctid BIGINT NOT NULL AUTO_INCREMENT,
    detail VARCHAR(300),
    mid BIGINT,
    PRIMARY KEY (ctid),
    FOREIGN KEY (mid) REFERENCES matchs(mid) ON UPDATE CASCADE ON DELETE CASCADE
);
INSERT INTO user
VALUES (1234567891234, 'somsak', 's1223ssd', NULL),
    (1234567891235, 'somchai', 'g9ad6fah2es8', NULL),
    (1234567891236, 'somying', 'd3k4a34ssda', NULL),
    (1234567891237, 'jasta', '53319231', NULL),
    (1234567891238, 'daviddesign', '7623442323', NULL),
    (1234567891239, 'karen', 'gks3dsa2ew23', NULL),
    (1234567891240, 'mike1988', 'dsas2sad31asd', NULL),
    (1234567891241, 'pancake', 'edwqw3fdl54', NULL),
    (1234567891242, 'pitchaya', 'egslireas', NULL),
    (1234567891243, 'bankgraphic', '346623178466', NULL),
    (1234567891244, 'george', 'afs2132g2314df6221', NULL),
    (1234567891245, 'chompu', 'g23fw4521a322dafd4', NULL);
INSERT INTO designer
VALUES (
        1234567891236,
        'Proficient in using Photoshop, Illustrator and Premiere Pro. Has been a graphic designer since 2011.',
        NULL
    ),
    (
        1234567891237,
        'Work quickly and carefully. Good at using Photoshop and Illustrator.',
        NULL
    ),
    (
        1234567891238,
        'Proficient in using Photoshop, Illustrator, Premiere and Aftereffect.',
        NULL
    ),
    (
        1234567891241,
        'Proficient in using Photoshop. Experience in graphic at least 3 years. Work with heart.',
        NULL
    ),
    (
        1234567891243,
        'I am a dedicated ads designer with direct experience in this field, Proficient in using Photoshop.',
        NULL
    );
INSERT INTO customer
VALUES (1234567891234),
    (1234567891235),
    (1234567891239),
    (1234567891240),
    (1234567891242);
INSERT INTO admin
VALUES (1234567891244),
    (1234567891245);
INSERT INTO advertisement
VALUES (
        4000000001,
        1234567891244,
        '2020/11/10',
        '2021/1/10',
        'lazada@gmail.com',
        'BLOB of a1.png'
    ),
    (
        NULL,
        1234567891244,
        '2020/11/11',
        '2021/2/11',
        'lazada@gmail.com',
        'BLOB of a2.png'
    ),
    (
        NULL,
        1234567891245,
        '2020/11/12',
        '2021/2/12',
        'shoppee@hotmail.com',
        'BLOB of a3.png'
    ),
    (
        NULL,
        1234567891245,
        '2020/11/13',
        '2021/1/13',
        'shoppee@hotmail.com',
        'BLOB of a4.png'
    ),
    (
        NULL,
        1234567891245,
        '2020/11/14',
        '2021/2/14',
        'adthailand@gmail.com',
        'BLOB of a5.png'
    );
INSERT INTO transaction (tid, bank, amount, status)
VALUES (
        5000000001,
        'Government Savings Bank',
        600,
        false
    ),
    (NULL, 'CIMB', 1000, false),
    (NULL, 'Thanachart ', 750, false),
    (NULL, 'Krung Thai', 1500, false);
INSERT INTO transaction
VALUES (
        NULL,
        'Krungsri',
        1700,
        true,
        'mobile banking payment'
    );
INSERT INTO matchs (mid, did, cid, tid)
VALUES (
        2000000001,
        1234567891243,
        1234567891234,
        5000000003
    ),
    (NULL, 1234567891238, 1234567891242, 5000000006),
    (NULL, 1234567891236, 1234567891235, 5000000001),
    (NULL, 1234567891241, 1234567891240, 5000000004),
    (NULL, 1234567891237, 1234567891239, 5000000002);
INSERT INTO jobposting
VALUES (
        NULL,
        1234567891236,
        'BLOB of j1.png',
        '9 years of design experience, the best quality at an affordable price. Feel free to send me a message about your desire banner :D'
    ),
    (
        NULL,
        1234567891243,
        'BLOB of j2.png',
        'Are you looking for an dedicated ads designer with direct experience in this field? Price is negotiable.'
    );
INSERT INTO contract
VALUES (
        1000000001,
        '1. designer will design 1 brochure  for 1000 baht 2. designer will finish the work within 3 days 3. no more than 2 redesign 4. customer will receive .JPG, .PDF and .AI files',
        2000000001
    ),
    (
        NULL,
        '1. designer will design 3 banners for 1500 baht 2. designer will finish the work within 3 days 3. no more than 3 redesign 4. customer will receive .JPG and .PNG files 5. additional 100 baht for each .AI file',
        2000000002
    ),
    (
        NULL,
        '1. designer will design 1 banner for 600 baht 2. designer will finish the work within 2 days 3. 2 times free redesign. if redesign more than 2 times, it will cost 100 bath for each redesign 4. customer will receive .JPG and .PNG files',
        2000000003
    ),
    (
        NULL,
        '1. designer will design 1 business card(both front and back) for 750 baht 2. designer will finish the work within 3 days 3. no more than 2 redesign 4. customer will receive .JPG, .PDF and .AI files',
        2000000004
    ),
    (
        NULL,
        '1. designer will design 1 logo for 1700 baht 2. designer will finish the work within 2 days 3. no more than 3 redesign customer will receive .JPG, .PDF and .AI files',
        2000000005
    );
\! clear
\! echo "Reset data complete"