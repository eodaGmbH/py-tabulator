(() => {
  // srcjs/index.js
  function createDownloadButton(el, table) {
    const container = document.createElement("div");
    container.id = "download-data";
    container.style.padding = "10px";
    const button = document.createElement("button");
    button.textContent = "Download";
    button.addEventListener("click", () => {
      table.download("csv", "data.csv");
    });
    container.appendChild(button);
    el.before(container);
  }
  var TabulatorOutputBinding = class extends Shiny.OutputBinding {
    find(scope) {
      return scope.find(".shiny-tabulator-output");
    }
    renderValue(el, payload) {
      console.log("payload", payload);
      const editable = false;
      const options = payload.options | {};
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
      const table = new Tabulator(
        el,
        Object.assign(
          {
            // height: 205,
            data: payload.data,
            layout: "fitColumns",
            columns: columnsDef
          },
          payload.options
        )
      );
      table.on("rowClick", function(e, row) {
        const inputName = `${el.id}_row`;
        console.log(inputName, row.getData());
        Shiny.onInputChange(inputName, row.getData());
      });
      if (payload.options.download) {
        createDownloadButton(el, table);
      }
    }
  };
  Shiny.outputBindings.register(
    new TabulatorOutputBinding(),
    "shiny-tabulator-output"
  );
})();
