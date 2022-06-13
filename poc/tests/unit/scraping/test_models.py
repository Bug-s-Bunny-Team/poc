from services.scraping.scraping.models import Social, Post, MediaType


def test_social():
    assert Social(0) == Social.TIKTOK
    assert Social(1) == Social.INSTAGRAM
    assert Social['INSTAGRAM'] == Social.INSTAGRAM
    assert Social['TIKTOK'] == Social.TIKTOK


def test_media_type():
    assert MediaType(0) == MediaType.IMAGE
    assert MediaType(1) == MediaType.VIDEO
    assert MediaType['IMAGE'] == MediaType.IMAGE
    assert MediaType['VIDEO'] == MediaType.VIDEO


def test_post():
    post = Post(
        id='sdfjbsdf',
        social=Social.INSTAGRAM,
        caption='a great experience at the restaurant #yum #friends',
        media_url='https://example.com/image.png'
    )
    
    hashtags = post.hashtags
    for expected in ['yum', 'friends']:
        assert expected in hashtags
