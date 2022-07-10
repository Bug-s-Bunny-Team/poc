from typing import Optional

from peewee import DoesNotExist, JOIN
from playhouse.shortcuts import model_to_dict

from common.providers import DataProvider
from db.models import Post, SocialProfile, Location


class PostProvider(DataProvider):
    def __init__(self):
        super().__init__(Post)

    def query_all(self):
        results = (
            Post.select(Post, SocialProfile, Location)
            .join(SocialProfile, on=(Post.social_profile == SocialProfile.id))
            .switch(Post)
            .join(Location, on=(Post.location == Location.id), join_type=JOIN.LEFT_OUTER)
        )
        return results

    def query_by_id(self, entity_id: int) -> Optional:
        try:
            return self.query_all().where(Post.id == entity_id).get()
        except DoesNotExist:
            return None

    # TODO: add scores
    @staticmethod
    def serialize(result: Post) -> dict:
        return {
            'id': result.id,
            'caption': result.caption,
            'media_url': result.media_s3_key,
            'media_score': 0.0,
            'caption_score': 0.0,
            'location': model_to_dict(result.location) if result.location else None,
            'profile': model_to_dict(result.social_profile),
        }
