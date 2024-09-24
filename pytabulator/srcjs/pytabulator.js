"use strict";
(() => {
  // built/utils.js
  function convertToDataFrame(data) {
    const res = {};
    if (data.length === 0) {
      return res;
    }
    const keys = Object.keys(data[0]);
    keys.forEach((key) => res[key] = data.map((item) => item[key]));
    return res;
  }

  // built/events.js
  function addEventListeners(tabulatorWidget) {
    const table = tabulatorWidget.getTable();
    const elementId = tabulatorWidget.getElementId();
    const bindingLang = tabulatorWidget.getBindingLang();
    console.log("binding lang", bindingLang);
    table.on("rowClick", function(e, row) {
      const inputName = `${elementId}_row_clicked`;
      console.log(inputName, row.getData());
      Shiny.onInputChange(inputName, row.getData());
    });
    table.on("rowClick", (e, row) => {
      const inputName = bindingLang === "r" ? `${elementId}_data:rtabulator.data` : `${elementId}_data`;
      const data = table.getSelectedRows().map((row2) => row2.getData());
      console.log(inputName, data);
      Shiny.onInputChange(inputName, { data: convertToDataFrame(data) });
    });
    table.on("cellEdited", function(cell) {
      const inputName = `${elementId}_cell_edited`;
      console.log(inputName, cell.getData());
      Shiny.onInputChange(inputName, cell.getData());
    });
    table.on("dataFiltered", function(filters, rows) {
      const inputName = bindingLang === "r" ? `${elementId}_data:rtabulator.data` : `${elementId}_data`;
      const data = rows.map((row) => row.getData());
      console.log(inputName, data);
      Shiny.onInputChange(inputName, { data: convertToDataFrame(data) });
    });
  }

  // built/widget.js
  function run_calls(tabulatorWidget, calls) {
    const table = tabulatorWidget.getTable();
    const elementId = tabulatorWidget.getElementId();
    const bindingLang = tabulatorWidget.getBindingLang();
    console.log("binding lang", bindingLang);
    calls.forEach(([method_name, options]) => {
      if (method_name === "getData") {
        const inputName = bindingLang === "r" ? `${elementId}_data:rtabulator.data` : `${elementId}_data`;
        console.log("custom call", inputName);
        Shiny.setInputValue(inputName, { data: convertToDataFrame(table.getData()) }, { priority: "event" });
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
      if (method_name === "getSheetData") {
        const inputName = bindingLang === "r" ? `${elementId}_sheet_data:rtabulator.sheet_data` : `${elementId}_sheet_data`;
        console.log("custom call", inputName);
        Shiny.setInputValue(inputName, { data: table.getSheetData() }, { priority: "event" });
        return;
      }
      console.log(method_name, options);
      table[method_name](...options);
    });
  }
  var TabulatorWidget = class {
    constructor(container, data, options, bindingOptions) {
      options.data = data;
      this._container = container;
      this._bindingOptions = bindingOptions;
      console.log("columns", options.columns);
      if (data !== null && options.columns == null) {
        options.autoColumns = true;
      }
      if (options.spreadsheet && options.spreadsheetData == null) {
        options.spreadsheetData = [];
      }
      this._table = new Tabulator(this._container, options);
      if (typeof Shiny === "object") {
        addEventListeners(this);
        this._addShinyMessageHandler();
      }
    }
    _addShinyMessageHandler() {
      const messageHandlerName = `tabulator-${this._container.id}`;
      Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
        console.log(payload);
        run_calls(this, payload.calls);
      });
    }
    getTable() {
      return this._table;
    }
    getElementId() {
      return this._container.id;
    }
    getBindingLang() {
      return this._bindingOptions.lang;
    }
  };

  // built/index-py.js
  var TabulatorOutputBinding = class extends Shiny.OutputBinding {
    find(scope) {
      return scope.find(".shiny-tabulator-output");
    }
    renderValue(el, payload) {
      console.log("payload", payload);
      const widget = new TabulatorWidget(el, payload.data, payload.options, payload.bindingOptions);
      const table = widget.getTable();
      table.on("tableBuilt", function() {
        if (payload.options.columnUpdates != null) {
          console.log("column updates", payload.options.columnUpdates);
        }
      });
    }
  };
  Shiny.outputBindings.register(new TabulatorOutputBinding(), "shiny-tabulator-output");
})();
