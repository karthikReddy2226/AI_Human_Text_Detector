from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "admin"
        self.password = "admin123"  # You can hash this with bcrypt
