import pytest
from pandas import DataFrame
from pytabulator import Tabulator
from pytabulator.tabulator_options import TabulatorOptions

@pytest.fixture
def df() -> DataFrame:
    data = [["Hans", "22"], ["Peter", [23]]]
    return DataFrame(data, columns=["Name", "Age"])


def test_table_pydantic(df: DataFrame) -> None:
    # Prepare
    table_options = TabulatorOptions(selectable_rows=3)

    # Act
    table = Tabulator(df, options=table_options)
    table_dict = table.to_dict()
    print(table_dict)

    # Assert
    assert list(table_dict.keys()) == ["schema", "data", "options", "bindingOptions"]
    assert isinstance(table_dict["options"], dict)
