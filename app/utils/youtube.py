from urllib.parse import (
    urlparse,
    parse_qs
)


def extract_video_id(
    url: str
) -> str:

    parsed_url = urlparse(url)

    return parse_qs(
        parsed_url.query
    )["v"][0]