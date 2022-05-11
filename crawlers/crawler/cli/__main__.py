import sys

from crawler.functions import (
    list_top_threads,
    parse_execution_arguments,
    prettify_results,
)


def main(execution_arguments: list) -> None:
    parsed_arguments = parse_execution_arguments(execution_arguments)

    top_threads = list_top_threads(parsed_arguments)

    print("")
    print(prettify_results(top_threads, parsed_arguments))


if __name__ == "__main__":
    main(sys.argv[1:])
