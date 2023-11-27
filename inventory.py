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
    
# #Deducing goods: removing an item from stock :
# def remove_stock
        
