from flask import Flask, request, session
from app import app
from app.model import *

@app.route('/')
def index():
    return 'index'

@app.route('/register/', methods=['POST'])
def register():
    #获取注册页面，用户输入的数据(用户名，密码)
    data = request.get_json()
    #将用户名和密码传入model模块(py文件)，生成user实例
    user = User(username=data.get('username'), password=data.get('password'))
    #在Flask-SQLAlchemy中，会话由db.session表示
    db.session.add(user)
    db.session.commit()
    return 'register'

@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json()
    #user代表登录时，根据其用户名和密码获得该条记录的id，first()之前的是一整条SQL语句
    user = User.query.filter(User.username == data.get('username'),
                             User.password == data.get('password')).first()
    #若该用户id存在，将user.id存入session
    if user:
        session['user_id'] = user.id
        return 'login'
    #否则登录错误
    else:
        return 'login error'

@app.route('/logout/')
def logout():
    session.clear()
    return 'logout'