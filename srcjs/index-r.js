import { TabulatorWidget } from "./widget";

function tabulatorFactory(widgetElement, width, height) {
  let table = null;

  function renderValue(payload) {
    payload.data = HTMLWidgets.dataframeToD3(payload.data);
    console.log(payload);
    if (payload.options === null) {
      payload.options = {};
    }
    const widget = new TabulatorWidget(widgetElement, payload.data, payload.options);
    table = widget.getTable();
  }

  function resize(width, height) {
    // not implemented yet
  }

  return { renderValue, resize };
}

HTMLWidgets.widget({
  name: "rtabulator",
  type: "output",
  factory: tabulatorFactory,
});