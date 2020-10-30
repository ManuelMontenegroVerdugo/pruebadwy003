/*validacion de blancos y largos
function validar() {
    var Rut, Nombre, Apellido, Edad, Email, Fecha;
    Rut = document.getElementById("Rut").value;
    Nombre = document.getElementById("Nombre").value;
    Apellido = document.getElementById("Apellido").value;
    Edad = document.getElementById("Edad").value;
    Email = document.getElementById("Email").value;
    Fecha = document.getElementById("Fecha").value;
    expresion = /\w@\w+\.+[a-z]/;

    if(Rut === "" || Nombre === "" || Apellido === "" || Edad === "" || Email === "" || Fecha === "" ){
        alert("Todos los campos son obligatorios");
        return false;
        
    
    }
    else if(nombre.trim().length<3 || nombre.trim().length<30){
        alert("El nombre debe ser minimo 3 caracteres y maximo 30");
        return false;
    
    }
    else if(Apellido.trim().length<2 || Apellido.trim().length<30){
        alert("El nombre del apellido es demasiado largo");
        return false;
    }
    else if(Email.trim().length>100){
        alert("El correo es demasiado largo");
        return false;
    }
    else if(!expresion.test(correo)){
        alert("El correo no es valido");
        return false;
    }
    
}*/


/*validacion de rut*/
function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.trim().length != 10) {
        alert("verifique el largo del rut");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();

    if (dv != dv_usuario) {
        alert("Rut incorrecto");
        return false;
    } else {
        return true;
    }
}

function validarNombre() {
    var nombre = document.getElementById("txtNombre").value;
    if (nombre.trim().length >= 3 && nombre.trim().length <= 80) {
        return true;
    }
    if (nombre.trim().length < 3) {
        alert("El Nombre no debe estar vacio y debe contener entre 3 y 80 caracteres");
        return false;
    }

}


function validarApellido() {
    var Apellido = document.getElementById("txtApellido").value;
    if (Apellido.trim().length >= 3 && Apellido.trim().length <= 80) {
        return true;
    }
    if (Apellido.trim().length < 3) {
        alert("El Apellido no debe estar vacio y debe contener entre 3 y 80 caracteres");
        return false;

    }
}


function validar_email(email) {
    var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email) ? true : false;
}




function validarEmail() {
    var email = document.getElementById("txtEmail").value;

    if (validar_email(email)) {
        return true;
    } else {
        alert("El email NO es correcto");
        return false;
    }

}

/*validacion de fecha*/
function validaFecha() {
    var fechaFormulario = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    //////////////////////////////////////////////////
    var anno = fechaFormulario.slice(0, 4);
    var mes = fechaFormulario.slice(5, 7);
    var dia = fechaFormulario.slice(8, 10);
    //////////////////////////////////////////////////
    var fechaMia = new Date(anno, (mes - 1), dia); //0-+
    //////////////////////////////////////////////////
    if (fechaMia > fechaSistema) {
        alert("fecha incorrecta");
        return false;
    } else {
        return true;
    }

}







/*validacion de fecha*/
function validaFecha() {
    var fechaFormulario = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    //////////////////////////////////////////////////
    var anno = fechaFormulario.slice(0, 4);
    var mes = fechaFormulario.slice(5, 7);
    var dia = fechaFormulario.slice(8, 10);
    //////////////////////////////////////////////////
    var fechaMia = new Date(anno, (mes - 1), dia); //0-+
    //////////////////////////////////////////////////
    if (fechaMia > fechaSistema) {
        alert("fecha incorrecta");
        return false;
    } else {
        return true;
    }

}




function validarFormularioCompra() {
    var resp = true;
    if (validarRut() == false) {
        resp = false;
    }
    if (validarNombre() == false) {
        resp = false;
    }
    if (validarApellido() == false) {
        resp = false;
    }
    if (validarEmail() == false) {
        resp = false;
    }
    if (validaFecha() == false) {
        resp = false;
    }
    
}