import pytest


@pytest.fixture(name="test_example")
def fixture_test_example() -> str:
    return """\
In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.
"""


@pytest.fixture(name="formatted_example")
def fixture_formatted_example() -> str:
    with open("output_parte1.txt", "r") as file:
        return file.read()


@pytest.fixture(name="justified_example")
def fixture_justified_example() -> str:
    with open("output-parte2.txt", "r") as file:
        return file.read()
