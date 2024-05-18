import { run_calls, TabulatorWidget } from "./widget";

class TabulatorOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-tabulator-output");
  }

  renderValue(el, payload) {
    console.log("payload", payload);
    const widget = new TabulatorWidget(el, payload.data, payload.options);
    const table = widget.getTable();

    table.on("tableBuilt", function () {
      if (payload.options.columnUpdates != null) {
        console.log("column updates", payload.options.columnUpdates);
      }
    });

    // This must be inside table.on("tableBuilt")
    const messageHandlerName = `tabulator-${el.id}`;
    // console.log(messageHandlerName);
    Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
      console.log(payload);
      run_calls(el, table, payload.calls);
    });
  }
}

// Register the binding
Shiny.outputBindings.register(
  new TabulatorOutputBinding(),
  "shiny-tabulator-output",
);
