<template>
  <BuscadorTags
    :tags="tagsStore.tags"
    @change="aplicarFiltros"
  />

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
      <AgregarElemento @crear="crear" />
    </tbody>
  </table>
  
  <EditorTags />
</template>

<script setup>
import { onMounted, ref } from 'vue' // Eliminado computed porque filtra el Store
import { useElementosStore } from '@/stores/elementos'
import { useTagsStore } from '@/stores/tags'

// Importaciones de componentes
import ElementoRow from '@/components/domain/ElementoRow.vue'
import BuscadorTags from '@/components/domain/BuscadorTags.vue'
import AgregarElemento from '@/components/domain/AgregarElemento.vue'
import EditorTags from './EditorTags.vue'

const elementosStore = useElementosStore()
const tagsStore = useTagsStore()

const editandoId = ref(null)

// --- Lógica de Interfaz ---

function editando(id) {
  editandoId.value = id
}

function guardarEdicion(elemento) {
  if (elemento === null) return
  elementosStore.editar(elemento)
  editandoId.value = null
}

// --- Lógica de Datos (Store) ---

function crear(nombre) {
  elementosStore.crear(nombre)
}

function eliminar(id) {
  elementosStore.eliminar(id)
}

function toggleChecked(elemento) {
  elementosStore.toggleChecked(elemento.id, elemento.checked)
}

function asociarTags({ elementoId, tags }) {
  elementosStore.actualizarTags(elementoId, tags)
}

/**
 * Esta es la clave. Si el filtro de tags falla al sacar las tags,
 * asegúrate de que tu elementosStore.cargar() maneje { tags: [] }
 */
async function aplicarFiltros(filtros) {
  console.log("Aplicando filtros:", filtros)
  // Llamamos a la API a través del store pasándole los parámetros
  await elementosStore.cargar(filtros)
}

onMounted(async () => {
  // Carga inicial
  await Promise.all([
    tagsStore.cargar(),
    elementosStore.cargar()
  ])
})
</script>