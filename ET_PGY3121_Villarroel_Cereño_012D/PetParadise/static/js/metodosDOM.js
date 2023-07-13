
//función que envia el contenido a un elemento de tipo textarea
function CrearCom(){
    var a = document.getElementById("rut").value;
    var b = document.getElementById("nom").value;
    var c = document.getElementById("fono").value;
    var d = document.getElementById("fechaem").value;
    var e = document.getElementById("email").value;
    

        var mensaje= "Contactanos por una duda: \n" 
                +"Rut: " + a + "\n" + "Nombre: " + b + "\n"+ "Teléfono: " + c 
                + "\n" + "Fecha de emisión: " + d
                + "\n" + "Correo electrónico: " + e;  
                
        document.getElementById("comentario").value = mensaje;
}

    //función que cambia el color de fondo a orange
function colorOrange(obj){
    obj.style.backgroundColor='orange';
}

function colorBlanco(obj){
    obj.style.backgroundColor='white';
}

function upperText(texto)
{
    const x = texto;
    x.value= x.value.toUpperCase();
}