from flask_smorest import Api
from app.resources import auth, store, item, tag, user


def initialize(app=None):
    api = Api(app)

    api.register_blueprint(auth)
    api.register_blueprint(store)
    api.register_blueprint(item)
    api.register_blueprint(tag)
    api.register_blueprint(user)

    return api
