from dataclasses import dataclass
from enum import Enum, auto
from typing import Set


class Social(Enum):
    TIKTOK = 0
    INSTAGRAM = 1


@dataclass
class Post:
    id: str
    social: Social
    caption: str

    @property
    def hashtags(self) -> Set[str]:
        tags = [tag.strip('#') for tag in self.caption.split() if tag.startswith('#')]
        return set(tags)
