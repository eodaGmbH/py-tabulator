import { run_calls, TabulatorWidget } from "./widget";

class TabulatorOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-tabulator-output");
  }

  renderValue(el, payload) {
    console.log("payload", payload);
    const widget = new TabulatorWidget(el, payload.data, payload.options);
    const table = widget.getTable();
    // el.style.background = "lightgreen";
    /*
    const editable =
      payload.options !== undefined ? payload.options.editor : false;
    */

    // const editable = false;
    // const options = payload.options | {};
    /*
    let columnsDef = payload.schema.fields.map((item) => {
      return {
        title: item.name,
        field: item.name,
        hozAlign: ["integer", "number"].includes(item.type) ? "right" : "left",
        editor: editable,
      };
    });
    */


    /*
    if (payload.options.movableRows === true) {
      columnsDef = [
        {
          rowHandle: true,
          formatter: "handle",
          headerSort: false,
          frozen: true,
          width: 30,
          minWidth: 30,
        },
      ].concat(columnsDef);
    }
    */
    //if (payload.options.columns == null) payload.options.columns = columnsDef;

    /*
    if (payload.options.download) {
      payload.options.footerElement =
        "<button id='tabulator-download-csv' class='tabulator-page'>Download csv</button>";
    }
    */
    /*
    const table = new Tabulator(
      el,
      Object.assign(
        {
          // height: 205,
          data: payload.data,
          layout: "fitColumns",
          // columns: columnsDef,
        },
        payload.options,
      ),
    );


     */
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
      // console.log("filters", filters);
      const data = rows.map((row) => row.getData());
      console.log(data);
      Shiny.onInputChange(`${el.id}_data_filtered`, data);
    });

    table.on("tableBuilt", function () {
      if (payload.options.columnUpdates != null) {
        console.log("column updates", payload.options.columnUpdates);
      }
      // TODO: DEPRECATED!?
      const downloadButton = document.getElementById("tabulator-download-csv");
      if (downloadButton) {
        downloadButton.addEventListener("click", () =>
          table.download("csv", "data.csv"),
        );
      }
    });

    // This must be inside table.on("tableBuilt")
    const messageHandlerName = `tabulator-${el.id}`;
    // console.log(messageHandlerName);
    Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
      console.log(payload);
      run_calls(el, table, payload.calls);
      /*
      payload.calls.forEach(([name, options]) => {
        if (name === "getData") {
          console.log("custom call");
          Shiny.onInputChange(`${el.id}_data`, table.getData());
          return;
        }

        if (name === "deleteSelectedRows") {
          console.log("custom call");
          const rows = table.getSelectedRows();
          rows.forEach((row) => {
            console.log(row.getIndex());
            table.deleteRow(row.getIndex());
          });
          return;
        }

        console.log(name, options);
        table[name](...options);
      });
      */
    });
  }
}

// Register the binding
Shiny.outputBindings.register(
  new TabulatorOutputBinding(),
  "shiny-tabulator-output",
);
