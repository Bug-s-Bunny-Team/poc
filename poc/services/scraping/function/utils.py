import os
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

from .custom import CustomInstaloader
from .scrapers import BaseScraper, InstagramScraper
from .sessions import InstagramSessionProvider


def create_scraper() -> BaseScraper:
    insta_username = os.environ['INSTA_USERNAME']
    sessions_table = os.environ['INSTA_SESSIONS_TABLE']

    session_provider = InstagramSessionProvider(sessions_table)
    insta = CustomInstaloader()

    session = session_provider.get_session(insta_username)
    if session:
        print('using saved session')
        insta.import_session_from_dict(session, insta_username)
    else:
        print('session not found, logging in')
        insta_password = os.environ['INSTA_PASSWORD']
        insta.login(insta_username, insta_password)
        session_provider.refresh_session(insta_username, session)

    return InstagramScraper(client=insta)


def s3_key_exists(bucket_name: str, key: str) -> bool:
    try:
        s3 = boto3.client('s3')
        s3.head_object(Bucket=bucket_name, Key=key)
        return True
    except ClientError:
        return False


def s3_upload_file(bucket_name: str, key: str, src: Path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file(str(src), key)
