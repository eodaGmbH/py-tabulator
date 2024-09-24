from pydantic import BaseModel

from typing import Optional, Literal

from ._utils import as_camel_dict_recursive
from enum import Enum


class Editors(Enum):
    INPUT = "input"
    TEXTAREA = "textarea"
    NUMBER = "number"
    RANGE = "range"
    TICK_CROSS = "tickCross"
    STAR = "star"
    PROGRESS = "progress"
    LIST = "list"


class Editor(BaseModel):
    @property
    def name(self) -> str:
        return ""

    def to_dict(self) -> dict:
        return as_camel_dict_recursive(self.model_dump(exclude_none=True))


class InputEditor(Editor):
    search: Optional[bool] = None
    mask: Optional[str] = None
    select_contents: Optional[bool] = None
    element_attributes: Optional[dict] = None

    @property
    def name(self) -> str:
        return Editors.INPUT.value


class TextareaEditor(Editor):
    mask: Optional[str] = None
    select_contents: Optional[bool] = None
    vertical_navigation: Literal["hybrid", "editor", "table"] = None
    shift_enter_submit: Optional[bool] = None

    @property
    def name(self) -> str:
        return Editors.TEXTAREA.value


class NumberEditor(Editor):
    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None
    element_attributes: Optional[dict] = None
    mask: Optional[str] = None
    select_contents: Optional[bool] = None
    vertical_navigation: Literal["editor", "table"] = None

    @property
    def name(self) -> str:
        return Editors.NUMBER.value


class RangeEditor(Editor):
    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None
    element_attributes: Optional[dict] = None

    @property
    def name(self) -> str:
        return Editors.RANGE.value


class TickCrossEditor(Editor):
    true_value: Optional[str] = None
    false_value: Optional[str] = None
    element_attributes: Optional[dict] = None

    @property
    def name(self) -> str:
        return Editors.TICK_CROSS.value


class StarEditor(Editor):
    @property
    def name(self) -> str:
        return Editors.STAR.value


class ProgressEditor(Editor):
    min: Optional[float] = None
    max: Optional[float] = None
    element_attributes: Optional[dict] = None

    @property
    def name(self) -> str:
        return Editors.PROGRESS.value


class ListEditor(Editor):
    values: Optional[list] = None
    values_lookup: Optional[bool] = True

    @property
    def name(self) -> str:
        return Editors.LIST.value
