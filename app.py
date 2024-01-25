from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URL')

db = SQLAlchemy()

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

db.init_app(app)
with app.app_context():
  db.create_all()

from myapp.controllers.UserController import *
app.register_blueprint(user_controller, url_prefix='/user')

from myapp.controllers.BookController import *
app.register_blueprint(book_controller, url_prefix='/book')

if __name__ == "__main__":
    app.run(port=5000)
