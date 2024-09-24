from pydantic import BaseModel

from typing import Optional

from ._utils import as_camel_dict_recursive
from enum import Enum


class Editors(Enum):
    NUMBER = "number"
    INPUT = "input"
    STAR = "star"
    PROGRESS = "progress"


class Editor(BaseModel):
    @property
    def name(self) -> str:
        return ""

    def to_dict(self) -> dict:
        return as_camel_dict_recursive(self.model_dump(exclude_none=True))


class NumberEditor(Editor):
    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None

    @property
    def name(self) -> str:
        return Editors.NUMBER.value


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
