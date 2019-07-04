from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, Items
import sqlite3
app = Flask(__name__)
api = Api(app)
app.secret_key = "soroush"
jwt = JWT(app, authenticate, identity)
api.add_resource(Item , '/item/<string:name>')
api.add_resource(Items , '/items', '/rel/<string:pet>')
api.add_resource(UserRegister , '/register')

if __name__ == "__main__":
    app.run( port = 5000, debug = True )
