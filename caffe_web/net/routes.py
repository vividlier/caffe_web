from flask import Blueprint, request, jsonify
from caffe_web.model import *
from caffe_web.utils import send

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/createNet', methods = ['POST'])
def createNet():
    data = request.get_json()
    net = Net(
        user_id = data.get('user_id'),
        net_name = data.get('net_name'),
        net_path = data.get('net_path')
    )
    db.session.add(net)
    try:
        db.session.commit()
        tmp = {
            "status": "ok",
            "data": {}
        }
        return jsonify(tmp)
    except IndexError:
        db.session.rollback()
        return "error"


@blueprint.route('/getNetByUser', methods = ['POST'])
def getNetByUser():
    data = request.get_json()
    userId = data.get('userId')
    net = Net.query.filter(Net.user_id == userId).all()
    list_tmp = []
    for item in net:
        list_tmp.append({
            "net_id": item.id,
            "net_name": item.net_name,
            "net_path": item.net_path
        })

    return send("ok", list_tmp)
