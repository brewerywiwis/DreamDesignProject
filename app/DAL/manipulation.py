import DAL.connection as connection

db = connection.db().getDB()


def validUser(username, password):
    global db
    cursor = db.cursor()
    args = (username, password, 0)
    # sql = ("CALL loginWithUsernamePassword(%s, %s, @output);\
    #         select @output;")
    # cursor.execute(sql, (username, password))
    result = cursor.callproc('loginWithUsernamePassword', args)
    cursor.close()
    #print(result)
    return 1 if (len(result) and result[2] == 1 ) else 0

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
            print("Something went wrong: not insert user")
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
        # sql3 = "DELETE FROM dreamdesignDB.user WHERE uid=%s;"
        # cursor.execute(sql3, (id,))
        db.commit()
        cursor.close()
        return True
    except:
        cursor.close()
        return False

################################# CUSTOMER #####################################

################################# DESIGNER #####################################


def insertDesigner(name, pw):
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
                sql2 = ("INSERT INTO dreamdesignDB.designer (uid) VALUES (%s);")
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
            sql2 = ("INSERT INTO dreamdesignDB.designer (uid) VALUES (%s);")
            cursor.execute(sql2, (id,))
            db.commit()
            cursor.close()
            return True
        except:
            print("Something went wrong: not insert user")
            cursor.close()
            return False


def queryDesigner():
    global db
    cursor = db.cursor(dictionary=True)
    query = ("SELECT * FROM dreamdesignDB.designer NATURAL JOIN dreamdesignDB.user")
    cursor.execute(query)
    result = [[row["uid"], row["username"], row["password"]] for row in cursor]
    cursor.close()
    return result


def deleteDesigner(name):
    global db
    cursor = db.cursor()
    print(name)
    try:
        sql1 = "SELECT * FROM dreamdesignDB.designer NATURAL JOIN dreamdesignDB.user where username=%s;"
        cursor.execute(sql1, (name,))
        ls = list(cursor)
        id = -1
        if len(ls):
            id = ls[0][0]
        else:
            cursor.close()
            return False
        sql2 = "DELETE FROM dreamdesignDB.designer WHERE uid=%s;"
        cursor.execute(sql2, (id,))
        # sql3 = "DELETE FROM dreamdesignDB.user WHERE uid=%s;"
        # cursor.execute(sql3, (id,))
        db.commit()
        cursor.close()
        return True
    except:
        cursor.close()
        return False

################################# DESIGNER #####################################

################################# MATCH #####################################


# def insertDesigner(name, pw):
#     global db
#     sql = ("SELECT * FROM dreamdesignDB.user WHERE username=%s;")
#     cursor = db.cursor()
#     cursor.execute(sql, (name,))
#     ls = list(cursor)
#     id = -1
#     if len(ls):
#         id = ls[0][0]
#     if id == -1:
#         if len(name) and len(pw) and insertUser(name, pw):
#             sql1 = "select * from user where username=%s and password=%s"
#             cursor.execute(sql1, (name, pw))
#             ls = list(cursor)
#             id = -1
#             if len(ls):
#                 id = ls[0][0]
#             else:
#                 sql2 = "DELETE FROM dreamdesignDB.user WHERE username=%s;"
#                 cursor.execute(sql2, (name,))
#                 db.commit()
#                 cursor.close()
#                 return False
#             try:
#                 sql2 = ("INSERT INTO dreamdesignDB.designer (uid) VALUES (%s);")
#                 cursor.execute(sql2, (id,))
#                 db.commit()
#                 cursor.close()
#                 return True
#             except:
#                 print("Something went wrong: insert user")
#                 sql2 = "DELETE FROM dreamdesignDB.user WHERE username=%s;"
#                 cursor.execute(sql2, (name,))
#                 db.commit()
#                 cursor.close()
#                 return False
#         else:
#             cursor.close()
#             return False
#     else:
#         try:
#             sql2 = ("INSERT INTO dreamdesignDB.designer (uid) VALUES (%s);")
#             cursor.execute(sql2, (id,))
#             db.commit()
#             cursor.close()
#             return True
#         except:
#             print("Something went wrong: not insert user")
#             cursor.close()
#             return False


def queryMatch():
    global db
    cursor = db.cursor(dictionary=True)
    query = ("select mid,designer_name,username as customer_name,tid\
            from (SELECT mid,username as designer_name,cid,tid\
            FROM dreamdesignDB.matchs\
            join dreamdesignDB.user on dreamdesignDB.user.uid = matchs.did\
            ) as T1\
            join dreamdesignDB.user on dreamdesignDB.user.uid = T1.cid")
    cursor.execute(query)
    result = [[row["mid"], row["designer_name"],
               row["customer_name"], row["tid"]] for row in cursor]
    cursor.close()
    return result


def deleteMatch(id):
    global db
    cursor = db.cursor()
    # print(name)
    try:
        # sql1 = "SELECT * FROM dreamdesignDB.designer NATURAL JOIN dreamdesignDB.user where username=%s;"
        # cursor.execute(sql1, (name,))
        # ls = list(cursor)
        # id = -1
        # if len(ls):
        #     id = ls[0][0]
        # else:
        #     cursor.close()
        #     return False
        sql2 = "DELETE FROM dreamdesignDB.matchs WHERE mid=%s;"
        cursor.execute(sql2, (id,))
        # sql3 = "DELETE FROM dreamdesignDB.user WHERE uid=%s;"
        # cursor.execute(sql3, (id,))
        db.commit()
        cursor.close()
        return True
    except:
        cursor.close()
        return False

################################# MATCH #####################################

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
        # sql3 = "DELETE FROM dreamdesignDB.user WHERE uid=%s;"
        # cursor.execute(sql3, (id,))
        db.commit()
        cursor.close()
        return True
    except:
        cursor.close()
        return False

################################# ADMIN #####################################

################################# JOB POSTING #####################################

def queryJobPosting():
    global db
    cursor = db.cursor()
    query = ("select JP.jid, UU.username, JP.description\
            FROM dreamdesignDB.jobposting JP, dreamdesignDB.designer D, dreamdesignDB.user UU\
            WHERE UU.uid = D.uid AND JP.did = D.uid")
    cursor.execute(query)
    result = list(cursor)
    cursor.close()
    return result

def deleteJobPosting(id):
    global db
    cursor = db.cursor()
    # print(name)
    try:
        sql1 = "SELECT jid FROM dreamdesignDB.jobposting WHERE jid=%s;"
        cursor.execute(sql1, (id,))
        ls = list(cursor)
        if len(ls) != 1:
            cursor.close()
            return False
        if(int(id)==int(ls[0][0])):
            sql2 = "DELETE FROM dreamdesignDB.jobposting WHERE jid=%s;"
            cursor.execute(sql2, (id,))
            db.commit()
            cursor.close()
            print('Deleted Already!')
            return True
    except:
        print('Something is wrong.')
        cursor.close()
        return False

def insertJobPosting(id, descriptionInput):
    global db
    sql = ("SELECT uid FROM dreamdesignDB.designer WHERE uid=%s;")
    cursor = db.cursor()
    cursor.execute(sql, (id,))
    ls = list(cursor)
    #print(ls)
    #print(id, descriptionInput)
    id = -1
    if len(ls):
        id = ls[0][0]
    if id == -1:
        cursor.close()
        print('''This designer id isn't exits''')
        return False
    else:
        try:
            sql2 = ("INSERT INTO dreamdesignDB.jobposting (did, description) VALUES (%s, %s);")
            cursor.execute(sql2, (id, descriptionInput))
            db.commit()
            cursor.close()
            return True
        except:
            print("Something went wrong: not insert user")
            cursor.close()
            return False

################################# JOB POSTING #####################################
