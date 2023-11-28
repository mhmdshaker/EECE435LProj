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
            'Password': good.Password,
            'Price_per_item': good.Price_per_item,
            'Description': good.Description,
            'Count_of_available_items': good.Count_of_available_items,
        }
        for good in goods
    ]

    return jsonify({"goods": goods_list}), 200


