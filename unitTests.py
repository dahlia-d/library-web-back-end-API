import requests, json

# Replace with your local development server address
BASE_URL = 'http://127.0.0.1:5000'

# Register a User
register_data = {'username': 'john_doe', 'password': 'secret123'}
register_response = requests.post(f'{BASE_URL}/user/register', json=register_data)
print(register_response.text)

# Login
login_data = {'username': 'john_doe', 'password': 'secret123'}
login_response = requests.post(f'{BASE_URL}/user/login', json=login_data)
print(login_response.json())
