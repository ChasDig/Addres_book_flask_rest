from typing import Type, List

from flask_restx import Namespace, Resource
from flask import request

from application.dao.models import Phones
from application.container import phone_service
from application.setup.api.models_serialization import phone_serializer
from rabbitmq_logging_service import rabbitmq_logging

api = Namespace("phones")


@api.route("/")
class PhonesViews(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def post(self) -> List[Type[Phones]]:
        return phone_service.get_all_phones()

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=201, description="Created")
    @rabbitmq_logging
    def put(self) -> Phones:
        data_json = request.json
        return phone_service.create_phones(data_json=data_json)


@api.route("/<int:phone_id>/")
class PhoneViews(Resource):

    @api.response(code=404, description="Not Found")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def post(self, phone_id: int) -> Type[Phones]:
        return phone_service.get_phone_by_id(phone_id=phone_id)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    @rabbitmq_logging
    def patch(self, phone_id: int) -> Type[Phones]:
        data_json = request.json
        return phone_service.update_phone(phone_id=phone_id, data_json=data_json)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=204, description="no content")
    @rabbitmq_logging
    def delete(self, phone_id: int) -> str:
        return phone_service.delete_phone(phone_id=phone_id)


@api.route("/order/<path:sort_values>/<int:reverse>/")
class PhonesOrderView(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def post(self, sort_values: str, reverse: int) -> List[Type[Phones]]:
        return phone_service.order_phones(sort_values=sort_values, reverse=reverse)
