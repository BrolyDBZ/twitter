from app import db
from flask_login import UserMixin


class user(db.Model,UserMixin):
    uniqueId=db.Column(db.String(),primary_key=True)
    userName=db.Column(db.String(32),nullable=False)
    password=db.Column(db.String(),nullable=False)
    firstName=db.Column(db.String(64),nulable=False)
    lastName=db.Column(db.String(64),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    bio=db.Column(db.Text)
    dateOfBirth=db.Column(db.DateTime,nullable=False)
    createdAt=db.Column(db.DateTime,nullable=False)
    following=db.Column(db.Integer,nullable=False,default=0)
    follower=db.Column(db.Integer,nullable=False,default=0)
    profilePicture=db.Column(db.LargeBinary)

    def __repr__(self):
        return self.userName+'-'+self.firstName+' '+self.lastName


class tweet(db.Model):
    pass



