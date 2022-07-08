import datetime

from rest_framework.views import exception_handler
import random


def handler_exception(exc, context):
    error_response = exception_handler(exc, context)

    if error_response is not None:
        error_response.data = get_response(exc.get_codes(), exc.detail)

    return error_response


def get_response(error_code, message):
    return {
        'error': {
            'error_code': error_code,
            "error_message": message,
            'trace': generate_trace(),
        }
    }


def generate_trace() -> str:
    trace_prefix = "sd_trace"
    trace_id = str(random.randint(10000, 99999))
    return trace_prefix + "-" + trace_id
