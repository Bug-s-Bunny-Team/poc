import json
from pathlib import Path

import boto3
from pydantic import ValidationError

from .models import LambdaEvent
from .utils import create_scraper, download_media, s3_key_exists


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

    post_key = f'instagram/{post.media_filename}'
    if s3_key_exists(boto3.client('s3'), 'swe-bucket-bugsbunny', post_key):
        print('post already downloaded, skipping')
    else:
        print('downloading post media')

        dest = Path('/tmp') / post.media_filename
        download_media(post.media_url, dest)

        print(f'uploading to s3 with key "{post_key}"')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('swe-bucket-bugsbunny')
        bucket.upload_file(str(dest), post_key)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__
        }),
    }
