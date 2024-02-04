from ._utils import set_theme


def tabulator_simple():
    """Simple

    A plain, simplistic layout showing only basic grid lines.
    """
    set_theme("tabulator_simple.min.css")


def tabulator_midnight():
    """Midnight

    A dark, stylish layout using simple shades of grey.
    """
    set_theme("tabulator_midnight.min.css")


def tabulator_modern():
    """Modern

    A neat, stylish layout using one primary color.
    """
    set_theme("tabulator_modern.min.css")


def tabulator_site():
    """Site

    The theme used for tables on the docs website of Tabulator JS."""
    set_theme("tabulator_site.min.css")
