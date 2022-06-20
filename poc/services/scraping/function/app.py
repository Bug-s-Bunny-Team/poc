from pydantic import ValidationError

from common.exceptions import ItemNotFoundException
from common.utils import create_error_response

from .models import ScrapingEvent
from .service import ScrapingService
from .utils import create_scraper


def lambda_handler(event, context):
    try:
        event = ScrapingEvent(**event)
    except ValidationError as e:
        return create_error_response(str(e))

    try:
        scraper = create_scraper()
    except ItemNotFoundException as e:
        return create_error_response(str(e), 500)

    service = ScrapingService(scraper)
    return service.process_event(event)
