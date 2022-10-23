from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.schemas.tag_schema import TagSchema
from app.models.tag import TagModel


resource = Blueprint("Tags", "tags", description="Operations on tags")


@resource.route("/tags/<string:tag_id>")
class Tags(MethodView):
    @resource.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        return tag

    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        tag.delete()

        return {"message": "Tag deleted"}
