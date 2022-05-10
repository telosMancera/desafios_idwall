from argparse import ArgumentParser

from crawler.enums import PeriodEnum
from crawler.settings import (
    INPUT_PERIOD_DEFAULT,
    INPUT_QUANTITY_DEFAULT,
    INPUT_UPVOTES_DEFAULT,
)

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

    print(f"Params :")
    biggest_key_length = max(len(key) for key in script_params)
    for key, value in script_params.items():
        print(f"* {key.capitalize():>{biggest_key_length}} : {value}")

    return script_params


def _validate_script_params(script_params: dict) -> None:
    # period
    assert (
        script_params["period"] in PeriodEnum.values()
    ), f"Period must be one of {PeriodEnum.values()}"


def _format_script_params(script_params: dict) -> None:
    # subreddits
    script_params["subreddits"] = tuple(script_params["subreddits"].split(";"))
