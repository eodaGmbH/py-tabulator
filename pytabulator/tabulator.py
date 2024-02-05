from __future__ import annotations

from pandas import DataFrame

from ._types import TableOptions
from ._utils import df_to_dict

# TODO: DEPRECATED
"""
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
"""


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
        self.table_options = table_options

    def to_dict(self) -> dict:
        data = df_to_dict(self.df)
        data["options"] = jsonifiable_table_options(self.table_options)
        return data
