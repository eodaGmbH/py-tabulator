import pandas as pd
from shiny import render
from shiny.express import input, ui
from tabylator import render_tabular
from tabylator.shiny_bindings import render_tabular_expirimental


@render.code
async def txt():
    print(input.tabylator_row())
    return input.tabylator_row()["Name"]


@render_tabular_expirimental(editor=True)
def tabylator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
