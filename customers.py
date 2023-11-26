from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

# Configure your MySQL database connection here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:new_password@localhost:3306/mydb'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)







