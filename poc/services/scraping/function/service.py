import json

from db.models import SocialProfile, Post
from db.utils import init_db, create_all_tables
from .download import download_and_save_post
from .models import LambdaEvent
from .scrapers import BaseScraper


class ScrapingService:
    def __init__(self, scraper: BaseScraper):
        self._scraper = scraper
        self._setup_db()

    def _setup_db(self):
        init_db()
        create_all_tables()

    def _download_post(self, post: Post):
        print(f'downloading post "{post.shortcode}"')
        key = download_and_save_post(post)
        if key:
            post.media_s3_key = key
            post.update()

    def process_event(self, event: LambdaEvent) -> dict:
        if event.username:
            print(f'getting last post for "{event.username}"')
            insta_post = self._scraper.get_last_post(event.username)
            username = event.username
        else:
            print(f'getting post from url')
            insta_post = self._scraper.get_post_from_url(event.url)
            username = insta_post.owner_username

        profile, _ = SocialProfile.get_or_create(username=username)

        post = Post.from_instaloader_post(insta_post, profile)
        post, created = post.get_or_create()

        if created:
            self._download_post(post)
        else:
            print('post already in db, skipping')

        return {
            'statusCode': 200,
            'body': json.dumps({
                'post': {
                    'shortcode': post.shortcode,
                    'media_url': post.media_url
                }
            }),
        }
