// Submit Tramo Validation

const Salida = document.getElementById("aeropuerto_salida");
const Llegada = document.getElementById("aeropuerto_llegada");
const message = document.getElementById("message");

document.getElementById('Formulario').addEventListener('submit', function(event) {
    if (Salida.value === Llegada.value)
        { 
            event.preventDefault();
            message.innerHTML = "La Salida y el Destino no pueden ser las mismas.";
            $('#myModal').modal('show');
        } 
});