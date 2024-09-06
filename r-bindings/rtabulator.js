(() => {
  // srcjs/events.js
  function addEventListeners(table, el) {
    table.on("rowClick", function(e, row) {
      const inputName = `${el.id}_row_clicked`;
      console.log(inputName, row.getData());
      Shiny.onInputChange(inputName, row.getData());
    });
    table.on("rowClick", (e, row) => {
      const inputName = `${el.id}_rows_selected`;
      const data = table.getSelectedRows().map((row2) => row2.getData());
      console.log(inputName, data);
      Shiny.onInputChange(inputName, data);
    });
    table.on("cellEdited", function(cell) {
      const inputName = `${el.id}_row_edited`;
      console.log(inputName, cell.getData());
      Shiny.onInputChange(inputName, cell.getData());
    });
    table.on("dataFiltered", function(filters, rows) {
      const inputName = `${el.id}_data_filtered`;
      const data = rows.map((row) => row.getData());
      console.log(inputName, data);
      Shiny.onInputChange(inputName, data);
    });
  }

  // srcjs/widget.js
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
  var TabulatorWidget = class {
    constructor(container, data, options) {
      options.data = data;
      this._container = container;
      console.log("columns", options.columns);
      if (options.columns == null)
        options.autoColumns = true;
      this._table = new Tabulator(this._container, options);
      if (typeof Shiny === "object") {
        addEventListeners(this._table, this._container);
        this._addShinyMessageHandler();
      }
    }
    _addShinyMessageHandler() {
      const messageHandlerName = `tabulator-${this._container.id}`;
      Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
        console.log(payload);
        run_calls(this._container, this._table, payload.calls);
      });
    }
    getTable() {
      return this._table;
    }
  };

  // srcjs/index-r.js
  function tabulatorFactory(widgetElement, width, height) {
    let table = null;
    function renderValue(payload) {
      console.log(payload);
      if (payload.options === null) {
        payload.options = {};
      }
      const widget = new TabulatorWidget(widgetElement, payload.data, payload.options);
      table = widget.getTable();
    }
    function resize(width2, height2) {
    }
    return { renderValue, resize };
  }
  HTMLWidgets.widget({
    name: "rtabulator",
    type: "output",
    factory: tabulatorFactory
  });
})();
