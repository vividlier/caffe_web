from flask import Blueprint, request
from caffe_web.model import *

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/getProjectDetailById', methods=["POST"])
def getProjectDetailById():
    data = request.get_json()
    projectId = data.get('projectId')
    project = Project.query.filter(Project.id == projectId).first()
    print project.project_name
    return 'detail'
