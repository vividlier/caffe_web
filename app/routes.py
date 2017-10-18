from app import app,db
from flask import request,session
from model import *


@app.route('/')
def index():
    return 'index'

@app.route('/register/',methods = ['POST'])
def register():
    data = request.get_json()
    password1 = request.form.get('password1')
    password2 = request.form.ger('password2')
    user = User(
        username = data.get('username'),
        password = data.get('password')
    )
    db.session.add(user)
    db.session.commit()
    return 'register'

@app.route('/login/',methods = ['POST'])
def login():
    data = request.get_json()
    user = User.query.filter(User.username == data.get('username'),User.password == data.get('password')).first()
    if user:
        session['user_id'] = user.index
        return 'login'
    else:
        return 'error'

@app.route('/logout/')
def logout():
    session.clear()
    return 'logout'  