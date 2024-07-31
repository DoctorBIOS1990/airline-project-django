document.getElementById('Formulario').addEventListener('submit', function(event) {

    const message = document.getElementById("message");
    const Salida = document.getElementById("aeropuerto_salida");
    const Llegada = document.getElementById("aeropuerto_llegada");
    const duracion = document.getElementById('duracion').value;
    const hora_salida = document.getElementById('hora_salida').value;
    const hora_entrada= document.getElementById('hora_entrada').value;
    const durationPattern = /^([0-9]+):([0-5][0-9]):([0-5][0-9])$/;  // HH:MM:SS
    const timePattern = /^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$/;  // HH:MM:SS

    const showModal = (messageHTML) => {
        message.innerHTML = messageHTML;
        $('#myModal').modal('show');
        event.preventDefault();
    };
    
    if (!durationPattern.test(duracion)) {
        showModal('<h1><i class="fa fa-clock-o"></i></h1> La duración debe estar en el formato HH:MM:SS.');
    }
    
    if (!timePattern.test(hora_entrada)) {
        showModal('<h1><i class="fa fa-clock-o"></i></h1> La hora de llegada debe estar en el formato HH:MM:SS.');
    }
    
    if (!timePattern.test(hora_salida)) {
        showModal('<h1><i class="fa fa-clock-o"></i></h1>La hora de salida debe estar en el formato HH:MM:SS.');
    }
    
    if (Salida.value == Llegada.value) { 
        showModal('<h1><i class="fa fa-exchange"></i></h1> La Salida y el Destino no pueden ser las mismas.');
    }
    
});


