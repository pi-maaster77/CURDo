<template>
  <tr class="buscador">
      <td>
        <CheckBoxGeneral v-model="checkedOnly" id="filterChecked" />
      </td>
      <td>
        <select v-model="tagMode">
          <option value="any">Cualquiera</option>
          <option value="all">Todos</option>
        </select>
      </td>
      <td>
        <button @click="limpiar" class="btn btn-secondary">limpiar</button>
      </td>
      <td>
        <ElementoTagsHover
          :all-tags="tags"
          :selected-ids="selectedTags"
          @update="onTagsUpdate"
        />
      </td>
  </tr>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits} from 'vue'
import ElementoTagsHover from '../ui/ElementoTagsHover.vue'
import CheckBoxGeneral from '../ui/CheckBoxGeneral.vue'

defineProps({
  tags: { type: Array, default: () => [] }
})

const emit = defineEmits(['change'])

const selectedTags = ref([])
const checkedOnly = ref(null)
const tagMode = ref('any')

// Función para manejar el update de tags
const onTagsUpdate = (ids) => {
  selectedTags.value = ids || []
}

// Observamos los cambios y emitimos el objeto de filtro
watch(
  [selectedTags, checkedOnly, tagMode],
  ([newTags, newChecked, newMode]) => {
    emit('change', {
      // Enviamos el array tal cual. Si está vacío, el padre debe mostrar todo.
      tags: newTags, 
      tagMode: newMode,
      checked: newChecked
    })
  },
  { immediate: true }
)
function limpiar() {
    selectedTags.value = []
    checkedOnly.value = null
    tagMode.value = 'any'
}

</script>