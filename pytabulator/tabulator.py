from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Literal, Union

from pandas import DataFrame

from ._utils import df_to_dict


@dataclass
class TabulatorOptions(object):
    index: str = "id"
    headerVisible: bool = True
    movableRows: bool = False
    groupBy: str = None
    height: str = None
    pagination: bool = False
    paginationAddRow: Literal["page", "table"] = "page"
    selectable: Union[str, bool, int] = "highlight"
    columns: list = None
    layout: Literal[
        "fitData", "fitDataFill", "fitDataStretch", "fitDataTable", "fitColumns"
    ] = "fitColumns"
    addRowPos: Literal["bottom", "top"] = "bottom"
    frozenRows: int = None
    rowHeight: int = None
    resizableColumnFit: bool = False
    history: bool = False
    editor: bool = False

    # TODO: Rename to 'download_csv'
    download: Literal["csv", "json"] = None


class Tabulator(object):
    def __init__(
        self, df: DataFrame, table_options: dict | TabulatorOptions = None
    ) -> None:
        self.df = df
        if isinstance(table_options, TabulatorOptions):
            table_options = asdict(table_options)

        self.table_options = table_options

    def to_dict(self) -> dict:
        data = df_to_dict(self.df)
        data["options"] = self.table_options
        return data


"""
class TabulatorContext(object):
    def get_data(self):
        pass

    def add_row(self):
        pass
"""
