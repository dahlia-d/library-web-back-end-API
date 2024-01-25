from myapp.models.Models import User, db

class UserService:

    users = User.query.all()

    @classmethod
    def register_user(cls, username, password):
        existing_user = next((user for user in cls.users if user.username == username), None)

        if existing_user:
            return None  # User already exists

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def authenticate_user(cls, username, password):
        user = next((user for user in cls.users if user.username == username and user.password == password), None)
        return user