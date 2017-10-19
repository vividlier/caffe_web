
from flask import Flask, render_template, request, redirect,url_for, session
from app import app
from app.model import *

@app.route('/')
def index():
    return 'index'

@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter(User.username == data.get('username'),
                             User.password == data.get('password')).first()
    if user:
        session['user_id'] = user.id
        return 'login'
    else:
        return 'login error'

@app.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    print(data.get('password'))
    user = User(username=data.get('username'), password=data.get('password'))
    db.session.add(user)
    db.session.commit()
    return 'register'

@app.route('/logout/')
def logout():
    session.clear()
    return 'logout'

