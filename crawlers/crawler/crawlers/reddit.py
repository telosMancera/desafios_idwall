from bs4 import BeautifulSoup
from crawler.crawlers.base import BaseCrawler
from crawler.enums import ListTopThreadsPeriodEnum
from crawler.settings import INPUT_PERIOD_DEFAULT, INPUT_UPVOTES_DEFAULT

_REDDIT_BASE_URL = "https://old.reddit.com"


class RedditCrawler(BaseCrawler):
    def __init__(self, subreddit: str) -> None:
        self._subreddit_url = f"{_REDDIT_BASE_URL}/r/{subreddit}/"

        super().__init__(self._subreddit_url)

    def list_top_threads(
        self,
        quantity,
        *,
        period: ListTopThreadsPeriodEnum = INPUT_PERIOD_DEFAULT,
        upvotes: int = INPUT_UPVOTES_DEFAULT,
    ) -> list[dict]:

        """
        Lists the top threads.
        """

        soup = self._get_soup_from_endpoint("/top/", sort="top", t=period)

        with open("result.html", "w") as file:
            file.write(str(soup))

        # import ipdb

        # ipdb.set_trace()

    def _get_threads(self, soup: BeautifulSoup) -> list:
        return []
