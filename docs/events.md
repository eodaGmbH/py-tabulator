# Events and triggers

## Events

Tabulator for Python provides the following reactive inputs:

- `input.{output_id}_row_clicked` event: Sends the data of the clicked row.
- `input.{output_id}_row_edited` event: Sends the data of the edited row. This event is fired each time a cell of the row is edited.
- `input.{output_id}_rows_selected` event: Sends the data of all selected rows. This event is fired each time a new row is selected.
- `input.{output_id}_data` event: Sends the complete data of the table. This event must be triggered from Shiny.
- `input.{output_id}_data_filtered` event: Sends data of filtered rows. This event is triggered each time a filter is applied.

```python
from shiny import render
from pandas import read_csv
from pytabulator import render_data_frame


# in this case (Shiny Express) the function name corresponds to the 'output_id'
# output_id = "tabulator"
#
# on-row-clicked event: input.tabulator_row_clicked
# on-row-edited event: input.tabulator_row_edited
#
@render_data_frame
def tabulator():
    return read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# row-on-click event
#
@render.code
async def txt():
    print(input.tabulator_row_clicked())
    return input.tabulator_row_clicked()["Name"]


# row-edited event
#
@render.code
def row_edited():
    data = input.tabulator_row_edited()
    print(data)
    return f"{data['Name']}, {data['Sex']}"
```

## Triggers

With `TabulatorContext` you can trigger events on the `table` object. `TabulatorContext` must be used in an async function:

```python
from shiny import reactive
from shiny.express import ui
from pytabulator import TabulatorContext

ui.input_action_button("trigger_download", "Download")
ui.input_action_button("add_row", "Add row")


# Trigger download of csv file
#
@reactive.Effect
@reactive.event(input.trigger_download)
async def trigger_download():
    print("download triggered")
    async with TabulatorContext("tabulator") as table:
        table.trigger_download("csv")


# Add a row to the table
#
@reactive.Effect
@reactive.event(input.add_row)
async def add_row():
    async with TabulatorContext("tabulator") as table:
        table.add_row({"Name": "Hans", "Sex": "male"})
```

## Detailed example

```python
-8<-- "getting_started/shiny_express_all.py"
```
