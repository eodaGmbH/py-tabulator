from os.path import join
from pathlib import Path

from shiny.ui import head_content, include_css

midnight_theme_url = "https://unpkg.com/browse/tabulator-tables@5.5.4/dist/css/tabulator_midnight.min.css"


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
