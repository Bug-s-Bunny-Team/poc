from instaloader import Instaloader
from pytest import fixture

from services.scraping.function.scrapers import InstagramScraper


@fixture
def insta_scraper() -> InstagramScraper:
    client = Instaloader()
    return InstagramScraper(client)


def test_extract_shortcode(insta_scraper):
    assert insta_scraper._extract_shortcode(
        'https://www.instagram.com/reel/CeqeNqdj9hC/?igshid=Ym34HBuPY=') == 'CeqeNqdj9hC'

    assert insta_scraper._extract_shortcode(
        'https://www.instagram.com/p/Cek7VMLjsOa/?igshid=Ym34HBuPY=') == 'Cek7VMLjsOa'

    assert insta_scraper._extract_shortcode(
        'https://www.instagram.com/reel/') is None
