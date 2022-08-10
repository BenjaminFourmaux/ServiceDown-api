from api.utils.errors.api_exceptions import APIError


class CountryException(APIError):
    pass


class CountryNotFound(CountryException):
    status_code = 404
    error_code = 101
    error_name = 'country_not_found'
    error_message = 'Country id: {0} not found'

    string_args = ['pk']


class CountryNotAvailable(CountryException):
    status_code = 403
    error_code = 102
    error_name = 'country_not_available'
    error_message = 'This country is not available'


class CountryShortnameNotExist(CountryException):
    status_code = 404
    error_code = 103
    error_name = 'country_shortname_not_exist'
    error_message = 'Country shortname: \'{0}\' not exist'

    string_args = ['shortname']
