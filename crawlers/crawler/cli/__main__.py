import sys

from crawler.cli.functions import (
    list_top_threads,
    parse_execution_arguments,
    show_results,
)


def main(execution_arguments: list) -> None:
    script_params = parse_execution_arguments(execution_arguments)

    top_threads = list_top_threads(script_params)
    show_results(top_threads, script_params)


if __name__ == "__main__":
    main(sys.argv[1:])
