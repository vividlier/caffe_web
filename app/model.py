from app import db

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
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)


class Project(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    user_id = db.Column(db.INTEGER)
    project_name = db.Column(db.String(50))
    net_id = db.Column(db.INTEGER)
    dataset_id = db.Column(db.INTEGER)
    solver_id = db.Column(db.INTEGER)

    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)


class Net(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    user_id = db.Column(db.INTEGER)
    net_path = db.Column(db.String(50))
    net_name = db.Column(db.String(50))

    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)


class Dataset(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    dataset_name = db.Column(db.String(50))
    dataset_size = db.Column(db.INTEGER)
    format = db.Column(db.String(50))
    project_id = db.Column(db.INTEGER)
    path = db.Column(db.String(100))
    description = db.Column(db.TEXT)

    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)


class Train(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    user_id = db.Column(db.INTEGER)
    train_path = db.Column(db.String(100))
    train_name = db.Column(db.String(50))

    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)
    delete_at = db.Column(db.DATETIME)

