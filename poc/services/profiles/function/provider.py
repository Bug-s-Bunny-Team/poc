from playhouse.shortcuts import model_to_dict

from common.providers import DataProvider
from common.utils import create_response, create_error_response
from db.models import SocialProfile


class ProfileProvider(DataProvider):
    def get_by_id(self, entity_id: int) -> dict:
        profile = SocialProfile.get_or_none(id=entity_id)
        if not profile:
            return create_error_response('Profile not found', 404)
        return create_response(model_to_dict(profile), 200)

    def get_all(self) -> dict:
        profiles = SocialProfile.select()
        profiles = [model_to_dict(p) for p in profiles]
        return create_response(profiles, 200)
