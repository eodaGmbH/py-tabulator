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
