from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal, Union

from ._utils import snake_to_camel_case


@dataclass
class TableOptions(object):
    add_row_pos: Literal["bottom", "top"] = "bottom"
    columns: list = None
    frozen_rows: int = None
    group_by: Union[str, list] = None
    header_visible: bool = True
    height: Union[int, str] = None
    history: bool = False
    index: str = "id"
    layout: Literal[
        "fitData", "fitDataFill", "fitDataStretch", "fitDataTable", "fitColumns"
    ] = "fitColumns"
    movable_rows: bool = False
    pagination_add_row: Literal["page", "table"] = "page"
    pagination: bool = False
    pagination_counter: str = "rows"
    resizable_column_fit: bool = False
    row_height: int = None
    selectable: Union[str, bool, int] = "highlight"

    def to_dict(self):
        return asdict(
            self,
            dict_factory=lambda x: {
                snake_to_camel_case(k): v for (k, v) in x if v is not None
            },
        )
