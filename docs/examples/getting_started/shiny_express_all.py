import pandas as pd
from pytabulator.shiny_bindings import render_data_frame, render_tabulator
from pytabulator.tabulator import Tabulator, TabulatorOptions
from pytabulator.tabulator_context import TabulatorContext
from shiny import reactive, render
from shiny.express import input, ui

ui.h1("Interactive Table", style="padding: 10px;")

ui.input_action_button("trigger_download", "Download")
ui.input_action_button("add_row", "Add row")
ui.input_action_button("delete_selected_rows", "Delete selected rows")
ui.input_action_button("undo", "Undo")
ui.input_action_button("redo", "Redo")
ui.input_action_button("trigger_get_data", "Get data")

ui.div("Click on row to print name.", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@reactive.Effect
@reactive.event(input.trigger_download)
async def trigger_download():
    print("download triggered")
    async with TabulatorContext("tabulator") as table:
        table.trigger_download("json")


@reactive.Effect
@reactive.event(input.add_row)
async def add_row():
    async with TabulatorContext("tabulator") as table:
        table.add_row({"Name": "Hans", "Sex": "male"})


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


@render_tabulator
def tabulator():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    return Tabulator(
        df,
        TabulatorOptions(
            height="600px",
            pagination=True,
            paginationAddRow="table",
            layout="fitColumns",
            index="PassengerId",
            addRowPos="top",
            selectable=True,
            history=True,
            # editor=True,
        ),
    )
