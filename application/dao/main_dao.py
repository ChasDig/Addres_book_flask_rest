from sqlalchemy import desc
import datetime

from .base_dao import BaseDAO
from .models import Users, Phones, Emails


class UsersDAO(BaseDAO):
    __model__ = Users

    def get_user_by_id(self, user_id):
        return self.get_one_by_id(sid=user_id).one()

    def create_user(self, data_json):
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

    def update_user(self, user_id,  data_json):
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

    def delete_user(self, user_id):
        return self.delete_by_id(user_id)

    def order_users(self, sort_values: str, reverse: bool = False):
        return self.order_by_values(sort_values=sort_values, reverse=reverse)


class PhonesDAO(BaseDAO):
    __model__ = Phones

    def get_phone_by_id(self, phone_id):
        return self.get_one_by_id(sid=phone_id).one()

    def create_phone(self, data_json):
        new_phone = self.__model__(
            user_id=data_json["user_id"],
            view=data_json["view"],
            number=data_json["number"],
        )
        self.db_session.add(new_phone)
        self.db_session.commit()
        return new_phone

    def update_phone(self, phone_id, data_json):
        phone = self.get_one_by_id(phone_id).one()
        if "view" in data_json:
            phone.view = data_json["view"]
        if "number" in data_json:
            phone.number = data_json["number"]
        self.db_session.add(phone)
        self.db_session.commit()
        return phone

    def delete_phone(self, phone_id):
        return self.delete_by_id(phone_id)

    def order_phones(self, sort_values: str, reverse: bool = False):
        return self.order_by_values(sort_values=sort_values, reverse=reverse)


class EmailsDAO(BaseDAO):
    __model__ = Emails

    def get_email_by_id(self, email_id):
        return self.get_one_by_id(sid=email_id).one()

    def create_email(self, data_json):
        new_email = self.__model__(
            user_id=data_json["user_id"],
            name_email=data_json["name_email"],
            view=data_json["view"],
        )
        self.db_session.add(new_email)
        self.db_session.commit()
        return new_email

    def update_email(self, email_id, data_json):
        email = self.get_one_by_id(email_id).one()
        if "name_email" in data_json:
            email.name_email = data_json["name_email"]
        if "view" in data_json:
            email.view = data_json["view"]
        self.db_session.add(email)
        self.db_session.commit()
        return email

    def delete_email(self, email_id):
        return self.delete_by_id(email_id)

    def order_emails(self, sort_values: str, reverse: bool = False):
        return self.order_by_values(sort_values=sort_values, reverse=reverse)
