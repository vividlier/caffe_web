from caffe_web.model import *

# u1 = User(username='john', password='john@example.com')
# db.session.add(u1)
# db.session.commit()
tst = Project.query.all()
print tst[0].user.username
