import pandas as pd
from pytabulator.shiny_bindings import render_tabulator
from pytabulator.tabulator import Tabulator, TabulatorOptions
from shiny import render
from shiny.express import input, ui

ui.div("Click on row to print name.", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


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
