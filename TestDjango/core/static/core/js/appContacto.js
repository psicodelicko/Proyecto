function validarFormulario() {

    $('.alert').remove();



    var nombre = $('#nombre').val(),
        email = $('#email').val(),
        telefono = $('#telefono').val()




    if (nombre == "" || nombre == null) {

        cambiarColor("nombre");

        mostraAlerta("Nombre es obligatorio");
        return false;
    } else {
        var expresion = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if (!expresion.test(nombre)) {

            cambiarColor("nombre");
            mostraAlerta("No se permiten carateres especiales o numeros");
            return false;
        }
    }


    if (telefono == "" || telefono == null) {

        cambiarColor("telefono");

        mostraAlerta("telefono es obligatorio");
        return false;
    }

    if (email == "" || email == null) {

        cambiarColor("email");

        mostraAlerta("Email obligatorio");
        return false;
    } else {
        var expresion = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if (!expresion.test(email)) {

            cambiarColor("email");
            mostraAlerta("Por favor ingrese un email válido");
            return false;
        }
    }


    $('form').submit();
    return true;

}

$('input').focus(function() {
    $('.alert').remove();
    colorDefault('nombre');
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
    $('#nombre').before('<div class="alert">Error: ' + texto + '</div>');
}