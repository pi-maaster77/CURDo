<template>
    <tr id="app">
        <td><input type="checkbox" name="" id="" disabled></td>
        <td>-</td>
        <td><input type="text" v-model="nombre"></td>
        <td><BotonAgregar @click="agregarElemento()"/></td>
        <td><TagsElemento :fila="fila" /></td>
    </tr>
</template>
<script>
import BotonAgregar from './botones/Agregar.vue';
import axios from 'axios';

export default {
    name: "AgregarElemento",
    components: {
        BotonAgregar
    },
    methods: {
        agregarElemento: function(){
            console.log("Agregar elemento", this.nombre);
            const url = process.env.VUE_APP_API_URL;
            axios.post(`${url}/api/elementos/crear`, { nombre: this.nombre });
            this.$emit('agregar-elemento', this.nombre);
            this.nombre = '';
        }
    },
    data() {
        return {
            nombre: '',
        }
    }
}
</script>