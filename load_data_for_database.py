import pathlib
import json
import datetime
from contextlib import suppress
from sqlalchemy.exc import IntegrityError

from application.service import create_application
from application.config import config
from application.setup.db import db
from application.dao.models.models import Users, Phones, Emails

BASE_PATH = pathlib.Path(__file__).resolve().parent.parent
DATA_FOR_DATABASE_PATH = BASE_PATH / "address_book_flask_rest" / "data_for_database.json"


def load_data_in_database(data, model):
    for item in data:
        item["id"] = item.pop("pk")
        if item.get("data_birth"):
            year, month, day = item["data_birth"].split("-")
            item["data_birth"] = datetime.date(int(year), int(month), int(day))
        db.session.add(model(**item))


if __name__ == "__main__":
    with open(DATA_FOR_DATABASE_PATH, encoding="utf-8") as file:
        data_for_database_json = json.load(file)

    app = create_application(config=config)

    with app.app_context():
        load_data_in_database(data_for_database_json["users"], Users)
        load_data_in_database(data_for_database_json["phones"], Phones)
        load_data_in_database(data_for_database_json["emails"], Emails)

        with suppress(IntegrityError):
            db.session.commit()