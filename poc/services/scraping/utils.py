from pathlib import Path

import requests


# TODO: add option to download file in memory and don't create a new file
def download_media(url: str, dest: Path):
    with requests.get(url, stream=True) as r:
        with open(dest, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
