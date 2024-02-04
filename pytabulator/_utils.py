import json
import os

from pandas import DataFrame


def df_to_dict(df: DataFrame) -> dict:
    return json.loads(df.to_json(orient="table", index=False))


def set_theme(stylesheet):
    os.environ["PY_TABULATOR_STYLESHEET"] = stylesheet


def snake_to_camel_case(snake_str: str) -> str:
    return snake_str[0].lower() + snake_str.title()[1:].replace("_", "")

    # return "".join(
    #    [item if not i else item.title() for i, item in enumerate(snake_str.split("_"))]
    # )
