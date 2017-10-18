from app import app
from flask import render_template, request, session, redirect, url_for
from app.model import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username, User.password == password).first()
        if user:
            # g.user = user
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return '用户名或密码错误'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.username == username).first()
        if user:
            return '改手机号码已被注册'
        else:
            if password1 != password2:
                return '两次密码不相等'
            else:
                user = User(
                    username=username,
                    password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    # session.pop('user_id')
    session.clear()
    return redirect(url_for('login'))

@app.route('/question/', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        pass

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    print(user_id)
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}
