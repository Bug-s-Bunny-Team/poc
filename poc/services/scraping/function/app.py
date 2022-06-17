import json

from pydantic import ValidationError

from db.utils import init_db, create_all_tables
from db.models import SocialProfile, Post

from .download import download_and_save_post
from .exceptions import ItemNotFoundException
from .models import LambdaEvent
from .utils import create_scraper


# TODO: scrape only if not in db

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

    init_db()
    create_all_tables()

    print('getting scraper')
    try:
        scraper = create_scraper()
    except ItemNotFoundException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            }),
        }

    if event.username:
        print(f'getting last post for "{event.username}"')
        insta_post = scraper.get_last_post(event.username)
        username = event.username
    else:
        print(f'getting post from url')
        insta_post = scraper.get_post_from_url(event.url)
        username = insta_post.owner_username

    profile, _ = SocialProfile.get_or_create(username=username)

    post = Post.from_instaloader_post(insta_post, profile)
    post.save()

    print(f'downloading post "{post.shortcode}"')
    download_and_save_post(post)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'post': {
                'shortcode': post.shortcode,
                'social_profile': post.social_profile.username,
                'media_url': post.media_url
            }
        }),
    }
