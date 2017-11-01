from flask import Blueprint, request, jsonify
from caffe_web.model import *
from caffe_web.utils import send

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/getProjectListByUser', methods = ["POST"])
def  getProjectListByUser():
    data = request.get_json()
    userId = data.get('userId')
    project = Project.query.filter(Project.user_id == userId).all()
    l = []
    for item in project:
        l.append({
            "project_id": item.id,
            "project_name": item.project_name,
            "updated_time": item.updated_at
        })
    print(l)
    result = {
        "status": "ok",
        "data": {
            "project_list":l
        }
    }
    return jsonify(result)


@blueprint.route('/getProjectDetailById', methods = ["POST"])
def getProjectDetailById():
    data = request.get_json()
    projectId = data.get('projectId')
    project = Project.query.filter(Project.id == projectId).first()
    tmp = {}
    tmp["dataset_name"] = project.dataset.dataset_name
    tmp["project_name"] = project.project_name
    tmp["net_name"] = project.net.net_name
    tmp["solver_name"] = project.solver.solver_name
    return send("ok", tmp)
