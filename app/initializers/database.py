from app.config.db import db
from flask_migrate import Migrate
from app.models import *


def init_db(app=None):
    db.init_app(app)

    # with app.app_context():
    #     db.create_all()

    migrate = Migrate(app, db)
