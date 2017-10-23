from flask import Blueprint, request
from caffe_web.model import *
import  json

blueprint = Blueprint(__name__, __name__)


@blueprint.route('/', methods=['POST'])
def test():
    rst = request.get_data()
    b = json.loads(rst)
    # print type(b)
    return '{} is ok'.format(b.get("username"))




# @blueprint.route('/test1', methods=['POST'])
# def test1():
#     rst = User.query.all()
#     return rst
