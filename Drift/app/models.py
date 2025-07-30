from app import db
from flask_login import UserMixin
from datetime import datetime, timezone
from bcrypt import hashpw, gensalt, checkpw


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)

    bio = db.Column(db.Text, nullable=True)
    static = db.Column(db.Text, nullable=True)

    email = db.Column(db.String(120), unique=True, nullable=False)

    avatar = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    newsletter = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

    def check_password(self, password):
        return checkpw(password.encode("utf-8"), self.password_hash.encode("utf-8"))


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
