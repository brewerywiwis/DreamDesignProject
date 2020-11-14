INSERT INTO Contract VALUES 
(1000000001, '1. designer will design 1 brochure  for 1000 baht 2. designer will finish the work within 3 days 3. no more than 2 redesign 4. customer will receive .JPG, .PDF and .AI files', 2000000001), 
(1000000002, '1. designer will design 3 banners for 1500 baht 2. designer will finish the work within 3 days 3. no more than 3 redesign 4. customer will receive .JPG and .PNG files 5. additional 100 baht for each .AI file', 2000000002), 
(1000000003, '1. designer will design 1 banner for 600 baht 2. designer will finish the work within 2 days 3. 2 times free redesign. if redesign more than 2 times, it will cost 100 bath for each redesign 4. customer will receive .JPG and .PNG files', 2000000003), 
(1000000004, '1. designer will design 1 business card(both front and back) for 750 baht 2. designer will finish the work within 3 days 3. no more than 2 redesign 4. customer will receive .JPG, .PDF and .AI files', 2000000004), 
(1000000005, '1. designer will design 1 logo for 1700 baht 2. designer will finish the work within 2 days 3. no more than 3 redesign customer will receive .JPG, .PDF and .AI files', 2000000005);

INSERT INTO User VALUES
(1234567891234, 'somsak', 's1223ssd'), 
(1234567891235, 'somchai', 'g9ad6fah2es8'), 
(1234567891236, 'somying', 'd3k4a34ssda'), 
(1234567891237, 'jasta', '53319231'), 
(1234567891238, 'daviddesign', '7623442323'),  
(1234567891239, 'karen', 'gks3dsa2ew23'), 
(1234567891240, 'mike1988', 'dsas2sad31asd'),  
(1234567891241, 'pancake', 'edwqw3fdl54'),  
(1234567891242, 'pitchaya', 'egslireas'),  
(1234567891243, 'bankgraphic', '346623178466'),
(1234567891244, 'george', 'afs2132g2314df6221'),  
(1234567891245, 'chompu', 'g23fw4521a322dafd4');

INSERT INTO Designer VALUES
(1234567891236, 'Proficient in using Photoshop, Illustrator and Premiere Pro. Has been a graphic designer since 2011.', 9.4), 
(1234567891237, 'Work quickly and carefully. Good at using Photoshop and Illustrator.', 9.6), 
(1234567891238, 'Proficient in using Photoshop, Illustrator, Premiere and Aftereffect.', 9.6), 
(1234567891241, 'Proficient in using Photoshop. Experience in graphic at least 3 years. Work with heart.', 9.8), 
(1234567891243, 'I am a dedicated ads designer with direct experience in this field, Proficient in using Photoshop.', 9.6);

INSERT INTO Customer VALUES
(1234567891234), (1234567891235), (1234567891239), (1234567891240), (1234567891242);
 
INSERT INTO Admin VALUES
(1234567891244), (1234567891245); 

INSERT INTO Advertisement VALUES
(4000000001, 1234567891244, '10/11/20', '10/1/21', 'lazada@gmail.com', 'BLOB of a1.png'), 
(4000000002, 1234567891244, '11/11/20', '11/2/21', 'lazada@gmail.com', 'BLOB of a2.png'), 
(4000000003, 1234567891245, '12/11/20', '12/2/21', 'shoppee@hotmail.com', 'BLOB of a3.png'), 
(4000000004, 1234567891245, '13/11/20', '13/1/21', 'shoppee@hotmail.com', 'BLOB of a4.png'), 
(4000000005, 1234567891245, '14/11/20', '14/2/21', 'adthailand@gmail.com', 'BLOB of a5.png');

INSERT INTO Transaction (tid, bank, amount, status) VALUES
(5000000001, 'Government Savings Bank', 600, false), 
(5000000003, 'CIMB', 1000, false), 
(5000000004, 'Thanachart ', 750, false), 
(5000000005, 'Krung Thai', 1500, false);
INSERT INTO Transaction VALUES
(5000000002, 'Krungsri', 1700, true, 'mobile banking payment');

INSERT INTO Matchs (mid, did, cid, tid) VALUES
(2000000001, 1234567891243, 1234567891234, 5000000003), 
(2000000002, 1234567891238, 1234567891242, 5000000005), 
(2000000003, 1234567891236, 1234567891235, 5000000001), 
(2000000004, 1234567891241, 1234567891240, 5000000004);
INSERT INTO Matchs VALUES
(2000000005, 1234567891237, 1234567891239, 5000000002, 9.8);

INSERT INTO JobPosting VALUES
(6000000001, 1234567891236, 'BLOB of j1.png', '9 years of design experience, the best quality at an affordable price. Feel free to send me a message about your desire banner :D'), 
(6000000002, 1234567891243, 'BLOB of j2.png', 'Are you looking for an dedicated ads designer with direct experience in this field? Price is negotiable.');