from flask import Blueprint, request, jsonify
from caffe_web.model import *
from caffe_web.utils import send

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/getProjectListByUser', methods = ["POST"])
def  getProjectListByUser():
    data = request.get_json()
    userId = data.get('userId')
    project = Project.query.filter(Project.user_id == userId).all()
    list_tmp = []
    for item in project:
        list_tmp.append({
            "project_id": item.id,
            "project_name": item.project_name,
            "updated_time": item.updated_at
        })
    tmp = {
        "project_list": list_tmp
    }
    return send("ok", tmp)


@blueprint.route('/getProjectDetailById', methods = ["POST"])
def getProjectDetailById():
    data = request.get_json()
    projectId = data.get('projectId')
    project = Project.query.filter(Project.id == projectId).first()
    tmp = {
        "dataset_name": project.dataset.dataset_name,
        "project_name": project.project_name,
        "net_name": project.net.net_name,
        "solver_name": project.solver.solver_name
    }
    return send("ok", tmp)

@blueprint.route('/createProject', methods=["POST"])
def createProject():
    data = request.get_json()
    projectName = data.get('projectName')
    project = Project(project_name = projectName)
    db.session.add(project)
    db.session.commit()
    result = {
        "status": "ok",
        "data": {}
    }
    return jsonify(result)
