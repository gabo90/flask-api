from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.models.store import StoreModel
from app.models.tag import TagModel
from app.schemas.store_schema import StoreSchema
from app.schemas.tag_schema import TagSchema


resource = Blueprint("Stores", "stores", description="Operations on stores")


@resource.route("/stores/<string:store_id>")
class Store(MethodView):
    @resource.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        store.delete()

        return {"message": "Store deleted"}


@resource.route("/stores")
class StoreList(MethodView):
    @resource.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @resource.arguments(StoreSchema)
    @resource.response(200, StoreSchema)
    def post(self, store_data):
        try:
            store = StoreModel(**store_data)
            store.save()

            return store
        except IntegrityError as err:
            print(err)
            abort(400, message="A Store with that name already exists.")

        except SQLAlchemyError as err:
            print(err)
            abort(500, message="An error occurred while inserting the store.")


@resource.route("/stores/<string:store_id>/tags")
class StoreTags(MethodView):
    @resource.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store.tags.all()

    @resource.arguments(TagSchema)
    @resource.response(200, TagSchema)
    def post(self, tag_data, store_id):
        try:
            tag = TagModel(store_id=store_id, **tag_data)
            tag.save()

            return tag
        except IntegrityError as err:
            print(err)
            abort(400, message=str(err))

        except SQLAlchemyError as err:
            print(err)
            abort(500, message=str(err))

