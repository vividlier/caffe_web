from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from caffe_web import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = config.secret
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

import caffe_web.routes
app.register_blueprint(caffe_web.routes.blueprint, url_prefix='/user')

import caffe_web.dataset.routes
app.register_blueprint(caffe_web.dataset.routes.blueprint, url_prefix='/dataset')

import caffe_web.project.routes
app.register_blueprint(caffe_web.project.routes.blueprint, url_prefix='/project')
