function actualizar(id) {
    const nombre = prompt("Ingrese el nuevo nombre:");
    if (nombre !== null) {
        fetch(`/elementos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nombre: nombre }),
        })
        .then(response => {
            if (response.ok) {
                alert('Elemento actualizado exitosamente');
                location.reload(); // Recargar la página para ver los cambios
            } else {
                alert('Error al actualizar el elemento');
            }
        })
        .catch(error => console.error('Error al actualizar el elemento:', error));
    }
}