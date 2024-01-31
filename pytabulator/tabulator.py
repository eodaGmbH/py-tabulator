from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal, Union

from pandas import DataFrame
from pydantic import BaseModel, Field

from ._utils import df_to_dict


class TableOptions(BaseModel):
    """Table options"""

    index: str = "id"
    header_visible: bool = Field(True, serialization_alias="headerVisible")
    movable_rows: bool = Field(False, serialization_alias="movableRows")
    group_by: Union[str, list] = Field(None, serialization_alias="groupBy")
    height: str = None
    pagination: bool = False
    pagination_add_row: Literal["page", "table"] = Field(
        "page", serialization_alias="paginationAddRow"
    )
    selectable: Union[str, bool, int] = "highlight"
    columns: list = None
    layout: Literal[
        "fitData", "fitDataFill", "fitDataStretch", "fitDataTable", "fitColumns"
    ] = "fitColumns"
    add_row_pos: Literal["bottom", "top"] = Field(
        "bottom", serialization_alias="addRowPos"
    )
    frozen_rows: int = Field(None, serialization_alias="frozenRows")
    row_height: int = Field(None, serialization_alias="rowHeight")
    resizable_column_fit: bool = Field(False, serialization_alias="resizableColumnFit")
    history: bool = False

    def to_dict(self) -> dict:
        return self.model_dump(by_alias=True, exclude_none=True)


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
