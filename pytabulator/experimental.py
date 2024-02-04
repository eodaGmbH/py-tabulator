import os
from os.path import join
from pathlib import Path

from htmltools import HTMLDependency, Tag
from shiny import ui
from shiny.ui import head_content, include_css

os.environ["PY_TABULATOR_STYLESHEET"] = ""

external_dep = ui.div(
    HTMLDependency(
        name="tabulator-theme",
        version="5.5.4",
        source={"href": "https://unpkg.com/tabulator-tables@5.5.4/dist/"},
        stylesheet={"href": "css/tabulator_bootstrap5.min.css"},
    )
)

midnight_theme_url = "https://unpkg.com/browse/tabulator-tables@5.5.4/dist/css/tabulator_midnight.min.css"

tag = Tag(
    "link",
    {
        "href": "https://unpkg.com/tabulator-tables@5.5.4/dist/css/tabulator_midnight.min.css",
        "rel": "stylesheet",
        "type": "text/css",
    },
)


def get_theme_css(name):
    return head_content(
        include_css(
            join(Path(__file__).parent, "srcjs", f"tabulator_{name}.min.css"),
            method="link",
        )
    )


def simple_theme():
    return get_theme_css("simple")


def midnight_theme():
    return get_theme_css("midnight")


# <script type="text/javascript" src="https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"></script>
# https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.mini.min.js
def use_xlsx() -> HTMLDependency:
    pass


# <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.20/jspdf.plugin.autotable.min.js"></script>
def use_jspdf() -> HTMLDependency:
    pass
