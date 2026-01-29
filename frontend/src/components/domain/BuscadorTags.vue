<template>
  <div class="buscador">
    <div class="controles">
      <label>
        <input type="checkbox" v-model="checkedOnly" />
        Solo checkeados
      </label>

      <select v-model="tagMode">
        <option value="any">Cualquiera</option>
        <option value="all">Todos</option>
      </select>
    </div>
    <button @click="limpiar">limpiar</button>
    <ElementoTagsHover
      :all-tags="tags"
      :selected-ids="selectedTags"
      @update="onTagsUpdate"
    />
  </div>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits} from 'vue'
import ElementoTagsHover from '../ui/ElementoTagsHover.vue'

defineProps({
  tags: { type: Array, default: () => [] }
})

const emit = defineEmits(['change'])

const selectedTags = ref([])
const checkedOnly = ref(false)
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
    checkedOnly.value = false
    tagMode.value = 'any'
}

</script>