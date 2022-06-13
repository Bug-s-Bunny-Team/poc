import os
from pathlib import Path

import requests

from .custom import CustomInstaloader
from .scrapers import BaseScraper, InstagramScraper
from .sessions import InstagramSessionProvider


# TODO: add option to download file in memory and don't create a new file
def download_media(url: str, dest: Path):
    with requests.get(url, stream=True) as r:
        with open(dest, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


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
