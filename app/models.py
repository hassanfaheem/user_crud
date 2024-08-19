import bcrypt

class User:
    def __init__(self, username, password, active):
        self.username = username
        self.set_password(password)
        self.active = active

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash)

    def __repr__(self):
        return f"User(username={self.username}, active={self.active})"
