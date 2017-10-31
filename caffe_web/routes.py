from flask import Blueprint, request, session, abort, url_for, jsonify, g

from caffe_web import model
from caffe_web import db, auth
from model import User
from sqlalchemy.exc import IntegrityError
import json

blueprint = Blueprint(__name__, __name__)
print __name__


@blueprint.route('/signUp', methods = ['POST'])
def signUp():
    # tmp = request.get_json()
    # print "username is {}".format(tmp.get("username"))
    # print "password is {}".format(tmp.get("password"))
    # user = model.User(username = tmp.get("username"), password = tmp.get("password"))
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username = username).first() is not None:
        abort(400)
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)

    db.session.commit()
    print user.id
    session['user_id'] = user.id
    # db.session.close()
    return (jsonify({'user_id': user.id, 'username': user.username}), 201,
            {'Location': url_for('caffe_web.routes.get_user', id = user.id, _external = True)})


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    # user = User.verify_auth_token(username_or_token)
    # if not user:
        # try to authenticate with username/password
    user = User.query.filter_by(username = username_or_token).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@blueprint.route('/signIn', methods = ['POST'])
def signIn():
    username = request.json.get('username')
    password = request.json.get('password')
    if verify_password(username, password):
        user = User.query.filter(User.username == username).first()
        session['user_id'] = user.id
        return (jsonify({
            "status":"200",
            "data":
                {
                    'user_id': user.id,
                    'username': user.username
                }
        }))
    else:
        abort(400)


@blueprint.route('/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})
