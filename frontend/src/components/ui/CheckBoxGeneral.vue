<template>
  <input
    type="checkbox"
    :checked="modelValue"
    @change="$emit('update:modelValue', $event.target.checked)"
  />
</template>

<script setup>
import { defineProps } from 'vue';
defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})
</script>
