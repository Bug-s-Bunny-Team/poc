from pony.orm import commit, db_session, select

from db import init_db
from db.models import SocialProfile


def test_add_social_profile():
    init_db('user', 'password', '172.18.0.10', 'poc')

    with db_session:
        social_profile = SocialProfile(username='test')
        commit()

        p = select(p for p in SocialProfile if p.id == social_profile.id)
        assert p

        p.delete()
        commit()
