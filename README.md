# py-tabulator

Shiny bindings for tabulator JS

## Installation

```bash
pip install git+https://github.com/eodaGmbH/py-tabulator
```

## Getting started

Shiny Express:

```python
import pandas as pd
from shiny import render
from shiny.express import input, ui
from pytabulator import render_data_frame_


@render.code
async def txt():
    print(input.tabulator_row())
    return input.tabulator_row()["Name"]


@render_data_frame_
def tabulator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
```

```bash
shiny run docs/examples/getting_started/shiny_express.py
```
