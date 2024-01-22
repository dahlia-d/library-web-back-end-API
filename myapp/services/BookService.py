from myapp.models.Models import Book

class BookService:

    @classmethod
    def get_books(cls):
        return cls.books

    @classmethod
    def change_status(cls, id, user_id):
        book = Book.query.get_or_404(id)
        if book.status == 1:
            return None
        else:
            book.assingedUserId = user_id
            book.status = 1
            return book