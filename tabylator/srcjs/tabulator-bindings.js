(() => {
  // srcjs/index.js
  var TabulatorOutputBinding = class extends Shiny.OutputBinding {
    find(scope) {
      return scope.find(".shiny-tabulator-output");
    }
    renderValue(el, payload) {
      console.log("payload", payload);
      const editable = payload.options !== void 0 ? payload.options.editor : false;
      const columnsDef = payload.schema.fields.map((item) => {
        return {
          title: item.name,
          field: item.name,
          hozAlign: ["integer", "number"].includes(item.type) ? "right" : "left",
          editor: editable
        };
      });
      const table = new Tabulator(el, {
        // height: 205,
        data: payload.data,
        layout: "fitColumns",
        columns: columnsDef
      });
      table.on("rowClick", function(e, row) {
        const inputName = `${el.id}_row`;
        console.log(inputName, row.getData());
        Shiny.onInputChange(inputName, row.getData());
      });
    }
  };
  Shiny.outputBindings.register(
    new TabulatorOutputBinding(),
    "shiny-tabulator-output"
  );
})();
