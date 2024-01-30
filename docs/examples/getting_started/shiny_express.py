import pandas as pd
from shiny import reactive, render
from shiny.express import input, ui
from tabylator import render_data_frame
from tabylator.shiny_bindings import render_tabulator, render_tabulator_experimental
from tabylator.tabulator import Tabulator, TabulatorOptions
from tabylator.tabulator_context import tabulator_get_data

ui.input_action_button("trigger_get_data", "Get data")


@render.code
async def txt():
    print(input.tabylator_row())
    return input.tabylator_row()["Name"]


# @render_tabulator_experimental(editor=True)
@render_tabulator
def tabylator():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    return Tabulator(
        df,
        TabulatorOptions(
            headerVisible=True,
            # movableRows=True,
            # groupBy=["Sex", "Age"],
            height="600px",
            pagination=True,
            # selectable=True,
            download=None,
            editor=True,
            columns=[
                {"title": "Name", "field": "Name", "editor": True},
                {"title": "Age", "field": "Age"},
                {"title": "Gender", "field": "Sex"},
            ],
        ),
    )


@reactive.Effect
@reactive.event(input.trigger_get_data)
async def trigger_get_data():
    print("triggered")
    await tabulator_get_data("tabylator")


@reactive.Effect
@reactive.event(input.tabylator_get_data)
async def get_data():
    data = input.tabylator_get_data()
    print("data", data[0], data[1])
