from abc import ABC
from typing import Type

from playhouse.shortcuts import model_to_dict

from common.models import Request
from common.utils import create_error_response, create_response
from db.models import BaseModel


class DataProvider(ABC):
    def __init__(self, model: Type[BaseModel]):
        self.model = model

    def get_by_id(self, entity_id: int) -> dict:
        result = self.model.get_or_none(id=entity_id)
        if not result:
            return create_error_response(f'{self.model.__name__} not found', 404)
        return create_response(model_to_dict(result), 200)

    def get_all(self) -> dict:
        results = self.model.select()
        results = [model_to_dict(r) for r in results]
        return create_response(results, 200)

    def handle_request(self, request: Request):
        parts = request.path.removeprefix('/').split('/')
        if len(parts) > 1:
            entity_id = int(parts[1])
            return self.get_by_id(entity_id)
        return self.get_all()
