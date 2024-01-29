import pandas as pd
from pandas import DataFrame
from shiny import App, reactive, ui
from tabylator.shiny_bindings import output_tabulator, render_tabular

app_ui = ui.page_fluid(output_tabulator("tabylator", height=600))


def server(input, output, session):
    @render_tabular
    def tabylator():
        return pd.read_csv(
            "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        )
        """
        return DataFrame(
            [
                ["a", 1, 2, 6],
                ["b", 3, 4, 7],
                ["d", 2, 45, 8],
                ["d", 2, 3, 4],
                ["d", 2, 3, 4],
                ["d", 2, 3, 4],
                ["d", 2, 3, 4.1],
            ],
            columns=["name", "a", "b", "c"],
        )
        """


app = App(app_ui, server)
