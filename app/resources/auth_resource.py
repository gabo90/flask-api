from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
)
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.models import UserModel
from app.schemas.user_schema import UserSchema

resource = Blueprint("Auth", "auth", description="Operations on auth")


@resource.route("/login")
class CreateToken(MethodView):
    @resource.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data['username']
        ).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            auth_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"auth_token": auth_token, "refresh_token": refresh_token}

        abort(401, message="Invalid credentials.")


@resource.route('/refresh')
class RefreshToken(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        fresh_token = create_access_token(identity=current_user, fresh=False)
        return {"auth_token": fresh_token}

