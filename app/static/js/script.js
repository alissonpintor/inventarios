$(function() {
    $('.datepicker').datepicker({
      dateFormat: "dd/mm/yy"
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

    //Preparar um formulario para envio por AJAX (serialize)
    $(function(){
     $('#my-form').bind('submit', function(e){
       e.preventDefault();

       var txt = $(this).serialize();
       console.log(txt);

       $.ajax({
         type:'POST',
         url:'produtos',
         data: txt,
         success: function(resultado){
           $("#mytable tbody").html('')
           $.each(resultado, function(key, ob){
             $("#mytable tbody").append(
              '<tr> \n'+
              '<td>'+ ob.id +'</td> \n'+
              '<td>'+ ob.descricao +'</td> \n'+
              '<td>'+ ob.fabricante +'</td> \n'+
              '<td>'+ 0 +'</td> \n </tr>');
             console.log(ob.id);
             console.log(ob.descricao);
           });
         },
         error: function(){
           alert('Ocorreu um erro!');
         }
       })
     });
    });
});
