from flask import jsonify


class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class BadRequest(BaseServiceError):
    code = 400


def register_base_exception(error: BaseServiceError):
    return jsonify({"error": str(error)}), error.code
