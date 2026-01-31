<template>
  <span 
    :style="style" 
    class="badge d-inline-flex align-items-center rounded-pill px-3 py-2 fw-medium transition-all"
    :class="{ 'border border-secondary-subtle': placeholder }"
  >
    <i 
      v-if="placeholder" 
      class="bi bi-tags-fill me-2" 
      style="font-size: 0.9em;"
    ></i>
    
    <span class="tag-text">{{ tag.nombre }}</span>
  </span>
</template>

<script setup>
import { computed , defineProps} from 'vue'

const props = defineProps({
  tag: {
    type: Object,
    required: true
  },
  alpha: {
    type: Number,
    default: 0.15 // Bootstrap usa transparencias bajas para badges sutiles
  },
  placeholder: {
    type: Boolean,
    default: false
  }
})

const style = computed(() => {
  const { rojo: r = 100, verde: g = 100, azul: b = 100 } = props.tag.color || {}
  
  return {
    color: `rgb(${r}, ${g}, ${b})`,
    backgroundColor: `rgba(${r}, ${g}, ${b}, ${props.alpha})`,
    border: `1px solid rgba(${r}, ${g}, ${b}, 0.3)`, // Añade un borde sutil del mismo color
    cursor: props.placeholder ? 'pointer' : 'default'
  }
})
</script>

<style scoped>
.transition-all {
  transition: all 0.2s ease-in-out;
}
/* Efecto hover sutil si es un placeholder/botón */
.badge:hover {
  filter: brightness(0.95);
}
</style>
