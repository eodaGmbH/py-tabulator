import pandas as pd
from pytabulator import TableOptions, Tabulator, theme
from pytabulator.shiny_bindings import render_tabulator
from shiny import render
from shiny.express import input, ui

table_options = TableOptions(
    height=600,
    pagination=True,
    layout="fitColumns",
)

# Set theme
#
theme.tabulator_midnight()

ui.div("Click on row to print name.", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row_clicked())
    return input.tabulator_row_clicked()["Name"]


@render_tabulator
def tabulator():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    return Tabulator(df, table_options)
