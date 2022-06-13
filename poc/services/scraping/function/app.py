import json
from pydantic import ValidationError

from .download import download_and_save_post
from .models import LambdaEvent
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

    print('getting scraper')
    scraper = create_scraper()

    print(f'getting last post for "{event.username}"')
    post = scraper.get_last_post(event.username)

    print(f'downloading post "{post.id}"')
    download_and_save_post(post)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__
        }),
    }
