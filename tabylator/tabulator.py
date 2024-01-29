from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Literal

from pandas import DataFrame


@dataclass
class TableOptions(object):
    headerVisible: bool = True
    movableRows: bool = False
    groupBy: str = None
    height: str = None
    pagination: bool = False
    selectable: bool = False
    download: Literal["csv", "json"] = None


class Tabulator(object):
    def __init__(
        self, df: DataFrame, table_options: dict | TableOptions = None
    ) -> None:
        self.df = df
        if isinstance(table_options, TableOptions):
            table_options = asdict(table_options)

        self.table_options = table_options

    def to_dict(self) -> dict:
        data = json.loads(self.df.to_json(orient="table", index=False))
        data["options"] = self.table_options
        return data
