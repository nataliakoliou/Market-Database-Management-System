from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
from datetime import date
from bson import json_util
import json
import uuid
import time

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose database
db = client['DSMarkets']

# Choose collections
users = db['Users']
products = db['Products']

# Initiate Flask App
app = Flask(__name__)

users_sessions = {}
admins_sessions = {}
cart = []
totalPrice = 0
alreadyIn = False

def create_user_session(email):
    user_uuid = str(uuid.uuid1())
    users_sessions[user_uuid] = (email, time.time())
    return user_uuid  

def create_admin_session(email):
    admin_uuid = str(uuid.uuid1())
    admins_sessions[admin_uuid] = (email, time.time())
    return admin_uuid  

def is_user_session_valid(user_uuid):
    return user_uuid in users_sessions

def is_admin_session_valid(admin_uuid):
    return admin_uuid in admins_sessions

# TASK-1: User creation
@app.route('/createUser', methods=['POST'])
def create_user():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "name" in data) or (not "email" in data) or (not "password" in data):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    # if there is no user with such an email in Users collection
    if users.count_documents({"email":data["email"]}) == 0 :  
        # add this user as a standard user into the Users collection
        user = {"name":data['name'],"email":data['email'],"password":data['password'],"category":"standard","orderHistory":[]} 
        users.insert(user)
        return Response(str(data["name"])+" was added to the DSMarkets.",status=200,mimetype='application/json') 
    # if there is a user with such an email in Users collection
    else:   
        return Response("A user with the given email already exists!",status=400,mimetype='application/json')

# TASK-2: Standard user login
@app.route('/userLogin', methods=['POST'])
def user_login():
    # Request JSON data
    cart.clear()
    totalPrice = 0
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "email" in data) or (not "password" in data):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    # if authentication is successful...
    if users.count_documents({"$and":[{"email":data["email"]}, {"password":data["password"]}, {"category":"standard"}]}) == 1 :
        user_uuid = create_user_session(data["email"])
        res = {"uuid": user_uuid, "email": data["email"]}
        return Response(json.dumps(res), status=200, mimetype='application/json')
    # otherwise, if authentication is not successful...
    else:    
        return Response("Wrong email or password! This person is not a standard user.",status=400,mimetype="application/json")

# TASK-3: Administrator login
@app.route('/adminLogin', methods=['POST'])
def admin_login():
    # Request JSON data
    cart.clear()
    totalPrice = 0
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "email" in data) or (not "password" in data):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    # if authentication is successful
    if users.count_documents({"$and":[{"email":data["email"]}, {"password":data["password"]}, {"category":"administrator"}]}) == 1 :
        admin_uuid = create_admin_session(data["email"])
        res = {"uuid": admin_uuid, "email": data["email"]}
        return Response(json.dumps(res), status=200, mimetype='application/json')
    # otherwise, if authentication is not successful...
    else:    
        return Response("Wrong email or password! This person is not an administrator.",status=400,mimetype="application/json")

# TASK-4: Product search
@app.route('/searchProduct', methods=['GET'])
def search_product():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "id" in data) and (not "name" in data) and (not "category" in data):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    products_l = []
    if is_user_session_valid(uuid):
        if "id" in data:
            product = products.find({"id":data["id"]})
        elif "name" in data:
            product = products.find({"name":data["name"]})
        elif "category" in data:
            product = products.find({"category":data["category"]})
        if product != None:
            for p in product:
                product_d = {"id":p["id"], "name":p["name"], "description":p["description"], "price":p["price"], "category":p["category"]}
                products_l.append(product_d)
            return Response(json.dumps(products_l), status=200, mimetype='application/json')
        else:
            return Response("There is no such product in the Market!",status=404,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")
        
# TASK-5: Add product to the cart
@app.route('/addToCart', methods=['GET'])
def add_to_cart():
    # Request JSON data
    alreadyIn = False
    totalPrice = 0
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "id" in data) or (not "quantity" in data):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_user_session_valid(uuid):
        product = products.find_one({"$and":[{"id":data["id"]}, {"stock":{"$gte":data["quantity"]}}]})
        if product != None:
            if not cart == False:
                for c in cart:
                    if c["id"] == product["id"]:
                        alreadyIn = True
                        c["quantity"] = c["quantity"] + data["quantity"]
                        totalPrice = totalPrice + c["price"]*c["quantity"]
                    else:
                        totalPrice = totalPrice + c["price"]*c["quantity"]
                if alreadyIn == False:
                    product_d = {"id":product["id"], "name":product["name"], "price":product["price"], "quantity":data["quantity"]}
                    cart.append(dict(product_d))
                    totalPrice = totalPrice + product["price"]*data["quantity"]
                return Response("Shopping Cart: "+json.dumps(cart)+"\nTotal Price: "+str(totalPrice), status=200, mimetype='application/json')
            else:
                product_d = {"id":product["id"], "name":product["name"], "price":product["price"], "quantity":data["quantity"]}
                cart.append(dict(product_d))
                totalPrice = product["price"]*data["quantity"]
                return Response("Shopping Cart: "+json.dumps(cart)+"\nTotal Price: "+str(totalPrice), status=200, mimetype='application/json')
        else:
            return Response("Your order is invalid! The product you are looking for is currently unavailable.",status=404,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")

# TASK-6: Display customer's cart
@app.route('/displayCart', methods=['GET'])
def display_cart():
    totalPrice = 0
    uuid = request.headers.get('authorization')
    if is_user_session_valid(uuid):
        if not cart:
            return Response("Your cart is empty! Try adding some products in it...",status=404,mimetype="application/json")
        else:
            for c in cart:
                totalPrice = totalPrice + c["price"]*c["quantity"]
            return Response("Shopping Cart: "+json.dumps(cart)+"Total Price: "+str(totalPrice), status=200, mimetype='application/json')
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")

# TASK-7: Delete product from the cart
@app.route('/removeFromCart', methods=['GET'])
def remove_from_cart():
    # Request JSON data
    totalPrice = 0
    alreadyIn = False
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if not "id" in data:
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_user_session_valid(uuid):
        for i in range(len(cart)):
            if cart[i]["id"] == data["id"]:
                del cart[i]
                alreadyIn = True
                break
            else:
                continue
        for c in cart:
            totalPrice = totalPrice + c["price"]*c["quantity"]
        if alreadyIn == True:
            return Response("Shopping Cart is updated as follows: "+json.dumps(cart)+"\nTotal Price: "+str(totalPrice), status=200, mimetype='application/json')
        else:
            return Response("This product is not in your cart!",status=404,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")

# TASK-8: Purchase products
@app.route('/buyProduct', methods=['PATCH'])
def buy_product():
    # Request JSON data
    receipt = []
    totalPrice = 0
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if not "cardNumber" in data:
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_user_session_valid(uuid):
        if (data["cardNumber"] >= 0000000000000000) and (data["cardNumber"] <= 9999999999999999):
            email = users_sessions[uuid][0]
            user = users.find_one({"email":email})
            if not cart:
                return Response("Your cart is empty! Try adding some products in it...",status=404,mimetype="application/json")
            else:
                for c in cart:
                    product = products.find_one({"id":c["id"]})
                    filter1 = {"id":c["id"]}
                    newStock = {"$set":{"stock":product["stock"]-c["quantity"]}}
                    products.update_one(filter1, newStock)
                    if c["id"] not in user["orderHistory"]:
                        filter2 = {"email":email}
                        newOrder = {"$push":{"orderHistory":c["id"]}}
                        users.update_one(filter2, newOrder)
                    receipt.append({"id":c["id"], "name":c["name"], "price":c["price"], "quantity": c["quantity"]})
                    totalPrice = totalPrice + c["price"]*c["quantity"]
                cart.clear()
                return Response("Your Receipt: "+str(receipt)+"\nTotal Price: "+str(totalPrice), status=200, mimetype='application/json')
        else:
            return Response("Invalid Card Number!",status=401,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")

# TASK-9: Display order history
@app.route('/showOrderHistory', methods=['GET'])
def show_order_history():
    uuid = request.headers.get('authorization')
    if is_user_session_valid(uuid):
        email = users_sessions[uuid][0]
        user = users.find_one({"email":email})
        if not user["orderHistory"]:
            return Response("Your History of Orders is empty! Try ordering some products from our Market...",status=404,mimetype="application/json")
        else:
            return Response("Your History of Orders: "+str(user["orderHistory"]), status=200, mimetype='application/json')
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")

# TASK-10: Delete user account
@app.route('/deleteUser', methods=['DELETE'])
def delete_user():
    uuid = request.headers.get('authorization')
    if is_user_session_valid(uuid):
        email = users_sessions[uuid][0]
        users.delete_one({"email":email})
        return Response("User deleted successfuly", status=200, mimetype='application/json')
    else:
        return Response("Invalid user unique identifier!",status=401,mimetype="application/json")

# TASK-11: Add product to the market
@app.route('/addToMarket', methods=['PATCH'])
def add_to_market():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "id" in data) or (not "name" in data) or (not "description" in data) or (not "price" in data) or (not "stock" in data) or (not "category" in data):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_admin_session_valid(uuid):
        product = products.find_one({"id":data["id"]})
        if product == None:
            product_d = {"id":data["id"], "name":data["name"], "description":data["description"], "price":data["price"], "stock":data["stock"], "category":data["category"]}
            product_d["_id"] = None
            users.insert(product_d)
            return Response("The following product is successfully inserted in the Market: "+json.dumps(product_d), status=200, mimetype='application/json')
        else:
            return Response("This product already exists! Try updating its data instead...",status=404,mimetype="application/json")
    else:
        return Response("Invalid administrator unique identifier!",status=401,mimetype="application/json")

# TASK-12: Delete product from the market
@app.route('/removeFromMarket', methods=['PATCH'])
def remove_from_market():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if not "id" in data:
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_admin_session_valid(uuid):
        product = products.find_one({"id":data["id"]})
        if product != None:
            products.delete_one({"id":data["id"]})
            return Response("The product was successfully removed from the Market.", status=200, mimetype='application/json')
        else:
            return Response("The product you wish to remove, is already unavailable in the Market!",status=404,mimetype="application/json")
    else:
        return Response("Invalid administrator unique identifier!",status=401,mimetype="application/json")

# TASK-13: Update product in the market
@app.route('/updateProduct', methods=['PATCH'])
def update_product():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad json content!",status=500,mimetype='application/json')
    if data == None:
        return Response("Bad request!",status=500,mimetype='application/json')
    if (not "id" in data) or ((not "name" in data) and (not "description" in data) and (not "price" in data) and (not "stock" in data) and (not "category" in data)):
        return Response("Information incomplete...",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_admin_session_valid(uuid):
        product = products.find_one({"id":data["id"]})
        filter = {"id":data["id"]}
        if product != None:
            if "name" in data:
                newName = {"$set":{"name":data["name"]}}
                products.update_one(filter, newName)
                return Response("The new name of this product is now: "+str(product["name"]), status=200, mimetype='application/json')
            if "description" in data:
                newDescription = {"$set":{"description":data["description"]}}
                products.update_one(filter, newDescription)
                return Response("The new description of this product is now: "+str(product["description"]), status=200, mimetype='application/json')
            if "price" in data:
                newPrice = {"$set":{"price":data["price"]}}
                products.update_one(filter, newPrice)
                return Response("The new price of this product is now: "+str(product["price"]), status=200, mimetype='application/json')
            if "stock" in data:
                newStock = {"$set":{"stock":data["stock"]}}
                products.update_one(filter, newStock)
                return Response("The new number of stocks for this product is now: "+str(product["stock"]), status=200, mimetype='application/json')            
            if "category" in data:
                newCategory = {"$set":{"category":data["category"]}}
                products.update_one(filter, newCategory)
                return Response("This product will belong from now on in this category: "+str(product["name"]), status=200, mimetype='application/json')            
        else:
            return Response("The product you wish to update does not exist in the Market!",status=404,mimetype="application/json")
    else:
        return Response("Invalid administrator unique identifier!",status=401,mimetype="application/json")
    
# Execute flask service in debug mode on port 5000 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
