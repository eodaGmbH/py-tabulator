import pandas as pd
from pytabulator.experimental import (
    midnight_theme,
    simple_theme,
    tabulator_midnight,
    tabulator_simple,
)
from pytabulator.shiny_bindings import render_tabulator
from pytabulator.tabulator import TableOptions, Tabulator
from shiny import render
from shiny.express import input, ui

ui.div("Click on row to print name.", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row_clicked())
    return input.tabulator_row_clicked()["Name"]


tabulator_simple()
tabulator_midnight()


@render_tabulator
def tabulator():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    return Tabulator(
        df,
        TableOptions(
            height=600,
            pagination=True,
            layout="fitColumns",
            columnDefaults={"tooltip": True},
        ),
    )


# midnight_theme()
# simple_theme()
