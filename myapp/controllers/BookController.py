from flask import request, jsonify, make_response, Blueprint
from myapp.services.BookService import *

book_controller = Blueprint('book_controller', __name__)

@book_controller.route('/books', methods=['GET'])
def get_books():
    return jsonify(get_books())

@book_controller.route('/status/<int:book_id>', methods=['PUT'])
def status():
    data = request.get_json()
    id = data.get('id')
    BookService.change_status(id, 0)  
    return make_response(jsonify({'message': 'test route'}), 200)

    
