import pytest

from pyformatter.formatter import StringFormatter


class TestStringFormatter:
    @staticmethod
    def test_format(text_example: str, formatted_text_example: str) -> None:
        formatter = StringFormatter()

        assert formatter.format(text_example, justify=False) == formatted_text_example

    @staticmethod
    def test_justify(text_example: str, justified_text_example: str) -> None:
        formatter = StringFormatter()

        assert formatter.format(text_example, justify=True) == justified_text_example

    @pytest.mark.parametrize("limit", (30, 40, 50))
    def test_limit(self, text_example: str, limit: int) -> None:
        formatter = StringFormatter(limit)

        assert all(
            len(line) <= limit for line in formatter.format(text_example).split("\n")
        )
