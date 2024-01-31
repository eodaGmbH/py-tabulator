class TabulatorOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-tabulator-output");
  }

  renderValue(el, payload) {
    console.log("payload", payload);
    // el.style.background = "lightgreen";
    const editable =
      payload.options !== undefined ? payload.options.editor : false;

    // const editable = false;
    // const options = payload.options | {};
    let columnsDef = payload.schema.fields.map((item) => {
      return {
        title: item.name,
        field: item.name,
        hozAlign: ["integer", "number"].includes(item.type) ? "right" : "left",
        editor: editable,
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
          minWidth: 30,
        },
      ].concat(columnsDef);
    }

    if (payload.options.columns == null) payload.options.columns = columnsDef;

    if (payload.options.download) {
      payload.options.footerElement =
        "<button id='tabulator-download-csv' class='tabulator-page'>Download csv</button>";
    }

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

    table.on("rowClick", function (e, row) {
      const inputName = `${el.id}_row`;
      console.log(inputName, row.getData());
      Shiny.onInputChange(inputName, row.getData());
    });

    table.on("cellEdited", function (cell) {
      const inputName = `${el.id}_row_edited`;
      console.log(inputName, cell.getData());
      Shiny.onInputChange(inputName, cell.getData());
    });

    table.on("tableBuilt", function () {
      const downloadButton = document.getElementById("tabulator-download-csv");
      if (downloadButton) {
        downloadButton.addEventListener("click", () =>
          table.download("csv", "data.csv"),
        );
      }
    });

    const messageHandlerName = `tabulator-${el.id}`;
    // console.log(messageHandlerName);
    Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
      console.log(payload);
      payload.calls.forEach( ([name, options]) => {
        console.log(name, options);
        table[name](...options);
      });
      /*
      if (payload.call === "getData") {
        console.log("getData call");
        Shiny.onInputChange(`${el.id}_get_data`, table.getData());
      } else if (payload.call === "triggerDownload") {
        console.log("Download triggered");
        table.download("csv", "test-data.csv");
      }
     */
    });
  }
}

// Register the binding
Shiny.outputBindings.register(
  new TabulatorOutputBinding(),
  "shiny-tabulator-output",
);
