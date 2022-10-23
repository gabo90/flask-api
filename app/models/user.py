from app.config.db import db
from app.models.helper import ModelHelper


class UserModel(db.Model, ModelHelper):
    __tablename__ = 'users'

    id: db.Column = db.Column(db.Integer, primary_key=True)
    username: db.Column = db.Column(db.String(80), unique=True, nullable=False)
    password: db.Column = db.Column(db.String(), nullable=False)
