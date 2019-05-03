from flask import Flask
from flaskext.mysql import MySQL
from app import app

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '1uVdc7W4i8'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Y6a4MtQ1Rt'
app.config['MYSQL_DATABASE_DB'] = '1uVdc7W4i8'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
app.config['MYSQL_DATABASE_PORT'] = 3306 # Default 3306

mysql.init_app(app)