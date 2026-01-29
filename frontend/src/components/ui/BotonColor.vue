<template>
  <button
    class="color-btn"
    :style="style"
    @click="$emit('click')"
  >..,</button>
</template>

<script setup>
import { defineProps, defineEmits, computed} from 'vue';


const props = defineProps({
  color: Object
})

defineEmits(['click'])

const style = computed(() => {
  if (!props.color) return {}
  return {
    backgroundColor: `rgb(${props.color.rojo}, ${props.color.verde}, ${props.color.azul})`,
    width: '20px',
    height: '20px',
    borderRadius: '50%'
  }
})
</script>
