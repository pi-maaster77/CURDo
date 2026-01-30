<template>
  <tr>
    <td>
      <CheckBoxGeneral disabled/>
    </td>
    <td>
        <EntradaTexto v-model="nombre"/>
    </td>

    <td>
      <span >
        <BotonCrear @click="crear()"/>
      </span>
    </td>
    <td>
        -
    </td>
  </tr>
</template>

<script setup>
import { defineEmits, ref } from 'vue'
import CheckBoxGeneral from '../ui/CheckBoxGeneral.vue';
import BotonCrear from '../ui/BotonCrear.vue';
import EntradaTexto from '../ui/EntradaTexto.vue';

const emit = defineEmits(['crear'])

const nombre = ref("")

function crear() {
  emit('crear', nombre.value)
  nombre.value = ""
}

</script>
