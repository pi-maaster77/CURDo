<template>
  <div
    class="tags-wrapper"
    @mouseenter="open = true"
    @mouseleave="open = false"
  >
    <div class="tags-preview">
      <TagEnLinea
        v-if="visibles.length < 1"
        :tag="placeholder"
        :placeholder="true"
      />
      <TagEnLinea
        v-for="tag in visibles"
        :key="tag.id"
        :tag="tag"
      />
      <span v-if="hayMas">...</span>
    </div>

    <div v-show="open" class="overlay">
      <TagSelector
        :tags="allTags"
        :selected-ids="selectedIds"
        @update="emit('update', $event)"
      />
    </div>
  </div>

</template>

<script setup>
import { ref, computed, defineProps, defineEmits } from 'vue'
import TagEnLinea from '../ui/TagEnLinea.vue'
import TagSelector from './TagSelector.vue'

const placeholder = {
  id:-1, 
  nombre: "Agregar Tags",
  color: {
    rojo: 127,
    verde: 127,
    azul: 0
  }
}

const props = defineProps({
  allTags: {
    type: Array,
    default: () => []
  },
  selectedIds: {
    type: Array,
    default: () => []
  }
})



const emit = defineEmits(['update'])

const open = ref(false)

const visibles = computed(() =>
  (props.selectedIds ?? [])
    .slice(0, 2)
    .map(id => props.allTags.find(t => t.id === id))
    .filter(Boolean)
)

const hayMas = computed(() =>
  (props.selectedIds ?? []).length > 2
)
</script>


<style>
.tags-wrapper {
  position: relative;
}

.overlay {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  background: white;
  border: 1px solid #ccc;
  padding: 6px;
}
</style>