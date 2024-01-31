from __future__ import annotations

from dataclasses import asdict

from htmltools import HTMLDependency, Tag
from pandas import DataFrame
from shiny import ui
from shiny.module import resolve_id
from shiny.render.renderer import Jsonifiable, Renderer, ValueFn

from ._utils import df_to_dict
from .tabulator import Tabulator, TabulatorOptions

tabulator_dep = HTMLDependency(
    "tabulator",
    "5.5.4",
    source={"package": "pytabulator", "subdir": "srcjs"},
    script={"src": "tabulator.min.js", "type": "module"},
    stylesheet={"href": "tabulator.min.css"},
    all_files=False,
)


tabulator_bindings_dep = HTMLDependency(
    "tabulatorbindings",
    "0.1.0",
    source={"package": "pytabulator", "subdir": "srcjs"},
    script={"src": "tabulator-bindings.js", "type": "module"},
    all_files=False,
)


def output_tabulator(id: str, height: int | str = 400):
    if isinstance(height, int):
        height = f"{height}px"

    return ui.div(
        tabulator_dep,
        tabulator_bindings_dep,
        id=resolve_id(id),
        class_="shiny-tabulator-output",
        # style=f"height: {height}",
    )


class render_tabulator(Renderer[Tabulator]):
    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    async def transform(self, value: Tabulator) -> Jsonifiable:
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        return value.to_dict()


class render_data_frame_(Renderer[DataFrame]):
    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    async def transform(self, df: DataFrame) -> Jsonifiable:
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        data = df_to_dict(df)
        data["options"] = {}
        return data


class render_data_frame(Renderer[DataFrame]):
    editor: bool

    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    def __init__(
        self,
        _fn: ValueFn[DataFrame] = None,
        *,
        table_options: TabulatorOptions = TabulatorOptions(),
    ) -> None:
        super().__init__(_fn)
        self.table_options = table_options

    async def render(self) -> Jsonifiable:
        df = await self.fn()
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        data = df_to_dict(df)
        data["options"] = asdict(self.table_options)
        return data
