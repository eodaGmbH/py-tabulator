import pandas as pd
from shiny.express import ui
from tabylator import render_tabular


@render_tabular
def tabylator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
