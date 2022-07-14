from api.utils.errors.api_exceptions import APIError


class ServiceException(APIError):
    pass


class CountryNotFound(ServiceException):
    status_code = 404
    error_code = 201
    error_name = 'service_not_found'
    error_message = 'Service id: {0} not found'

    string_args = ['pk']
