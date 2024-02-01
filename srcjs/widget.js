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

export { run_calls };
