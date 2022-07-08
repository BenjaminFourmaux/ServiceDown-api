from api.utils.errors.api_exceptions import APIError


class CountryException(APIError):
    pass


class CountryNotAvailable(CountryException):
    status_code = 403
    default_code = 'country_not_available'
    default_detail = 'This country is not available'
