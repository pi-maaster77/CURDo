<template>
  <tr>
    <td>
        <EntradaTexto v-model="nombre" />
    </td>
        
    <td>  
        <BotonCrear @click="crear"/>  
    </td>
  </tr>
</template>

<script setup>
import { ref, defineEmits} from 'vue'
import BotonCrear from '../ui/BotonCrear.vue';
import EntradaTexto from '../ui/EntradaTexto.vue';

const emit = defineEmits(['crear'])

const nombre = ref("")

function crear(){
    emit("crear", {
        "nombre": nombre.value,
        "color": 1
    })
    nombre.value = ""
}

</script>
