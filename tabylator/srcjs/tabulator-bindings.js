(() => {
  // srcjs/index.js
  var TabulatorOutputBinding = class extends Shiny.OutputBinding {
    find(scope) {
      return scope.find(".shiny-tabulator-output");
    }
    renderValue(el, payload) {
      console.log("payload", payload);
      const columnsDef = payload.schema.fields.map((item) => {
        return {
          title: item.name,
          field: item.name,
          hozAlign: ["integer", "number"].includes(item.type) ? "right" : "left"
        };
      });
      const table = new Tabulator(el, {
        // height: 205,
        data: payload.data,
        layout: "fitColumns",
        columns: columnsDef
      });
    }
  };
  Shiny.outputBindings.register(
    new TabulatorOutputBinding(),
    "shiny-tabulator-output"
  );
})();
