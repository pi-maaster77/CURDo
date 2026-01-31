function eliminar(id) {
    fetch(`/elementos/${id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            alert('Elemento eliminado exitosamente');
            location.reload(); // Recargar la página para ver los cambios
        } else {
            alert('Error al eliminar el elemento');
        }
    })
    .catch(error => console.error('Error al eliminar el elemento:', error));
}