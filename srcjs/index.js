import { run_calls, TabulatorWidget } from "./widget";

class TabulatorOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-tabulator-output");
  }

  renderValue(el, payload) {
    console.log("payload", payload);
    const widget = new TabulatorWidget(el, payload.data, payload.options);
    const table = widget.getTable();

    /*
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
    */
    table.on("tableBuilt", function () {
      if (payload.options.columnUpdates != null) {
        console.log("column updates", payload.options.columnUpdates);
      }
    });

    // This must be inside table.on("tableBuilt")
    const messageHandlerName = `tabulator-${el.id}`;
    // console.log(messageHandlerName);
    Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
      console.log(payload);
      run_calls(el, table, payload.calls);
    });
  }
}

// Register the binding
Shiny.outputBindings.register(
  new TabulatorOutputBinding(),
  "shiny-tabulator-output",
);
