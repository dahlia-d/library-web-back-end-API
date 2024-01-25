from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String, unique = True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    status = db.Column(db.Boolean)
    assingedUserId = db.Column(db.Integer)

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = False
        assingedUserId = None