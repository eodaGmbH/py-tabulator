from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal, Union
from warnings import warn

from pandas import DataFrame
from pydantic import BaseModel, Field, field_validator

from ._utils import df_to_dict


class TableOptions(BaseModel):
    """Table options

    Attributes:
        index (str, optional): The index of the table. Defaults to `id`.
        header_visible (bool, optional): Whether to display the header of the table. Defaults to `True`.
        movable_rows (bool, optional): Whether rows are movable or not. Defaults to `False`.
        group_by: Columns to group by. Defaults to `None`.
        height (int, optional): Height in px. Defaults to `300`.
        pagination (bool, optional): Whether to enable pagination. Defaults to `False`.
        pagination_add_row: Where to add rows when pagination is enabled. Defaults to `page`.
        selectable: Whether a row is selectable. An integer value sets the maximum number of rows, that can be selected.
            If set to `highlight`, rows do not change state when clicked. Defaults to `highlight`.
        columns (list, optional): Columns configuration. Defaults to `None`,
            which means that the default configuration is used.
        layout: The layout of the table. Defaults to `fitColumns`.
        add_row_pos: Where to add rows. Defaults to `bottom`.
        frozen_rows (int, optional): Number of frozen rows. Defaults to `Ǹone`.
        row_height: Fixed height of rows. Defaults to `None`.
        history (bool, optional): Whether to enable history. Must be set if `undo` and `redo` is used. Defaults to `False`.

    Note:
        See [Tabulator Setup Options](https://tabulator.info/docs/5.5/options) for details.

    Examples:
        >>> from pytabulator import TableOptions

        >>> table_options = TableOptions(height=500, pagination=True)
    """

    index: str = "id"
    header_visible: bool = Field(True, serialization_alias="headerVisible")
    movable_rows: bool = Field(False, serialization_alias="movableRows")
    group_by: Union[str, list] = Field(None, serialization_alias="groupBy")
    height: Union[int, str] = None
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

    @field_validator("height")
    def validate_height(cls, v):
        if isinstance(v, int):
            return f"{v}px"

        return v

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
    initialFilter: list = None
    editor: bool = False

    # TODO: Rename to 'download_csv'
    download: Literal["csv", "json"] = None


class Tabulator(object):
    """Tabulator

    Args:
        df (DataFrame): A data frame.
        table_options (TableOptions): Table options.
    """

    def __init__(
        self,
        df: DataFrame,
        table_options: TableOptions | dict | TabulatorOptions = None,
    ) -> None:
        self.df = df
        if isinstance(table_options, TableOptions):
            table_options = table_options.model_dump(by_alias=True)
        # Legacy
        elif isinstance(table_options, TabulatorOptions):
            warn(
                "'TabulatorOptions' is deprecated and will be removed in one of the next releases. Use 'TableOptions' instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            table_options = asdict(table_options)

        self.table_options = table_options

    def to_dict(self) -> dict:
        data = df_to_dict(self.df)
        data["options"] = self.table_options
        return data
