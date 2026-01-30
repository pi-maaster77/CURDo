<template>
  <input
    ref="el"
    type="checkbox"
    :checked="modelValue === true"
    class="form-check-input"
    @change="handleChange"
  />
</template>

<script setup>
import { ref, watch, onMounted , defineProps, defineEmits} from 'vue';

const props = defineProps({
  modelValue: {
    // Permitimos Boolean para true/false y null para el estado intermedio
    type: [Boolean, Object], 
    default: null
  }
})

const emit = defineEmits(['update:modelValue'])
const el = ref(null)

// Función para sincronizar la propiedad 'indeterminate' del DOM
const syncIndeterminate = () => {
  if (el.value) {
    el.value.indeterminate = (props.modelValue === null || props.modelValue === undefined)
  }
}

const handleChange = (event) => {
  // Al hacer clic, el navegador lo pone en true o false, rompiendo el null
  emit('update:modelValue', event.target.checked)
}

// Vigilamos los cambios para aplicar la rayita visual
watch(() => props.modelValue, syncIndeterminate)

// Sincronizamos al cargar el componente
onMounted(syncIndeterminate)
</script>