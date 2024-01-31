# Columns and filters

With the `columns` argument of `TableOptions` you can configure the columns of the table.

See [Tabulator JS columns docs](https://tabulator.info/docs/5.5/columns) for a complete list of available setup options.

## Default definition

If no `columns` arguments is provided, `title` and `field` is set to the column name of the data frame.
Furthermore, the alignment is set to `right` for numeric columns.

```python
from pandas import DataFrame
from pytabulator import render_data_frame

data = [["Peter", 10], ["Hans", 12]]

df = DataFrame(data, columns=["Name", "Age"])

@render_data_frame
def tabulator():
    return df
```

The following definition is created by default for the above data frame:

```python
columns = [
    {"title": "Name", "field": "Name", "horizAlign": "left"},
    {"title": "Age", "field": "Age", "horizAlign": "right"}
]
```

## Calculations

Calculations can be set with the `bottomCalc` parameter:

```python
from pytabulator import TableOptions

columns = [
    {"title": "Name", "field": "Name", "horizAlign": "left"},
    {"title": "Age", "field": "Age", "horizAlign": "right", "bottomCalc": "avg"}
]

table_options = TableOptions(columns=columns)
```

## Filters

You can add a filter to the columns with the `headerFilter` parameter:

```python
from pytabulator import TableOptions

columns = [
    {
        "title": "Name",
        "field": "Name",
        "horizAlign": "left",
        "headerFilter": True
    },
    {
        "title": "Age",
        "field": "Age",
        "horizAlign": "right",
        "bottomCalc": "avg",
        "headerFilter": "number"
    }
]

table_options = TableOptions(columns=columns)
```

## Editor

Set `editor` to `True` to make the cells of a column editable:

```python
columns = [
    {"title": "Name", "field": "Name", "horizAlign": "left", "editor": True},
    {"title": "Age", "field": "Age", "horizAlign": "right", "editor": True}
]
```
