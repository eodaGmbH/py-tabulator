import pandas as pd
from pytabulator import render_data_frame_
from pytabulator.shiny_bindings import render_data_frame, render_tabulator
from pytabulator.tabulator import Tabulator, TabulatorOptions
from pytabulator.tabulator_context import tabulator_get_data
from shiny import reactive, render
from shiny.express import input, ui

ui.input_action_button("trigger_get_data", "Get data")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@render.code
def row_edited():
    data = input.tabulator_row_edited()
    print(data)
    return f"{data['Name']}, {data['Sex']}"


# @render_tabulator_experimental(editor=True)
@render_tabulator
def tabulator():
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
            # pagination=True,
            # selectable=True,
            download=None,
            editor=True,
            resizableColumnFit=False,
            columns=[
                {
                    "title": "Name",
                    "field": "Name",
                    "editor": True,
                    "frozen": True,
                    "resizable": False,
                    "headerFilter": True,
                    "headerFilterParams": {"starts": True},
                },
                {
                    "title": "AgeP",
                    "field": "Age",
                    "formatter": "progress",
                },
                {
                    "title": "Age",
                    "field": "Age",
                    "bottomCalc": "avg",
                    "headerFilter": "number",
                },
                {
                    "title": "Gender",
                    "field": "Sex",
                    "editor": "list",
                    "editorParams": {"values": ["male", "female"]},
                    "width": 200,
                    "headerFilter": True,
                    "headerFilterParams": {
                        "values": ["male", "female"],
                        "clearable": True,
                        "starts": True,
                    },
                },
            ],
            # layout="fitDataTable",
            layout="fitColumns",
            frozenRows=3,
        ),
    )


@reactive.Effect
@reactive.event(input.trigger_get_data)
async def trigger_get_data():
    print("triggered")
    await tabulator_get_data("tabulator")


@reactive.Effect
@reactive.event(input.tabulator_get_data)
async def get_data():
    data = input.tabulator_get_data()
    print("data", data[0], data[1])
