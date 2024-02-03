import json
import os

from pandas import DataFrame


def df_to_dict(df: DataFrame) -> dict:
    return json.loads(df.to_json(orient="table", index=False))


def set_theme(stylesheet):
    os.environ["PY_TABULATOR_STYLESHEET"] = stylesheet
