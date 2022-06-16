import pytest

from db import db
from db.models import SocialProfile, Post
from db.utils import init_db, create_all_tables


@pytest.fixture
def transaction():
    init_db('user', 'password', '172.18.0.10', 'poc')
    with db.transaction() as txn:
        create_all_tables()
        yield txn
        txn.rollback()


def test_create_profile(transaction):
    profile = SocialProfile.create(username='testuser123')
    assert profile


def test_create_post(transaction):
    profile = SocialProfile.create(username='testuser123')
    post = Post.create(social_profile=profile, media_type='image', media_s3_key='test/sdfjkhn.jpg')
    assert post
