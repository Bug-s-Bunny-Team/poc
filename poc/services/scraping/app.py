import json

from pydantic import ValidationError

from models import LambdaEvent
from utils import create_scraper


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

    scraper = create_scraper()
    post = scraper.get_last_post(event.username)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__
        }),
    }
