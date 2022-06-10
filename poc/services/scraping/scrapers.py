from abc import ABC, abstractmethod
from typing import List

from .models import Post


class BaseScraper(ABC):
    @abstractmethod
    def get_last_post(self, username: str) -> Post:
        pass

    @abstractmethod
    def get_posts(self, username: str) -> List[Post]:
        pass


class TikTokScraper(BaseScraper):
    pass


class InstagramScraper(BaseScraper):
    def get_last_post(self, username: str) -> Post:
        return Post(
            id='',
            caption='',
            media_url=''
        )

    def get_posts(self, username: str) -> List[Post]:
        return []
