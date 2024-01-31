import pandas as pd
from pytabulator import TableOptions, render_data_frame
from shiny import render
from shiny.express import input, ui

ui.div("Click on row to print name", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@render_data_frame(table_options=TableOptions(height=500))
def tabulator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
