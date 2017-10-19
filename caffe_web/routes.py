from flask import Blueprint

blueprint = Blueprint(__name__,__name__)
print __name__


@blueprint.route('/', methods=['POST'])
def fun():
    print '1'
    return '1'
