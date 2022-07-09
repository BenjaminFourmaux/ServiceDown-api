from rest_framework.exceptions import APIException


class APIError(APIException):
    # Error properties
    error_code: int
    error_name: str
    error_message: str

    string_args = []

