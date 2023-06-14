from typing import Type, List
from flask_restx import Namespace, Resource
from flask import request

from application.dao.models import Users
from application.container import users_service
from application.setup.api.models_serialization import users_serializer
from application.rabbitmq_logging_service import rabbitmq_logging

api = Namespace("users")


@api.route("/")
class UsersView(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(users_serializer, as_list=True, code=200, description="OK")
    def post(self) -> List[Type[Users]]:
        return users_service.get_all_users()

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(users_serializer, as_list=True, code=201, description="Created")
    @rabbitmq_logging
    def put(self) -> Users:
        data_json = request.json
        return users_service.create_user(data_json=data_json)


@api.route("/<int:user_id>/")
class UserView(Resource):

    @api.response(code=404, description="Not Found")
    @api.marshal_with(users_serializer, as_list=True, code=200, description="OK")
    def post(self, user_id: int) -> Type[Users]:
        return users_service.get_user_by_id(user_id=user_id)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(users_serializer, as_list=True, code=200, description="OK")
    @rabbitmq_logging
    def patch(self, user_id: int) -> Type[Users]:
        data_json = request.json
        return users_service.update_user(user_id=user_id, data_json=data_json)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(users_serializer, as_list=True, code=204, description="no content")
    @rabbitmq_logging
    def delete(self, user_id: int) -> str:
        return users_service.delete_user(user_id=user_id)


@api.route("/order/<path:sort_values>/<int:reverse>/")
class UsersOrderView(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(users_serializer, as_list=True, code=200, description="OK")
    def post(self, sort_values: str, reverse: int) -> List[Type[Users]]:
        return users_service.order_users(sort_values=sort_values, reverse=reverse)
