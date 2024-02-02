from pandas import DataFrame


def create_columns(
    df: DataFrame, default_filter: bool = False, default_editor: bool = False
) -> list:
    # (hozAlign, headerFilter, editor)
    setup = [
        (
            ("right", "number", "number")
            if dtype in [int, float]
            else ("left", "input", "input")
        )
        for dtype in df.dtypes.tolist()
    ]
    columns = [
        {"title": column, "field": column, "hozAlign": setup[i][0]}
        for i, column in enumerate(df.columns)
    ]

    if default_filter:
        for i, column in enumerate(columns):
            column["headerFilter"] = setup[i][1]

    if default_editor:
        for i, column in enumerate(columns):
            column["editor"] = setup[i][2]

    return columns
