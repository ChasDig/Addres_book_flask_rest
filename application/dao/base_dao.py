from sqlalchemy import desc
from typing import Generic, Union, TypeVar, Optional, Type, List
from sqlalchemy.orm import scoped_session

from application.setup.db import base_models

BaseModelTypes = TypeVar("BaseModelTypes", bound=base_models.BaseModel)


class BaseDAO(Generic[BaseModelTypes]):
    """Base DAO for all DAO in the application."""
    __model__ = base_models.BaseModel

    def __init__(self, db_session: scoped_session) -> None:
        self.db_session = db_session

    def get_one_by_id(self, sid: int) -> Type[BaseModelTypes]:
        return self.db_session.query(self.__model__).filter(self.__model__.id == sid).one()

    def get_all(self) -> List[Type[BaseModelTypes]]:
        return self.db_session.query(self.__model__).all()

    def delete_by_id(self, sid: int) -> str:
        self.db_session.query(self.__model__).filter(self.__model__.id == sid).delete()
        self.db_session.commit()
        return f"Delete object with id={sid}"

    def order_by_values(self, sort_values: str, reverse: bool = False) -> Union[List[Type[BaseModelTypes]], None]:
        value_order = None
        match reverse:
            case True:
                value_order = self.db_session.query(self.__model__).order_by(desc(sort_values)).all()
            case False:
                value_order = self.db_session.query(self.__model__).order_by(sort_values).all()
        return value_order
