def queryUser(db):
    cursor = db.cursor()

    query = ("SELECT * FROM User")

    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query)

    # for (first_name, last_name, hire_date) in cursor:
    #     print("{}, {} was hired on {:%d %b %Y}".format(
    #         last_name, first_name, hire_date))
    for i in cursor:
        print(i)

    cursor.close()


def insertUser(db, name, pw):
    cursor = db.cursor()

    sql = ("INSERT INTO User (username, password) VALUES (%s,%s);")

    cursor.execute(sql, (name, pw))

    db.commit()

    print("insert completed")
    cursor.close()
