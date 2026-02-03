function gestionarTags(elementoId) {
    fetch(`/elementos/${elementoId}/tags/`)
        .then(response => response.json())
        .then(data => {
            const tagsActuales = data.tagsActuales;
            const todosLosTags = data.todosLosTags;

            let tagListHTML = '<h3>Gestionar Tags para el elemento ' + elementoId + '</h3><ul>';
            todosLosTags.forEach(tag => {
                const estaAsignado = tagsActuales.some(t => t.id === tag.id);
                tagListHTML += `<li>
                    <input type="checkbox" id="tag-${tag.id}" ${estaAsignado ? 'checked' : ''} 
                    onchange="toggleTag(${elementoId}, ${tag.id}, this.checked)">
                    <label for="tag-${tag.id}">${tag.nombre}</label>
                </li>`;
            });
            tagListHTML += '</ul>';

            const modal = document.createElement('div');
            modal.id = 'tag-modal';
            modal.innerHTML = `
                <div class="modal-content">
                    <span class="close-button" onclick="closeTagModal()">&times;</span>
                    ${tagListHTML}
                </div>
            `;
            document.body.appendChild(modal);
        })
        .catch(error => console.error('Error al obtener los tags:', error));

}

