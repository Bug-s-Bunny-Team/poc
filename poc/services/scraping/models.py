from dataclasses import dataclass
from enum import Enum, auto
from typing import Set


class Social(Enum):
    TIKTOK = 0
    INSTAGRAM = 1


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
