import { TabulatorWidget } from "./widget";

class TabulatorOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-tabulator-output");
  }

  renderValue(el, payload) {
    console.log("payload", payload);
    const widget = new TabulatorWidget(el, payload.data, payload.options);
    const table = widget.getTable();

    // Jus a test move to widget as well.
    table.on("tableBuilt", function () {
      if (payload.options.columnUpdates != null) {
        console.log("column updates", payload.options.columnUpdates);
      }
    });
  }
}

// Register the binding
Shiny.outputBindings.register(
  new TabulatorOutputBinding(),
  "shiny-tabulator-output",
);
