import os
import datetime
import json
from typing import List, Dict, Any, Type
from contextlib import suppress
from sqlalchemy.exc import IntegrityError

from application.setup.db.base_models import BaseModel
from application.service import create_application
from application.config import config
from application.setup.db import db
from application.dao.models.models import Users, Phones, Emails


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FOR_DATABASE_PATH = BASE_PATH + "/data_for_database.json"


def load_data_in_database(data: List[Dict["str", Any]], model: Type[BaseModel]) -> None:
    for item in data:
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
