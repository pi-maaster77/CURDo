function agregar() {
    document.getElementById("nombre-input").value
    const nombre = document.getElementById("nombre-input").value;
    
    fetch('/elementos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre: nombre }),
    })
    .then(response => {
        if (response.ok) {
            alert('Elemento agregado exitosamente');
            location.reload(); // Recargar la página para ver el nuevo elemento
        } else {
            alert('Error al agregar el elemento');
        }
    })
    .catch(error => console.error('Error al agregar el elemento:', error));
    }