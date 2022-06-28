from pydantic import ValidationError

from common.models import Request
from common.utils import create_error_response
from db.utils import init_db

from .provider import PostProvider


def lambda_handler(event, context):
    try:
        request = Request(**event)
    except ValidationError as e:
        return create_error_response(str(e))

    init_db()

    provider = PostProvider()
    return provider.handle_request(request)
