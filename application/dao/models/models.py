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

    def __init__(self, username, user_images, sex, data_birth, address):
        self.username = username
        self.user_images = user_images
        self.sex = sex
        self.data_birth = data_birth
        self.address = address

    def __repr__(self):
        return f"id {self.id}"

    @validates("sex")
    def validate_user_sex(self, _, address: str) -> str:
        if address not in USER_SEX:
            raise BadRequest(f"Error: user_sex must be 'male' or 'female', not '{address}'!")
        return address


class Phones(base_models.BaseModel):
    __tablename__ = "phones"

    user_id = Column(Integer, ForeignKey(f"{Users.__tablename__}.id"), nullable=False)
    user = relationship("Users")

    view = Column(String(), nullable=False)
    number = Column(String(), nullable=False)

    def __init__(self, user_id, view, number):
        self.user_id = user_id
        self.view = view
        self.number = number

    def __repr__(self):
        return f"id {self.id}"

    @validates("view")
    def validate_phones_view(self, _, address: str) -> str:
        if address not in PHONES_VIEW:
            raise BadRequest(f"Error: view must be 'Городской' or 'Мобильный', not '{address}'!")
        return address

    @validates("number")
    def validate_phones_number(self, _, address: str) -> str:
        if len(address) != 11:
            raise BadRequest("Error: number length must be equal to 11 and start with 8-***-***-**-**!")
        return address


class Emails(base_models.BaseModel):
    __tablename__ = "emails"

    user_id = Column(Integer, ForeignKey(f"{Users.__tablename__}.id"), nullable=False)
    users = relationship("Users")

    name_email = Column(String(128), nullable=False)
    view = Column(String(), nullable=False)

    def __init__(self, user_id, name_email, view):
        self.user_id = user_id
        self.name_email = name_email
        self.view = view

    def __repr__(self):
        return f"id {self.id}"

    @validates("name_email")
    def validate_email_name_email(self, _, address: str) -> str:
        if "@" not in address:
            raise BadRequest(f"Error: '@' should be in 'name_email'!")
        return address

    @validates("view")
    def validate_email_view(self, _, address: str) -> str:
        if address not in EMAIL_VIEW:
            print(type(address))
            raise BadRequest(f"Error: view must be 'Личная' or 'Рабочая', not '{address}'!")
        return address
