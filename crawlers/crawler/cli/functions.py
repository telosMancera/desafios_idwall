from argparse import ArgumentParser

from crawler.crawlers.reddit import RedditCrawler
from crawler.enums import PeriodEnum
from crawler.settings import (
    INPUT_PERIOD_DEFAULT,
    INPUT_QUANTITY_DEFAULT,
    INPUT_UPVOTES_DEFAULT,
)
from crawler.utils import print_pretty_object

PROGRAM_NAME = "Crawler"
PROGRAM_DESCRIPTION = """\
List the most highlighted threads in Reddit.\
"""


def parse_execution_arguments(execution_arguments: list) -> dict:

    """
    Parses execution arguments passed via command line.
    """

    parser = ArgumentParser(prog=PROGRAM_NAME, description=PROGRAM_DESCRIPTION)

    parser.add_argument(
        "subreddits",
        metavar="subreddits",
        type=str,
        help="List with subbredits, in the format `subreddit1;subreddit2;...",
    )

    parser.add_argument(
        "--quantity",
        type=int,
        default=INPUT_QUANTITY_DEFAULT,
        help=f"Number of results to show. Defaults to {INPUT_QUANTITY_DEFAULT}",
    )

    parser.add_argument(
        "--period",
        type=str,
        default=INPUT_PERIOD_DEFAULT,
        help=f"Search period, must be one of {PeriodEnum.values()}  Defaults to {INPUT_QUANTITY_DEFAULT}",
    )

    parser.add_argument(
        "--upvotes",
        type=int,
        default=INPUT_UPVOTES_DEFAULT,
        help=f"Minimum of upvotes to a thread be considered highlighted. Defaults to {INPUT_UPVOTES_DEFAULT}",
    )

    script_params = vars(parser.parse_args(execution_arguments))
    _validate_script_params(script_params)
    _format_script_params(script_params)

    print_pretty_object(script_params, header="Params :")
    print("")

    return script_params


def list_top_threads(script_params: dict) -> list[dict]:

    """
    Lists the top threads.
    """

    print("Listing the top threads...")

    # List top threads for each subreddit
    top_threads = []
    for subreddit in script_params["subreddits"]:
        crawler = RedditCrawler(subreddit)
        _top_threads = crawler.list_top_threads(
            script_params["quantity"],
            period=script_params["period"],
            upvotes=script_params["upvotes"],
        )

        top_threads.extend(_top_threads)

    # List top threads between all of them
    top_threads = sorted(
        top_threads, key=lambda thread: thread["upvotes"], reverse=True
    )[: script_params["quantity"]]

    print("Listed!")

    return top_threads


def show_results(top_threads: list, script_params: dict) -> None:

    """
    Shows the top threads.
    """

    quantity = script_params["quantity"]
    print(f"\nThe {quantity} top threads are :\n")
    for thread in top_threads:
        print_pretty_object(thread)
        print("")


def _validate_script_params(script_params: dict) -> None:
    # period
    assert (
        script_params["period"] in PeriodEnum.values()
    ), f"Period must be one of {PeriodEnum.values()}"


def _format_script_params(script_params: dict) -> None:
    # subreddits
    script_params["subreddits"] = tuple(script_params["subreddits"].split(";"))
