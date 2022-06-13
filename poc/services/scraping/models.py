from dataclasses import dataclass
from enum import Enum, unique
from typing import Set

from instaloader import Post as InstaPost
from pydantic import BaseModel


@unique
class Social(str, Enum):
    TIKTOK = 'tiktok'
    INSTAGRAM = 'instagram'


@unique
class MediaType(str, Enum):
    IMAGE = 'image'
    VIDEO = 'video'


@dataclass
class Post:
    id: str
    caption: str
    media_url: str
    social: Social = Social.INSTAGRAM
    media_type: MediaType = MediaType.IMAGE

    @property
    def hashtags(self) -> Set[str]:
        tags = [tag.strip('#') for tag in self.caption.split() if tag.startswith('#')]
        return set(tags)

    @classmethod
    def from_instaloader_post(cls, post: InstaPost):
        return cls(
            id=post.shortcode,
            caption=post.caption,
            media_url=post.video_url if post.is_video else post.url,
            social=Social.INSTAGRAM,
            media_type=MediaType.VIDEO if post.is_video else MediaType.IMAGE
        )


class LambdaEvent(BaseModel):
    social: Social
    username: str
