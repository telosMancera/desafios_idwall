import pytest


@pytest.fixture(name="execution_arguments_example")
def fixture_execution_arguments_example() -> list:
    return [
        "cats;brazil",
        "--quantity",
        50,
        "--period",
        "month",
        "--upvotes",
        10000,
    ]


@pytest.fixture(name="script_params_example")
def fixture_script_params_example() -> dict:
    return {
        "subreddits": ("cats", "brazil"),
        "quantity": 50,
        "period": "month",
        "upvotes": 10000,
    }
