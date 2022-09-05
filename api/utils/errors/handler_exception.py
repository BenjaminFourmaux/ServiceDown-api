import random

import rest_framework.exceptions
from django.http import Http404
from rest_framework.views import exception_handler
from api.utils.errors.api_exceptions import APIError, MethodNotAllowed


def handler_exception(exc, context):
    error_response = exception_handler(exc, context)
    if error_response is not None:

        if type(exc) == Http404:  # Django HTTP error
            print('django error')
        elif type(exc) == rest_framework.exceptions.MethodNotAllowed:  # Rest Framework error
            error_response.data = custom_method_not_allowed(context)
        elif issubclass(type(exc), APIError):  # Custom error
            if exc.string_args:
                error_message = get_error_message(exc.error_message, exc.string_args,
                                                  context.get('kwargs'))
            else:
                # MethodNotAllowed error
                if type(exc) is MethodNotAllowed:
                    error_message = method_not_allowed_error_message(exc.error_message, context)
                else:
                    error_message = exc.error_message

            error_response.data = get_response(exc.error_code, exc.error_name, error_message)

    return error_response


def get_response(error_code, error_name, message):
    return {
        'error': {
            'error_code': error_code,
            'error_name': error_name,
            'error_message': message,
            'trace': generate_trace(),
        }
    }


def get_error_message(message: str, tab_properties, args: dict) -> str:
    tab_properties_value = []

    for parameter in tab_properties:
        tab_properties_value.append(args.get(parameter))
    return message.format(*tab_properties_value)


def generate_trace() -> str:
    trace_prefix = "sd_trace"
    trace_id = str(random.randint(10000, 99999))
    return trace_prefix + "-" + trace_id


def method_not_allowed_error_message(message, context) -> str:
    return message.format(*[context.get('request').method, context.get('request').get_full_path()])


def custom_method_not_allowed(context):
    return get_response(MethodNotAllowed.error_code, MethodNotAllowed.error_name, method_not_allowed_error_message(
        MethodNotAllowed.error_message, context))
