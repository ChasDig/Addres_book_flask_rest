from application.setup.db import base_models
from sqlalchemy import desc


class BaseDAO:
    """Base DAO for all DAO in the application."""
    __model__ = base_models.BaseModel

    def __init__(self, db_session):
        self.db_session = db_session

    def get_one_by_id(self, sid):
        return self.db_session.query(self.__model__).filter(self.__model__.id == sid)

    def get_all(self):
        return self.db_session.query(self.__model__).all()

    def delete_by_id(self, sid):
        self.get_one_by_id(sid).delete()
        self.db_session.commit()
        return "Delete"

    def order_by_values(self, sort_values: str, reverse: bool = False):
        value_order = None
        match reverse:
            case True:
                value_order = self.db_session.query(self.__model__).order_by(desc(sort_values)).all()
            case False:
                value_order = self.db_session.query(self.__model__).order_by(sort_values).all()
        return value_order
