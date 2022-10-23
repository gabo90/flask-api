from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from app.models import TagModel
from app.models.item import ItemModel
from app.schemas.item_schema import ItemSchema, ItemUpdateSchema
from app.schemas.item_tags_schema import ItemTagsSchema
from app.schemas.tag_schema import TagSchema

resource = Blueprint("Items", "items", description="Operations on items")


@resource.route("/items/<string:item_id>")
class Item(MethodView):
    @resource.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)

        return item

    @resource.arguments(ItemUpdateSchema)
    @resource.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        item.save()

        return item

    @jwt_required()
    def delete(self, item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        item = ItemModel.query.get_or_404(item_id)
        item.delete()

        return {"message": "Item deleted"}


@resource.route("/items")
class ItemList(MethodView):
    @jwt_required(fresh=True)
    @resource.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @jwt_required()
    @resource.arguments(ItemSchema)
    @resource.response(201, ItemSchema)
    def post(self, item_data):
        try:
            item = ItemModel(**item_data)
            item.save()

            return item
        except SQLAlchemyError as err:
            print(err)
            abort(500, message="An error occurred while inserting the item")


@resource.route("/items/<string:item_id>/tags/<string:tag_id>")
class ItemTags(MethodView):
    @resource.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)

        try:
            item.save()
            return tag
        except SQLAlchemyError as err:
            print(err)
            abort(500, message="An error occurred while inserting the tag")

    @resource.response(200, ItemTagsSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            item.save()
            return {"message": "Tag remove from item", "item": item, "tag": tag}
        except SQLAlchemyError as err:
            print(err)
            abort(500, message="An error occurred while deleting the tag")
