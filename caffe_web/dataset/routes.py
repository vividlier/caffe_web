from flask import Blueprint, request
from caffe_web.model import *
import  json
from caffe_web.utils import send

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


@blueprint.route('/createDataset', methods=['POST'])
def createDataset():
    data = request.get_json()
    dataset = Dataset(
        dataset_name=data.get("dataset_name"),
        dataset_size=data.get("dataset_size"),
        format=data.get("format"),
        user_id=data.get("user_id"),
        path=data.get("path"),
        description=data.get("description"),
    )
    db.session.add(dataset)
    try:
        db.session.commit()
        return send('ok', dataset)
    except IndexError:
        db.session.rollback()
        return send('error', 'error')
