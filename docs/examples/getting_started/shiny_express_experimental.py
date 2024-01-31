import pandas as pd
from pytabulator.shiny_bindings import render_data_frame, render_tabulator
from pytabulator.tabulator import Tabulator, TabulatorOptions
from pytabulator.tabulator_context import tabulator_trigger_download
from shiny import reactive, render
from shiny.express import input, ui

ui.div("Click on row to print name.", style="padding: 10px;")

ui.input_action_button("trigger_download", "Download")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@reactive.Effect
@reactive.event(input.trigger_download)
async def trigger_download():
    print("download triggered")
    await tabulator_trigger_download("tabulator")


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
