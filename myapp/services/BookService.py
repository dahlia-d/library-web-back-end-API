from app import Book, db, app

class BookService:

    with app.app_context():
        books = Book.query.all()

    @classmethod
    def add_book(cls, title, author):
        existing_book = next((book for book in cls.books if book.title == title and book.author == author), None)

        if existing_book:
            return None  # User already exists

        new_book = Book(title, author)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @classmethod
    def get_all_books(cls):
        return cls.books

    @classmethod
    def change_status(cls, id, user_id):
        book = Book.query.get_or_404(id)
        if book.status == 1:
            return None
        else:
            book.assignedUserId = user_id
            book.status = 1
            db.session.commit()
            return book