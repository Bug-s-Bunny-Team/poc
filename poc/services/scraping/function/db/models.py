from . import db

from pony.orm import *


class SocialProfile(db.Entity):
    id = PrimaryKey(int, auto=True)
    posts = Set('Post')
    suggested_profiles = Set('SocialProfile', reverse='suggested_profiles')
    username = Required(str)


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
