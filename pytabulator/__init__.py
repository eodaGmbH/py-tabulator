from importlib.metadata import PackageNotFoundError, version

try:
    pydantic_version = [int(i) for i in version("pydantic").split(".")]
    if pydantic_version[0] == 1:
        raise PackageNotFoundError()

    from ._table_options_pydantic import TableOptionsPydantic as TableOptions

    # print("pydantic")
except PackageNotFoundError:
    from ._table_options_dc import TableOptionsDC as TableOptions

    # print("dataclass")

# from ._table_options_pydantic import TableOptionsPydantic as TableOptions
from .shiny_bindings import output_tabulator, render_data_frame, render_tabulator
from .tabulator import Tabulator
from .tabulator_context import TabulatorContext

# __all__ = []
