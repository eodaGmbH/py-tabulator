import json

from pandas import DataFrame


def df_to_dict(df: DataFrame) -> dict:
    return json.loads(df.to_json(orient="table", index=False))
