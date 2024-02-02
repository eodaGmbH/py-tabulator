from pandas import DataFrame


def create_columns(
    df: DataFrame,
    default_filter: bool = False,
    default_editor: bool = False,
    updates: dict = {},
) -> list:
    """Create columns configuration from a data frame

    Args:
        df (DataFrame): The data frame to create columns from.
        default_filter (bool): Whether to add a default header filter to each column.
        default_editor (bool): Whether to add a default editor to each column.
        updates (dict): Dictionary of updates that overwrite the default settings or add additional settings the columns.
    """
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

    for key in updates:
        for column in columns:
            if column["field"] == key:
                column.update(updates[key])

    return columns


# {Age: {}}
