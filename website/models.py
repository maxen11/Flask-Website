from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10_000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique id to identify entry
    email = db.Column(db.String(150), unique=True)  # Unique email, no duplicate emails
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship("Note")
