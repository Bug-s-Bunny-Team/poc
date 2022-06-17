import pytest

from db import db
from db.models import SocialProfile, Post, MediaType
from db.utils import init_db, create_all_tables


@pytest.fixture
def transaction():
    init_db('user', 'password', '172.18.0.10', 'poc')
    with db.transaction() as txn:
        create_all_tables()
        yield txn
        txn.rollback()


@pytest.fixture
def profile() -> SocialProfile:
    return SocialProfile(username='testuser123')


@pytest.fixture
def post(profile) -> Post:
    return Post(
        shortcode='Cef7VMLloOP',
        social_profile=profile,
        media_type='image',
        caption='Great stuff #yum #friends'
    )


def test_create_profile(transaction, profile):
    profile.save()


def test_create_post(transaction, profile, post):
    profile.save()
    post.save()


def test_post_hashtags(post):
    hashtags = post.hashtags
    for expected in ['yum', 'friends']:
        assert expected in hashtags


def test_post_media_filename(post):
    assert post.media_filename == 'Cef7VMLloOP.jpg'


def test_media_type():
    assert MediaType('image') == MediaType.IMAGE
    assert MediaType('video') == MediaType.VIDEO
    assert MediaType['IMAGE'] == MediaType.IMAGE
    assert MediaType['VIDEO'] == MediaType.VIDEO
