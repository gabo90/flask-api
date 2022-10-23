from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.models import UserModel
from app.schemas.user_schema import UserSchema

resource = Blueprint("Users", "users", description="Operations on users")


@resource.route("/users")
class User(MethodView):
    @resource.arguments(UserSchema)
    def post(self, user_data):
        try:
            user = UserModel(
                username=user_data['username'],
                password=pbkdf2_sha256.hash(user_data['password'])
            )

            user.save()
            return {"message": "User created successfully."}
        except IntegrityError as err:
            print(err)
            abort(400, message="An user with that name already exists.")

        except SQLAlchemyError as err:
            print(err)
            abort(500, message="An error occurred while registering the user.")


@resource.route("/users/<int:user_id>")
class Users(MethodView):
    @resource.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        user.delete()

        return {"message": "User deleted"}

