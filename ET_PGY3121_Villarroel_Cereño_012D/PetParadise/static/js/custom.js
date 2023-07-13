$(document).ready(function() {
  var estadoElement = $('#estado');
  var btnActualizarEstado = $('#btn-actualizar-estado');

  btnActualizarEstado.on('click', function() {
      var csrfToken = $('[name=csrfmiddlewaretoken]').val(); // Obtener el token CSRF

      $.ajax({
          url: '/actualizar_estado/',
          method: 'POST',
          data: {
              estado_inicial: estadoElement.text().trim(),
              csrfmiddlewaretoken: csrfToken // Agregar el token CSRF a los datos de la solicitud
          },
          success: function(response) {
              estadoElement.text(response.estado);
              if (response.estado === 'Procesando Pedido' || response.estado === 'En Proceso') {
                  btnActualizarEstado.prop('disabled', true);
              }
          },
          error: function(xhr, status, error) {
              console.log(error);
          }
      });
  });
});
