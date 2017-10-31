from flask import Blueprint, request, jsonify
from caffe_web.model import *

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/getProjectListByUser', methods = ["POST"])
def  getProjectListByUser():
    data = request.get_json()
    userId = data.get('userId')
    project = Project.query.filter(Project.user_id == userId).first()
    d = {
        "status": "ok",
        "data":{
            "project_list":[
                {
                    "project_id": project.id,
                    "project_name": project.project_name,
                    "updated_time": project.updated_at
                }
            ]
        }
    }
    return jsonify(d)


@blueprint.route('/getProjectDetailById', methods = ["POST"])
def getProjectDetailById():
    data = request.get_json()
    projectId = data.get('projectId')
    project = Project.query.filter(Project.id == projectId).first()
    print(project.project_name)
    return 'detail'
