import pytest

from crawler.functions import parse_execution_arguments
from crawler.settings import (
    INPUT_PERIOD_DEFAULT,
    INPUT_QUANTITY_DEFAULT,
    INPUT_UPVOTES_DEFAULT,
)


class TestParseExecutionArguments:
    def test_success(
        self, execution_arguments_example: list, script_params_example: dict
    ) -> None:
        assert (
            parse_execution_arguments(execution_arguments_example)
            == script_params_example
        )

    @pytest.mark.parametrize("argument_pos", (0,))
    def test_missing_positional_arguments(
        self, execution_arguments_example: list, argument_pos: int
    ) -> None:
        execution_arguments_example = [
            value
            for index, value in enumerate(execution_arguments_example)
            if index != argument_pos
        ]

        with pytest.raises(SystemExit):
            parse_execution_arguments(execution_arguments_example)

    @pytest.mark.parametrize(
        "argument_pos, field, expected_value",
        (
            ((1, 2), "quantity", INPUT_QUANTITY_DEFAULT),
            ((3, 4), "period", INPUT_PERIOD_DEFAULT),
            ((5, 6), "upvotes", INPUT_UPVOTES_DEFAULT),
        ),
    )
    def test_missing_optional_arguments(
        self,
        execution_arguments_example: list,
        argument_pos: tuple,
        field: str,
        expected_value: any,
    ) -> None:
        execution_arguments = [
            value
            for index, value in enumerate(execution_arguments_example)
            if index not in argument_pos
        ]

        script_params = parse_execution_arguments(execution_arguments)

        assert field in script_params
        assert script_params[field] == expected_value
