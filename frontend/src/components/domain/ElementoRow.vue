<template>
  <tr>
    <td>
      <CheckBoxGeneral
        :model-value="elemento.checked"
        @update:model-value="onToggle"
      />

    </td>
    <td>
      <template v-if="meEditan">
        <input v-model="nombre" />
      </template>
      <template v-else>
        {{ elemento.nombre }}
      </template>
    </td>

    <td>
      <span v-if="!meEditan">
        <BotonEditar @click="empezarEditar()"/>
        <BotonEliminar @click="eliminar()"/>
      </span>
      <span v-else>
        <BotonGuardar @click="guardarEdicion()"/>
        <BotonCerrar @click="cancelarEditar()"/>
      </span>
    </td>
    <td>
      <ElementoTagsHover
        :all-tags="tagsStore.tags"
        :selected-ids="elemento.tags"
          @update="ids => emitirEtiquetado(ids)"
      />
      <span v-if="hayMasTags">...</span>
    </td>
  </tr>
</template>

<script setup>
import { ref, defineProps, defineEmits, computed } from 'vue'
import BotonEditar from '../ui/BotonEditar.vue';
import BotonEliminar from '../ui/BotonEliminar.vue';
import CheckBoxGeneral from '../ui/CheckBoxGeneral.vue';
import ElementoTagsHover from '../ui/ElementoTagsHover.vue';
import { useTagsStore } from '@/stores/tags';
import BotonCerrar from '../ui/BotonCerrar.vue';
import BotonGuardar from '../ui/BotonGuardar.vue';


const props = defineProps({
  elemento:{
    type: Object,
    required: true
  },
  editandoId: {
    type: Number
  }
})

console.log(props.editandoId===props.elemento.id)

const emit = defineEmits(['editando', 'guardar', 'eliminar', 'etiquetando', 'toggle-checked'])
const tagsStore = useTagsStore()

const nombre = ref(props.elemento.nombre)
const meEditan = computed(
  () => props.editandoId===props.elemento.id
)

const hayMasTags = computed(() => {
  return props.elemento.tags && props.elemento.tags.length > 2
})

function empezarEditar() {
  nombre.value = props.elemento.nombre
  emit('editando', props.elemento.id)
}

function cancelarEditar() {
  emit('editando', null)
}

function guardarEdicion() {
  emit('guardar', {
    id: props.elemento.id,
    nombre: nombre.value
  })
}

function emitirEtiquetado(ids) {
  emit('etiquetando', {
    elementoId: props.elemento.id,
    tags: ids
  })
}


function eliminar() {
  emit('eliminar', props.elemento.id)
  console.log(props.elemento.id)
}

function onToggle(valor) {
  emit('toggle-checked', {
    id: props.elemento.id,
    checked: valor
  })
}


</script>
