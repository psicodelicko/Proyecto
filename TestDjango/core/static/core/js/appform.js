function validarFormulario() {

    $('.alert').remove();



    var boleta = $('#boleta').val()



    if (boleta == "" || boleta == null) {

        cambiarColor("boleta");

        mostraAlerta("boleta es obligatorio");
        return false;
    }


    $('form').submit();
    return true;

}

$('input').focus(function() {
    $('.alert').remove();
    colorDefault('boleta');
    colorDefault('correo');
    colorDefault('asunto');
});

$('textarea').focus(function() {
    $('.alert').remove();
    colorDefault('mensaje');
});


function colorDefault(dato) {
    $('#' + dato).css({
        border: "1px solid #999"
    });
}


function cambiarColor(dato) {
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
}



function mostraAlerta(texto) {
    $('#boleta').before('<div class="alert">Error: ' + texto + '</div>');
}