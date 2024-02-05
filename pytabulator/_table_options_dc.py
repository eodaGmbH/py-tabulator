from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal, Union

from ._types import TableOptions
from ._utils import snake_to_camel_case


@dataclass
class TableOptionsDC(TableOptions):
    """Table options

    Attributes:
        add_row_pos: Where to add rows. Defaults to `"bottom"`.
        columns: Column definitions.
        frozen_rows: Number of frozen rows. Defaults to `Ǹone`.
        group_by: Columns to group by. Defaults to `None`.
        header_visible: Whether to display the header of the table. Defaults to `True`.
        height: The height of the table in pixels. Defaults to `311`.
        history: Whether to enable history. Must be set if `undo` and `redo` is used. Defaults to `False`.
        index: The field to be used as a unique index for each row. Defaults to `"id"`.
        layout: The layout of the table. Defaults to `"fitColumns"`.
        movable_rows: Whether rows are movable. Defaults to `False`.
        pagination_add_row: Where to add rows when pagination is enabled. Defaults to `"page"`.
        pagination: Whether to enable pagination. Defaults to `False`.
        pagination_counter: Whether to display counted rows in footer. Defaults to `"rows"`.
        resizable_column_fit: Maintain total column width when resizing a column. Defaults to `False`.
        row_height: Fixed height for rows. Defaults to `None`.
        selectable: Whether a row is selectable. An integer value sets the maximum number of rows, that can be selected.
            If set to `"highlight"`, rows do not change their state when they are clicked. Defaults to `"highlight"`.
    """

    add_row_pos: Literal["bottom", "top"] = "bottom"
    columns: list = None
    frozen_rows: int = None
    group_by: Union[str, list] = None
    header_visible: bool = True
    height: Union[int, None] = 311
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
