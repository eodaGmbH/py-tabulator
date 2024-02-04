from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TableOptions(BaseModel):
    index: str = "id"
    header_visible: bool = Field(True, serialization_alias="headerVisible")
    movable_rows: bool = Field(False, serialization_alias="movableRows")
    group_by: Union[str, list] = Field(None, serialization_alias="groupBy")
    height: Union[int, str] = None
    pagination: bool = False
    pagination_counter: str = Field("rows", serialization_alias="paginationCounter")
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
