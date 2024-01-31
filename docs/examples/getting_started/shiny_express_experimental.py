import pandas as pd
from pytabulator.shiny_bindings import render_data_frame, render_tabulator
from pytabulator.tabulator import Tabulator, TabulatorOptions
from pytabulator.tabulator_context import TabulatorContext
from shiny import reactive, render
from shiny.express import input, ui

ui.div("Click on row to print name.", style="padding: 10px;")

ui.input_action_button("trigger_download", "Download")

ui.input_action_button("add_row", "Add row")

ui.input_action_button("trigger_get_data", "Get data")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@reactive.Effect
@reactive.event(input.trigger_download)
async def trigger_download():
    print("download triggered")
    async with TabulatorContext("tabulator") as table:
        table.trigger_download()


@reactive.Effect
@reactive.event(input.add_row)
async def add_row():
    async with TabulatorContext("tabulator") as table:
        table.add_row({"Name": "Hans", "Sex": "male"})


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
            layout="fitColumns",
        ),
    )
