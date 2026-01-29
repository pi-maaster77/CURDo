<template>
    <span :style="style">{{ tag.nombre }}</span>
</template>

<script setup>
import { computed, defineProps } from 'vue'

const props = defineProps({
  tag: {
    type: Object,
    required: true
  },
  alpha: {
    type: Number,
    default: 0.2
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
