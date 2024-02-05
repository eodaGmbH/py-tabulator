from __future__ import annotations

import os

from htmltools import HTMLDependency, Tag
from shiny import ui
from shiny.module import resolve_id

# <script type="text/javascript" src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>
# https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.mini.min.js
XLSX_VERSION = "0.20.1"

sheetjs_dep = HTMLDependency(
    name="sheetjs",
    version=XLSX_VERSION,
    source={"href": f"https://cdn.sheetjs.com/xlsx-{XLSX_VERSION}/package/dist/"},
    script={"src": "xlsx.mini.min.js", "type": "module"},
)


def use_sheetjs() -> Tag:
    return ui.div(sheetjs_dep)


def tabulator_dep() -> HTMLDependency:
    return HTMLDependency(
        "tabulator",
        "5.5.4",
        source={"package": "pytabulator", "subdir": "srcjs"},
        script={"src": "tabulator.min.js", "type": "module"},
        stylesheet={"href": os.getenv("PY_TABULATOR_STYLESHEET", "tabulator.min.css")},
        all_files=False,
    )


tabulator_bindings_dep = HTMLDependency(
    "tabulatorbindings",
    "0.1.0",
    source={"package": "pytabulator", "subdir": "srcjs"},
    script={"src": "tabulator-bindings.js", "type": "module"},
    all_files=False,
)


def output_tabulator(id: str):
    """Create an output container for a `Tabulator` table

    Args:
        id (str): An output id of a `Tabulator` table.
    """
    return ui.div(
        tabulator_dep(),
        tabulator_bindings_dep,
        id=resolve_id(id),
        class_="shiny-tabulator-output",
    )
