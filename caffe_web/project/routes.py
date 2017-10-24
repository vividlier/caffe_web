from flask import Blueprint
from flask import request
from caffe_web.model import Project

blueprint = Blueprint(__name__, __name__)


@blueprint.route('/getProjectListByUser', methods=['POST'])
def getPorjectListByUser():
    data = request.get_json()
    userId = 13
    # 由user_id查到Project表的信息
    # print(Project.query.filter(Project.user_id == 13).first())
    # print(Project.query.filter(Project.user_id == 13).all())
    project = Project.query.filter(Project.user_id == userId).all()
    for data in project:
        print(data.id, data.project_name, data.updated_at)

    return 'got it'