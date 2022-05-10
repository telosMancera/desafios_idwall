import sys

from pyformatter.functions import (
    format_text,
    parse_execution_arguments,
    store_formatted_text,
)


def main(execution_arguments: list) -> None:
    script_params = parse_execution_arguments(execution_arguments)

    formatted_text = format_text(script_params)

    if script_params["file"]:
        store_formatted_text(formatted_text, script_params)


if __name__ == "__main__":
    main(sys.argv[1:])
