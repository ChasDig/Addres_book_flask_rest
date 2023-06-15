import flask
from flask_migrate import Migrate

from application.setup.db import db
from application.setup.api import api
from application.exceptions import register_base_exception, BaseServiceError
from application.views import user_namespace, phone_namespace, email_namespace


def create_application(config: str) -> flask.Flask:
    app = flask.Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    api.init_app(app)

    migrate = Migrate(app=app, db=db)

    api.add_namespace(user_namespace)
    api.add_namespace(phone_namespace)
    api.add_namespace(email_namespace)

    app.register_error_handler(BaseServiceError, register_base_exception)

    return app
