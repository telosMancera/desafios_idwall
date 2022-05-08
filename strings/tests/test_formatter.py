from pyformatter.formatter import StringFormatter


class TestStringFormatter:
    @staticmethod
    def test_format(text_example: str, formatted_example: str) -> None:
        formatter = StringFormatter()

        with open("test1.txt", "w") as file:
            file.write(formatter.format(text_example))

        assert formatter.format(text_example) == formatted_example

    @staticmethod
    def test_justify(text_example: str, justified_example: str) -> None:
        formatter = StringFormatter()

        with open("test2.txt", "w") as file:
            file.write(formatter.format(text_example, justify=True))

        assert formatter.format(text_example, justify=True) == justified_example
