<template>
    <EntradaTexto v-model="nombre"/><BotonCrear @click="crear()" />
</template>
<script setup>
import { defineEmits } from 'vue';

import BotonCrear from '../ui/BotonCrear.vue';
import EntradaTexto from '../ui/EntradaTexto.vue';

const emit = defineEmits(["agregar-elemento"])

let nombre = ""

function crear(){
    emit('agregar-elemento', nombre)
}

</script>