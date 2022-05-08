import pytest
from pyformatter.settings import INPUT_JUSTIFY_DEFAULT, INPUT_LIMIT_DEFAULT


@pytest.fixture(name="text_example")
def fixture_text_example() -> str:
    return """\
In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.
"""


@pytest.fixture(name="output_file_example")
def fixture_output_file_example() -> list:
    return "output_example.txt"


@pytest.fixture(name="execution_arguments_example")
def fixture_execution_arguments_example(
    text_example: str, output_file_example: str
) -> list:
    return [
        text_example,
        "--limit",
        "40",
        "--no-justify" if INPUT_JUSTIFY_DEFAULT else "--justify",
        "--file",
        output_file_example,
    ]


@pytest.fixture(name="script_params_example")
def fixture_script_params_example(text_example: str, output_file_example: str) -> dict:
    return {
        "text": text_example,
        "limit": INPUT_LIMIT_DEFAULT,
        "justify": not INPUT_JUSTIFY_DEFAULT,
        "file": output_file_example,
    }


@pytest.fixture(name="formatted_example")
def fixture_formatted_example() -> str:
    with open("output_parte1.txt", "r") as file:
        return file.read()


@pytest.fixture(name="justified_example")
def fixture_justified_example() -> str:
    with open("output-parte2.txt", "r") as file:
        return file.read()
