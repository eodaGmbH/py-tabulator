import pandas as pd
from pytabulator import TableOptions, Tabulator, TabulatorContext, render_tabulator
from shiny import reactive, render
from shiny.express import input, ui

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

# Setup
#
columns = [
    {
        "title": "Name",
        "field": "Name",
        "headerFilter": True,
        "headerFilterPlaceholder": "Find a Person...",
        # "headerFilterLiveFilter": False,
    },
    {
        "title": "Survived",
        "field": "Survived",
        "hozAlign": "right",
        "headerFilter": "list",
        "headerFilterParams": {
            "values": {
                "1": "Survived",
                "0": "Died",
            }
        },
    },
]

table_options = TableOptions(
    height=600, pagination=True, layout="fitDataTable", columns=columns
)

# Shiny Express app
#
ui.div(
    ui.input_action_button("clear_filter", "Clear Filter"),
    style="padding-bottom: 10px; padding-top: 10px;",
)


@reactive.Effect
@reactive.event(input.clear_filter)
async def clear_filter():
    async with TabulatorContext("tabulator") as table:
        table.add_call("clearHeaderFilter")


@render.code
async def txt():
    print(input.tabulator_data_filtered())
    return f"Number of search result: {len(input.tabulator_data_filtered())}"


@render_tabulator
def tabulator():
    return Tabulator(df, table_options)
