from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

       
# Define the Customer model
class Customer(db.Model):
    Fullname = db.Column(db.String(255), nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255), nullable=False)
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(255))
    Gender = db.Column(db.Enum('Male', 'Female'))
    MaritalStatus = db.Column(db.Enum('Single', 'Married', 'Divorced', 'Widowed'))