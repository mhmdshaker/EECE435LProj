from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Customer, db

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


#delete a customer from the database:
def delete_customer():
    data = request.get_json()
    to_be_deleted = Customer.query.filter_by(Username=data['Username']).first()
    
    #if not found:
    if to_be_deleted is None:
        return jsonify({"error": "Customer not found"}), 404
    
    db.session.delete(to_be_deleted)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"}), 200