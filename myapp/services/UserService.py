from myapp.models.UserModel import User

class UserService:
    users = []  # In-memory storage, replace with a database later

    @classmethod
    def register_user(cls, username, password):
        existing_user = next((user for user in cls.users if user.username == username), None)

        if existing_user:
            return None  # User already exists

        new_user = User(username, password)
        cls.users.append(new_user)
        return new_user

    @classmethod
    def authenticate_user(cls, username, password):
        user = next((user for user in cls.users if user.username == username and user.password == password), None)
        return user
