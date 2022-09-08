from api.utils.errors.api_exceptions import APIError


class ServiceException(APIError):
    pass


class ServiceNotFound(ServiceException):
    status_code = 404
    error_code = 201
    error_name = 'service_not_found'
    error_message = 'Service id: {0} not found'

    string_args = ['pk']


class ServiceNotInCountry(ServiceException):
    status_code = 404
    error_code = 202
    error_name = 'service_not_in_country'
    error_message = 'Service: {0} not available in Country: {1}'

    string_args = ['service_id', 'country_id']

