from pyformatter.formatter import StringFormatter
from pyformatter.functions import parse_execution_arguments


def main() -> None:
    execution_arguments = parse_execution_arguments()
    print(execution_arguments)
    print("")

    formatter = StringFormatter(execution_arguments["limit"])
    formatted = formatter.format(
        execution_arguments["text"], justify=execution_arguments["justify"]
    )
    print(formatted)

    if execution_arguments["file"]:
        with open(execution_arguments["file"], "w") as file:
            file.write(formatted)


if __name__ == "__main__":
    main()
