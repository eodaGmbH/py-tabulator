import pandas as pd
from pytabulator.shiny_bindings import output_tabulator, render_tabulator
from pytabulator.tabulator import Tabulator
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.output_text_verbatim("txt", placeholder=True),
    output_tabulator("tabulator"),
)


def server(input, output, session):
    @render_tabulator
    def tabulator():
        df = pd.read_csv(
            "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        )
        return Tabulator(df, options={"height": 311})

    @render.code
    async def txt():
        print(input.tabulator_row_clicked())
        return str(input.tabulator_row_clicked())


app = App(app_ui, server)
