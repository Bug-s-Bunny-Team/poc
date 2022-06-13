from abc import ABC, abstractmethod
from typing import List, Optional

from instaloader import Instaloader, Profile

from .models import Post


class BaseScraper(ABC):
    @abstractmethod
    def get_last_post(self, username: str) -> Post:
        pass

    # @abstractmethod
    # def get_posts(self, username: str) -> List[Post]:
    #     pass


class TikTokScraper(BaseScraper):
    pass


class InstagramScraper(BaseScraper):
    def __init__(self, client: Instaloader):
        self._client = client

    def get_profile(self, username: str) -> Profile:
        return Profile.from_username(self._client.context, username)

    def get_last_post(self, username: str) -> Post:
        profile = self.get_profile(username)
        post = next(profile.get_posts())
        return Post.from_instaloader_post(post)
