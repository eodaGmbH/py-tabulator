from pydantic import BaseModel

from ._utils import as_camel_dict_recursive


class MyBaseModel(BaseModel):
    def to_dict(self) -> dict:
        return as_camel_dict_recursive(self.model_dump(exclude_none=True))
