from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key=config.secret
db = SQLAlchemy(app)

from app import routes
abc

