import json

from pandas import DataFrame


class TableOptions(object):
    pass


class Tabulator(object):
    def __init__(self, df: DataFrame, table_option: dict = None) -> None:
        self.df = df
        self.table_option = table_option

    def to_dict(self) -> dict:
        return {
            "df": json.loads(self.df.to_json(orient="table", index=False)),
            "options": self.table_option,
        }
