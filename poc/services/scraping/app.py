import os
import json

from scrapers import InstagramScraper
from custom import CustomInstaloader


def lambda_handler(event, context):
    username = event['username']

    insta_username = os.environ.get('INSTA_USERNAME')
    insta_session = json.loads(os.environ.get('INSTA_SESSION'))

    insta = CustomInstaloader()
    insta.import_session_from_dict(insta_session, insta_username)

    scraper = InstagramScraper(client=insta)
    post = scraper.get_last_post(username)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__,
        }),
    }
