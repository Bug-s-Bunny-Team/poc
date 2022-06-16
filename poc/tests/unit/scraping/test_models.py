from services.scraping.function.models import Social, Post, MediaType


def test_social():
    assert Social('tiktok') == Social.TIKTOK
    assert Social('instagram') == Social.INSTAGRAM
    assert Social['INSTAGRAM'] == Social.INSTAGRAM
    assert Social['TIKTOK'] == Social.TIKTOK


def test_media_type():
    assert MediaType('image') == MediaType.IMAGE
    assert MediaType('video') == MediaType.VIDEO
    assert MediaType['IMAGE'] == MediaType.IMAGE
    assert MediaType['VIDEO'] == MediaType.VIDEO


def test_post():
    post = Post(
        id='sdfjbsdf',
        social=Social.INSTAGRAM,
        caption='a great experience at the restaurant #yum #friends',
        media_url='https://example.com/image.png',
        owner_username='useless_person'
    )
    
    hashtags = post.hashtags
    for expected in ['yum', 'friends']:
        assert expected in hashtags
