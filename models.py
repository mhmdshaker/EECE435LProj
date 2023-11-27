from flask_sqlalchemy import SQLAlchemy

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

#Define the Goods model
class Goods(db.Model):
    Name = db.Column(db.String(255), nullable = False, primary_key = True)
    Category = db.Column(db.Enum('food', 'clothes', 'accessories', 'electronics'))
    Price_per_item = db.Column(db.models.DecimalField(("10, 2"), max_digits=5, decimal_places=2), nullable = False)
    Description = db.Column(db.String(225))
    Count_of_available_items = db.Column(db.Integer, nullable = False)
    