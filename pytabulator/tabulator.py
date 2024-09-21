from __future__ import annotations

from pandas import DataFrame

from ._utils import df_to_dict
from typing import Self, Any

from .tabulator_options import TabulatorOptions
from .utils import create_columns


class Tabulator(object):
    """Tabulator

    Args:
        df (DataFrame): A data frame.
        options (TabulatorOptions): Setup options.
    """

    def __init__(
        self,
        df: DataFrame,
        options: TabulatorOptions | dict = TabulatorOptions(),
    ) -> None:
        self.df = df
        self._options = (
            options
            if isinstance(options, TabulatorOptions)
            else TabulatorOptions(**options)
        )
        if not self._options.columns:
            self._options.columns = create_columns(self.df)

    @property
    def columns(self) -> list[dict]:
        return self._options.columns

    def _find_column(self, col_name: str) -> tuple:
        for i, col in enumerate(self.columns):
            if col["field"] == col_name:
                return i, col

        return None, None

    def update_column(self, col_name: str, **kwargs: Any) -> Self:
        i, col = self._find_column(col_name)
        if col is not None:
            self._options.columns[i] = col | kwargs

        return self

    def set_formatter(
        self,
        col_name: str,
        formatter: str,
        formatter_params: dict = None,
        **kwargs: Any,
    ) -> Self:
        return self.update_column(
            col_name,
            **dict(
                formatter=formatter,
                formatterParams=formatter_params or dict(),
                **kwargs,
            ),
        )

    def set_options(self, **kwargs) -> Self:
        pass
        return self

    def to_dict(self) -> dict:
        # TODO: Rename 'data' to ???
        data = df_to_dict(self.df)
        data["options"] = self._options.to_dict()
        return data
