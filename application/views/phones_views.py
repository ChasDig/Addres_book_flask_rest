from flask_restx import Namespace, Resource
from flask import request

from application.container import phone_service
from application.setup.api.models_serialization import phone_serializer
from application.app_logger import start_logging

api = Namespace("phones")


@api.route("/")
class PhonesViews(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def post(self):
        return phone_service.get_all_phones()

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=201, description="Created")
    def put(self):
        start_logging()
        data_json = request.json
        return phone_service.create_phones(data_json=data_json)


@api.route("/<int:phone_id>/")
class PhoneViews(Resource):

    @api.response(code=404, description="Not Found")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def post(self, phone_id):
        return phone_service.get_phone_by_id(phone_id=phone_id)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def patch(self, phone_id):
        start_logging()
        data_json = request.json
        return phone_service.update_phone(phone_id=phone_id, data_json=data_json)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=204, description="no content")
    def delete(self, phone_id):
        start_logging()
        return phone_service.delete_phone(phone_id=phone_id)


@api.route("/order/<path:sort_values>/<path:reverse>/")
class PhonesOrderView(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(phone_serializer, as_list=True, code=200, description="OK")
    def post(self, sort_values, reverse):
        return phone_service.order_phones(sort_values=sort_values, reverse=reverse)
