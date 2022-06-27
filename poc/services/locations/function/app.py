from pydantic import ValidationError

from common.models import Request
from common.utils import create_error_response

from .provider import LocationProvider


def lambda_handler(event, context):
    try:
        request = Request(**event)
    except ValidationError as e:
        return create_error_response(str(e))

    provider = LocationProvider()
    return provider.handle_request(request)
