from pydantic import ValidationError

from common.utils import create_error_response

from .handler import RequestsHandler
from .models import Request


def lambda_handler(event, context):
    try:
        request = Request(**event)
    except ValidationError as e:
        return create_error_response(str(e))

    handler = RequestsHandler()
    return handler.handle_request(request)
