from common.providers import DataProvider
from db.models import Post


class PostProvider(DataProvider):
    def __init__(self):
        super().__init__(Post)
