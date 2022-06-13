import json
from pathlib import Path

from pydantic import ValidationError

from .models import LambdaEvent
from .utils import create_scraper, download_media


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

    print('downloading post media')
    dest = Path('/tmp') / post.media_filename
    print(dest)
    download_media(post.media_url, dest)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__
        }),
    }
