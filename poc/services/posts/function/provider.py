from common.providers import DataProvider
from db.models import Post


class PostProvider(DataProvider):
    def get_by_id(self, entity_id: int) -> dict:
        return {
            'id': entity_id
        }

    def get_all(self) -> list:
        return ['aaa']