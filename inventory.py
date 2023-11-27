from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Customer, db