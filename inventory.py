from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Goods, db

#add good to DB:
def add_good():
    data = request.get_json()
    try:
        new_good = Goods(
            Name = data['Name'],
            Category = data['Category'],
            Price_per_item = data['Price_per_item'],
            Description = data['Description'],
            Count_of_available_items = data['Count_of_available_items']
        )
        
        db.session.add(new_good)
        db.session.commit()
        return jsonify({"message": "Good added successfully"})
    except Exception as e:
        if 'duplicate entry' in str(e).lower():
            return jsonify({"error": "The item already exists, please update its fields instead"}), 400
        return jsonify({"error": str(e)}), 400
    
#Deducing goods: removing an item from stock :
def remove_stock():
    data = request.get_json()
    # Check if 'Name' is provided in the JSON data
    if 'Name' not in data:
        return jsonify({"error": "Name is required in the request"}), 400
    if 'Amount_to_be_removed' not in data:
        return jsonify({"error": "Amount to be deducted is required as an input"}), 400
    
    to_be_updated = Goods.query.filter_by(Name=data['Name']).first()
    to_be_updated.Count_of_available_items = to_be_updated.Count_of_available_items - data['Amount_to_be_removed']

    db.session.commit()
    return jsonify({"message": "Amount count changed successfuly"}), 200
        
