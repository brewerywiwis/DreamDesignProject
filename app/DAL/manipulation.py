import DAL.connection as connection

db = connection.db().getDB()


def validUser(username, password):
    global db
    cursor = db.cursor()
    sql = ("SELECT * FROM dreamdesignDB.admin NATURAL JOIN dreamdesignDB.user WHERE username=%s and password=%s;")
    cursor.execute(sql, (username, password))
    result = list(cursor)
    cursor.close()

    return 1 if len(result) else 0


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
    try:
        sql = ("INSERT INTO dreamdesignDB.user (username, password) VALUES (%s,%s);")
        cursor.execute(sql, (name, pw))
        db.commit()
        cursor.close()
    except:
        print("insert user")
        cursor.close()
        return False
    return True


################################# CUSTOMER #####################################

def insertCustomer(name, pw):
    global db
    sql = ("SELECT * FROM dreamdesignDB.user WHERE username=%s;")
    cursor = db.cursor()
    cursor.execute(sql, (name,))
    ls = list(cursor)
    id = -1
    if len(ls):
        id = ls[0][0]
    if id == -1:
        if len(name) and len(pw) and insertUser(name, pw):
            sql1 = "select * from user where username=%s and password=%s"
            cursor.execute(sql1, (name, pw))
            ls = list(cursor)
            id = -1
            if len(ls):
                id = ls[0][0]
            else:
                sql2 = "DELETE FROM dreamdesignDB.user WHERE username=%s;"
                cursor.execute(sql2, (name,))
                db.commit()
                cursor.close()
                return False
            try:
                sql2 = ("INSERT INTO dreamdesignDB.customer (uid) VALUES (%s);")
                cursor.execute(sql2, (id,))
                db.commit()
                cursor.close()
                return True
            except:
                print("Something went wrong: insert user")
                sql2 = "DELETE FROM dreamdesignDB.user WHERE username=%s;"
                cursor.execute(sql2, (name,))
                db.commit()
                cursor.close()
                return False
        else:
            cursor.close()
            return False
    else:
        try:
            sql2 = ("INSERT INTO dreamdesignDB.customer (uid) VALUES (%s);")
            cursor.execute(sql2, (id,))
            db.commit()
            cursor.close()
            return True
        except:
            print("Something went wrong: not insert customer")
            cursor.close()
            return False


def queryCustomer():
    global db
    cursor = db.cursor()
    query = ("SELECT * FROM dreamdesignDB.customer NATURAL JOIN dreamdesignDB.user")
    cursor.execute(query)
    result = list(cursor)
    cursor.close()
    return result


def deleteCustomer(name):
    global db
    cursor = db.cursor()
    print(name)
    try:
        sql1 = "SELECT * FROM dreamdesignDB.customer NATURAL JOIN dreamdesignDB.user where username=%s;"
        cursor.execute(sql1, (name,))
        ls = list(cursor)
        id = -1
        if len(ls):
            id = ls[0][0]
        else:
            cursor.close()
            return False
        sql2 = "DELETE FROM dreamdesignDB.customer WHERE uid=%s;"
        cursor.execute(sql2, (id,))
        sql3 = "DELETE FROM dreamdesignDB.user WHERE uid=%s;"
        cursor.execute(sql3, (id,))
        db.commit()
        cursor.close()
        return True
    except:
        cursor.close()
        return False

################################# CUSTOMER #####################################


################################# ADMIN #####################################
def insertAdmin(name, pw):
    global db
    sql = ("SELECT * FROM dreamdesignDB.user WHERE username=%s;")
    cursor = db.cursor()
    cursor.execute(sql, (name,))
    ls = list(cursor)
    id = -1
    if len(ls):
        id = ls[0][0]
    if id == -1:
        if len(name) and len(pw) and insertUser(name, pw):
            sql1 = "select * from user where username=%s and password=%s"
            cursor.execute(sql1, (name, pw))
            ls = list(cursor)
            id = -1
            if len(ls):
                id = ls[0][0]
            else:
                sql2 = "DELETE FROM dreamdesignDB.user WHERE username=%s;"
                cursor.execute(sql2, (name,))
                db.commit()
                cursor.close()
                return False
            try:
                sql2 = ("INSERT INTO dreamdesignDB.admin (uid) VALUES (%s);")
                cursor.execute(sql2, (id,))
                db.commit()
                cursor.close()
                return True
            except:
                print("Something went wrong: insert admin")
                sql2 = "DELETE FROM dreamdesignDB.user WHERE username=%s;"
                cursor.execute(sql2, (name,))
                db.commit()
                cursor.close()
                return False
        else:
            cursor.close()
            return False
    else:
        try:
            sql2 = ("INSERT INTO dreamdesignDB.admin (uid) VALUES (%s);")
            cursor.execute(sql2, (id,))
            db.commit()
            cursor.close()
            return True
        except:
            print("Something went wrong: not insert admin")
            cursor.close()
            return False


def queryAdmin():
    global db
    cursor = db.cursor()
    query = ("SELECT * FROM dreamdesignDB.admin NATURAL JOIN dreamdesignDB.user")
    cursor.execute(query)
    result = list(cursor)
    cursor.close()
    return result


def deleteAdmin(name):
    global db
    cursor = db.cursor()
    print(name)
    try:
        sql1 = "SELECT * FROM dreamdesignDB.admin NATURAL JOIN dreamdesignDB.user where username=%s;"
        cursor.execute(sql1, (name,))
        ls = list(cursor)
        id = -1
        if len(ls):
            id = ls[0][0]
        else:
            cursor.close()
            return False
        sql2 = "DELETE FROM dreamdesignDB.admin WHERE uid=%s;"
        cursor.execute(sql2, (id,))
        sql3 = "DELETE FROM dreamdesignDB.user WHERE uid=%s;"
        cursor.execute(sql3, (id,))
        db.commit()
        cursor.close()
        return True
    except:
        cursor.close()
        return False

################################# ADMIN #####################################
