from api.utils.errors.api_exceptions import APIError


class SearchException(APIError):
    pass


class MissingQueryParameter(SearchException):
    status_code = 400
    error_code = 401
    error_name = 'missing_query_parameter'
    error_message = "Missing query parameter : 'q'"
