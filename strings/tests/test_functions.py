from os import remove, rmdir
from os.path import basename, exists, join

import pytest
from pyformatter.functions import (
    format_text,
    parse_execution_arguments,
    store_formatted_text,
)
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
        "argument_pos, field, expected_value",
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


class TestFormatText:
    def test_format(
        self, script_params_example: dict, formatted_text_example: str
    ) -> None:
        script_params_example["justify"] = False

        assert format_text(script_params_example) == formatted_text_example

    def test_justify(
        self, script_params_example: dict, justified_text_example: str
    ) -> None:
        script_params_example["justify"] = True

        assert format_text(script_params_example) == justified_text_example


class TestStoreFormattedText:
    def test_in_same_folder(
        self,
        formatted_text_example: str,
        script_params_example: dict,
        output_file_example: str,
    ) -> None:
        script_params_example["file"] = basename(output_file_example)

        store_formatted_text(formatted_text_example, script_params_example)

        assert exists(script_params_example["file"])
        with open(script_params_example["file"], "r") as file:
            assert file.read() == formatted_text_example

        remove(script_params_example["file"])

    def test_in_different_folder(
        self,
        formatted_text_example: str,
        script_params_example: dict,
        output_file_example: str,
    ) -> None:
        script_params_example["file"] = join("folder", basename(output_file_example))

        store_formatted_text(formatted_text_example, script_params_example)

        assert exists(script_params_example["file"])
        with open(script_params_example["file"], "r") as file:
            assert file.read() == formatted_text_example

        remove(script_params_example["file"])
        rmdir("folder")
