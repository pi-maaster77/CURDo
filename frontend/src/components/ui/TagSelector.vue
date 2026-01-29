<template>
  <div class="tags">
    <TagSeleccionable
      v-for="tag in tags"
      :key="tag.id"
      :tag="tag"
      :seleccionado="selectedIds.includes(tag.id)"
      @click="toggle(tag.id)"
    />

  </div>
</template>

<script setup>
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
  emit(
    'update',
      (props.selectedIds ?? []).includes(id)
      ?(props.selectedIds ?? []).filter(t => t !== id)
      : [... (props.selectedIds ?? []), id]
  )
}
</script>
