import pytest

from application.service import create_application
from application.setup.db import db as database
from application.config import TestConfig


@pytest.fixture
def app():
    app = create_application(config=TestConfig)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    # database.init_app(app=app)
    database.drop_all()
    database.create_all()
    database.session.commit()
    yield database
    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client
