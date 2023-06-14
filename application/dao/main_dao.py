import datetime
from sqlalchemy import desc
from typing import Type, List

from .base_dao import BaseDAO, BaseModelTypes
from .models import Users, Phones, Emails


class UsersDAO(BaseDAO[Users]):
    __model__ = Users

    def get_user_by_id(self, user_id: int) -> Type[Users]:
        return self.get_one_by_id(sid=user_id)

    def get_all_users(self) -> List[Type[Users]]:
        return self.get_all()

    def create_user(self, data_json: dict) -> Users:
        year, month, day = data_json["data_birth"].split("-")
        data_json["data_birth"] = datetime.date(int(year), int(month), int(day))
        new_user = self.__model__(
            username=data_json["username"],
            user_images=data_json["user_images"],
            sex=data_json["sex"],
            data_birth=data_json["data_birth"],
            address=data_json["address"],
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user

    def update_user(self, user_id: int,  data_json: dict) -> Type[Users]:
        user = self.get_user_by_id(user_id)
        if "username" in data_json:
            user.username = data_json["username"]
        if "sex" in data_json:
            user.sex = data_json["sex"]
        if "data_birth" in data_json:
            year, month, day = data_json["data_birth"].split("-")
            user.data_birth = datetime.date(int(year), int(month), int(day))
        if "address" in data_json:
            user.address = data_json["address"]
        self.db_session.add(user)
        self.db_session.commit()
        return user

    def delete_user(self, user_id: int) -> str:
        return self.delete_by_id(user_id)

    def order_users(self, sort_values: str, reverse: bool = False) -> List[Type[Users]]:
        return self.order_by_values(sort_values=sort_values, reverse=reverse)


class PhonesDAO(BaseDAO[Phones]):
    __model__ = Phones

    def get_phone_by_id(self, phone_id: int) -> Type[Phones]:
        return self.get_one_by_id(sid=phone_id)

    def get_all_phones(self) -> List[Type[Phones]]:
        return self.get_all()

    def create_phone(self, data_json: dict) -> Phones:
        new_phone = self.__model__(
            user_id=data_json["user_id"],
            view=data_json["view"],
            number=str(data_json["number"]),
        )
        self.db_session.add(new_phone)
        self.db_session.commit()
        return new_phone

    def update_phone(self, phone_id: int, data_json: dict) -> Type[Phones]:
        phone = self.get_one_by_id(phone_id)
        if "view" in data_json:
            phone.view = data_json["view"]
        if "number" in data_json:
            phone.number = str(data_json["number"])
        self.db_session.add(phone)
        self.db_session.commit()
        return phone

    def delete_phone(self, phone_id: int) -> str:
        return self.delete_by_id(phone_id)

    def order_phones(self, sort_values: str, reverse: bool = False) -> List[Type[Phones]]:
        return self.order_by_values(sort_values=sort_values, reverse=reverse)


class EmailsDAO(BaseDAO[Emails]):
    __model__ = Emails

    def get_email_by_id(self, email_id: int) -> Type[Emails]:
        return self.get_one_by_id(sid=email_id)

    def get_all_emails(self) -> List[Type[Emails]]:
        return self.get_all()

    def create_email(self, data_json: dict) -> Emails:
        new_email = self.__model__(
            user_id=data_json["user_id"],
            name_email=data_json["name_email"],
            view=data_json["view"],
        )
        self.db_session.add(new_email)
        self.db_session.commit()
        return new_email

    def update_email(self, email_id: int, data_json: dict) -> Type[Emails]:
        email = self.get_one_by_id(email_id)
        if "name_email" in data_json:
            email.name_email = data_json["name_email"]
        if "view" in data_json:
            email.view = data_json["view"]
        self.db_session.add(email)
        self.db_session.commit()
        return email

    def delete_email(self, email_id: int) -> str:
        return self.delete_by_id(email_id)

    def order_emails(self, sort_values: str, reverse: bool = False) -> List[Type[Emails]]:
        return self.order_by_values(sort_values=sort_values, reverse=reverse)
