from typing import Type, List

from application.dao.models import Emails
from application.dao.main_dao import EmailsDAO
from application.exceptions import BadRequest, ItemNotFound

EMAIL_BASE_FIELDS = ["id", "user_id", "name_email", "view"]


class EmailServices:
    def __init__(self, dao: EmailsDAO) -> None:
        self.dao = dao

    def get_email_by_id(self, email_id: int) -> Type[Emails]:
        try:
            return self.dao.get_email_by_id(email_id=email_id)
        except Exception:
            raise ItemNotFound(f"Error: user with id = {email_id} not found!")

    def get_all_emails(self) -> List[Type[Emails]]:
        return self.dao.get_all_emails()

    def create_email(self, data_json: dict) -> Emails:
        try:
            return self.dao.create_email(data_json=data_json)
        except KeyError as ex:
            raise BadRequest(f"Error: field with name '{ex}' not found!")

    def update_email(self, email_id: int, data_json: dict) -> Type[Emails]:
        for field in data_json.keys():
            if field not in EMAIL_BASE_FIELDS:
                raise BadRequest(f"Error: Field '{field}' not in Emails table!")
        return self.dao.update_email(email_id=email_id, data_json=data_json)

    def delete_email(self, email_id: int) -> str:
        try:
            return self.dao.delete_email(email_id=email_id)
        except Exception:
            raise ItemNotFound(f"Error: email with id = {email_id} not found!")

    def order_emails(self, sort_values: str, reverse: str) -> List[Type[Emails]]:
        if sort_values not in EMAIL_BASE_FIELDS:
            raise BadRequest(f"Error: Field '{sort_values}' not in Emails table!")
        if int(reverse) not in [0, 1]:
            raise BadRequest(f"Error: reverse must be 0 or 1, not '{reverse}'!")
        return self.dao.order_emails(sort_values=sort_values, reverse=bool(reverse))
