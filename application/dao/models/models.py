from sqlalchemy import Column, Integer, Float, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, validates

from application.setup.db import db, base_models
from application.exceptions import BadRequest

USER_SEX = ["male", "female"]
PHONES_VIEW = ["Городской", "Мобильный"]
EMAIL_VIEW = ["Личная", "Рабочая"]


class Users(base_models.BaseModel):
    __tablename__ = "users"

    username = Column(String(256), nullable=False, unique=True)
    user_images = Column(String())
    sex = Column(String(), nullable=False)
    data_birth = Column(Date, nullable=False)
    address = Column(String(256), nullable=False)

    @validates("sex")
    def validate_user_sex(self, _, address):
        if address not in USER_SEX:
            raise BadRequest(f"Error: user_sex must be 'male' or 'female', not '{address}'!")
        return address


class Phones(base_models.BaseModel):
    __tablename__ = "phones"

    user_id = Column(Integer, ForeignKey(f"{Users.__tablename__}.id"), nullable=False)
    user = relationship("Users")

    view = Column(String(), nullable=False)
    number = Column(String(), nullable=False)

    @validates("view")
    def validate_phones_view(self, _, address):
        if address not in PHONES_VIEW:
            raise BadRequest(f"Error: view must be 'Городской' or 'Мобильный', not '{address}'!")
        return address

    @validates("number")
    def validate_phones_number(self, _, address):
        if len(address) != 11:
            raise BadRequest("Error: number length must be equal to 11 and start with 8-***-***-**-**!")
        return address


class Emails(base_models.BaseModel):
    __tablename__ = "emails"

    user_id = Column(Integer, ForeignKey(f"{Users.__tablename__}.id"), nullable=False)
    users = relationship("Users")

    name_email = Column(String(128), nullable=False)
    view = Column(String(), nullable=False)

    @validates("name_email")
    def validate_email_name_email(self, _, address):
        if "@" not in address:
            raise BadRequest(f"Error: '@' should be in 'name_email'!")
        return address

    @validates("view")
    def validate_email_view(self, _, address):
        if address not in EMAIL_VIEW:
            raise BadRequest(f"Error: view must be 'Личная' or 'Рабочая', not '{address}'!")
        return address
