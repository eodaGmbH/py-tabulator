from random import randrange

import pandas as pd
from pytabulator import TableOptions, Tabulator, TabulatorContext, render_tabulator
from pytabulator.utils import create_columns
from shiny import reactive, render
from shiny.express import input, ui

# Fetch data
#
df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

# Setup
#
table_options = TableOptions(
    columns=create_columns(
        df,
        default_filter=True,
        default_editor=True,
        updates={
            "Pclass": {
                "formatter": "star",
                "formatterParams": {"stars": 3},
                "hozAlign": "center",
            },
            "Survived": {"formatter": "tickCross"},
            "Fare": {"formatter": "progress", "hozAlign": "left"},
        },
    ),
    height=400,
    pagination=True,
    pagination_add_row="table",
    layout="fitColumns",
    index="PassengerId",
    add_row_pos="top",
    selectable=True,
    history=True,
)

# Shiny Express App
#
ui.div(
    ui.input_action_button("trigger_download", "Download"),
    ui.input_action_button("add_row", "Add row"),
    ui.input_action_button("delete_selected_rows", "Delete selected rows"),
    ui.input_action_button("undo", "Undo"),
    ui.input_action_button("redo", "Redo"),
    ui.input_action_button("trigger_get_data", "Submit data"),
    style="padding-top: 20px;",
)
ui.div(
    ui.input_text("name", "Click on 'Add row' to add the Person to the table."),
    style="padding-top: 20px;",
)
ui.div("Click on rows to print name.", style="padding: 10px;"),


@render.code
async def txt():
    print(input.tabulator_row_clicked())
    return input.tabulator_row_clicked()["Name"]


ui.div("Select multiple rows to print names of selected rows.", style="padding: 10px;"),


@render.code
def selected_rows():
    data = input.tabulator_rows_selected()
    output = [item["Name"] for item in data]
    return "\n".join(output)


@render_tabulator
def tabulator():
    return Tabulator(df, table_options)


@reactive.Effect
@reactive.event(input.trigger_download)
async def trigger_download():
    print("download triggered")
    async with TabulatorContext("tabulator") as table:
        table.trigger_download("csv")


@reactive.Effect
@reactive.event(input.add_row)
async def add_row():
    async with TabulatorContext("tabulator") as table:
        table.add_row(
            {
                "Name": input.name() or "Hans",
                "Age": randrange(55),
                "Survived": randrange(2),
                "PassengerId": randrange(10000, 20000, 1),
                "SibSp": randrange(9),
            }
        )


@reactive.Effect
@reactive.event(input.delete_selected_rows)
async def delete_selected_rows():
    async with TabulatorContext("tabulator") as table:
        table.delete_selected_rows()


@reactive.Effect
@reactive.event(input.undo)
async def undo():
    async with TabulatorContext("tabulator") as table:
        table.undo()


@reactive.Effect
@reactive.event(input.redo)
async def redo():
    async with TabulatorContext("tabulator") as table:
        table.redo()


@reactive.Effect
@reactive.event(input.trigger_get_data)
async def trigger_get_data():
    async with TabulatorContext("tabulator") as table:
        table.trigger_get_data()


@reactive.Effect
@reactive.event(input.tabulator_data)
def tabulator_data():
    print(input.tabulator_data()[0])
