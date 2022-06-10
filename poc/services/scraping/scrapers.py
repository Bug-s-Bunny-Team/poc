from abc import ABC, abstractmethod
from typing import List


from .models import Post


class BaseScraper(ABC):
    @abstractmethod
    def get_last_post(username: str) -> Post:
        pass
    
    @abstractmethod
    def get_posts(username: str) -> List[Post]:
        pass


class TikTokScraper(BaseScraper):
    pass


class InstagramScraper(BaseScraper):
    pass
