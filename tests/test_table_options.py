import pytest
from pytabulator import TableOptions


@pytest.fixture
def table_options():
    return {"columns": []}


expected_table_options = [
    ("index", "id"),
    ("headerVisible", True),
    ("movableRows", False),
    ("pagination", False),
    ("paginationCounter", "rows"),
    ("paginationAddRow", "page"),
    ("selectable", "highlight"),
    ("layout", "fitColumns"),
    ("addRowPos", "bottom"),
    ("resizableColumnFit", False),
    ("history", True),
]


def test_table_options():
    # Prepare
    table_options = TableOptions(
        history=True, pagination_counter="rows", header_visible=True
    )

    # Act
    table_options_dict = table_options.to_dict()
    print(table_options_dict.items())

    # Assert
    sorted_list = list(table_options_dict.items()).sort(key=lambda item: item[0])
    print(sorted_list)
    assert sorted_list == expected_table_options.sort(key=lambda item: item[0])
