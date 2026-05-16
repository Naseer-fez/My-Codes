from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__="User"
    id = db.Column(db.Integer, primary_key=True,unique=True,autoincrement=True)
    Username=db.Column(db.String(50),nullable=False,unique=True)
    Password=db.Column(db.String(256),nullable=False)
    Email=db.Column(db.String(50),nullable=True,unique=True)
    links = db.relationship('Links', backref='owner', lazy=True)
    

