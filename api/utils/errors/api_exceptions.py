from rest_framework.exceptions import APIException


class APIError(APIException):
    error_type: str
