import json
import os

import boto3
from instaloader import Post as InstaPost

from db.models import SocialProfile, Post, Location
from db.utils import init_db
from .download import download_and_save_post
from .models import ScrapingEvent
from .scrapers import InstagramScraper


class ScrapingService:
    def __init__(self, scraper: InstagramScraper):
        self._scraper = scraper
        self._sns_topic = boto3.resource('sns').Topic(os.environ['SNS_SCORING_TOPIC'])
        init_db()

    def _get_success_response(self, post: Post):
        return {
            'statusCode': 200,
            'body': json.dumps(
                {'post': {'shortcode': post.shortcode, 'media_url': post.media_url}}
            ),
        }

    def _download_post(self, post: Post):
        print(f'downloading post "{post.shortcode}"')
        key = download_and_save_post(post)
        post.media_s3_key = key
        post.save()

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
        location = None
        if insta_location := insta_post.location:
            print('post has location data')
            location, _ = Location.from_instaloader_location(insta_location)
        post, created = Post.from_instaloader_post(insta_post, profile, location)

        if created:
            self._download_post(post)
        else:
            print('post already in db, skipping download')

        print('publishing scoring message to topic')
        self._sns_topic.publish(Message=json.dumps({
            'post_id': post.id
        }))

        return self._get_success_response(post)
