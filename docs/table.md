# Table

The table configuration is set with `TableOptions`:

```python
from pytabulator import TableOptions

table_options = TableOptions(
    layout="fitData",
    height="600px",
    pagination=True,
    selectable=True
)
```

The table options can either be passed to the render function or to the `Table` object:

```python
from pandas import read_csv
from pytabulator import render_data_frame, TableOptions

df = read_csv("titanic.csv")

table_options = TableOptions(
    height="600px",
    pagination=True
)

@render_data_frame(table_options=table_options)
def tabulator():
    return df
```
