from __future__ import annotations

from htmltools import Tag
from pandas import DataFrame
from shiny.render.renderer import Jsonifiable, Renderer, ValueFn

from ._utils import df_to_dict
from .shiny_ui import output_tabulator
from .tabulator import TableOptions, Tabulator, jsonifiable_table_options


class render_tabulator(Renderer[Tabulator]):
    """A decorator for a function that returns a `Tabulator` table"""

    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    async def transform(self, value: Tabulator) -> Jsonifiable:
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        return value.to_dict()


# DEPRECATED
"""
class render_data_frame_(Renderer[DataFrame]):
    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    async def transform(self, df: DataFrame) -> Jsonifiable:
        # return {"values": value.values.tolist(), "columns": value.columns.tolist()}
        # TODO: convert with js
        data = df_to_dict(df)
        data["options"] = {}
        return data
"""


class render_data_frame(Renderer[DataFrame]):
    """A decorator for a function that returns a `DataFrame`

    Args:
        table_options (TableOptions): Table options.
    """

    editor: bool

    def auto_output_ui(self) -> Tag:
        return output_tabulator(self.output_id)

    def __init__(
        self,
        _fn: ValueFn[DataFrame] = None,
        *,
        table_options: TableOptions | dict = TableOptions(),
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
