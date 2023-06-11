from sqlalchemy import Column, Integer
from application.setup.db import db


class BaseModel(db.Model):
    """Base model for the application."""
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
