<template>
  <span 
    :style="style" 
    class="badge d-inline-flex align-items-center rounded-pill px-2 py-1 fw-medium border transition-all"
  >
    <CheckBoxGeneral 
      disabled 
      :model-value="seleccionado" 
      class="me-2 custom-check-sm"
    />
    
    <span class="tag-label me-1">{{ tag.nombre }}</span>
  </span>
</template>

<script setup>
import { computed, defineProps } from 'vue'
import CheckBoxGeneral from './CheckBoxGeneral.vue'

const props = defineProps({
  tag: {
    type: Object,
    required: true
  },
  alpha: {
    type: Number,
    default: 0.15 // Bootstrap usa opacidades bajas para un look moderno
  },
  seleccionado: {
    type: Boolean,
    default: false
  }
})

const style = computed(() => {
  const { rojo: r = 100, verde: g = 100, azul: b = 100 } = props.tag.color || {}
  
  return {
    color: `rgb(${r}, ${g}, ${b})`,
    backgroundColor: `rgba(${r}, ${g}, ${b}, ${props.alpha})`,
    borderColor: `rgba(${r}, ${g}, ${b}, 0.3) !important`, // Borde sutil del mismo tono
  }
})
</script>

<style scoped>
.badge {
  /* Evita que el texto se rompa en varias líneas */
  white-space: nowrap; 
  /* Mejora la fuente para que parezca de sistema */
  font-family: system-ui, -apple-system, sans-serif;
  font-size: 0.85rem;
}

/* Ajuste opcional para que el checkbox no se vea gigante dentro del tag */
:deep(.form-check-input) {
  width: 0.9em;
  height: 0.9em;
  margin-top: 0;
  cursor: default;
}

.transition-all {
  transition: all 0.2s ease;
}
</style>