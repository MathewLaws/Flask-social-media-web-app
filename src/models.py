from flask_login.mixins import UserMixin
from . import db
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    posts = db.relationship("Post")


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250))
    img = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    mimetype = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
