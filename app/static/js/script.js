$(function(){
    $('.datepicker').datepicker({
      dateFormat: "dd/mm/yy"
    });

    $('.nav-link').click(function(){
      $('.active').removeClass('active');
      $(this).addClass('active');
    });

    var $table = $('#table');
    $('#toolbar').find('select').change(function() {
        $table.bootstrapTable('refreshOptions', {
            exportDataType: $(this).val()
        });
    });

    $('#hide-zero').bind('click', function() {
      if($('#hide-zero').hasClass('selected')){
        console.log('checked');
        $('#hide-zero').removeClass('selected');
      }
      else{
        $('#hide-zero').addClass('selected');
        $('#table').bootstrapTable("filterBy", {
          'saldo': '0.0'
        });
      }
    });

    $('#get-data').bind('click', function() {
      if($('#get-data').hasClass('selected')){
        console.log('checked');
        $('#get-data').removeClass('selected');
        $('#messages').toggle('fast');
      }
      else{
        $('#messages').html(JSON.stringify($('#table').bootstrapTable('getData')));
        $('#messages').css('overflow-y', 'scroll');
        $('#get-data').addClass('selected');
        $('#messages').toggle('fast');
      }
    });

    $("#hide").bind("click", function() {
        $('#my-form').slideToggle();
        var status = $('#hide').html();
        if (status == 'hide') {
            $('#hide').html('show');
            $('#hide').attr('id', 'show');
        } else {
            $('#show').html('hide');
            $('#show').attr('id', 'hide');
        }
    });

    $('.box-filter').bind('blur', function() {
        //Acoes...
        $('.box-filter').toggle('fast');
    });

    $('.button-filter').bind('click', function() {
        var ele = $('.button-filter');

        if ($(ele).hasClass('rotatereverse')) {
            $(ele).removeClass('rotatereverse');
            $(ele).addClass('rotate');
        } else if ($(ele).hasClass('rotate')) {
            $(ele).removeClass('rotate');
            $(ele).addClass('rotatereverse');
        }

        $('.box-filter').toggle('fast');
        if ($('.box-filter').css('display') == 'block') {
            //$('.box-filter').toggle('fast');
            //$('#text').focus();
            if ($('.box-filter').is(':focus')) {
                console.log('bbb');
            }
        }
    });

    $( "#messages" ).delay( 3000 ).toggle( 700 );

    $('.bs-example-modal-lg').on('hide.bs.modal', function(){
      $('#div-input-id').remove();
      $('#modal-descricao').val('');
    });

    function addIdOnModal(){
      $('.update').on('click', function(e){
        e.preventDefault();
        $('.modal-title').html('Alterar Cadastrado');
        $('.modal-body').prepend(
          '<div class="row" id="div-input-id">'+
          '<div class="col-xs-2">'+
          '<div class="form-group">'+
              '<label for="id">Id</label>'+
              '<input name="id" id="modal-id" type="text" class="form-control" readonly>'+
          '</div>'+
          '</div>'+
          '</div>'
        );
        var id = $(this).closest('tr').find('td:eq(1)').html();
        var descricao = $(this).closest('tr').find('td:eq(2)').html();
        $('#modal-id').val(id);
        $('#modal-descricao').val(descricao);
      });
    }

    addIdOnModal()

    //Preparar um formulario para envio por AJAX (serialize)
    $(function(){
     $('#form-modal').bind('submit', function(e){
       e.preventDefault();
       var txt = $(this).serialize();

       $.ajax({
         type:'POST',
         method: 'POST',
         url:'/cadastrar_marca',
         data: txt,
         dataType: 'json',
         success: function(resultado){
           $("#mytable tbody").html('')
           $.each(resultado, function(key, ob){
             $("#mytable tbody").append(
              '<tr> \n'+
               '<td>'+
                   '<a class="btn btn-default update" href="" data-toggle="modal" data-target=".bs-example-modal-lg">'+
                     '<span class="glyphicon glyphicon-edit" aria-hidden="true"></span>'+
                   '</a>'+
                   '<a class="btn btn-default detele" href="/marcas/delete/'+ob.id+'">'+
                     '<span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span>'+
                   '</a>'+
              '</td>'+
              '<td>'+ ob.id +'</td> \n'+
              '<td>'+ ob.descricao +'</td> \n'+
              '<td>'+ ob.create_at +'</td> \n'+
              '<td>'+ ob.update_at +'</td> \n </tr>');
           });
           addIdOnModal()
           $('.modal-body').prepend(
             '<div id="messages-modal" class="alert alert-success" role="alert">'+
                 '<strong>Sucesso! </strong> Registro cadastrado com sucesso.'+
             '</div>'
           );
           $( "#messages-modal" ).delay( 3000 ).toggle( 700 ).delay( 3000 ).queue(function() { $(this).remove(); });
           if(!$('#modal-id')){
             $('#modal-descricao').val('');
           }
         },
         error: function(error){
           $('.modal-body').prepend(
             '<div id="messages-modal" class="alert alert-warning" role="alert">'+
                 '<strong>Ops! </strong> Você deve informar o nome da marca.'+
             '</div>'
           );
           $( "#messages-modal" ).delay( 3000 ).toggle( 700 ).delay( 3000 ).queue(function() { $(this).remove(); });
         }
       })
     });
    });
});
