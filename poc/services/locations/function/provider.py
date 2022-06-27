from playhouse.shortcuts import model_to_dict

from common.providers import DataProvider
from common.utils import create_error_response, create_response
from db.models import Location


class LocationProvider(DataProvider):
    def get_by_id(self, entity_id: int) -> dict:
        location = Location.get_or_none(id=entity_id)
        if not location:
            return create_error_response('Location not found', 404)
        return create_response(model_to_dict(location), 200)

    def get_all(self) -> dict:
        locations = Location.select()
        locations = [model_to_dict(l) for l in locations]
        return create_response(locations, 200)
