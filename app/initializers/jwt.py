import os

from flask import jsonify
from flask_jwt_extended import JWTManager


def initialize(app=None):
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        print("expired_token", "jwt:", jwt_header, "payload", jwt_payload)

        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_loader_callback(error):
        print("invalid_token", "error:", error)

        return (
            jsonify({"message": "Signature verification failed", "error": "invalid_token"}),
            401,
        )

    @jwt.unauthorized_loader
    def unauthorized_loader_callback(error):
        print("unauthorized_loader", "error:", error)

        return (
            jsonify({
                "description": "Request does not contain an access token.",
                "error": "authorization_required"
            }),
            401,
        )
