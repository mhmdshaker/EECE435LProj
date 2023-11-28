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


