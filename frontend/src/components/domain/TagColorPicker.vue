<template>
  <div class="card shadow-lg border-0 position-absolute start-0 mt-2" style="width: 300px; z-index: 1050;">
    <div class="card-header d-flex justify-content-between align-items-center bg-white border-bottom-0 pt-3">
      <h6 class="mb-0 fw-bold text-secondary text-uppercase small">Colores</h6>
      <BotonCerrar @click="emit('cerrar')"/>
    </div>

    <div class="card-body p-0">
      <div class="list-group list-group-flush overflow-auto">
        <div
          v-for="c in colores"
          :key="c.id"
          class="list-group-item list-group-item-action d-flex align-items-center justify-content-between border-0 py-2"
          :class="{ 'bg-light': c.id === colorActualId }"
        >
          <div 
            @click="emit('seleccionar', { colorId: c.id })" 
            class="d-flex align-items-center flex-grow-1 cursor-pointer"
          >
            <span 
              class="rounded-circle me-3 shadow-sm" 
              :style="{ backgroundColor: rgb(c), width: '20px', height: '20px', display: 'block' }"
            ></span>
            <span class="small fw-medium">{{ c.nombre }}</span>
          </div>

          <BotonEliminar
            class="btn btn-link btn-sm text-danger p-0"
            @click="emit('eliminar', c.id)"
          />
        </div>
      </div>
    </div>

    <div class="card-footer bg-white border-top-0 p-3">
      <div class="input-group input-group-sm mb-2">
        <EntradaTexto type="text"
          v-model="nuevoNombre" 
          placeholder="Nombre del color" 
        />
      </div>
      <div class="d-flex gap-2 align-items-center">
        <input 
          type="color" 
          v-model="hex" 
          class="form-control form-control-color border-0 p-0" 
          title="Elige un color"
        />
        <button 
          @click="crearColor" 
          class="btn btn-primary btn-sm flex-grow-1 d-flex align-items-center justify-content-center gap-1"
        >
          <i class="bi bi-plus-lg"></i> Crear
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits} from 'vue' // defineProps y defineEmits no necesitan importarse
import BotonEliminar from '../ui/BotonEliminar.vue'
import BotonCerrar from '../ui/BotonCerrar.vue'
import EntradaTexto from '../ui/EntradaTexto.vue'

defineProps({
  colores: Array,
  colorActualId: Number
})

const emit = defineEmits(['seleccionar', 'crear', 'eliminar', 'cerrar'])

const nuevoNombre = ref('')
const hex = ref('#000000')

const rgb = (c) => `rgb(${c.rojo}, ${c.verde}, ${c.azul})`

function crearColor() {
  if (!nuevoNombre.value) return
  const r = parseInt(hex.value.slice(1, 3), 16)
  const g = parseInt(hex.value.slice(3, 5), 16)
  const b = parseInt(hex.value.slice(5, 7), 16)
  emit('crear', { nombre: nuevoNombre.value, rojo: r, verde: g, azul: b })
  nuevoNombre.value = ''
}
</script>

<style scoped>
.cursor-pointer {
  cursor: pointer;
}
/* Estilo especial para el input de color de Bootstrap */
.form-control-color {
  width: 38px;
  height: 31px;
  background: none;
}
</style>