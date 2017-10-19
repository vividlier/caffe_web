from app import db
from datetime import datetime
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)

    projects = db.relationship('Project', backref='user')
    nets = db.relationship('Net', backref='user')
    datasets = db.relationship('Dataset', backref='user')
    trains = db.relationship('Train', backref='user')
    solvers = db.relationship('Solver', backref='user')


class Project(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    project_name = db.Column(db.String(50), nullable=False)
    net_id = db.Column(db.INTEGER, db.ForeignKey('net.id'))
    dataset_id = db.Column(db.INTEGER, db.ForeignKey('dataset.id'))
    solver_id = db.Column(db.INTEGER, db.ForeignKey('solver.id'))

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)
    net = db.relationship('Net', backref='project')
    dataset = db.relationship('Dataset', backref='project')
    solver = db.relationship('Solver', backref='project')


class Net(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    net_path = db.Column(db.String(50), nullable=False)
    net_name = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)
    # project = db.relationship('Project', uselist=False, back_populates='net')


class Dataset(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    dataset_name = db.Column(db.String(50), nullable=False)
    dataset_size = db.Column(db.INTEGER)
    format = db.Column(db.String(50))
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    path = db.Column(db.String(100))
    description = db.Column(db.TEXT)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)
    # project = db.relationship('Project', uselist=False, back_populates='dataset')


class Train(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    train_path = db.Column(db.String(100))
    train_name = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)


class Solver(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    solver_path = db.Column(db.String(100))
    solver_name = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)
