from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Goods, db




#Adding good to DB, as in creating a new good but not adding quantity:
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
    if (to_be_updated.Count_of_available_items - data['Amount_to_be_removed'] < 0):
        return jsonify({"error": "The inventory has a number of items of this good that is less than what you are demanding"}), 400
        
    to_be_updated.Count_of_available_items = to_be_updated.Count_of_available_items - data['Amount_to_be_removed']

    db.session.commit()
    return jsonify({"message": "Amount count changed successfuly"}), 200
        
        
        
        
#Updating fields of an item, including increasing amopunts of goods:
def update_good_info():
    data = request.get_json()

    # Check if 'Name' is provided in the JSON data
    if 'Name' not in data:
        return jsonify({"error": "Name is required in the request"}), 400

    to_be_updated = Goods.query.filter_by(Name=data['Name']).first()

    # if not found
    if to_be_updated is None:
        return jsonify({"error": "Name not found"}), 404

    # Update customer information based on the provided data
    if 'Name' in data:
        to_be_updated.Name = data['Name']
    if 'Category' in data:
        to_be_updated.Category = data['Category']
    if 'Price_per_item' in data:
        to_be_updated.Price_per_item = data['Price_per_item']
    if 'Description' in data:
        to_be_updated.Description = data['Description']
    if 'Count_of_available_items' in data:
        to_be_updated.Count_of_available_items = data['Count_of_available_items']

    db.session.commit()
    return jsonify({"message": "Item (Good) information updated successfully"}), 200
