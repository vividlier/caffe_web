from caffe_web import db,User

u1 = User(username= 'john', email = 'john@example.com')
db.session.add(u1)
db.session.commit()
