from argparse import ArgumentParser

from pyformatter.settings import (
    INPUT_JUSTIFY_DEFAULT,
    INPUT_LIMIT_DEFAULT,
    PROGRAM_DESCRIPTION,
    PROGRAM_NAME,
)


def parse_execution_arguments() -> dict:

    """
    Parses execution arguments passed via command line.
    """

    parser = ArgumentParser(prog=PROGRAM_NAME, description=PROGRAM_DESCRIPTION)

    parser.add_argument(
        "text",
        metavar="text",
        type=str,
        help="Text to be formatted. Must be passed between quotation marks.",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=INPUT_LIMIT_DEFAULT,
        help=f"Limit of characters per line. Defaults to {INPUT_LIMIT_DEFAULT}",
    )

    if INPUT_JUSTIFY_DEFAULT:
        parser.add_argument(
            "--no-justify",
            dest="justify",
            action="store_false",
            help="Indicates if formatter must let the lines unjustified.",
        )

    else:
        parser.add_argument(
            "--justify",
            dest="justify",
            action="store_true",
            help="Indicates if formatter must justify the lines.",
        )

    parser.add_argument(
        "--file",
        type=str,
        help="File where the formatted text will be stored.",
    )

    return vars(parser.parse_args())
