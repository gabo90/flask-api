from app.config.db import db
from app.models.helper import ModelHelper


class ItemModel(db.Model, ModelHelper):
    __tablename__ = "items"

    id: db.Column = db.Column(db.Integer, primary_key=True)
    name: db.Column = db.Column(db.String(80), unique=True, nullable=False)
    description: db.Column = db.Column(db.String)
    price: db.Column = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id: db.Column = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)

    store: db.relationship = db.relationship("StoreModel", back_populates="items")
    tags: db.relationship = db.relationship("TagModel", back_populates="items", secondary="items_tags")
