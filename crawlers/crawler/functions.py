from argparse import ArgumentParser

from crawler.settings import INPUT_UPVOTES_DEFAULT, PROGRAM_DESCRIPTION, PROGRAM_NAME


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
        "--upvotes",
        type=int,
        default=INPUT_UPVOTES_DEFAULT,
        help=f"Minimum of upvotes to a thread be considered highlighted. Defaults to {INPUT_UPVOTES_DEFAULT}",
    )

    script_params = vars(parser.parse_args(execution_arguments))
    _format_script_params(script_params)

    print(f"Params :")
    biggest_key_length = max(len(key) for key in script_params)
    for key, value in script_params.items():
        print(f"* {key.capitalize():>{biggest_key_length}} : {value}")

    return script_params


def _format_script_params(script_params: dict) -> None:
    # subreddits
    script_params["subreddits"] = tuple(script_params["subreddits"].split(";"))
