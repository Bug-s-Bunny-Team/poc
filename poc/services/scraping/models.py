from dataclasses import dataclass
from enum import Enum, unique
from typing import Set


@unique
class Social(Enum):
    TIKTOK = 0
    INSTAGRAM = 1


@unique
class MediaType(Enum):
    IMAGE = 0
    VIDEO = 1


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
