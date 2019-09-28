from .blog.schemas import serializer
from .blog.models import Model
from flask import Flask
from flask_migrate import Migrate

from .blog.controllers import BlogController


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    Model.configure(app)
    Migrate(app, app.db)

    serializer.configure(app)
    BlogController.configure(app)

    return app
