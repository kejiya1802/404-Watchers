import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    )
}


def fetch_page(url):
    """
    Fetch a webpage and return its HTML.
    """

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        return {
            "success": True,
            "status_code": response.status_code,
            "url": url,
            "html": response.text
        }

    except requests.exceptions.Timeout:

        return {
            "success": False,
            "error": "Request timed out",
            "url": url
        }

    except requests.exceptions.RequestException as error:

        return {
            "success": False,
            "error": str(error),
            "url": url
        }