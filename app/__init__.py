from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key=config.secret
db = SQLAlchemy(app)

<<<<<<< HEAD
from app import routes
=======
from app import routes

>>>>>>> 6dd41bfded570a5236c7bd8c6e9619ea32bc5d8e
