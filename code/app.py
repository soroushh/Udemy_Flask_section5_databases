from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
app = Flask(__name__)
api = Api(app)
app.secret_key = "soroush"
jwt = JWT(app, authenticate, identity)
items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
    "price",
    type=float ,
    required = True,
    help="The price should be float and it is required to have it in your request."
    )

    @jwt_required()
    def get(self,name):
        item = next(filter(lambda item: item["name"]== name , items), None)
        return {"item":item} ,200 if item else 404

    def post(self, name):
        if next(filter(lambda item: item["name"]== name , items), None):
            return {"message":"Item exists already"}, 400
        request_data = Item.parser.parse_args()
        items.append({"name":name , "price":request_data["price"]})
        return {"name":name , "price" :request_data["price"]}, 201
    def delete(self,name):
        global items
        items = list(filter(lambda item: item["name"] != name , items))
        return({"message": "The '{}' item was deleted." .format(name)})
    def put(self, name):
        request_data = Item.parser.parse_args()
        item = next(filter(lambda item: item["name"] == name , items), None)
        if item is None:
            item = {"name": name , "price": request_data["price"]}
            items.append(item)
        else :
            item.update(request_data)
        return item

class Items(Resource):
    def get(self):
        return {"items":items}
api.add_resource(Item , '/item/<string:name>')
api.add_resource(Items , '/items')
api.add_resource(UserRegister , '/register')
app.run( port = 5000, debug = True )
