from flask import Flask
from models import db, Customer
import customers

app = Flask(__name__)

# Configure your MySQL database connection here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:new_password@localhost:3306/mydb'
db.init_app(app)
# db = SQLAlchemy(app)


#test
@app.route('/khalil', methods=['GET'])
def hello_worldd():
    return customers.hello_world()

#add customer to DB:
@app.route('/create_customer', methods=['POST'])
def create_customer():
    return customers.create_customer()

#delete a costumer
@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    return customers.delete_customer()

def hello():
    print('hello')