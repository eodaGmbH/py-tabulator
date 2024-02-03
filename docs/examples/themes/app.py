import pandas as pd
from pytabulator.shiny_bindings import render_tabulator
from pytabulator.tabulator import TableOptions, Tabulator
from pytabulator.themes import tabulator_midnight, tabulator_modern, tabulator_simple
from shiny import render
from shiny.express import input, ui

table_options = TableOptions(
    height=600,
    pagination=True,
    layout="fitColumns",
)

# Set theme
#
# tabulator_simple()
tabulator_midnight()
tabulator_modern()

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
