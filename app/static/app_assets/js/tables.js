$(document).ready(function () {
    
    // TABLES
    var restoTable = $('#orders_table_index').DataTable({

        pageLength: 5,
        "iDisplayLength": 5,
        "order": [ 0, 'desc' ],
        "responsive": true,
        "dom": '<"top"Bi>rt<"bottom"><"clear">',
        //"paging":false,
        "info":false,
        
        "language": {
            "lengthMenu": "Mostrar _MENU_ ordens por página",
            "zeroRecords": "Nada Encontrado",
            //"info": "Mostrando _PAGE_ de _PAGES_ páginas",
            "info": "Mostrando <b>_START_</b> a  <b>_END_</b> de <b>_TOTAL_</b> registros",
            "infoEmpty": "Nenhum registro encontrado",
            "infoFiltered": "(Filtrado do total de _MAX_ registros)",
            "search": "Procurar:",
            "paginate": {
                "first": "Primeira",
                "last": "Última",
                "next": "Próxima",
                "previous": "Prévia"
            },
           
        },
        columnDefs: [{
            targets: [0,8],
            width: "1%",
            },
            {
            targets: [8],
            orderable: false,
            },
            
            
           ],
        
        buttons: [
            {
                extend: 'csvHtml5',
                text: '<i class="fa fa-file"></i> CSV',
                titleAttr: 'Download CSV',
                className: 'btn btn-sm btn-info',
                exportOptions: {
                    columns: ':visible:not(:last-child)',
                    //columns: ':visible',
                    rows: ':visible' 
                },
            },
            {
                extend: 'pdfHtml5',
                text: '<i class="fa fa-file-pdf"></i> PDF',
                titleAttr: 'Download PDF',
                className: 'btn btn-sm btn-primary',
                exportOptions: {
                    columns: ':visible:not(:last-child)',
                    //columns: ':visible',
                    rows: ':visible' 
                },
            },
            {
                extend: 'excel',
                text: '<i class="fa fa-file-excel"></i> Excel',
                titleAttr: 'Excel',
                className: 'btn btn-sm btn-tertiary',
                exportOptions: {
                    columns: ':visible:not(:last-child)',
                    //columns: ':visible',
                    rows: ':visible' 
                },
            },
            {
                extend: 'colvis',
                text: '<i class="fa fa-columns"></i> Colvis',
                titleAttr: 'Colvis',
                className: 'btn btn-sm btn-primary',
                
            },  
        ], 

        initComplete: function() {
       	 var $buttons = $('.dt-buttons').hide();
         $('#exportLinkapps').on('change', function() {
            var btnClass = $(this).find(":selected")[0].id 
               ? '.buttons-' + $(this).find(":selected")[0].id 
               : null;
            if (btnClass) $buttons.find(btnClass).click(); 
         })
       }, 
    })
    
    $('#search_order').keyup(function(){
        restoTable.search($(this).val()).draw() ;
    })
    
    $('#entries_order').change(function(){
        restoTable.page.len($(this).val()).draw();
    })

    $('#resto_table5').show();
        restoTable.columns.adjust().draw();


    //Table Obras
    var restoTable = $('#orders_table').DataTable({

        //order: [[0, 'desc']],
        "order": [ 0, 'desc' ],
        "responsive": true,
        "dom": '<"top"Bi>rt<"bottom"p><"clear">',
        
        "language": {
            "lengthMenu": "Mostrar _MENU_ ordens por página",
            "zeroRecords": "Nada Encontrado",
            //"info": "Mostrando _PAGE_ de _PAGES_ páginas",
            "info": "Mostrando <b>_START_</b> a  <b>_END_</b> de <b>_TOTAL_</b> registros",
            "infoEmpty": "Nenhum registro encontrado",
            "infoFiltered": "(Filtrado do total de _MAX_ registros)",
            "search": "Procurar:",
            "paginate": {
                "first": "Primeira",
                "last": "Última",
                "next": "Próxima",
                "previous": "Prévia"
            },
            
        },
        columnDefs: [{
            targets: [0,9],
            width: "1%",
            },
            {
            targets: [9],
            orderable: false,
            },
            {
            targets: [1,2,3,4,5,6,7],
            width: "11%",
            },
            
           ],
        "iDisplayLength": 12,
        buttons: [
            {
                extend: 'csvHtml5',
                text: '<i class="fa fa-file"></i> CSV',
                titleAttr: 'Download CSV',
                className: 'btn btn-sm btn-info',
                exportOptions: {
                    columns: ':visible:not(:last-child)',
                    //columns: ':visible',
                    rows: ':visible' 
                },
            },
            {
                extend: 'pdfHtml5',
                text: '<i class="fa fa-file-pdf"></i> PDF',
                titleAttr: 'Download PDF',
                className: 'btn btn-sm btn-primary',
                exportOptions: {
                    columns: ':visible:not(:last-child)',
                    //columns: ':visible',
                    rows: ':visible' 
                },
            },
            {
                extend: 'excel',
                text: '<i class="fa fa-file-excel"></i> Excel',
                titleAttr: 'Excel',
                className: 'btn btn-sm btn-tertiary',
                exportOptions: {
                    columns: ':visible:not(:last-child)',
                    //columns: ':visible',
                    rows: ':visible' 
                },
            },
            {
                extend: 'colvis',
                text: '<i class="fa fa-columns"></i> Colvis',
                titleAttr: 'Colvis',
                className: 'btn btn-sm btn-primary',
                
            },  
        ], 

        initComplete: function() {
       	 var $buttons = $('.dt-buttons').hide();
         $('#exportlink_orders').on('change', function() {
            var btnClass = $(this).find(":selected")[0].id 
               ? '.buttons-' + $(this).find(":selected")[0].id 
               : null;
            if (btnClass) $buttons.find(btnClass).click(); 
         })
       }, 
    })
    
    $('#search_order').keyup(function(){
        restoTable.search($(this).val()).draw() ;
    })
    
    $('#entries_order').change(function(){
        restoTable.page.len($(this).val()).draw();
    })

    $('#resto_table').show();
        restoTable.columns.adjust().draw();


        var restoTable = $('#orders_table_user').DataTable({

            //order: [[0, 'desc']],
            "order": [ 0, 'desc' ],
            "responsive": true,
            "dom": '<"top"Bi>rt<"bottom"p><"clear">',
            
            "language": {
                "lengthMenu": "Mostrar _MENU_ ordens por página",
                "zeroRecords": "Nada Encontrado",
                //"info": "Mostrando _PAGE_ de _PAGES_ páginas",
                "info": "Mostrando <b>_START_</b> a  <b>_END_</b> de <b>_TOTAL_</b> registros",
                "infoEmpty": "Nenhum registro encontrado",
                "infoFiltered": "(Filtrado do total de _MAX_ registros)",
                "search": "Procurar:",
                "paginate": {
                    "first": "Primeira",
                    "last": "Última",
                    "next": "Próxima",
                    "previous": "Prévia"
                },
                
            },
            columnDefs: [{
                targets: [0,8],
                width: "1%",
                },
                {
                targets: [8],
                orderable: false,
                },
                {
                targets: [1,2,3,4,5,6,7],
                width: "11%",
                },
                
               ],
            "iDisplayLength": 12,
            buttons: [
                {
                    extend: 'csvHtml5',
                    text: '<i class="fa fa-file"></i> CSV',
                    titleAttr: 'Download CSV',
                    className: 'btn btn-sm btn-info',
                    exportOptions: {
                        columns: ':visible:not(:last-child)',
                        //columns: ':visible',
                        rows: ':visible' 
                    },
                },
                {
                    extend: 'pdfHtml5',
                    text: '<i class="fa fa-file-pdf"></i> PDF',
                    titleAttr: 'Download PDF',
                    className: 'btn btn-sm btn-primary',
                    exportOptions: {
                        columns: ':visible:not(:last-child)',
                        //columns: ':visible',
                        rows: ':visible' 
                    },
                },
                {
                    extend: 'excel',
                    text: '<i class="fa fa-file-excel"></i> Excel',
                    titleAttr: 'Excel',
                    className: 'btn btn-sm btn-tertiary',
                    exportOptions: {
                        columns: ':visible:not(:last-child)',
                        //columns: ':visible',
                        rows: ':visible' 
                    },
                },
                {
                    extend: 'colvis',
                    text: '<i class="fa fa-columns"></i> Colvis',
                    titleAttr: 'Colvis',
                    className: 'btn btn-sm btn-primary',
                    
                },  
            ], 
    
            initComplete: function() {
                var $buttons = $('.dt-buttons').hide();
             $('#exportlink_orders').on('change', function() {
                var btnClass = $(this).find(":selected")[0].id 
                   ? '.buttons-' + $(this).find(":selected")[0].id 
                   : null;
                if (btnClass) $buttons.find(btnClass).click(); 
             })
           }, 
        })
        
        $('#search_order').keyup(function(){
            restoTable.search($(this).val()).draw() ;
        })
        
        $('#entries_order').change(function(){
            restoTable.page.len($(this).val()).draw();
        })
    
        $('#resto_table').show();
            restoTable.columns.adjust().draw();


    // Table APP 

    var appTable = $('#app_table').DataTable({
        order: [[0, 'desc']],
        "responsive": true,
        "dom": '<"top"Bi>rt<"bottom"p><"clear">',
        
        "language": {
            "lengthMenu": "Mostrar _MENU_ ordens por página",
            "zeroRecords": "Nada Encontrado",
            //"info": "Mostrando _PAGE_ de _PAGES_ páginas",
            "info": "Mostrando <b>_START_</b> a  <b>_END_</b> de <b>_TOTAL_</b> registros",
            "infoEmpty": "Nenhum registro encontrado",
            "infoFiltered": "(Filtrado do total de _MAX_ registros)",
            "search": "Procurar:",
            "paginate": {
                "first": "Primeira",
                "last": "Última",
                "next": "Próxima",
                "previous": "Prévia"
            },
            
        },
        columnDefs: [{
            targets: [0,5],
            width: "1%",
            },
            {
            targets: [5],
            orderable: false,
            },
            ],
            "pageLength":12,
            buttons: [
                {
                    extend: 'csvHtml5',
                    text: '<i class="fa fa-file"></i> CSV',
                    titleAttr: 'Download CSV',
                    className: 'btn btn-sm btn-info',
                    exportOptions: {
                        columns: ':visible:not(:last-child)',
                        //columns: ':visible',
                        rows: ':visible' 
                    },
                },
                {
                    extend: 'pdfHtml5',
                    text: '<i class="fa fa-file-pdf"></i> PDF',
                    titleAttr: 'Download PDF',
                    className: 'btn btn-sm btn-primary',
                    exportOptions: {
                        columns: ':visible:not(:last-child)',
                        //columns: ':visible',
                        rows: ':visible' 
                    },
                },
                {
                    extend: 'excel',
                    text: '<i class="fa fa-file-excel"></i> Excel',
                    titleAttr: 'Excel',
                    className: 'btn btn-sm btn-tertiary',
                    exportOptions: {
                        columns: ':visible:not(:last-child)',
                        //columns: ':visible',
                        rows: ':visible' 
                    },
                },
                {
                    extend: 'colvis',
                    text: '<i class="fa fa-columns"></i> Colvis',
                    titleAttr: 'Colvis',
                    className: 'btn btn-sm btn-primary',
                    
                },  
            ], 
        initComplete: function() {
            var $buttons = $('.dt-buttons').hide();
            $('#exportLinkapps').on('change', function() {
            var btnClass = $(this).find(":selected")[0].id 
                ? '.buttons-' + $(this).find(":selected")[0].id 
                : null;
            if (btnClass) $buttons.find(btnClass).click(); 
            })
        },
        
    })
    
    $('#searchapp').keyup(function(){
        appTable.search($(this).val()).draw() ;
    })
    
    $('#entriesapp').change(function(){
        appTable.page.len($(this).val()).draw();
    })

    $('#app_table').show();
        appTable.columns.adjust().draw();


        var appTable = $('#app_table_user').DataTable({
            order: [[0, 'desc']],
            "responsive": true,
            "dom": '<"top"Bi>rt<"bottom"p><"clear">',
            
            "language": {
                "lengthMenu": "Mostrar _MENU_ ordens por página",
                "zeroRecords": "Nada Encontrado",
                //"info": "Mostrando _PAGE_ de _PAGES_ páginas",
                "info": "Mostrando <b>_START_</b> a  <b>_END_</b> de <b>_TOTAL_</b> registros",
                "infoEmpty": "Nenhum registro encontrado",
                "infoFiltered": "(Filtrado do total de _MAX_ registros)",
                "search": "Procurar:",
                "paginate": {
                    "first": "Primeira",
                    "last": "Última",
                    "next": "Próxima",
                    "previous": "Prévia"
                },
                
            },
            columnDefs: [{
                targets: [0,4],
                width: "1%",
                },
                {
                targets: [4],
                orderable: false,
                },
                ],
                "pageLength":12,
                buttons: [
                    {
                        extend: 'csvHtml5',
                        text: '<i class="fa fa-file"></i> CSV',
                        titleAttr: 'Download CSV',
                        className: 'btn btn-sm btn-info',
                        exportOptions: {
                            columns: ':visible:not(:last-child)',
                            //columns: ':visible',
                            rows: ':visible' 
                        },
                    },
                    {
                        extend: 'pdfHtml5',
                        text: '<i class="fa fa-file-pdf"></i> PDF',
                        titleAttr: 'Download PDF',
                        className: 'btn btn-sm btn-primary',
                        exportOptions: {
                            columns: ':visible:not(:last-child)',
                            //columns: ':visible',
                            rows: ':visible' 
                        },
                    },
                    {
                        extend: 'excel',
                        text: '<i class="fa fa-file-excel"></i> Excel',
                        titleAttr: 'Excel',
                        className: 'btn btn-sm btn-tertiary',
                        exportOptions: {
                            columns: ':visible:not(:last-child)',
                            //columns: ':visible',
                            rows: ':visible' 
                        },
                    },
                    {
                        extend: 'colvis',
                        text: '<i class="fa fa-columns"></i> Colvis',
                        titleAttr: 'Colvis',
                        className: 'btn btn-sm btn-primary',
                        
                    },  
                ], 
            initComplete: function() {
                var $buttons = $('.dt-buttons').hide();
                $('#exportLinkapps').on('change', function() {
                var btnClass = $(this).find(":selected")[0].id 
                    ? '.buttons-' + $(this).find(":selected")[0].id 
                    : null;
                if (btnClass) $buttons.find(btnClass).click(); 
                })
            },
            
        })
        
        $('#searchapp').keyup(function(){
            appTable.search($(this).val()).draw() ;
        })
        
        $('#entriesapp').change(function(){
            appTable.page.len($(this).val()).draw();
        })
    
        $('#app_table_user').show();
            appTable.columns.adjust().draw();    

});











