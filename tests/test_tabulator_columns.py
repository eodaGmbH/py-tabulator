from pytabulator import Tabulator


def test_tabulator_columns(persons):
    # print(persons)
    table = Tabulator(persons)

    print(table.columns)

    col = table._find_column("Name")
    print(col)

    table = table.update_column("Name", editor = True)
    print(table.columns)

    table = table.set_formatter("Age", "html", hozAlign="center")
    print(table.columns)
