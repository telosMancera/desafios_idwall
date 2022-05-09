from crawler.crawlers.reddit import RedditCrawler


class TestRedditCrawler:
    def test_success(self) -> None:
        crawler = RedditCrawler("cats")

        crawler.list_top_threads(10)
