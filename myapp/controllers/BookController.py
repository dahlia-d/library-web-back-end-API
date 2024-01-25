from flask import request, jsonify, make_response, Blueprint
from myapp.services.BookService import *

book_controller = Blueprint('book_controller', __name__)

@book_controller.route('/get_all', methods=['GET'])
def get_books():
    return make_response(jsonify(BookService.get_all_books()))

@book_controller.route('/add', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')

    if not title or not author:
        return make_response(jsonify({'error': 'Missing title or author'}), 400)
    
    book = BookService.add_book(title, author)

    if book:
        return make_response(jsonify({'message': 'Book is added successfully'}))
    else:
        return make_response(jsonify({'error': 'There is book with the same title and author'}))

@book_controller.route('/status', methods=['PUT'])
def status():
    data = request.get_json()
    book_id = data.get('book_id')
    user_id = data.get('user_id')
    if BookService.change_status(book_id, user_id) == None:
        return make_response(jsonify({'message': 'The book is already assigned'}), 200)
    else:
        return make_response(jsonify({'message': 'The book is assigned successfully'}), 409)