import pandas as pd
from pytabulator.shiny_bindings import (
    output_tabulator,
    render_data_frame,
    render_tabulator,
)
from pytabulator.tabulator import Tabulator
from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.output_text_verbatim("txt", placeholder=True),
    output_tabulator("tabylator", height=600),
)


def server(input, output, session):
    @render_tabulator
    def tabylator():
        df = pd.read_csv(
            "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        )
        return Tabulator(df=df)

    @render.code
    async def txt():
        print(input.tabylator_row())
        return str(input.tabylator_row())


app = App(app_ui, server)
