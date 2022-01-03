from flask import Flask
from .routes import short
from .extensions import db

def create_app(config_file='settings.py'):
    url_shortener_app = Flask(__name__)
    url_shortener_app.config.from_pyfile(config_file)

    db.init_app(url_shortener_app)
    url_shortener_app.register_blueprint(short)

    return url_shortener_app