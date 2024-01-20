from flask import Blueprint, request, jsonify
from myapp.services.UserService import UserService

user_controller = Blueprint('UserController', __name__)

@user_controller.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = UserService.register_user(username, password)

    if user:
        return jsonify({'message': 'User registered successfully'})
    else:
        return jsonify({'error': 'Username already exists'}), 409

@user_controller.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserService.authenticate_user(username, password)

    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401