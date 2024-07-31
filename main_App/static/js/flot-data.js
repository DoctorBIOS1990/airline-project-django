//Flot Pie Chart
$(function() {

    var data = [{
        label: "Pasajeros",
        data:  contarPasajeros.value
    }, {
        label: "Aviones",
        data: contarAviones.value
    }, {
        label: "Aeropuertos",
        data: contarAeropuertos.value
    }, {
        label: "Tramos",
        data: contarTramos.value
    }, {
        label: "Vuelos",
        data:   contarVuelos.value
    }, {
        label: "Reservas",
        data: contarReservas.value
    }, {
        label: "Tarifas",
        data: contarTarifas.value
    }];

    var plotObj = $.plot($("#flot-pie-chart"), data, {
        series: {
            pie: {
                show: true
            }
        },
        grid: {
            hoverable: true
        },
        tooltip: true,
        tooltipOpts: {
            content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
            shifts: {
                x: 20,
                y: 0
            },
            defaultTheme: true
        }
    });

});
