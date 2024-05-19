import addEventListeners from "./events";

function run_calls(el, table, calls) {
  calls.forEach(([method_name, options]) => {
    if (method_name === "getData") {
      console.log("custom call");
      Shiny.onInputChange(`${el.id}_data`, table.getData());
      return;
    }

    if (method_name === "deleteSelectedRows") {
      console.log("custom call");
      const rows = table.getSelectedRows();
      rows.forEach((row) => {
        console.log(row.getIndex());
        table.deleteRow(row.getIndex());
      });
      return;
    }

    console.log(method_name, options);
    table[method_name](...options);
  });
}

class TabulatorWidget {
  constructor(container, data, options) {
    options.data = data;
    this._container = container;
    console.log("columns", options.columns);
    if (options.columns == null) options.autoColumns = true;
    this._table = new Tabulator(this._container, options);
    if (typeof Shiny === "object") {
      addEventListeners(this._table, this._container);
      this._addShinyMessageHandler();
    }
  }

  _addShinyMessageHandler() {
    // This must be inside table.on("tableBuilt")
    const messageHandlerName = `tabulator-${this._container.id}`;
    Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
      console.log(payload);
      run_calls(this._container, this._table, payload.calls);
    });
  }

  getTable() {
    return this._table;
  }
}

export { run_calls, TabulatorWidget };
