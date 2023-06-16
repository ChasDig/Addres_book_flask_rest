from typing import Type, List

from flask_restx import Namespace, Resource
from flask import request

from application.dao.models import Emails
from application.container import email_service
from application.setup.api.models_serialization import email_serializer
from rabbitmq_logging_service import rabbitmq_logging

api = Namespace("emails")


@api.route("/")
class EmailViews(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def post(self) -> List[Type[Emails]]:
        return email_service.get_all_emails()

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=201, description="Created")
    @rabbitmq_logging
    def put(self) -> Emails:
        data_json = request.json
        return email_service.create_email(data_json=data_json)


@api.route("/<int:email_id>/")
class EmailsViews(Resource):

    @api.response(code=404, description="Not Found")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def post(self, email_id: int) -> Type[Emails]:
        return email_service.get_email_by_id(email_id=email_id)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    @rabbitmq_logging
    def patch(self, email_id: int) -> Type[Emails]:
        data_json = request.json
        return email_service.update_email(email_id=email_id, data_json=data_json)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=204, description="no content")
    @rabbitmq_logging
    def delete(self, email_id: int) -> str:
        return email_service.delete_email(email_id=email_id)


@api.route("/order/<path:sort_values>/<int:reverse>/")
class PhonesOrderViews(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def post(self, sort_values: str, reverse: int) -> List[Type[Emails]]:
        return email_service.order_emails(sort_values=sort_values, reverse=reverse)
