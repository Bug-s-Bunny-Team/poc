from typing import Optional

from peewee import DoesNotExist, JOIN
from playhouse.shortcuts import model_to_dict

from common.providers import DataProvider
from db.models import Post, SocialProfile, Location, PostScore


class PostProvider(DataProvider):
    def __init__(self):
        super().__init__(Post)

    def query_all(self):
        results = (
            Post.select(Post, SocialProfile, Location, PostScore)
            .join(SocialProfile, on=(Post.social_profile == SocialProfile.id))
            .switch(Post)
            .join(
                Location, on=(Post.location == Location.id), join_type=JOIN.LEFT_OUTER
            )
            .switch(Post)
            .join(PostScore, on=(Post.id == PostScore.post), join_type=JOIN.LEFT_OUTER)
            .order_by(-Post.added)
        )
        return results

    def query_by_id(self, entity_id: int) -> Optional:
        try:
            return self.query_all().where(Post.id == entity_id).get()
        except DoesNotExist:
            return None

    @staticmethod
    def serialize(result: Post) -> dict:
        # ugly, causes n+1 problem
        score = result.score.get_or_none()
        score_serialized = None

        if score:
            score_serialized = model_to_dict(
                score,
                recurse=False,
                exclude=[PostScore.id, PostScore.post_id, PostScore.created],
            )
            score_serialized.update({'created': str(score.created)})

        return {
            'id': result.id,
            'caption': result.caption,
            'media_url': result.media_s3_key,
            'added': str(result.added),
            'profile': model_to_dict(result.social_profile),
            'location': model_to_dict(result.location) if result.location else None,
            'score': score_serialized,
        }
