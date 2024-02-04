# Themes

See [Tabulator JS Themes](https://tabulator.info/docs/5.5/theme) for details.

Pytabulator comes with a number of pre-packaged theme stylesheets to make styling your table really simple.
To use one of these instead of the default theme simply include the matching function before you render the table:

```python
from pytabulator import theme

theme.tabulator_midnight()
```

## Standard themes

::: pytabulator.theme
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false
        show_symbol_type_toc: true
        members:
            - tabulator_midnight
            - tabulator_modern
            - tabulator_simple
            - tabulator_site


## Framework themes

::: pytabulator.theme
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false
        show_symbol_type_toc: true
        members:
            - tabulator_bootstrap3
            - tabulator_bootstrap4
            - tabulator_bootstrap5
            - tabulator_semanticui
            - tabulator_bulma
            - tabulator_materialize
