from pandas import DataFrame
from pytabulator import TableOptions, Tabulator, TabulatorOptions


def test_table_options():
    # Prepare
    group_by = ["Sex", "Age"]

    # Act
    table_options = TableOptions(group_by=group_by)
    table_options_dict = table_options.to_dict()
    print(table_options_dict)

    # Assert
    assert table_options_dict["groupBy"] == ["Sex", "Age"]


def test_table():
    # Prepare
    data = [["Hans", "22"], ["Peter", [23]]]
    df = DataFrame(data, columns=["Name", "Age"])

    # Act
    table = Tabulator(df, table_options=TableOptions(selectable=3))
    table_dict = table.to_dict()
    print(table_dict)

    # Assert
    assert list(table_dict.keys()) == ["schema", "data", "options"]
    # assert not table_dict["options"]
