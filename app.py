from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URL')

from myapp.models.Models import *
db = SQLAlchemy()
db.init_app(app)
with app.app_context():
  db.create_all()

from myapp.controllers.UserController import *
app.register_blueprint(user_controller, url_prefix='/user')

if __name__ == "__main__":
    app.run(port=5000)
