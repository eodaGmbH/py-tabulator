from __future__ import annotations

from pandas import DataFrame

from ._utils import df_to_dict, as_camel_dict_recursive
from typing import Self, Any

from .tabulator_options import TabulatorOptions
from .utils import create_columns
from .editors import Editor
from .formatters import Formatter

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

    # Update single column
    def _update_column(self, col_name: str, **kwargs: Any) -> Self:
        i, col = self._find_column(col_name)
        if col is not None:
            self._options.columns[i] = col | as_camel_dict_recursive(kwargs)

        return self

    # ----- Column generics -----
    def update_column(self, col_name: str | list, **kwargs: Any) -> Self:
        col_names = [col_name] if isinstance(col_name, str) else col_name
        for col_name in col_names:
            self._update_column(col_name, **kwargs)

        return self

    def set_column_formatter(
        self,
        col_name: str | list,
        formatter: str | Formatter,
        formatter_params: dict = None,
        **kwargs: Any,
    ) -> Self:
        if isinstance(formatter, Formatter):
            formatter_name = formatter.name
            formatter_params = formatter.to_dict()
        else:
            formatter_name = formatter

        return self.update_column(
            col_name,
            **dict(
                formatter=formatter_name,
                formatterParams=formatter_params or dict(),
                **kwargs,
            ),
        )

    def set_column_editor(
        self,
        col_name: str | list,
        editor: str | Editor,
        editor_params: dict = None,
        validator: Any = None,
        **kwargs: Any,
    ) -> Self:
        if isinstance(editor, Editor):
            editor_name = editor.name
            editor_params = editor.to_dict()
        else:
            editor_name = editor

        return self.update_column(
            col_name,
            **dict(
                editor=editor_name,
                editorParams=editor_params or dict(),
                validator=validator,
                **kwargs,
            ),
        )

    # ----- Column formatters -----
    def set_column_formatter_star(
        self, col_name: str | list, stars: int, **kwargs
    ) -> Self:
        formatter_params = dict(stars=stars)
        self.set_column_formatter(
            col_name, "star", formatter_params, hozAlign="center", **kwargs
        )
        return self

    def set_column_formatter_tick_cross(self, col_name: str | list, **kwargs) -> Self:
        self.set_column_formatter(col_name, "tickCross", **kwargs)
        return self

    # ----- Column editor -----
    def set_column_editor_number(
        self,
        col_name: str | list,
        min_value: float = None,
        max_value: float = None,
        step: float = None,
        validator=None,
        **kwargs,
    ) -> Self:
        editor_params = dict(min=min_value, max=max_value, step=step)
        return self.set_column_editor(
            col_name, "number", editor_params, validator, **kwargs
        )

    # ----- Column headers -----
    def set_column_title(self, col_name: str, title: str, **kwargs) -> Self:
        return self.update_column(col_name, title=title, **kwargs)

    # ----- Misc -----
    def set_options(self, **kwargs) -> Self:
        self._options = self._options.model_copy(update=kwargs)
        return self

    def to_dict(self) -> dict:
        payload = df_to_dict(self.df)
        payload["options"] = self._options.to_dict()
        payload["bindingOptions"] = dict(lang="python")
        return payload

    def to_html(self):
        pass
