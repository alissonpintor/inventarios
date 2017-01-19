$(function() {
    var saldo = $('.saldo');

    $('#hide-zero').bind('click', function(){
      if($('#hide-zero:checked')){

        if($(saldo).html() == 0.0 || $(saldo).html() == 0){
            console.log('teste');
            $(saldo).closest('tr').css('display', 'none');

        };

      };
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

    $('.box-filter').bind('blur', function(){
    	//Acoes...
      $('.box-filter').toggle('fast');
    });

    $('.button-filter').bind('click', function(){
      var ele = $('.button-filter');

      if($(ele).hasClass('rotatereverse')){
        $(ele).removeClass('rotatereverse');
        $(ele).addClass('rotate');
      }
      else if ($(ele).hasClass('rotate')){
        $(ele).removeClass('rotate');
        $(ele).addClass('rotatereverse');
      }

      $('.box-filter').toggle('fast');
      if($('.box-filter').css('display') == 'block'){
        //$('.box-filter').toggle('fast');
        //$('#text').focus();
        if($('.box-filter').is(':focus')){
            console.log('bbb');
        }
      }
    });
});
