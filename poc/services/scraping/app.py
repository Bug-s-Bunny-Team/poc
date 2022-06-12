import os
import json

from scrapers import InstagramScraper, BaseScraper
from custom import CustomInstaloader
from sessions import InstagramSessionProvider


def create_scraper() -> BaseScraper:
    insta_username = os.environ.get('INSTA_USERNAME')

    session_provider = InstagramSessionProvider('poc-instagram-sessions')
    insta = CustomInstaloader()

    session = session_provider.get_session(insta_username)
    if session:
        print('using saved session')
        insta.import_session_from_dict(session, insta_username)
    else:
        print('session not found, logging in')
        insta_password = os.environ.get('INSTA_PASSWORD')
        insta.login(insta_username, insta_password)
        session_provider.refresh_session(insta_username, session)

    return InstagramScraper(client=insta)


def lambda_handler(event, context):
    username = event['username']

    scraper = create_scraper()
    post = scraper.get_last_post(username)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__
        }),
    }
