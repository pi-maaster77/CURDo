const tabla = document.getElementById("tabla-principal")

fetch('/elementos/')
    .then(response => response.json())
    .then(data => {
        data.forEach(elemento => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${elemento.id}</td>
                <td><input id="tick-${elemento.id}" type="checkbox" ${elemento.tick ? "checked" : ""} onclick="toggleTick(${elemento.id})"></td>
                <td>${elemento.nombre}</td>
                <td><button onclick="eliminar(${elemento.id})">Eliminar</button></td>
                <td><button onclick="actualizar(${elemento.id})">Actualizar</button></td>
            `;
            tabla.appendChild(fila);
        });
    })
    .catch(error => console.error('Error al obtener los datos:', error));

function toggleTick(id) {
    fetch(`/elementos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tick: document.getElementById(`tick-${id}`).checked})
    })
    .then(response => {
        if (!response.ok) {
            alert('Error al actualizar el tick');
        }
    })
    .catch(error => console.error('Error al actualizar el tick:', error));
}