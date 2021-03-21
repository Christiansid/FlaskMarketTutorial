from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c88864af30a971bfb83ed19c'
db = SQLAlchemy(app)

#from market import routes