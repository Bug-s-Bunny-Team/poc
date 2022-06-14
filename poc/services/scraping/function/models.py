from dataclasses import dataclass
from enum import Enum, unique
from functools import cached_property
from typing import Set, Optional

from instaloader import Post as InstaPost
from pydantic import BaseModel, validator, root_validator


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

    @cached_property
    def hashtags(self) -> Set[str]:
        tags = [tag.strip('#') for tag in self.caption.split() if tag.startswith('#')]
        return set(tags)

    @cached_property
    def media_filename(self) -> str:
        extension = 'mp4' if self.media_type == MediaType.VIDEO else 'png'
        return f'{self.id}.{extension}'

    @classmethod
    def from_instaloader_post(cls, post: InstaPost):
        return cls(
            id=post.shortcode,
            caption=post.caption,
            media_url=post.video_url if post.is_video else post.url,
            social=Social.INSTAGRAM,
            media_type=MediaType.VIDEO if post.is_video else MediaType.IMAGE
        )


########################################################################################################################


class LambdaEvent(BaseModel):
    social: Social
    username: Optional[str] = None
    url: Optional[str] = None

    @validator('url', always=True)
    def mutually_exclusive(cls, v, values):
        if values['username'] is not None and v:
            raise ValueError('"username" and "url" are mutually exclusive')
        return v

    @root_validator()
    def check_required(cls, values):
        if (values.get('username') is None) and (values.get('url') is None):
            raise ValueError('either "username" or "url" is required')
        return values
