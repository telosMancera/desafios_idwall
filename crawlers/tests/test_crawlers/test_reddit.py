from crawler.crawlers.reddit import RedditCrawler


class TestRedditCrawler:
    def test_success(self) -> None:
        crawler = RedditCrawler("cats")

        top = crawler.list_top_threads(40, upvotes=200)

        assert all(thread["upvotes"] >= 200 for thread in top)
