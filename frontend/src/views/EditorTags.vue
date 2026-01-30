<template>
    <table class="table table-striped table-hover">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Color</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <TagRow 
                v-for="tag in tagsStore.tags"
                :key="tag.id"
                :tag="tag"
                :editando-id="editandoId"
                :coloreando-id="coloreandoId"
                @editando="editando"
                @guardar="guardarEdicion"
                @eliminar="eliminar"
                @coloreando="coloreando"
            />

            <AgregarTag
            @crear="crear"
            />
        </tbody>
    </table>
</template>

<script setup>
import AgregarTag from '@/components/domain/AgregarTag.vue';
import TagRow from '@/components/domain/TagRow.vue';
import { useTagsStore } from '@/stores/tags';
import { useColorsStore } from '@/stores/colores';
import { onMounted, ref } from 'vue';

const tagsStore = useTagsStore()
const coloresStore = useColorsStore()

onMounted(async () => {
    await tagsStore.cargar()
    await coloresStore.cargar()
})


const editandoId= ref(null)
const coloreandoId= ref(null)

function crear({nombre, color}) {
    tagsStore.crear({nombre: nombre, color_id: color})
    console.log()
}

function editando(id){
    editandoId.value = id
}

function guardarEdicion(tag){
    if(tag === null) return
    tagsStore.editar(tag)
    console.log(tag)
    editandoId.value = null
}

function eliminar(id){
  tagsStore.eliminar(id)
}

function coloreando(id){
    coloreandoId.value = id
}



</script>