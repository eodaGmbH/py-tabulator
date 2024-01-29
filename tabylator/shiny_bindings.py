from __future__ import annotations

import json
from typing import Union

from htmltools import HTMLDependency, Tag
from pandas import DataFrame
from shiny import ui
from shiny.module import resolve_id
from shiny.render.renderer import Jsonifiable, Renderer, ValueFn

from .tabulator import Tabulator

tabulator_dep = HTMLDependency(
    "tabulator",
    "5.5.4",
    source={"package": "tabylator", "subdir": "srcjs"},
    script={"src": "tabulator.min.js", "type": "module"},
    stylesheet={"href": "tabulator.min.css"},
    all_files=False,
)


tabulator_bindings_dep = HTMLDependency(
    "tabulatorbindings",
    "0.1.0",
    source={"package": "tabylator", "subdir": "srcjs"},
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
        return value.to_dict()["df"]


class render_data_frame(Renderer[DataFrame]):
    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    async def transform(self, value: DataFrame) -> Jsonifiable:
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        return json.loads(value.to_json(orient="table", index=False))


class render_tabulator_experimental(Renderer[DataFrame]):
    editor: bool

    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    def __init__(self, _fn: ValueFn[DataFrame] = None, *, editor: bool = False) -> None:
        super().__init__(_fn)
        self.editor = editor

    async def render(self) -> Jsonifiable:
        value = await self.fn()
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        data = json.loads(value.to_json(orient="table", index=False))
        data["options"] = {"editor": self.editor}
        return data
