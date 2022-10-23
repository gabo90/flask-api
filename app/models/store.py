from app.config.db import db
from app.models.helper import ModelHelper


class StoreModel(db.Model, ModelHelper):
    __tablename__ = "stores"

    id: db.Column = db.Column(db.Integer, primary_key=True)
    name: db.Column = db.Column(db.String(80), unique=True, nullable=False)

    items: db.relationship = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
    tags: db.relationship = db.relationship("TagModel", back_populates="store", lazy="dynamic")
