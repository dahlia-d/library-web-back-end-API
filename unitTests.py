import requests, json

BASE_URL = 'http://127.0.0.1:5000'

register_data = {'username': 'john_doe', 'password': 'secret123'}
register_response = requests.post(f'{BASE_URL}/user/register', json=register_data)
print(register_response.json())

login_data = {'username': 'john_doe', 'password': 'secret123'}
login_response = requests.post(f'{BASE_URL}/user/login', json=login_data)
print(login_response.json())
wrong_login_data = {'username': 'john_doe', 'password': 'wrong'}
error_login_response = requests.post(f'{BASE_URL}/user/login', json=wrong_login_data)
print(error_login_response.json())

book_data = {'title': 'Diskworld', 'author': 'Terry Pratchett'}
book_response = requests.post(f'{BASE_URL}/book/add', json=book_data)
print(book_response.json())

#books_response = requests.post(f'{BASE_URL}/book/get_all')
#print(books_response.json())

assign_book_data = {'book_id': 1, 'user_id': 1}
assign_book_response = requests.put(f'{BASE_URL}/book/status', json=assign_book_data)
print(assign_book_response.json())
