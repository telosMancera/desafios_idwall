from crawler.crawlers.reddit import RedditCrawler
from crawler.enums import PeriodEnum
from crawler.exceptions import InvalidArgumentError
from crawler.logs import get_logger
from crawler.parsers import ArgumentParser
from crawler.settings import (
    INPUT_PERIOD_DEFAULT,
    INPUT_QUANTITY_DEFAULT,
    INPUT_UPVOTES_DEFAULT,
)
from crawler.utils import prettify_object

PROGRAM_NAME = "Crawler"
PROGRAM_DESCRIPTION = """\
List the most highlighted threads in Reddit.\
"""


logger = get_logger(__name__)


def parse_execution_arguments(
    execution_arguments: list, *, prog: str = None, exit_on_error: bool = True
) -> dict:

    """
    Parses execution arguments.
    """

    parsed = _parse_arguments(execution_arguments, prog, exit_on_error)

    _validate_parsed_arguments(parsed)
    _format_parsed_arguments(parsed)

    for line in prettify_object(parsed, header="Execution arguments :").split("\n"):
        logger.info(line)

    return parsed


def list_top_threads(parsed_arguments: dict) -> list[dict]:

    """
    Lists the top threads.
    """

    logger.info("Listing the top threads...")

    # List top threads for each subreddit
    top_threads = []
    for subreddit in parsed_arguments["subreddits"]:
        crawler = RedditCrawler(subreddit)
        _top_threads = crawler.list_top_threads(
            parsed_arguments["quantity"],
            period=parsed_arguments["period"],
            upvotes=parsed_arguments["upvotes"],
        )

        top_threads.extend(_top_threads)

    # List top threads between all of them
    top_threads = sorted(
        top_threads, key=lambda thread: thread["upvotes"], reverse=True
    )[: parsed_arguments["quantity"]]

    logger.info("Listed!")

    return top_threads


def prettify_results(top_threads: list, parsed_arguments: dict) -> str:

    """
    Shows the top threads.
    """

    quantity = parsed_arguments["quantity"]
    prettier = f"The {quantity} top threads are :\n\n"
    for thread in top_threads:
        prettier += f"{prettify_object(thread)}\n"

    return prettier


def _parse_arguments(
    execution_arguments: list, prog: str, exit_on_error: bool
) -> dict[str, any]:
    prog = prog or PROGRAM_NAME
    parser = ArgumentParser(
        prog=prog,
        description=PROGRAM_DESCRIPTION,
        add_help=(prog is None),
        exit_on_error=exit_on_error,
    )

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

    return vars(parser.parse_args(execution_arguments))


def _validate_parsed_arguments(parsed_arguments: dict) -> None:
    # period
    if parsed_arguments["period"] not in PeriodEnum.values():
        raise InvalidArgumentError(f"Period must be one of {PeriodEnum.values()}")


def _format_parsed_arguments(parsed_arguments: dict) -> None:
    # subreddits
    parsed_arguments["subreddits"] = tuple(parsed_arguments["subreddits"].split(";"))
