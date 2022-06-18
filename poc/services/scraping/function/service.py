import json

from instaloader import Post as InstaPost

from db.models import SocialProfile, Post
from db.utils import init_db, create_all_tables

from .download import download_and_save_post
from .models import ScrapingEvent
from .scrapers import InstagramScraper


class ScrapingService:
    def __init__(self, scraper: InstagramScraper):
        self._scraper = scraper
        self._setup_db()

    def _setup_db(self):
        init_db()
        create_all_tables()  # TODO: don't do this in production

    def _get_success_response(self, post: Post):
        return {
            'statusCode': 200,
            'body': json.dumps({
                'post': {
                    'shortcode': post.shortcode,
                    'media_url': post.media_url
                }
            }),
        }

    def _download_post(self, post: Post):
        print(f'downloading post "{post.shortcode}"')
        key = download_and_save_post(post)
        post.media_s3_key = key
        post.update()

    def _scrape_last_post(self, username: str) -> InstaPost:
        print(f'getting last post for "{username}"')
        insta_post = self._scraper.get_last_post(username)
        return insta_post

    def _scrape_url(self, url: str) -> InstaPost:
        print(f'getting post from url')
        insta_post = self._scraper.get_post_from_url(url)
        return insta_post

    def process_event(self, event: ScrapingEvent) -> dict:
        if event.username:
            insta_post = self._scrape_last_post(event.username)
        else:
            shortcode = self._scraper.extract_shortcode(event.url)
            post = Post.get_or_none(shortcode=shortcode)
            if not post:
                insta_post = self._scrape_url(event.url)
            else:
                print('post already in db, skipping')
                return self._get_success_response(post)

        profile, _ = SocialProfile.get_or_create(username=insta_post.owner_username)
        post = Post.from_instaloader_post(insta_post, profile)
        post, created = post.get_or_create()

        if created:
            self._download_post(post)
        else:
            print('post already in db, skipping download')

        return self._get_success_response(post)
