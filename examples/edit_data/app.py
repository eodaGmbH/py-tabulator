import pandas as pd
from pytabulator import (
    TableOptions,
    Tabulator,
    TabulatorContext,
    output_tabulator,
    render_tabulator,
)
from pytabulator.utils import create_columns
from shiny import App, reactive, ui

df = pd.DataFrame({"id": [1, 2, 3], "name": ["Hans", "Peter", "Hanna"]})
table_options = TableOptions(columns=create_columns(df, default_editor=True))

app_ui = ui.page_auto(
    ui.h1("Edit data and submit changes", style="padding-top: 10px;"),
    output_tabulator("tabulator"),
    ui.div(ui.input_action_button("submit", "Submit data"), style="padding-top: 10px;"),
)


def server(input, output, session):
    @render_tabulator
    def tabulator():
        return Tabulator(df, table_options)

    @reactive.Effect
    @reactive.event(input.submit)
    async def trigger_get_data():
        async with TabulatorContext("tabulator") as table:
            print("get data")
            table.trigger_get_data()

    @reactive.Effect
    @reactive.event(input.tabulator_data)
    def tabulator_data():
        df_submitted = pd.DataFrame(input.tabulator_data())
        print(df_submitted)


app = App(app_ui, server)
