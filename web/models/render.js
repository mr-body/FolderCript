async function listHistory(value) {
  // Chame a função history() do backend para obter os dados
  let dados = await eel.history(value)();

  // Limpe o conteúdo existente da tabela
  $("#listaHistoric").empty();

  // Loop através dos dados recuperados e adicione linhas à tabela
  for (let dado of dados) {
      // Create a new table row element
      let row = $("<tr>");

      // Append table data elements to the row with data from the retrieved dictionary
      row.append(`<td hidden>${dado.id}</td>`); // Access "id" attribute of the dictionary
      row.append(`<td>${dado.date}</td>`); // Access "date" attribute of the dictionary
      row.append(`<td>${dado.folder_path}</td>`); // Access "folder_path" attribute of the dictionary
      row.append(`<td hidden>${dado.password}</td>`); // Access "password" attribute of the dictionary
      row.append(`<td>${dado.description}</td>`); // Access "description" attribute of the dictionary
      row.append(`<td>Remove</td>`);

      // Append the row to the table
      $("#listaHistoric").append(row);
  }
}
