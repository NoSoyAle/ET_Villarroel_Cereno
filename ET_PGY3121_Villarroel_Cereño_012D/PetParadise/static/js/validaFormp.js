//funcion que valida un formulario

$(function (){
    console.log("dentro de la funcion");
    $("#form-contact").validate({

        rules:{
            rut:{
                required:true
            },
            nom:{
                required:true
            },
            fono:{
                required:true
            },
            fechaem:{
                required:true
            },
            email:{
                required:true,
                email:true
            },
            comentario:{
                required:false
            }           
        },//rules
        messages:{
            rut:{
                required:'Ingrese rut',
                minlength:'Caracteres insuficientes (9)'
            },
            nom:{
                required:'Ingrese Nombre',
                minlength:'Caracteres insuficientes (3)'
            },
            fono:{
                required:'Ingrese número de teléfono',
                minlength:'Digitos insuficientes (9)'
            },
            fechaem:{
                required:'Ingrese una fecha',
                min:'Seleccione una fecha válida'
            },
            email:{
                required: 'Ingrese su correo electrónico',
                email:'Formato de correo no válido'
            }
        },
    })
});
