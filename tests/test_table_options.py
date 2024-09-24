import pytest

from pytabulator.tabulator_options import TabulatorOptions


@pytest.fixture
def some_table_options():
    return {
        "history": True,
        "pagination_counter": "rows",
        "index": "PassengerId",
        "pagination_add_row": "table",
    }


def test_table_options(some_table_options):
    # Prepare
    table_options = TabulatorOptions(**some_table_options)

    # Act
    table_options_dict = table_options.to_dict()

    # Assert
    print(table_options_dict)
    assert table_options_dict["movableRows"] == False
