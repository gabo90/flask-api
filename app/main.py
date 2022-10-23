from asgiref.wsgi import WsgiToAsgi
from app.config.application import app


asgi_app = WsgiToAsgi(app)
