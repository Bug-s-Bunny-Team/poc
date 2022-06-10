from pathlib import Path

from services.scraping.utils import download_media


def test_downloader(tmp_path: Path):
    dest = tmp_path / 'image.jpeg'

    download_media('https://httpbin.org/image/jpeg', dest)

    assert dest.is_file()
