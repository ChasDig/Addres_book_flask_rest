from flask_restx import Namespace, Resource
from flask import request

from application.container import email_service
from application.setup.api.models_serialization import email_serializer

api = Namespace("emails")


@api.route("/")
class EmailViews(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def post(self):
        return email_service.get_all_emails()

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=201, description="Created")
    def put(self):
        data_json = request.json
        return email_service.create_email(data_json=data_json)


@api.route("/<int:email_id>/")
class EmailsViews(Resource):

    @api.response(code=404, description="Not Found")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def post(self, email_id):
        return email_service.get_email_by_id(email_id=email_id)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def patch(self, email_id):
        data_json = request.json
        return email_service.update_email(email_id=email_id, data_json=data_json)

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=204, description="no content")
    def delete(self, email_id):
        return email_service.delete_email(email_id=email_id)


@api.route("/order/<path:sort_values>/<path:reverse>/")
class PhonesOrderViews(Resource):

    @api.response(code=400, description="Bad Request")
    @api.marshal_with(email_serializer, as_list=True, code=200, description="OK")
    def post(self, sort_values, reverse):
        return email_service.order_emails(sort_values=sort_values, reverse=reverse)
