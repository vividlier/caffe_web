from flask import jsonify


def send(status, data={}):
    if status == 'error':
        pass
    else:
        rst = {'status': status, 'data': data}
        return jsonify(rst)


def ensureAuth():
    pass
