import pandas as pd
from pytabulator import TableOptions, Tabulator, TabulatorContext, render_tabulator
from shiny import reactive, render
from shiny.express import input, ui

# ui.div("Hit enter in name search field to start search.", style="padding: 10px;")
ui.div(
    ui.input_action_button("clear_filter", "Clear Filter"),
    style="padding-bottom: 10px; padding-top: 10px;",
)


@reactive.Effect
@reactive.event(input.clear_filter)
async def trigger_get_data():
    async with TabulatorContext("tabulator") as table:
        table.add_call("clearHeaderFilter")


@render.code
async def txt():
    print(input.tabulator_data_filtered())
    return f"Number of search result: {len(input.tabulator_data_filtered())}"


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
            layout="fitDataTable",
            columns=[
                {
                    "title": "Name",
                    "field": "Name",
                    "headerFilter": True,
                    "headerFilterPlaceholder": "Find a Person...",
                    # "headerFilterLiveFilter": False,
                    # "headerFilterLiveFilterDelay": 20000,
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
                        },
                        "clearable": True,
                    },
                },
            ],
        ),
    )
