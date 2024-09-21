from __future__ import annotations

from pandas import DataFrame

from ._types import TableOptions
from ._utils import df_to_dict
from typing import Self

# TODO: Move somewhere else!?
def jsonifiable_table_options(
    table_options: TableOptions | dict,
) -> dict:
    if isinstance(table_options, TableOptions):
        return table_options.to_dict()

    return table_options


class Tabulator(object):
    """Tabulator

    Args:
        df (DataFrame): A data frame.
        table_options (TableOptions): Table options.
    """

    def __init__(
        self,
        df: DataFrame,
        table_options: TableOptions | dict = {},
    ) -> None:
        self.df = df
        # self.table_options = table_options
        self._table_options = jsonifiable_table_options(table_options)

    @property
    def columns(self) -> list[dict]:
        return self._table_options["columns"]

    # TODO: Rename to set_options
    def options(self, **kwargs) -> Self:
        self._table_options.update(kwargs)
        return self

    def to_dict(self) -> dict:
        data = df_to_dict(self.df)
        # data["options"] = jsonifiable_table_options(self.table_options)
        data["options"] = self._table_options
        return data
