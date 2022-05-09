from bs4 import BeautifulSoup
from crawler.crawlers.functions import (
    generate_proxies,
    get_random_proxy,
    get_random_user_agent,
)
from crawler.settings import SOUP_FEATURES
from requests import get


class BaseCrawler:

    _already_genereated_proxies: bool = False

    def __init__(self, url: str) -> None:
        if url.endswith("/"):
            self._base_url = url[:-1]

        else:
            self._base_url = url

        if not type(self)._already_genereated_proxies:
            generate_proxies()

            type(self)._already_genereated_proxies = True

    def _get_soup_from_endpoint(
        self, endpoint: str = None, **query_params
    ) -> BeautifulSoup:
        url = self._base_url
        if endpoint:
            if endpoint.startswith("/"):
                url += endpoint

            else:
                url += f"/{endpoint}"

        if query_params:
            url += "?" + "&".join(
                f"{key}={value}" for key, value in query_params.items()
            )

        headers = {
            "User-Agent": get_random_user_agent(),
            "Accept-Language": "en-US, en;q=0.5",
        }
        proxy = get_random_proxy()
        response = get(url, headers=headers, proxies=proxy)

        return BeautifulSoup(response.content, SOUP_FEATURES)
