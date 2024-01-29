import pandas as pd
from shiny import App, reactive, render, ui
from tabylator.shiny_bindings import output_tabulator, render_tabular

app_ui = ui.page_fluid(
    ui.output_text_verbatim("txt", placeholder=True),
    output_tabulator("tabylator", height=600),
)


def server(input, output, session):
    @render_tabular
    def tabylator():
        return pd.read_csv(
            "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        )

    @render.code
    async def txt():
        print(input.tabylator_row())
        return str(input.tabylator_row())


app = App(app_ui, server)
