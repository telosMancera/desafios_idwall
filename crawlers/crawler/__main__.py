import sys

from crawler.functions import parse_execution_arguments


def main(execution_arguments: list) -> None:
    script_params = parse_execution_arguments(execution_arguments)


if __name__ == "__main__":
    main(sys.argv[1:])
