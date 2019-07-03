import sqlite3
class User:
    def __init__(self, _id, username , password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
    @classmethod
    def sign_up(cls,_id, username , password):
        if cls.find_by_username(username):
            return("The username already exists.")
        else:
            connection = sqlite3.connect("data.db")
            create_query = "INSERT INTO users VALUES (?,?,?)"
            cursor = connection.cursor()
            cursor.execute(create_query , (_id,username , password))
            connection.commit()
            connection.close()
            return cls(_id, username , password)
User.sign_up(2,"ali","1234")
