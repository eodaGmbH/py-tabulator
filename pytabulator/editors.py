from enum import Enum
from typing import Literal, Optional

from ._abstracts import MyBaseModel


class Editors(Enum):
    INPUT = "input"
    TEXTAREA = "textarea"
    NUMBER = "number"
    RANGE = "range"
    TICK_CROSS = "tickCross"
    STAR = "star"
    PROGRESS = "progress"
    LIST = "list"


class Editor(MyBaseModel):
    _name: str = ""

    @property
    def name(self) -> str:
        return self._name


class InputEditor(Editor):
    _name: str = Editors.INPUT.value

    search: Optional[bool] = None
    mask: Optional[str] = None
    select_contents: Optional[bool] = None
    element_attributes: Optional[dict] = None


class TextareaEditor(Editor):
    _name: str = Editors.TEXTAREA.value

    mask: Optional[str] = None
    select_contents: Optional[bool] = None
    vertical_navigation: Literal["hybrid", "editor", "table"] = None
    shift_enter_submit: Optional[bool] = None


class NumberEditor(Editor):
    _name: str = Editors.NUMBER.value

    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None
    element_attributes: Optional[dict] = None
    mask: Optional[str] = None
    select_contents: Optional[bool] = None
    vertical_navigation: Literal["editor", "table"] = None


class RangeEditor(Editor):
    _name: str = Editors.RANGE.value

    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None
    element_attributes: Optional[dict] = None


class TickCrossEditor(Editor):
    _name: str = Editors.TICK_CROSS.value

    true_value: Optional[str] = None
    false_value: Optional[str] = None
    element_attributes: Optional[dict] = None


class StarEditor(Editor):
    _name: str = Editors.STAR.value


class ProgressEditor(Editor):
    _name: str = Editors.PROGRESS.value

    min: Optional[float] = None
    max: Optional[float] = None
    element_attributes: Optional[dict] = None


class ListEditor(Editor):
    _name: str = Editors.LIST.value

    values: Optional[list] = None
    values_lookup: Optional[bool] = True
