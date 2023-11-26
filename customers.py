from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

# Configure your MySQL database connection here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:new_password@localhost:3306/mydb'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)





#test
@app.route('/khalil', methods=['GET'])
def hello_world():
    return 'Hello, World!'

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Fullname = db.Column(db.String(255), nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(255))
    Gender = db.Column(db.Enum('Male', 'Female'))
    MaritalStatus = db.Column(db.Enum('Single', 'Married', 'Divorced', 'Widowed'))

#add customer to DB:
@app.route('/create_customer', methods=['POST'])
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

