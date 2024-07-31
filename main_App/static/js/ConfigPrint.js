$(document).ready(function () {
    $('#dataTables-example').DataTable({
        responsive: true,
        buttons: [
            {
                extend: 'csv',
                text: 'Exportar a CSV',
                exportOptions: {
                    columns: ':not(:last-child)' // Excluir la última columna
                }
            },
            {
                extend: 'pdf',
                text: 'Exportar a PDF',
                exportOptions: {
                    columns: ':not(:last-child)' // Excluir la última columna
                }
            },
            {
                extend: 'print',
                exportOptions: { // Excluir la última columna
                    columns: ':not(:last-child)',
                }, 
            }
        ]
    }).buttons().container().appendTo('#example1_wrapper');
});


