from htmltools import HTMLDependency, Tag
from shiny import ui as shiny_ui

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
    return shiny_ui.div(sheetjs_dep)
