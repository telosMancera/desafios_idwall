from pyformatter.formatter import StringFormatter


class TestStringFormatter:
    @staticmethod
    def test_format(test_example: str, formatted_example: str) -> None:
        formatter = StringFormatter()

        with open("test1.txt", "w") as file:
            file.write(formatter.format(test_example))

        assert formatter.format(test_example) == formatted_example

    @staticmethod
    def test_justify(test_example: str, justified_example: str) -> None:
        formatter = StringFormatter()

        with open("test2.txt", "w") as file:
            file.write(formatter.format(test_example, justify=True))

        assert formatter.format(test_example, justify=True) == justified_example
