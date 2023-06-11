from application.dao.main_dao import PhonesDAO
from application.exceptions import ItemNotFound, BadRequest

PHONE_BASE_FIELDS = ["id", "user_id", "view", "number"]


class PhonesService:
    def __init__(self, dao: PhonesDAO):
        self.dao = dao

    def get_phone_by_id(self, phone_id):
        try:
            return self.dao.get_phone_by_id(phone_id=phone_id)
        except Exception:
            raise ItemNotFound(f"Error: phone with id = {phone_id} not found!")

    def get_all_phones(self):
        return self.dao.get_all()

    def create_phones(self, data_json):
        try:
            return self.dao.create_phone(data_json=data_json)
        except KeyError as ex:
            raise BadRequest(f"Error: field with name '{ex}' not found!")

    def update_phone(self, phone_id, data_json):
        for field in data_json.keys():
            if field not in PHONE_BASE_FIELDS:
                raise BadRequest(f"Error: Field '{field}' not in Phones table!")
        return self.dao.update_phone(phone_id=phone_id, data_json=data_json)

    def delete_phone(self, phone_id):
        try:
            phone = self.get_phone_by_id(phone_id=phone_id)
            if phone:
                self.dao.delete_phone(phone_id=phone_id)
        except Exception:
            raise ItemNotFound(f"Error: phone with id = {phone_id} not found!")

    def order_phones(self, sort_values: str, reverse: str):
        if sort_values not in PHONE_BASE_FIELDS:
            raise BadRequest(f"Error: Field '{sort_values}' not in Phones table!")
        if int(reverse) not in [0, 1]:
            raise BadRequest(f"Error: reverse must be 0 or 1, not '{reverse}'!")
        return self.dao.order_phones(sort_values=sort_values, reverse=bool(int(reverse)))
