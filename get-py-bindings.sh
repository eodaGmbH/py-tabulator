#!/bin/sh
branch=${1:-dev}
# curl -O https://raw.githubusercontent.com/eodaGmbH/tabulator-bindings/${branch}/r-bindings/rtabulator.js
curl -o pytabulator/srcjs/pytabulator.js https://raw.githubusercontent.com/eodaGmbH/tabulator-bindings/refs/heads/feature/typescript/py-bindings/pytabulator.js
