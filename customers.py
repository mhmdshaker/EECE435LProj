from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
# from app import Customer
# from app import db
from models import Customer, db

def hello_world():
    return 'Hello, World!'

#add customer to DB:
def create_customer():
    data = request.get_json()
    try:
        new_customer = Customer(
            Fullname=data['Fullname'],
            Username=data['Username'],
            Password=data['Password'],
            Age=data['Age'],
            Address=data['Address'],
            Gender=data['Gender'],
            MaritalStatus=data['MaritalStatus']
        )

        db.session.add(new_customer)
        db.session.commit()

        return jsonify({"message": "Customer created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

