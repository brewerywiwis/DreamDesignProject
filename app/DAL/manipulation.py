import DAL.connection as connection


db = connection.db().getDB()


def queryUser():
    global db
    cursor = db.cursor()

    query = ("SELECT * FROM user")

    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query)
    result = list(cursor)
    # for (first_name, last_name, hire_date) in cursor:
    #     print("{}, {} was hired on {:%d %b %Y}".format(
    #         last_name, first_name, hire_date))
    # for i in cursor:
    #     print(i)

    cursor.close()
    return result


def insertUser(name, pw):
    global db
    cursor = db.cursor()

    sql = ("INSERT INTO user (username, password) VALUES (%s,%s);")

    cursor.execute(sql, (name, pw))

    db.commit()

    print("insert completed")
    cursor.close()


def validUser(username, password):
    global db
    cursor = db.cursor()
    sql = ("SELECT * FROM dreamdesignDB.admin NATURAL JOIN dreamdesignDB.user WHERE username=%s and password=%s;")
    cursor.execute(sql, (username, password))
    result = list(cursor)
    cursor.close()

    return 1 if len(result) else 0
