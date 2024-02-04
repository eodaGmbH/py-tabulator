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
        members:
            - tabulator_midnight
            - tabulator_modern
            - tabulator_simple
            - tabulator_site


## Framework themes
