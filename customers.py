from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Customer, db

#add customer to DB:
def create_customer():
    data = request.get_json()
    try:
        if "wallet" not in data:
            data['wallet'] = 0.00

        new_customer = Customer(
            Fullname=data['Fullname'],
            Username=data['Username'],
            Password=data['Password'],
            Age=data['Age'],
            Address=data['Address'],
            Gender=data['Gender'],
            MaritalStatus=data['MaritalStatus'],
            wallet = data['wallet']
        )

        db.session.add(new_customer)
        db.session.commit()

        return jsonify({"message": "Customer created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


#delete a customer from the database:
def delete_customer():
    data = request.get_json()
    # Check if 'Username' is provided in the JSON data
    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400
    
    to_be_deleted = Customer.query.filter_by(Username=data['Username']).first()
    #if not found:
    if to_be_deleted is None:
        return jsonify({"error": "Customer not found"}), 404
    
    db.session.delete(to_be_deleted)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"}), 200

#update customer info:
def update_customer_info():
    data = request.get_json()

    # Check if 'Username' is provided in the JSON data
    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400

    to_be_updated = Customer.query.filter_by(Username=data['Username']).first()

    # if not found
    if to_be_updated is None:
        return jsonify({"error": "Customer not found"}), 404

    # Update customer information based on the provided data
    if 'Fullname' in data:
        to_be_updated.Fullname = data['Fullname']
    if 'Username' in data:
        to_be_updated.Username = data['Username']
    if 'Password' in data:
        to_be_updated.Password = data['Password']
    if 'Age' in data:
        to_be_updated.Age = data['Age']
    if 'Address' in data:
        to_be_updated.Address = data['Address']
    if 'Gender' in data:
        to_be_updated.Gender = data['Gender']
    if 'MaritalStatus' in data:
        to_be_updated.MaritalStatus = data['MaritalStatus']

    db.session.commit()
    return jsonify({"message": "Customer information updated successfully"}), 200


# Get all customers from the database
def get_all_customers():
    try:
        customers = Customer.query.all()

        # Convert the list of customers to a list of dictionaries
        customers_list = [
            {
                'Fullname': customer.Fullname,
                'Username': customer.Username,
                'Password': customer.Password,
                'Age': customer.Age,
                'Address': customer.Address,
                'Gender': customer.Gender,
                'MaritalStatus': customer.MaritalStatus
            }
            for customer in customers
        ]

        return jsonify({"customers": customers_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a customer by username
def get_customer_by_username():
    data = request.get_json()

    # Check if 'Username' is provided in the JSON data
    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400

    customer = Customer.query.filter_by(Username=data['Username']).first()

    # if not found
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404


    try:
        customer_data = {
            'Fullname': customer.Fullname,
            'Username': customer.Username,
            'Password': customer.Password,
            'Age': customer.Age,
            'Address': customer.Address,
            'Gender': customer.Gender,
            'MaritalStatus': customer.MaritalStatus
        }

        return jsonify({"customer": customer_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
