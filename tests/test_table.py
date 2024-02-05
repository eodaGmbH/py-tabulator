from pandas import DataFrame
from pytabulator import Tabulator
from pytabulator._table_options_dc import TableOptions

# from pytabulator import TableOptions, Tabulator

# DEPRECATED: Moved to separate test file
"""
def test_table_options():
    # Prepare
    group_by = ["Sex", "Age"]

    # Act
    table_options = TableOptions(group_by=group_by)
    table_options_dict = table_options.to_dict()
    print(table_options_dict)

    # Assert
    assert table_options_dict["groupBy"] == ["Sex", "Age"]
"""


def test_table():
    # Prepare
    data = [["Hans", "22"], ["Peter", [23]]]
    df = DataFrame(data, columns=["Name", "Age"])
    table_options = TableOptions(selectable=3)

    # Act
    table = Tabulator(df, table_options=table_options)
    table_dict = table.to_dict()
    print(table_dict)
    print(table_dict["options"])

    # Assert
    assert list(table_dict.keys()) == ["schema", "data", "options"]
    assert isinstance(table_dict["options"], dict)
    # assert not table_dict["options"]
