<template>
  <button
    type="button"
    class="btn btn-sm d-inline-flex align-items-center rounded-pill border shadow-sm transition-all px-2 py-1"
    :style="containerStyle"
    @click="$emit('click')"
  >
    <span 
      class="rounded-circle me-2 border border-white border-2 shadow-sm"
      :style="circleStyle"
    ></span>
    
    <small class="fw-medium text-dark">{{ props.color?.nombre }}</small>
  </button>
</template>

<script setup>
import { defineProps, defineEmits, computed } from 'vue';

const props = defineProps({
  color: {
    type: Object,
    required: true
  },
  alpha: {
    type: Number,
    default: 0.15
  }
})

defineEmits(['click'])

// Estilo para el fondo del botón (estilo badge transparente como tus tags)
const containerStyle = computed(() => {
  if (!props.color) return {}
  const { rojo: r, verde: g, azul: b } = props.color
  return {
    backgroundColor: `rgba(${r}, ${g}, ${b}, ${props.alpha})`,
    borderColor: `rgba(${r}, ${g}, ${b}, 0.3) !important`
  }
})

// Estilo para el círculo sólido de color
const circleStyle = computed(() => {
  if (!props.color) return {}
  const { rojo: r, verde: g, azul: b } = props.color
  return {
    backgroundColor: `rgb(${r}, ${g}, ${b})`,
    width: '14px',
    height: '14px',
    flexShrink: 0
  }
})
</script>

<style scoped>
.transition-all {
  transition: all 0.2s ease-in-out;
}

.btn:hover {
  filter: brightness(0.9);
  transform: translateY(-1px);
}

.btn:active {
  transform: translateY(0);
}
</style>