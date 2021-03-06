import psycopg2

class UserDAO:
    def __init__(self):
        conn_string = "host='localhost' dbname='chatapp' user='postgres' password='postgres'"
        self.conn = psycopg2.connect(conn_string)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Users")
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT userid, name, email, username, phone FROM Users where userid=%s", (str(id)))

        return cursor.fetchone()

    def activeUsers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) FROM Users where active=1")
        return cursor.fetchone()

    def searchByUsername(self, user):
        cursor = self.conn.cursor()
        cursor.execute("SELECT userid, name, email, username, phone FROM Users where username=%s",(str(user),))
        return cursor.fetchone()
    def verify(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("select userid from users where email=%s and password=%s;",
                       (username, password))
        return cursor.fetchone()

    def register(self, name, email, username, password, phone):
        cursor = self.conn.cursor()
        cursor.execute("insert into users values(DEFAULT, %s, %s, %s, %s, %s, 0);",
                       (name, email, username, password, phone))
        self.conn.commit()