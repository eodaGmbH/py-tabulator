# py-tabulator: Tabulator for Python

[![Release](https://img.shields.io/github/v/release/eodaGmbH/py-tabulator)](https://img.shields.io/github/v/release/eodaGmbH/py-tabulator)
[![pypi](https://img.shields.io/pypi/v/pytabulator.svg)](https://pypi.python.org/pypi/pytabulator)
[![Build status](https://img.shields.io/github/actions/workflow/status/eodaGmbH/py-tabulator/pytest.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/eodaGmbH/py-tabulator/pytest.yml?branch=main)
[![License](https://img.shields.io/github/license/eodaGmbH/py-tabulator)](https://img.shields.io/github/license/eodaGmbH/py-tabulator)
[![License](https://img.shields.io/github/license/eodaGmbH/py-maplibregl)](https://img.shields.io/github/license/eodaGmbH/py-maplibregl)
[![Tabulator](https://img.shields.io/badge/Tabulator-v6.2.1-blue.svg)](https://github.com/olifolkerd/tabulator/releases/tag/6.2.1)

[Shiny for Python](https://shiny.posit.co/py/) bindings for [Tabulator JS](https://tabulator.info/)

## Features

* Filtering
* Grouping
* Editing
* Input validation
* History with undo and redo actions
* Pagination
* Layout
* Column formatters
* Column calculations
* Multi column headers
* Packaged themes
* Spreadsheets supporting multiple sheets
* Download data
* Freeze data

To learn more about pytabulator, see the documentation at https://eodagmbh.github.io/py-tabulator/.

Bindings for R are available at https://github.com/eodaGmbH/rtabulator.

## Installation

You can install the released version of pytabulator from [PyPI](https://pypi.org/) with:

```bash
pip install pytabulator
```

You can install the development version of pytabulator like so:

```bash
pip install git+https://github.com/eodaGmbH/py-tabulator
```

## Basic usage

[Shiny Express](https://shiny.posit.co/blog/posts/shiny-express/):

```python
import pandas as pd
from pytabulator import TableOptions, render_data_frame
from shiny import render
from shiny.express import input, ui

ui.div("Click on row to print name", style="padding: 10px;")


@render.code
async def txt():
    print(input.tabulator_row_clicked())
    return input.tabulator_row_clicked()["Name"]


@render_data_frame(table_options=TableOptions(height=500))
def tabulator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
```

[Shiny core](https://shiny.posit.co/py/):

```python
# uvicorn docs.examples.getting_started.shiny_core_basic:app

import pandas as pd
from pytabulator import TableOptions, Tabulator, output_tabulator, render_tabulator
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.output_text_verbatim("txt", placeholder=True),
    output_tabulator("tabulator"),
)


def server(input, output, session):
    @render_tabulator
    def tabulator():
        df = pd.read_csv(
            "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        )
        return Tabulator(df, table_options=TableOptions(height=311))

    @render.code
    async def txt():
        print(input.tabulator_row_clicked())
        return str(input.tabulator_row_clicked())


app = App(app_ui, server)
```

Run detailed example:

```bash
shiny run docs/examples/getting_started/shiny_express_all.py
```

![](docs/images/shiny-express-detailed-example.png)

## Development

### Python

```bash
poetry install

poetry run pytest
```

### JavaScript

```bash
npm install

npm run prettier

npm run build
```
