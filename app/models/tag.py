from app.config.db import db
from app.models.helper import ModelHelper


class TagModel(db.Model, ModelHelper):
    __tablename__ = "tags"

    id: db.Column = db.Column(db.Integer, primary_key=True)
    name: db.Column = db.Column(db.String(80), unique=True, nullable=False)
    store_id: db.Column = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store: db.relationship = db.relationship("StoreModel", back_populates="tags")
    items: db.relationship = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")
