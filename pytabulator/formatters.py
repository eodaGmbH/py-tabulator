from enum import Enum
from pydantic import BaseModel
from typing import Optional
from ._utils import as_camel_dict_recursive

class Formatters(Enum):
    STAR = "star"
    PROGRESS = "progress"
    TICK_CROSS = "tickCross"

class Formatter(BaseModel):
    def to_dict(self) -> dict:
        return as_camel_dict_recursive(self.model_dump(exclude_none=True))

    @property
    def name(self) -> str:
        return ""

class StarFormatter(Formatter):
    stars: Optional[int] = None

    @property
    def name(self) -> str:
        return Formatters.STAR.value
