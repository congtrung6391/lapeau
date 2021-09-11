from flask_login import UserMixin

from .db import get_db

class User(UserMixin):
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @staticmethod
    def get(username):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()
        if not user:
            return None

        user = User(
            username=user[0], password=user[1], name=user[2], email=user[3]
        )
        return user

    @staticmethod
    def create(username, password, name, email):
        db = get_db()
        db.execute(
            "INSERT INTO user (username, password, name, email) "
            "VALUES (?, ?, ?, ?)",
            (username, password, name, email),
        )
        db.commit()