import pandas as pd
from shiny import render
from shiny.express import input, ui
from tabylator import render_data_frame
from tabylator.shiny_bindings import render_tabulator, render_tabulator_experimental
from tabylator.tabulator import Tabulator, TabulatorOptions


@render.code
async def txt():
    print(input.tabylator_row())
    return input.tabylator_row()["Name"]


# @render_tabulator_experimental(editor=True)
@render_tabulator
def tabylator():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    return Tabulator(
        df,
        TabulatorOptions(
            headerVisible=True,
            movableRows=True,
            # groupBy=["Sex", "Age"],
            height="600px",
            pagination=True,
            selectable=True,
            download=None,
            editor=True,
        ),
    )
