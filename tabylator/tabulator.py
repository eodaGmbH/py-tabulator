from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Literal

from pandas import DataFrame

from ._utils import df_to_dict


@dataclass
class TabulatorOptions(object):
    headerVisible: bool = True
    movableRows: bool = False
    groupBy: str = None
    height: str = None
    pagination: bool = False
    selectable: bool = False
    columns: list = None
    layout: str = "fitColumns"
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
