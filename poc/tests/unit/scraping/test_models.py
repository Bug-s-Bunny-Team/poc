from services.scraping.models import Social, Post


def test_social():
    assert Social(0) == Social.TIKTOK
    assert Social(1) == Social.INSTAGRAM
    assert Social['INSTAGRAM'] == Social.INSTAGRAM
    assert Social['TIKTOK'] == Social.TIKTOK


def test_post():
    post = Post('sdfjbsdf', Social.TIKTOK, 'a great experience at the restaurant #yum #friends')
    
    hashtags = post.hashtags
    for expected in ['yum', 'friends']:
        assert expected in hashtags
