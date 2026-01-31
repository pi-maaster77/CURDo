<template>
  <div class="tag-selector d-flex flex-wrap gap-2 py-2">
    <div v-if="tags.length === 0" class="text-muted small fst-italic">
      No hay etiquetas disponibles
    </div>

    <TagSeleccionable
      v-for="tag in tags"
      :key="tag.id"
      :tag="tag"
      :seleccionado="selectedIds?.includes(tag.id)"
      class="selectable-tag shadow-sm"
      @click="toggle(tag.id)"
    />
  </div>
</template>

<script setup>
// No es necesario importar defineProps/defineEmits en script setup
import { defineProps, defineEmits } from 'vue';
import TagSeleccionable from './TagSeleccionable.vue';


const props = defineProps({
  tags: {
    type: Array,
    default: () => []
  },
  selectedIds: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['update'])

function toggle(id) {
  const currentIds = props.selectedIds ?? [];
  const newIds = currentIds.includes(id)
    ? currentIds.filter(t => t !== id)
    : [...currentIds, id];
  
  emit('update', newIds);
}
</script>

<style scoped>
.selectable-tag {
  cursor: pointer;
  transition: transform 0.15s ease, filter 0.15s ease;
  user-select: none; /* Evita que el texto se seleccione al hacer muchos clics */
}

.selectable-tag:hover {
  transform: translateY(-2px);
  filter: brightness(0.9);
}

.selectable-tag:active {
  transform: translateY(0);
}
</style>