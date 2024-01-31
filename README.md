# py-tabulator

[Shiny for Python](https://shiny.posit.co/py/) bindings for [Tabulator JS](https://tabulator.info/)

## Installation

```bash
pip install git+https://github.com/eodaGmbH/py-tabulator
```

## Getting started

Using [Shiny Express](https://shiny.posit.co/blog/posts/shiny-express/):

```python
import pandas as pd
from pytabulator import TableOptions, render_data_frame
from shiny import render
from shiny.express import input, ui

ui.div("Click on row to print name", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@render_data_frame(table_options=TableOptions(height=500))
def tabulator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
```

```bash
shiny run docs/examples/getting_started/shiny_express.py
```
