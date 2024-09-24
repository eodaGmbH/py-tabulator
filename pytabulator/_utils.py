import json
import os

from pandas import DataFrame


def df_to_dict(df: DataFrame) -> dict:
    return json.loads(df.to_json(orient="table", index=False))


def set_theme(stylesheet):
    os.environ["PY_TABULATOR_STYLESHEET"] = stylesheet


def snake_to_camel_case(snake_str: str) -> str:
    return snake_str[0].lower() + snake_str.title()[1:].replace("_", "")


def as_camel_dict(snake_dict: dict) -> dict:
    return {snake_to_camel_case(k): v for (k, v) in snake_dict.items() if v is not None}


def as_camel_dict_recursive(snake_dict: dict) -> dict:
    camel_case_dict = {}
    for k, v in snake_dict.items():
        if v is not None:
            if isinstance(v, dict):
                camel_case_dict[snake_to_camel_case(k)] = as_camel_dict_recursive(v)
            else:
                camel_case_dict[snake_to_camel_case(k)] = v

    return camel_case_dict
