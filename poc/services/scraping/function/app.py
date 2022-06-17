import json

from pydantic import ValidationError

from .exceptions import ItemNotFoundException
from .models import LambdaEvent
from .service import ScrapingService
from .utils import create_scraper


def lambda_handler(event, context):
    try:
        event = LambdaEvent(**event)
    except ValidationError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            }),
        }

    try:
        scraper = create_scraper()
    except ItemNotFoundException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            }),
        }

    service = ScrapingService(scraper)
    return service.process_event(event)
