import sqlite3
from flask import request, jsonify
from flask_restful import Api, Resource, reqparse
from flask import Flask, request, jsonify
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

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
    'username',
    # type= str,
    required = True ,
    help = "The request should include a username."
    )
    parser.add_argument(
    'password',
    # type= str,
    required = True ,
    help = "The request should include a password."
    )
    def post(self):
        # data = request.get_json()

        data = UserRegister.parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        if cursor.execute("SELECT * FROM users WHERE username=?", (data["username"],)).fetchone():
            return(jsonify({"message":"user already exists."}))
        add_user = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(add_user, (data["username"], data["password"]))
        connection.commit()
        connection.close()
        return jsonify({"message":"user created."})

#     @classmethod
#     def sign_up(cls,_id, username , password):
#         if cls.find_by_username(username):
#             print("The username already exists.")
#         else:
#             connection = sqlite3.connect("data.db")
#             create_query = "INSERT INTO users VALUES (?,?,?)"
#             cursor = connection.cursor()
#             cursor.execute(create_query , (_id,username , password))
#             connection.commit()
#             connection.close()
#             return cls(_id, username , password)
# User.sign_up(2,"al","1234")
