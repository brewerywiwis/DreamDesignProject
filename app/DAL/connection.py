import mysql.connector
from mysql.connector import errorcode


class db:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(host="34.87.125.21",
                                              user="admin",
                                              password="1234",
                                              database="dreamdesignDB")
            print("Dream Design DB connected")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def getDB(self):
        return self.db

    def close(self):
        self.db.close()
