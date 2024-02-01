(() => {
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

  // srcjs/index.js
  var TabulatorOutputBinding = class extends Shiny.OutputBinding {
    find(scope) {
      return scope.find(".shiny-tabulator-output");
    }
    renderValue(el, payload) {
      console.log("payload", payload);
      const editable = payload.options !== void 0 ? payload.options.editor : false;
      let columnsDef = payload.schema.fields.map((item) => {
        return {
          title: item.name,
          field: item.name,
          hozAlign: ["integer", "number"].includes(item.type) ? "right" : "left",
          editor: editable
        };
      });
      if (payload.options.movableRows === true) {
        columnsDef = [
          {
            rowHandle: true,
            formatter: "handle",
            headerSort: false,
            frozen: true,
            width: 30,
            minWidth: 30
          }
        ].concat(columnsDef);
      }
      if (payload.options.columns == null)
        payload.options.columns = columnsDef;
      if (payload.options.download) {
        payload.options.footerElement = "<button id='tabulator-download-csv' class='tabulator-page'>Download csv</button>";
      }
      const table = new Tabulator(
        el,
        Object.assign(
          {
            // height: 205,
            data: payload.data,
            layout: "fitColumns"
            // columns: columnsDef,
          },
          payload.options
        )
      );
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
        const data = rows.map((row) => row.getData());
        console.log(data);
        Shiny.onInputChange(`${el.id}_data_filtered`, data);
      });
      table.on("tableBuilt", function() {
        const downloadButton = document.getElementById("tabulator-download-csv");
        if (downloadButton) {
          downloadButton.addEventListener(
            "click",
            () => table.download("csv", "data.csv")
          );
        }
      });
      const messageHandlerName = `tabulator-${el.id}`;
      Shiny.addCustomMessageHandler(messageHandlerName, (payload2) => {
        console.log(payload2);
        run_calls(el, table, payload2.calls);
      });
    }
  };
  Shiny.outputBindings.register(
    new TabulatorOutputBinding(),
    "shiny-tabulator-output"
  );
})();
