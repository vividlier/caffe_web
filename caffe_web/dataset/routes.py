from flask import Blueprint, request
# from caffe_web.model import *

blueprint = Blueprint(__name__,__name__)


@blueprint.route('/', methods=['POST'])
def test():
    rst = request.get_data()
    print rst
    return rst


# @blueprint.route('/test1', methods=['POST'])
# def test1():
#     rst = User.query.all()
#     return rst
