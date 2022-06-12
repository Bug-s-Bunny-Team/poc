import os
import json

import boto3

from scrapers import InstagramScraper
from custom import CustomInstaloader


def refresh_session(table, username: str, session: dict):
    table.update_item(
        Key={'username': username},
        UpdateExpression='SET session_data = :s',
        ExpressionAttributeValues={':s': session}
    )


def lambda_handler(event, context):
    username = event['username']

    insta_username = os.environ.get('INSTA_USERNAME')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('poc-instagram-sessions')

    insta = CustomInstaloader()
    insta_session = table.get_item(Key={'username': insta_username}).get('Item')

    if insta_session:
        print('using saved session')
        insta.import_session_from_dict(insta_session.get('session_data'), insta_username)
    else:
        print('session not found, logging in')
        insta_password = os.environ.get('INSTA_PASSWORD')
        insta.login(insta_username, insta_password)
        refresh_session(table, insta_username, insta.export_session_as_dict())

    scraper = InstagramScraper(client=insta)
    post = scraper.get_last_post(username)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': post.__dict__
        }),
    }
