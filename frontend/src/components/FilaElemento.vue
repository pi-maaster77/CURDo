<template>
    <tr id="app">
        <td><input type="checkbox" name="" id="" v-model="checkedEditable" v-on:change="tickedChange"></td>
        <td>{{ fila.id }}</td>
        <td><span v-if="editando!=fila.id">{{ nombreEditable }}</span><input type="text" v-model="nombreEditable" v-if="editando==fila.id"></td>
        <td><BotonEditar :fila="fila" @click="editar()"/><BotonEliminar :fila="fila" @click="eliminar()"/><Tags :fila="fila" /></td>
        <td><TagsElemento :fila="fila" /></td>
    </tr>
</template>

<script>
import axios from 'axios';
import BotonEditar from './botones/Editar.vue';
import BotonEliminar from './botones/Eliminar.vue';
import Tags from './botones/Tags.vue';
import TagsElemento from './TagsElemento.vue';

export default {
    name: "FilaElemento",
    components: {
        BotonEditar,
        BotonEliminar,
        Tags,
        TagsElemento
    },
    props: {
        fila: Object,
        editando: -1
    },
    methods: {
        editar: function(){
            console.log("Editar fila", this.fila.id);
            if (this.editando == this.fila.id) {
                axios.patch(`${this.url}/api/elementos/editar`, {
                    id: this.fila.id,
                    nombre: this.nombreEditable
                }).then(response => {
                    console.log(response.data);
                }).catch(error => {
                    console.error("Error al actualizar la fila", error);
                });
                this.$emit('editar-fila', -1);
            } else {
                this.$emit('editar-fila', this.fila);
            }
        },
        eliminar: function(){
            console.log("Eliminar fila", this.fila.id);
            this.$emit('eliminar-fila', this.fila); 
        },
        tickedChange: function(){
            console.log("Cambio en checkbox fila", this.fila.id, this.checkedEditable);
            // Lógica para manejar el cambio del checkbox
            axios.patch(`${this.url}/api/elementos/editar`, {
                id: this.fila.id,
                checked: this.checkedEditable
            }).then(response => {
                console.log(response.data);
            }).catch(error => {
                console.error("Error al actualizar el checkbox", error);
            });
        }
    },
    data() {
        return {
            nombreEditable: this.fila.nombre,
            checkedEditable: this.fila.checked,
            url: process.env.VUE_APP_API_URL
        }
    }
}
</script>
<style scoped>
#app {
    border: 1px solid black;
    padding: 10px;
    margin: 10px;
}
</style>