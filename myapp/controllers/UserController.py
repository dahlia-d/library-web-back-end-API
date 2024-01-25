from flask import Blueprint, request, jsonify, make_response
from myapp.services.UserService import UserService

user_controller = Blueprint('user_controller', __name__)


@user_controller.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test test test'}), 200)

@user_controller.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = UserService.register_user(username, password)

    if user:
        return make_response(jsonify({'message': 'User registered successfully'}), 200)
    else:
        return make_response(jsonify({'error': 'Username already exists'}), 409)

@user_controller.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserService.authenticate_user(username, password)

    if user:
        return make_response(jsonify({'message': 'Login successful'}))
    else:
        return make_response(jsonify({'error': 'Invalid credentials'}), 401)