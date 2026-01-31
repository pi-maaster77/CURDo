<template>
  <div class="position-fixed top-0 end-0 p-3" style="z-index: 1080">
    <div
      v-for="(n, i) in mensajes"
      :key="i"
      class="alert alert-dismissible alert alert-danger fade show" 
      :class="`alert-${n.tipo}`"
      role="alert"
    >
      {{ n.texto }}

      <button
        type="button"
        class="btn-close"
        aria-label="Close"
        @click="remove(i)">
      </button>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useNotificacionesStore } from '@/stores/notificaciones'

const store = useNotificacionesStore()
const { mensajes } = storeToRefs(store)
const { remove } = store
</script>
