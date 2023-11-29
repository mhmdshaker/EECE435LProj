from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric

db = SQLAlchemy()

       
#Define the Customer model
class Customer(db.Model):
    Fullname = db.Column(db.String(255), nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255), nullable=False)
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(255))
    Gender = db.Column(db.Enum('Male', 'Female'))
    MaritalStatus = db.Column(db.Enum('Single', 'Married', 'Divorced', 'Widowed'))
    wallet = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)

class Goods(db.Model):
    __tablename__ = 'goods'
    Name = db.Column(db.String(255), primary_key=True, nullable=False)
    Category = db.Column(db.Enum('food', 'clothes', 'accessories', 'electronics'), nullable=False)
    Price_per_item = db.Column(db.Numeric(10, 2), nullable=False)
    Description = db.Column(db.String(225))
    Count_of_available_items = db.Column(db.Integer, nullable=False)
    payment_history_username = db.Column(db.String(225), db.ForeignKey('payment_history.customer_username'), nullable=False)

class Payment_History(db.Model):
    __tablename__ = 'payment_history'
    customer_username = db.Column(db.String(225), primary_key=True, nullable=False)
    goods = db.relationship('Goods', backref='payment_history_user', lazy=True)
