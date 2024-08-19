from app.models import User

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password, active):
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")
        if username in self.users:
            raise ValueError("User already exists.")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        self.users[username] = User(username, password, active)
        return self.users[username]

    def read_user(self, username):
        if not username:
            raise ValueError("Username cannot be empty.")
        user = self.users.get(username)
        if user is None:
            raise ValueError("User not found.")
        return user

    def update_user(self, username, password=None, active=None):
        if not username:
            raise ValueError("Username cannot be empty.")
        user = self.users.get(username)
        if user is None:
            raise ValueError("User not found.")
        if password is not None:
            if len(password) < 6:
                raise ValueError("Password must be at least 6 characters long.")
            user.set_password(password)
        if active is not None:
            user.active = active
        return user

    def delete_user(self, username):
        if not username:
            raise ValueError("Username cannot be empty.")
        if username not in self.users:
            raise ValueError("User not found.")
        del self.users[username]
