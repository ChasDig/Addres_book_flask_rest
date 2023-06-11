from application.service import create_application
from application.config import config
from application.setup.db import db

if __name__ == "__main__":
    with create_application(config=config).app_context():
        db.create_all()
