from functools import cached_property
from enum import Enum, unique
from typing import Set, Optional

from peewee import *

from . import db


@unique
class MediaType(str, Enum):
    IMAGE = 'image'
    VIDEO = 'video'


class BaseModel(Model):
    class Meta:
        database = db


class SocialProfile(BaseModel):
    username = CharField(unique=True, null=False)


class Location(BaseModel):
    name = CharField(unique=True)
    lat = FloatField(default=0)
    long = FloatField(default=0)
    score = FloatField()


class Post(BaseModel):
    shortcode = CharField(unique=True)
    caption = TextField()
    social_profile = ForeignKeyField(SocialProfile, backref='posts', lazy_load=False)
    media_type = CharField(choices=[MediaType.IMAGE, MediaType.VIDEO])
    media_url = CharField(max_length=512)
    media_s3_key = CharField(null=True, unique=True)
    location = ForeignKeyField(Location, backref='posts', lazy_load=False, null=True)

    @cached_property
    def media_filename(self) -> str:
        extension = 'mp4' if self.media_type == MediaType.VIDEO else 'jpg'
        return f'{self.shortcode}.{extension}'

    @cached_property
    def hashtags(self) -> Set[str]:
        tags = [tag.strip('#') for tag in self.caption.split() if tag.startswith('#')]
        return set(tags)

    @classmethod
    def from_instaloader_post(cls, insta_post, profile: Optional[SocialProfile] = None):
        if not profile:
            profile = SocialProfile.get_or_create(username=insta_post.owner_username)
        return cls(
            shortcode=insta_post.shortcode,
            caption=insta_post.caption,
            media_url=insta_post.video_url if insta_post.is_video else insta_post.url,
            media_type=MediaType.VIDEO if insta_post.is_video else MediaType.IMAGE,
            social_profile=profile
        )


class PostScore(BaseModel):
    media_score = FloatField(default=0)
    caption_score = FloatField(default=0)
    post = ForeignKeyField(Post, backref='post_score', lazy_load=False, unique=True)
