def send(status, data={}):
    if status == 'error':
        pass
    else:
        rst = {'status': status, 'data': data}
        return rst


def ensureAuth():
    pass
