import os

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@115.159.43.33:3306/cambricon'
SQLALCHEMY_TRACK_MODIFICATIONS = False
secret = 'aGVsbG8gd29ybGQ='
