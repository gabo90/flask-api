from app.config.db import db
from app.models.helper import ModelHelper


class ItemTagsModel(db.Model, ModelHelper):
    __tablename__ = "items_tags"

    id: db.Column = db.Column(db.Integer, primary_key=True)
    item_id: db.Column = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id: db.Column = db.Column(db.Integer, db.ForeignKey("tags.id"))
