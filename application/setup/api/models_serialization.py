from flask_restx import fields, Model

from application.setup.api import api

users_serializer = api.model(
    "Users",
    {
        "id": fields.Integer(required=True),
        "username": fields.String(required=True, max_length=256),
        "user_images": fields.String(required=True),
        "sex": fields.String(required=True, max_length=5),
        "data_birth": fields.Date(required=True),
        "address": fields.String(required=True, max_length=256),
    },
)
phone_serializer = api.model(
    "Phones",
    {
        "id": fields.Integer(required=True),
        "user_id": fields.Integer(required=True),
        "view": fields.String(required=True, max_length=16),
        "number": fields.Integer(required=True),
    },
)
email_serializer = api.model(
    "Emails",
    {
        "id": fields.Integer(required=True),
        "user_id": fields.Integer(required=True),
        "name_email": fields.String(required=True, max_length=128),
        "view": fields.String(required=True, max_length=16),
    },
)
