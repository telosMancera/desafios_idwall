import pytest
from pyformatter.functions import parse_execution_arguments
from pyformatter.settings import INPUT_JUSTIFY_DEFAULT, INPUT_LIMIT_DEFAULT


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
        "argument_pos, field, value",
        (
            ((1, 2), "limit", INPUT_LIMIT_DEFAULT),
            ((3,), "justify", INPUT_JUSTIFY_DEFAULT),
            ((4, 5), "file", None),
        ),
    )
    def test_missing_optional_arguments(
        self,
        execution_arguments_example: list,
        argument_pos: tuple,
        field: str,
        value: any,
    ) -> None:
        execution_arguments = [
            value
            for index, value in enumerate(execution_arguments_example)
            if index not in argument_pos
        ]

        script_params = parse_execution_arguments(execution_arguments)

        assert field in script_params
        assert script_params[field] == value
