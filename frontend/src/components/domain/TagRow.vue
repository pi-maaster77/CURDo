<template>
  <tr>
    <td>
      <template v-if="meEditan">
        <input v-model="nombre" />
      </template>
      <template v-else>
        {{ tag.nombre }}
      </template>
    </td>

    <td>
      <span class="btn-group" v-if="!meEditan">
        <BotonEditar @click="empezarEditar()"/>
        <BotonEliminar @click="eliminar()"/>
      </span>
      <span class="btn-group" v-else>
        <BotonGuardar @click="guardarEdicion()"/>
        <BotonCerrar @click="cancelarEditar()"/>
      </span>
    </td>
    <td>
      <TagColorSelector
        :tag="tag"
        :meColorean="meColorean"
        @change="guardar"
        @colorear="colorear"
        @cerrar="cerrar"
      />

    </td>
  </tr>
</template>

<script setup>
import { ref, defineProps, defineEmits, computed } from 'vue'
import BotonEditar from '../ui/BotonEditar.vue';
import BotonEliminar from '../ui/BotonEliminar.vue';
import TagColorSelector from './TagColorSelector.vue';
import BotonGuardar from '../ui/BotonGuardar.vue';
import BotonCerrar from '../ui/BotonCerrar.vue';


const props = defineProps({
  tag: Object,
  editandoId: String,
  coloreandoId: Number
})

const emit = defineEmits(['editando', 'guardar', 'eliminar', 'etiquetando', 'toggle-checked', 'coloreando', 'colorear'])

const nombre = ref(props.tag?.nombre || '')
const meEditan = computed(
  () => props.tag && props.editandoId === props.tag.id
)
const meColorean = computed(
  () => props.coloreandoId === props.tag?.id
)

function empezarEditar() {
  if (!props.tag) return
  nombre.value = props.tag.nombre
  emit('editando', props.tag.id)
}

function cancelarEditar() {
  emit('editando', null)
}

function guardarEdicion() {
  emit('guardar', {
    id: props.tag.id,
    nombre: nombre.value
  })
}

function eliminar() {
  emit('eliminar', props.tag.id)
}

function colorear(){
  emit('coloreando', props.tag.id)
}

function cerrar(){
  emit('coloreando', null)
}

</script>
