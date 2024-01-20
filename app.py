from flask import Flask, request, jsonify
from myapp.controllers.UserController import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)