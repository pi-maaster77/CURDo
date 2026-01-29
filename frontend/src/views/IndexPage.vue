<template>
    <BuscadorTags/>
  <table>
    <thead>
      <tr>
        <th>✔</th>
        <th>Nombre</th>
        <th>Tags</th>
        <th>Acciones</th>
      </tr>
    </thead>

    <tbody>
      <ElementoRow
        v-for="el in elementosStore.elementos"
        :key="el.id"
        :elemento="el"
        :editando-id="editandoId"
        @editando="editando"
        @guardar="guardarEdicion"
        @eliminar="eliminar"
        @etiquetando="asociarTags"
        @toggle-checked="toggleChecked"
      />
      <AgregarElemento
        @crear="crear"
      />
    </tbody>
  </table>
  <EditorTags />
</template>


<script setup>
import { onMounted, ref } from 'vue'
import { useElementosStore } from '@/stores/elementos'
import { useTagsStore } from '@/stores/tags'
import ElementoRow from '@/components/domain/ElementoRow.vue'
import BuscadorTags from '@/components/domain/BuscadorTags.vue'
import AgregarElemento from '@/components/domain/AgregarElemento.vue'
import EditorTags from './EditorTags.vue'
// import TagsPage from './TagsPage.vue'

const elementosStore = useElementosStore()
const tagsStore = useTagsStore()

const editandoId = ref(null)

function editando(id){
    editandoId.value = id
}

function guardarEdicion(elemento){
    if(elemento === null) return
    elementosStore.editar(elemento)
    editandoId.value = null
}

function crear(nombre){
  console.log(nombre)  
  elementosStore.crear({nombre})
}

function eliminar(id){
  elementosStore.eliminar(id)
}

function toggleChecked(elemento){
  elementosStore.toggleChecked(elemento.id, elemento.checked)
}

function asociarTags({ elementoId, tags }) {
  console.log(elementoId, tags)
  elementosStore.actualizarTags(elementoId, tags)
}


onMounted(async () => {
  await tagsStore.cargar()
  await elementosStore.cargar()
})
</script>