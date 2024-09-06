export default function addEventListeners(table, el) {
  // console.log("table", table);
  table.on("rowClick", function (e, row) {
    const inputName = `${el.id}_row_clicked`;
    console.log(inputName, row.getData());
    Shiny.onInputChange(inputName, row.getData());
  });

  table.on("rowClick", (e, row) => {
    const inputName = `${el.id}_rows_selected`;
    const data = table.getSelectedRows().map((row) => row.getData());
    console.log(inputName, data);
    Shiny.onInputChange(inputName, data);
  });

  table.on("cellEdited", function (cell) {
    const inputName = `${el.id}_row_edited`;
    console.log(inputName, cell.getData());
    Shiny.onInputChange(inputName, cell.getData());
  });

  table.on("dataFiltered", function (filters, rows) {
    const inputName = `${el.id}_data_filtered`;
    const data = rows.map((row) => row.getData());
    console.log(inputName, data);
    Shiny.onInputChange(inputName, data);
  });
}
