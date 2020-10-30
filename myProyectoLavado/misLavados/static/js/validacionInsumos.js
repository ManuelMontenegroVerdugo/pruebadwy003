

function validarNombreInsumo() {
    var nom = document.getElementById("txtInsumo").value;
    if (nom.trim().length >= 3 && nom.trim().length <= 80) {
        return true;
    }
    else{
        alert("Nombre de insumo debe contener como minimo 3 caracteres y maximo 120");
        return false;
    }
    
}


function validarDescripcion() {
    var nom = document.getElementById("txtDescripcion").value;
    if (nom.trim().length >= 3 && nom.trim().length <= 200) {
        return true;
    }

    if (nom.trim().length >= 1 && nom.trim().length <= 2 || nom.trim().length >= 201) {
        alert("La Descripcion debe contener como minimo 3 caracteres y maximo 200");
        return false;
    }
    if (nom.trim().length == 0) {
        return false;
    }

    
}





function validarPrecio() {
    var nom = document.getElementById("txtPrecio").value;
    if (nom >= 1) {
        return true;
    }
    if (nom < 1) {
        alert("El precio debe ser minimo 1 peso");
        return false;

    }
}


function validarStock() {
    var nom = document.getElementById("txtStock").value;
    if (nom >= 0) {
        return true;
    }
    else {
        alert("Debe ingresar un stock minimo de 0");
        return false;

    }
}





function ValidacionInsumos() {
    var resp = true;

    if (validarNombreInsumo() == false) {
        resp = false;
    }
    if (validarPrecio() == false) {
        resp = false;
    }
    if (validarDescripcion() == false) {
        resp = false;
    }
    if (validarStock() == false) {
        resp = false;
    }


}