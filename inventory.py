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
        db.session.commit
        return jsonify({"message": "Good added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
        
