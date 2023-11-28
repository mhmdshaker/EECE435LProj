from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Customer, Goods, db

#Display available goods:
def display_available_goods():
    goods = Goods.query.all()
    # Convert the list of customers to a list of dictionaries to be used for the json file
    goods_list = [
        {
            'Name': good.Name,
            'Category': good.Category,
            'Price_per_item': good.Price_per_item,
            'Description': good.Description,
            'Count_of_available_items': good.Count_of_available_items,
        }
        for good in goods
    ]

    return jsonify({"goods": goods_list}), 200

#Get goods details: This API should return full information related to a specific good:
def good_details():
    data = request.get_json()

    # Check if 'good' is provided in the JSON data
    if 'Name' not in data:
        return jsonify({"error": "Name of good is required in the request"}), 400

    good = Goods.query.filter_by(Name=data['Name']).first()

    # if not found
    if good is None:
        return jsonify({"error": "Good name is not found"}), 404
    
    try:
        good_data = {
            'Name': good.Name,
            'Category': good.Category,
            'Price_per_item': good.Price_per_item,
            'Description': good.Description,
            'Count_of_available_items': good.Count_of_available_items,
        }
        return jsonify({"Good ": good_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


#to make a sale from a customer to a good:
def make_sale():
    data = request.get_json()
    #i should get the Username of the customer and the Name of the good
    if 'Name' not in data:
        return jsonify({"error": "Name of good is required in the request"}), 400
    good = Goods.query.filter_by(Name=data['Name']).first()
    
    if 'Username' not in data:
        return jsonify({"error": "Customer name is required in the request"}), 400
    customer = Customer.query.filter_by(Username=data['Username']).first()
    
    # if not found
    if good is None:
        return jsonify({"error": "Good name is not found"}), 404
    if customer is None:
        return jsonify({"error": "Customer name is not found"}), 404
    
    #check if the user has enough money:
    if customer.wallet < good.Price_per_item :
        return jsonify({"error": "No enough amount to buy the good"}), 404
    
    #check if the amount of the good is greater than 0:
    if good.Count_of_available_items == 0:
        return jsonify({"error": "No more amount of this good is available. Out of Stock!"}), 404
    
    good.Count_of_available_items -= 1
    customer.wallet -= good.Price_per_item
    
    db.session.commit()