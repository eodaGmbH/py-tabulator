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

    def set_column_formatter(
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

    def set_column_formatter_star(self, col_name: str, stars: int, **kwargs) -> Self:
        formatter_params = dict(stars=stars)
        self.set_column_formatter(
            col_name, "star", formatter_params, hozAlign="center", **kwargs
        )
        return self

    def set_column_formatter_tick_cross(self, col_name, **kwargs) -> Self:
        self.set_column_formatter(col_name, "tickCross", **kwargs)
        return self

    def set_column_editor(self, col_name: str, editor: str, editor_params: dict = None, **kwargs: Any) -> Self:
        return self.update_column(
            col_name,
            **dict(
                editor=editor,
                editorParams=editor_params or dict(),
                **kwargs,
            ),
        )

    def set_options(self, **kwargs) -> Self:
        self._options = self._options.model_copy(update = kwargs)
        return self

    def to_dict(self) -> dict:
        payload = df_to_dict(self.df)
        payload["options"] = self._options.to_dict()
        payload["bindingOptions"] = dict(lang="python")
        return payload

    def to_html(self):
        pass
