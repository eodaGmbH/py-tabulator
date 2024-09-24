import pandas as pd
from pytabulator.shiny_bindings import output_tabulator, render_tabulator
from pytabulator.tabulator import Tabulator
from pytabulator.editors import NumberEditor, StarEditor, ProgressEditor
from pytabulator.formatters import StarFormatter
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
        """
        return Tabulator(df, options={"height": 311}).set_column_formatter(
            "Pclass", "star", {"stars": 3}, hozAlign="center"
        )
        """
        return (
            Tabulator(df)
            .set_options(height=311)
            # .set_column_formatter_star("Pclass", 3)
            .set_column_formatter("Pclass", StarFormatter(stars=3), hoz_align="center")
            .set_column_formatter_tick_cross("Survived", hoz_align="center")
            # .set_column_editor("Fare", "number", dict(min=0, max=10))
            .set_column_editor_number("Fare", min_=0, max_=5)
            .set_column_title("Pclass", "PassengerClass")
            .set_column_editor(["Name", "Sex"], "input", hoz_align="center")
            .set_column_editor("PassengerId", NumberEditor(min=0, max=1000, step=1))
            .set_column_editor("Pclass", StarEditor())
            .set_column_formatter("Fare", "progress")
            .set_column_editor(
                "Fare",
                ProgressEditor(min=0, max=100, element_attributes=dict(title="Hey ho")),
                hoz_align="left",
            )
        )

    @render.code
    async def txt():
        print(input.tabulator_row_clicked())
        return str(input.tabulator_row_clicked())


app = App(app_ui, server)
