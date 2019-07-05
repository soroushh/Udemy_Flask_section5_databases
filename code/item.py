# I am just adding some comment.
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
import sqlite3
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
        # item = next(filter(lambda item: item["name"]== name , items), None)
        # return {"item":item} ,200 if item else 404
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        find_item_query = "SELECT * FROM items WHERE name=? "
        result = cursor.execute(find_item_query , (name,))
        item_row = result.fetchone()
        connection.close()
        if item_row :
            return({"item id:{}".format(current_identity.id):{"name": item_row[0], "price": item_row[1]}}), 200
        else :
            return({"message":"item not found"}), 404

    def post(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        item_row = cursor.execute("SELECT * FROM items WHERE name = ?", (name,)).fetchone()
        if item_row :
            connection.close()
            return {"message": "Item already exists"}
        data = Item.parser.parse_args()
        item = {"name":name , "price":data["price"]}
        cursor.execute("INSERT INTO items VALUES (?,?)", (item["name"],item["price"]))
        connection.commit()
        connection.close()
        return({"meassgae":"item created"})

    def delete(self,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        item_row = cursor.execute("SELECT * FROM items WHERE name=?", (name,)).fetchone()
        if item_row == None:
            connection.close()
            return {"message":"The item does not exist."}
        cursor.execute("DELETE FROM items WHERE name=?", (name,))
        connection.commit()
        connection.close()
        return({"message":"Item '{}' is now deleted.".format(name)})

    def put(self, name):
        request_data = Item.parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        if cursor.execute("SELECT * FROM items WHERE name=?",(name,)).fetchone() is None:
            connection.close()
            return {"message": "Item was not found"}, 404
        cursor.execute("UPDATE items SET price=? WHERE name=?", (request_data["price"], name))
        connection.commit()
        connection.close()
        return {"message":"Item '{}' was updated".format(name)}, 202

class Items(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM items")
        items = []
        for item in result:
            items.append({ "name":item[0], "price": item[1]})
        return ({"items":items})
    def post(self, pet):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM items WHERE name=?",(pet,))
        connection.commit()
        if result.fetchone():
            connection.close()
            return({"message":"item exists"})
        else:
            connection.close()
            return({"message":"item does not exist"})
