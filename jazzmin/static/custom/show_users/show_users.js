fetch('get_users')
  .then(response => response.json())
  .then(data => {
    var table = new Tabulator("#tabla", {
      data: data['users'],
      layout: "fitColumns",
      pagination: "local",
      paginationSize: 50,
      paginationSizeSelector: [50, 100, 150],
      columns: [
        {title: "Usuario num.", field: "employeeNo"},
        {title: "Nombre", field: "name"},
        {title: "Género", field: "gender"},
        {title: "Inicio", field: "Valid.beginTime"},
        {title: "Final", field: "Valid.endTime"},
        {title: "Tipo de usuario", field: "userType"}
      ],
      initialSort: [
        {column: "employeeNo", dir: "asc"}
      ],
      rowFormatter: function(row){
        var index = row.getPosition(true);
        if(index % 2 === 0){
          row.getElement().classList.add("even");
        }else{
          row.getElement().classList.add("odd");
        }
      },
      headerFilter: true
    });
  })
  .catch(error => console.error(error));
