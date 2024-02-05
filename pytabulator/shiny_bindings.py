from __future__ import annotations

import os

from htmltools import HTMLDependency, Tag
from pandas import DataFrame
from shiny import ui
from shiny.module import resolve_id
from shiny.render.renderer import Jsonifiable, Renderer, ValueFn

from ._types import TableOptions
from ._utils import df_to_dict
from .tabulator import Tabulator, jsonifiable_table_options

# from . import TableOptions


# --
# UI
# --


def tabulator_dep() -> HTMLDependency:
    return HTMLDependency(
        "tabulator",
        "5.5.4",
        source={"package": "pytabulator", "subdir": "srcjs"},
        script={"src": "tabulator.min.js", "type": "module"},
        stylesheet={"href": os.getenv("PY_TABULATOR_STYLESHEET", "tabulator.min.css")},
        all_files=False,
    )


tabulator_bindings_dep = HTMLDependency(
    "tabulatorbindings",
    "0.1.0",
    source={"package": "pytabulator", "subdir": "srcjs"},
    script={"src": "tabulator-bindings.js", "type": "module"},
    all_files=False,
)


def output_tabulator(id: str):
    """Create an output container for a `Tabulator` table

    Args:
        id (str): An output id of a `Tabulator` table.
    """
    return ui.div(
        tabulator_dep(),
        tabulator_bindings_dep,
        id=resolve_id(id),
        class_="shiny-tabulator-output",
    )


# ------
# Render
# ------


class render_tabulator(Renderer[Tabulator]):
    """A decorator for a function that returns a `Tabulator` table"""

    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    async def transform(self, value: Tabulator) -> Jsonifiable:
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        return value.to_dict()


class render_data_frame(Renderer[DataFrame]):
    """A decorator for a function that returns a `DataFrame`

    Args:
        table_options (TableOptions): Table options.
    """

    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    def __init__(
        self,
        _fn: ValueFn[DataFrame] = None,
        *,
        table_options: TableOptions | dict = {},
    ) -> None:
        super().__init__(_fn)
        self.table_options = table_options

    async def render(self) -> Jsonifiable:
        df = await self.fn()
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        data = df_to_dict(df)
        data["options"] = jsonifiable_table_options(self.table_options)
        return data
