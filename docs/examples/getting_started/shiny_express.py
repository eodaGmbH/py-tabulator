import pandas as pd
from pytabulator import TableOptions, Tabulator, TabulatorContext, render_tabulator
from shiny import reactive, render
from shiny.express import input, ui

ui.input_action_button("trigger_get_data", "Get data")


@render.code
async def txt():
    print(input.tabulator_row_clicked())
    return input.tabulator_row_clicked()["Name"]


@render.code
def row_edited():
    data = input.tabulator_row_edited()
    print(data)
    return f"{data['Name']}, {data['Sex']}"


@render_tabulator
def tabulator():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    return Tabulator(
        df,
        TableOptions(
            header_visible=True,
            movable_rows=True,
            group_by=["Sex", "Age"],
            height=500,
            pagination=True,
            selectable=1,
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
            layout="fitDataTable",
            # layout="fitColumns",
            frozenRows=3,
        ),
    )


@reactive.Effect
@reactive.event(input.trigger_get_data)
async def trigger_get_data():
    print("triggered")
    async with TabulatorContext("tabulator") as table:
        table.trigger_get_data()


@reactive.Effect
@reactive.event(input.tabulator_data)
async def get_data():
    data = input.tabulator_data()
    print("data", data[0], data[1])
