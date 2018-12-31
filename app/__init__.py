from app.db import db
from app.ma import ma
from flask import Flask
from flask_migrate import Migrate
from app.routes import register_route


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py", silent=True)
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    register_route(app)
    return app

