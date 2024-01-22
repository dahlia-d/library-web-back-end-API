from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from myapp.controllers.UserController import *
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URL')

from myapp.models.Models import *

db.init_app(app)
with app.app_context():
  db.create_all()

@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test rrrsssroute'}), 200)

if __name__ == "__main__":
    app.run(port=5000)
