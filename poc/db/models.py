from peewee import *

from . import db


class BaseModel(Model):
    class Meta:
        database = db


class SocialProfile(BaseModel):
    username = CharField(unique=True)
    suggested_profiles = ForeignKeyField('self', null=True)


class Location(BaseModel):
    score = FloatField()


class Post(BaseModel):
    social_profile = ForeignKeyField(SocialProfile, backref='posts', lazy_load=False)
    media_type = CharField(choices=['image', 'video'])
    media_s3_key = CharField()
    location = ForeignKeyField(Location, backref='posts', lazy_load=False)


class PostScore(BaseModel):
    media_score = FloatField(default=0)
    caption_score = FloatField(default=0)
    post = ForeignKeyField(Post, backref='post_score', lazy_load=False, unique=True)
