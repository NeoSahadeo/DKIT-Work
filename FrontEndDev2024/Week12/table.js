function generate_table(rows, columns) {
  const table = [];

  // Generate Columns
  for (let x = 0; x < columns; ++x) {
    table.push([]);
  }
  // Generate Rows
  table.forEach((value, index) => {
    for (let x = 0; x < rows; ++x) {
      table[index].push([]);
    }
  });

  // Fill in table
  table.forEach((columns, col_x) => {
    columns.forEach((row, row_x) => {
      table[col_x][row_x] = `${col_x}.${row_x}`;
    });
  });

  return table;
}

function generate_html(rows, columns) {
  const table = generate_table(rows, columns);

  const html_table = [];
  table.forEach((e) => {
    let table_row = "";
    e.forEach((x) => {
      table_row += `<td>${x}</td>`;
    });
    html_table.push(`<tr>${table_row}</tr>`);
  });
  return "<table>" + html_table.join() + "</table>";
}

export { generate_table, generate_html };
