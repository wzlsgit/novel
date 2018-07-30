from exts import db
from datetime import datetime
class Novels(db.Model):
    __tablename__='novels'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    edits=db.Column(db.String(30),nullable=False)
    name=db.Column(db.String(50),nullable=False)
    image=db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now)
class Contents(db.Model):
    __tablename__ = 'contents'
    novels_id = db.Column(db.Integer,db.ForeignKey('novels.id'))
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author=db.relationship('Novels',backref=db.backref('questions'))
# class Answer(db.Model):
#     __tablename__ = 'answer'
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     content=db.Column(db.Text, nullable=False)
#     create_time = db.Column(db.DateTime, default=datetime.now)
#     question_id=db.Column(db.Integer, db.ForeignKey('question.id'))
#     author_id=db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     question=db.relationship('Question',backref=db.backref('answers',order_by=create_time.desc()))
#     author = db.relationship('User', backref=db.backref('answers'))