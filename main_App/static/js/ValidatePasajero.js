    document.getElementById('Formulario').addEventListener('submit', function(event) {
        const dni = document.getElementById('dni');
        const dniError = document.getElementById('dni-error');
        
        // Validar DNI
        if (!/^\d{11}$/.test(dni.value)) {
            dniError.textContent = 'El DNI debe tener exactamente 11 dígitos y contener solo números.';
            event.preventDefault();
        } else {
            dniError.textContent = ''; 
        }
    });