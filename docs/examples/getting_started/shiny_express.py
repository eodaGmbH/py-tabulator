import pandas as pd
from shiny import render
from shiny.express import input, ui
from tabylator import render_data_frame
from tabylator.shiny_bindings import render_tabulator_experimental


@render.code
async def txt():
    print(input.tabylator_row())
    return input.tabylator_row()["Name"]


@render_tabulator_experimental(editor=True)
def tabylator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
