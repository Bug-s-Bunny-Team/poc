from pydantic import ValidationError

from common.models import Request
from common.providers import DataProvider
from common.utils import create_error_response
from db.models import Location
from db.utils import init_db, create_all_tables


def lambda_handler(event, context):
    try:
        request = Request(**event)
    except ValidationError as e:
        return create_error_response(str(e))

    init_db()

    provider = DataProvider(model=Location)
    return provider.handle_request(request)
