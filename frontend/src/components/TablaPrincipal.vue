<template>
    <table id="app">
        <FilaElemento 
        v-for="fila in filas" 
        :key="fila.id" 
        :fila="fila"
        :editando="editando"
        @editar-fila="editarFila"
        @eliminar-fila="eliminarFila"
        />
        <AgregarElemento />
    </table>
</template>

<script>
import AgregarElemento from './AgregarElemento.vue';
import FilaElemento from './FilaElemento.vue';
import axios from 'axios';

export default {
    name: "TablaPrincipal",
    components: {
        FilaElemento,
        AgregarElemento
    },
    mounted() {
        this.obtenerFilas();
    },

    data() {
        return {
            filas: [],
            editando: -1,
        }
    },
    methods: {
        editarFila(fila) {
            this.editando = fila.id;
            // Lógica para editar la fila
        },
        eliminarFila(fila) {
            console.log("Eliminar fila desde TablaPrincipal", fila.id);
            this.obtenerFilas();
            // Lógica para eliminar la fila
        },
        AgregarElemento() {
            this.obtenerFilas();
        },
        obtenerFilas() {
            const url = process.env.VUE_APP_API_URL;
            axios.get(`${url}/api/elementos/listar`)
                .then(response => {
                    this.filas = response.data;
                })
                .catch(error => {
                    console.error("Error al obtener las filas", error);
                });
        }
    }
}

</script>