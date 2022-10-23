import os
import logging
from dotenv import load_dotenv
from flask import Flask
from app.initializers import database
from app.initializers import api
from app.initializers import jwt


# load_dotenv('../.env.local')
print(os.environ)
app = Flask(__name__)

logging.basicConfig(level=os.getenv("LOG_LEVEL", "info").upper())

app.config["PROPAGATE_EXCEPTIONS"] = bool(os.getenv("PROPAGATE_EXCEPTIONS"))
app.config["API_TITLE"] = os.getenv("API_TITLE")
app.config["API_VERSION"] = os.getenv("API_VERSION")
app.config["OPENAPI_VERSION"] = os.getenv("OPENAPI_VERSION")
app.config["OPENAPI_URL_PREFIX"] = os.getenv("OPENAPI_URL_PREFIX")
app.config["OPENAPI_SWAGGER_UI_PATH"] = os.getenv("OPENAPI_SWAGGER_UI_PATH")
app.config["OPENAPI_SWAGGER_UI_URL"] = os.getenv("OPENAPI_SWAGGER_UI_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_db(app)
api.initialize(app)
jwt.initialize(app)
