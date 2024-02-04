for base_theme in midnight modern simple site; do
  echo $base_theme
  # rm tabulator_${base_theme}.min.css
  # wget https://unpkg.com/tabulator-tables@5.5.4/dist/css/tabulator_${base_theme}.min.css
done

for framework_theme in bootstrap3 bootstrap4 bootstrap5 bulma materialize semanticui; do
  echo $framework_theme
  # rm tabulator_${framework_theme}.min.css
  # wget https://unpkg.com/tabulator-tables@5.5.4/dist/css/tabulator_${framework_theme}.min.css
done

# wget https://unpkg.com/tabulator-tables@5.5.4/dist/css/tabulator_midnight.min.css
# wget https://unpkg.com/tabulator-tables@5.5.4/dist/css/tabulator_simple.min.css
