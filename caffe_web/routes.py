from flask import Blueprint
from flask import request
from caffe_web import model
from caffe_web import db
from sqlalchemy.exc import IntegrityError
import json

blueprint = Blueprint(__name__,__name__)
print __name__


@blueprint.route('/signUp', methods=['POST'])
def signUp():
    tmp = json.loads(request.get_data())
    print "username is {}".format(tmp.get("username"))
    print "password is {}".format(tmp.get("password"))
    user = model.User(username = tmp.get("username"), password = tmp.get("password"))
    db.session.add(user)
    try:
        db.session.commit()
        return '{} is added'.format(tmp.get("username"))
    except IntegrityError:
        db.session.rollback()
        return "SignUp failed"




@blueprint.route('/signIn', methods=['POST'])
def fun():
    print '1'
    return '1'
