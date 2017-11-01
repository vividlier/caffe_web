from flask import Blueprint, request
from caffe_web.model import *
from caffe_web.utils import send

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/getProjectDetailById', methods=["POST"])
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
