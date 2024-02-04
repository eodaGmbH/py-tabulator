from __future__ import annotations

from dataclasses import asdict, dataclass

from ._utils import snake_to_camel_case


@dataclass
class TableOptions(object):
    group_by: str | list = None
    header_visible: bool = True
    movable_rows: bool = False

    def to_dict(self):
        return asdict(
            self,
            dict_factory=lambda x: {
                snake_to_camel_case(k): v for (k, v) in x if v is not None
            },
        )
