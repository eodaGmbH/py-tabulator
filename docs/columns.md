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

## Customize default configuration

With `create_columns` you can customize the default configuration:

```python
from pandas import DataFrame
from pytabulator import TableOptions
from pytabulator.utils import create_columns

data = [["Peter", 10, 102.5], ["Hans", 12, 200.9]]
df = DataFrame(data, columns=["Name", "Age", "JustANumber"])

table_options = TableOptions(
    columns=create_columns(
        df,
        default_filter=True,
        default_editor=True,
        updates={"JustANumber": {"formatter": "progress", "horizAlign": "left"}})
)
```

In the example above with `default_editor=True` all columns are set to editable and with `default_filter=True` a header filter is added to all columns.
For numeric columns the editor and filter mode is set to `number`.

The `updates` arguments allows you to overwrite any defaults set for a column. In this case the `formatter` of the numeric column `JustANumber` is set to `progress`
and the alignment is changed from `right` to `left`.

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

[Shiny Express](https://shiny.posit.co/blog/posts/shiny-express/) example:

```python
-8<-- "getting_started/shiny_express_filters.py"
```

## Editor

Set `editor` to `True`, `"input"` or `"number"` to make the cells of a column editable:

```python
columns = [
    {"title": "Name", "field": "Name", "horizAlign": "left", "editor": True},
    {"title": "Age", "field": "Age", "horizAlign": "right", "editor": "number"}
]
```
