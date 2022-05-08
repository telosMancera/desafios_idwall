from argparse import ArgumentParser
from os import makedirs
from os.path import dirname, exists

from pyformatter.formatter import StringFormatter
from pyformatter.settings import (
    INPUT_JUSTIFY_DEFAULT,
    INPUT_LIMIT_DEFAULT,
    PROGRAM_DESCRIPTION,
    PROGRAM_NAME,
)


def parse_execution_arguments(execution_arguments: list) -> dict:

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

    script_params = vars(parser.parse_args(execution_arguments))
    print(f"Execution arguments : {script_params}")

    return script_params


def format_text(script_params: dict) -> str:

    """
    Formats the text.
    """

    print("Formatting the text...")

    formatter = StringFormatter(script_params["limit"])
    formatted = formatter.format(
        script_params["text"], justify=script_params["justify"]
    )

    print("Result :\n")
    print(formatted)

    return formatted


def store_formatted_text(formatted_text: str, script_params: dict) -> None:

    """
    Stores the formatted text into passed output file.
    """

    print("Storing into file...")

    folder = dirname(script_params["file"])
    if folder and not exists(folder):
        makedirs(folder)

    with open(script_params["file"], "w") as file:
        file.write(formatted_text)
