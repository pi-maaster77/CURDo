<template>
  <tr>
    <td>
        <input v-model="nombre" />
    </td>
        <BotonCrear @click="crear"/>
    <td>    
    </td>
    <td>
      <!--<BotonColor :tag="tag"/>--> 
    </td>
  </tr>
</template>

<script setup>
import { ref, defineEmits} from 'vue'
import BotonCrear from '../ui/BotonCrear.vue';
// import BotonColor from '../ui/BotonColor.vue';

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
