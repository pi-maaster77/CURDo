<template>
  <div class="picker-overlay" @click.self="emit('cerrar')">
    <div class="picker">
      <h4>Colores</h4>

      <!-- Lista de colores -->
      <div class="colores">
        <div
          v-for="c in colores"
          :key="c.id"
          class="color-item"
          :class="{ activo: c.id === colorActualId }"
        >
          <button
            class="color-btn"
            :style="{ backgroundColor: rgb(c) }"
            @click="emit('seleccionar', { colorId: c.id })"
          >
            {{ c.nombre }}
          </button>

          <BotonEliminar
            class="delete"
            @click="emit('eliminar', c.id)"
          />
        </div>
      </div>

      <!-- Crear color -->
      <div class="crear">
        <input v-model="nuevoNombre" placeholder="Nombre" />

        <input type="color" v-model="hex" />

        <button @click="crearColor">
          ➕ Crear
        </button>
      </div>

      <button class="cerrar" @click="emit('cerrar')">
        Cerrar
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits, defineProps } from 'vue'
import BotonEliminar from '../ui/BotonEliminar.vue'

defineProps({
  colores: Array,
  colorActualId: Number
})

const emit = defineEmits([
  'seleccionar',
  'crear',
  'eliminar',
  'cerrar'
])

const nuevoNombre = ref('')
const hex = ref('#000000')

function rgb(c) {
  return `rgb(${c.rojo}, ${c.verde}, ${c.azul})`
}

function crearColor() {
  if (!nuevoNombre.value) return

  const r = parseInt(hex.value.slice(1, 3), 16)
  const g = parseInt(hex.value.slice(3, 5), 16)
  const b = parseInt(hex.value.slice(5, 7), 16)

  emit('crear', {
    nombre: nuevoNombre.value,
    rojo: r,
    verde: g,
    azul: b
  })

  nuevoNombre.value = ''
}
</script>

