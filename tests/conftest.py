import pytest
import pandas as pd

@pytest.fixture
def persons():
    data = [["Peter", 10, 10.5], ["Hans", 12, 13.7]]
    return pd.DataFrame(data, columns=["Name", "Age", "JustANumber"])
