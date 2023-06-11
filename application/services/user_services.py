from application.dao.main_dao import UsersDAO
from application.exceptions import ItemNotFound, BadRequest

USERS_BASE_FIELDS = ["id", "username", "user_images", "sex", "data_birth", "address"]


class UsersServices:
    def __init__(self, dao: UsersDAO):
        self.dao = dao

    def get_user_by_id(self, user_id):
        try:
            return self.dao.get_user_by_id(user_id=user_id)
        except Exception:
            raise ItemNotFound(f"Error: user with id = {user_id} not found!")

    def get_all_users(self):
        return self.dao.get_all()

    def create_user(self, data_json):
        try:
            return self.dao.create_user(data_json=data_json)
        except KeyError as ex:
            raise BadRequest(f"Error: field with name '{ex}' not found!")

    def update_user(self, user_id, data_json):
        for field in data_json.keys():
            if field not in USERS_BASE_FIELDS:
                raise BadRequest(f"Error: Field '{field}' not in Users table!")
        return self.dao.update_user(user_id=user_id, data_json=data_json)

    def delete_user(self, user_id):
        try:
            user = self.get_user_by_id(user_id=user_id)
            if user:
                self.dao.delete_user(user_id=user_id)
        except Exception:
            raise ItemNotFound(f"Error: user with id = {user_id} not found!")

    def order_users(self, sort_values: str, reverse: str):
        if sort_values not in USERS_BASE_FIELDS:
            raise BadRequest(f"Error: Field '{sort_values}' not in Users table!")
        if int(reverse) not in [0, 1]:
            raise BadRequest(f"Error: reverse must be 0 or 1, not '{reverse}'!")
        return self.dao.order_users(sort_values=sort_values, reverse=bool(int(reverse)))
