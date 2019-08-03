from flask import Flask, flash , redirect
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e613744db63f28a3a3ac4bc1671da00a5d121727bb099f31cea00711'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aman'
app.config['MYSQL_DATABASE_DB'] = 'quora'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db = MySQL(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from quora_app import routes
