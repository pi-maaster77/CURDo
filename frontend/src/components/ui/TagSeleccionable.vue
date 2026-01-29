<template>
    
    <span :style="style"><CheckBoxGeneral disabled :model-value="seleccionado"/>{{ tag.nombre }}</span>
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
    default: 0.2
  },
  seleccionado: {
    type: Boolean
  }
})

const style = computed(() => {
  const r = props.tag.color?.rojo || 100
  const g = props.tag.color?.verde || 100
  const b = props.tag.color?.azul || 100
  
  return {
    color: `rgb(${r}, ${g}, ${b})`,
    backgroundColor: `rgba(${r}, ${g}, ${b}, ${props.alpha})`,
    display: 'inline-block'
  }
})
</script>
