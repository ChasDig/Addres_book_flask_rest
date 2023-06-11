from sqlalchemy import Column, Integer, Float, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship

from application.setup.db import db, base_models


class Users(base_models.BaseModel):
    __tablename__ = "users"

    username = Column(String(256), nullable=False, unique=True)
    user_images = Column(String())
    sex = Column(String(5))
    data_birth = Column(Date, nullable=False)
    address = Column(String(256))


class Phones(base_models.BaseModel):
    __tablename__ = "phones"

    user_id = Column(Integer, ForeignKey(f"{Users.__tablename__}.id"), nullable=False)
    user = relationship("Users")

    view = Column(String(16))
    number = Column(Integer())


class Emails(base_models.BaseModel):
    __tablename__ = "emails"

    user_id = Column(Integer, ForeignKey(f"{Users.__tablename__}.id"), nullable=False)
    users = relationship("Users")

    name_email = Column(String(128), nullable=False)
    view = Column(String(16), nullable=False)