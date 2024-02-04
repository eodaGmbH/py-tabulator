import pandas as pd
from pytabulator import (
    TableOptions,
    Tabulator,
    TabulatorContext,
    render_tabulator,
    theme,
)
from pytabulator.ui import use_sheetjs
from shiny import reactive
from shiny.express import input, ui

# Include sheetjs to support xlsx downloads
#
use_sheetjs()

with ui.div(style="padding-top: 10px;"):
    ui.input_action_button("trigger_download", "Download")

with ui.div(style="padding-top: 10px;"):
    ui.input_select("data_type", label="Data type", choices=["csv", "json", "xlsx"])


theme.tabulator_site()


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
        ),
    )


@reactive.Effect
@reactive.event(input.trigger_download)
async def trigger_download():
    print("download triggered")
    async with TabulatorContext("tabulator") as table:
        table.trigger_download(input.data_type())
