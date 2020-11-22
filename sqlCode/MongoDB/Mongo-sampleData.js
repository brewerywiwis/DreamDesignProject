//ChatRoom sample data
db.ChatRoom.insert({
  rid: 3000000001,
  message: [
    { time: new Date("2020-11-11T16:13:50Z") },
    { time: new Date("2020-11-11T16:17:41Z") },
    { time: new Date("2020-11-11T16:18:53Z") },
  ],
  uid: [{ uid1: 1234567891235, uid2: 1234567891236 }],
});

db.ChatRoom.insert({
  rid: 3000000002,
  message: [
    { time: new Date("2020-11-11T18:31:03Z") },
    { time: new Date("2020-11-11T19:00:02Z") },
  ],
  uid: [{ uid1: 1234567891234, uid2: 1234567891243 }],
});

db.ChatRoom.insert({
  rid: 3000000003,
  message: [{ time: new Date("2020-11-12T09:54:43Z") }],
  uid: [{ uid1: 1234567891239, uid2: 1234567891237 }],
});

db.ChatRoom.insert({
  rid: 3000000004,
  message: [{ time: new Date("2020-11-12T13:15:04Z") }],
  uid: [{ uid1: 1234567891240, uid2: 1234567891241 }],
});

db.ChatRoom.insert({
  rid: 3000000005,
  message: [{ time: new Date("2020-11-14T16:46:21Z") }],
  uid: [{ uid1: 1234567891242, uid2: 1234567891238 }],
});

//Message sample data
db.Message.insert({
  time: new Date("2020-11-11T16:13:50Z"),
  message: "Hi Somying. I'd like you to design snack banner ads",
  rid: 3000000001,
  uid: 1234567891235,
});

db.Message.insert({
  time: new Date("2020-11-11T16:17:41Z"),
  message: "Hello Somchai. Let's talk about the detail of your banner",
  rid: 3000000001,
  uid: 1234567891236,
});

db.Message.insert({
  time: new Date("2020-11-11T16:18:53Z"),
  message: "I want a banner like this",
  picture: "BLOB of m1.png",
  rid: 3000000001,
  uid: 1234567891235,
});

db.Message.insert({
  time: new Date("2020-11-11T18:31:03Z"),
  message: "Can you design a brochure?",
  rid: 3000000002,
  uid: 1234567891234,
});

db.Message.insert({
  time: new Date("2020-11-11T19:00:02Z"),
  message: "Sure",
  rid: 3000000002,
  uid: 1234567891243,
});

db.Message.insert({
  time: new Date("2020-11-12T09:54:43Z"),
  message: "I want cute and friendly bingsu shop logo",
  rid: 3000000003,
  uid: 1234567891239,
});

db.Message.insert({
  time: new Date("2020-11-12T13:15:04Z"),
  message: "I want a business card like this",
  picture: "BLOB of m2.png",
  rid: 3000000004,
  uid: 1234567891240,
});

db.Message.insert({
  time: new Date("2020-11-14T16:46:21Z"),
  message: "I want elegant cosmetic banners",
  rid: 3000000005,
  uid: 1234567891242,
});
