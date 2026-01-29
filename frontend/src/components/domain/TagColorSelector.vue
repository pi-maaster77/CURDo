<template>
  <div class="color-wrapper">
    <BotonColor
      :color="tag.color"
      @click="colorear"
    />
    <span v-if="meColorean">  
      <TagColorPicker

        :colores="coloresStore.colores"
        :selected-id="tag.color?.id"
        @seleccionar="seleccionar"
        @cerrar="cerrar"
        @crear="crear"
        @eliminar="eliminar"
      />
    </span>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import { useColorsStore } from '@/stores/colores'
import BotonColor from '../ui/BotonColor.vue'
import TagColorPicker from './TagColorPicker.vue'
import { useTagsStore } from '@/stores/tags'

const props = defineProps({
  tag: Object, 
  meColorean: Boolean
})

const emit = defineEmits(['change', 'colorear', 'cerrar'])

const coloresStore = useColorsStore()
const tagsStore = useTagsStore()

console.log("colores:", coloresStore.colores)


function seleccionar(color) {
  tagsStore.editar({id: props.tag.id, color_id:color.colorId})
}
function colorear(){
  emit('colorear')
}
function cerrar(){
  emit('cerrar')
}
function crear(payload){
  coloresStore.crear(payload)
}
function eliminar(payload){
  coloresStore.eliminar(payload)
}

</script>

