from abc import ABC, abstractmethod

from common.models import Request


class DataProvider(ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int) -> dict:
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass

    def handle_request(self, request: Request):
        parts = request.path.removeprefix('/').split('/')
        if len(parts) > 1:
            entity_id = int(parts[1])
            return self.get_by_id(entity_id)
        return self.get_all()
