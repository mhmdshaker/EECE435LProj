from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
import customers

app = Flask(__name__)

# Configure your MySQL database connection here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:new_password@localhost:3306/mydb'
db = SQLAlchemy(app)

    
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
    
    
#test
@app.route('/khalil', methods=['GET'])
def hello_worldd():
    return customers.hello_world()

