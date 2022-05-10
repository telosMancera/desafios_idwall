from bs4 import BeautifulSoup
from crawler.crawlers.base import BaseCrawler
from crawler.enums import PeriodEnum
from crawler.settings import INPUT_PERIOD_DEFAULT, INPUT_UPVOTES_DEFAULT

_REDDIT_BASE_URL = "https://old.reddit.com"


def _get_threads(soup: BeautifulSoup) -> list[dict]:
    threads = []

    threads_table = soup.find_all(id="siteTable")[0]
    for thread_tag in threads_table.find_all(class_="thing"):
        title_tag = thread_tag.find_all("a", class_="title")[0]
        attrs = thread_tag.attrs

        threads.append(
            {
                "title": title_tag.text,
                "subreddit": f'/{attrs["data-subreddit-prefixed"]}',
                "upvotes": int(attrs["data-score"]),
                "link": attrs["data-url"],
                "link_comments": attrs["data-permalink"],
                "after": attrs["data-fullname"],  # used for pagination
            }
        )

    return threads


class RedditCrawler(BaseCrawler):
    def __init__(self, subreddit: str) -> None:
        self._subreddit = subreddit

        super().__init__(f"{_REDDIT_BASE_URL}/r/{subreddit}/")

    def list_top_threads(
        self,
        quantity,
        *,
        period: PeriodEnum = INPUT_PERIOD_DEFAULT,
        upvotes: int = INPUT_UPVOTES_DEFAULT,
    ) -> list[dict]:

        """
        Lists the top threads.
        """

        print(f"Listing top threads for {self._subreddit}...")

        top_threads = []
        after = None
        while (left_to_complete := quantity - len(top_threads)) > 0:
            # Get threads
            if after:
                soup = self._get_soup_from_endpoint(
                    "/top/", sort="top", t=period, after=after
                )

            else:
                soup = self._get_soup_from_endpoint("/top/", sort="top", t=period)

            threads = _get_threads(soup)

            # Get next page
            for thread in threads:
                after = thread.pop("after")  # it will store the after from last thread

            # Filter threads
            threads = [thread for thread in threads if thread["upvotes"] >= upvotes]
            if not threads:
                # No more threads with the minimum upvotes
                break

            # Store result
            if left_to_complete < len(threads):
                top_threads.extend(threads[:left_to_complete])

            else:
                top_threads.extend(threads)

        print(f"Found {len(top_threads)} with more than or equal to {upvotes} upvotes!")

        return top_threads
