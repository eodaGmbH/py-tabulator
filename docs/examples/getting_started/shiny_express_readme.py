import pandas as pd
from pytabulator import (
    TabulatorOptions,
    render_data_frame,
    render_tabulator_experimental,
)
from shiny import render
from shiny.express import input, ui

ui.div("Click on row to print name", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


# @render_data_frame()
@render_tabulator_experimental(table_options=TabulatorOptions(height="500px"))
def tabulator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
