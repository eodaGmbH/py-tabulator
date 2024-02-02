from pandas import DataFrame
from pytabulator.utils import create_columns


def test_create_columns():
    # Prepare
    data = [["Peter", 10, 10.5], ["Hans", 12, 13.7]]
    df = DataFrame(data, columns=["Name", "Age", "JustANumber"])

    # Act
    columns = create_columns(df, default_filter=True, default_editor=True)
    print(columns)

    # Assert
    assert len(columns) == 3
    assert [column["hozAlign"] for column in columns] == ["left", "right", "right"]
    assert [column["headerFilter"] for column in columns] == [
        "input",
        "number",
        "number",
    ]
