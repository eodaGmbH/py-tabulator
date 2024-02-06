import pytest

# from pytabulator import TableOptions
from pytabulator._table_options_dc import TableOptionsDC
from pytabulator._table_options_dc import TableOptionsDC as TableOptionsDC
from pytabulator._table_options_pydantic import TableOptionsPydantic as TableOptions


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
    table_options_pydantic = TableOptions(**some_table_options)
    print("pydantic", table_options_pydantic)

    table_options_dc = TableOptionsDC(**some_table_options)
    print("dc", table_options_dc)

    # Act
    table_options_pydantic_dict = table_options_pydantic.to_dict()
    table_options_dc_dict = table_options_dc.to_dict()

    # Assert
    assert list(table_options_pydantic_dict.items()).sort(
        key=lambda item: item[0]
    ) == list(table_options_dc_dict.items()).sort(key=lambda item: item[0])
