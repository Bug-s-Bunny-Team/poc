import os

from pony.orm import *

db = Database()


def init_db():
    db.bind(
        provider='postgres',
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
    )
    db.generate_mapping(create_tables=True)


class SocialProfile(db.Entity):
    id = PrimaryKey(int, auto=True)
    posts = Set('Post')
    suggested_profiles = Set('SocialProfile', reverse='suggested_profiles')


class Post(db.Entity):
    id = PrimaryKey(int, auto=True)
    social_profile = Required(SocialProfile)
    media_type = Required(str, default='image')
    media_s3_key = Required(str)
    post_score = Optional('PostScore')
    location = Optional('Location')


class Location(db.Entity):
    id = PrimaryKey(int, auto=True)
    posts = Set(Post)
    score = Optional(float)


class PostScore(db.Entity):
    id = PrimaryKey(int, auto=True)
    post = Required(Post)
    media_score = Required(float, default=0)
    caption_score = Optional(float, default=0)
