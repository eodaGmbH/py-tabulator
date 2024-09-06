import pandas as pd
from pytabulator import TableOptions, Tabulator, output_tabulator, render_tabulator
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.output_text_verbatim("txt", placeholder=True),
    output_tabulator("tabulator"),
)

df = pd.DataFrame(
    dict(
        a=[1, 2, 3],
        b=[11, 22, 33],
        x=["Hans", "Peter", "Jochem"],
        y=["hungry", "proud", "joyful"],
    )
)

columns = [
    {
        "title": "Numbers",
        "columns": [
            {"title": "A number", "field": "a", "hozAlign": "right"},
            {"title": "Another number", "field": "b", "hozAlign": "right"},
        ],
    },
    {
        "title": "Personal info",
        "columns": [
            {"title": "Name", "field": "x"},
            {"title": "Attribute", "field": "y"},
        ],
    },
]


def server(input, output, session):
    @render_tabulator
    def tabulator():
        return Tabulator(df, table_options=TableOptions(columns=columns))

    @render.code
    async def txt():
        return str(input.tabulator_row_clicked())


app = App(app_ui, server)
