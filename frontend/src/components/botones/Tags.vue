<template>
        
        <button @click="isVisible = !isVisible">
           🏷️ 
        </button>
        
        <div><span v-if="isVisible"><MenuTags :fila="fila"/></span></div>
</template>

<script>
import MenuTags from '../MenuTags.vue';

export default {
    name: "MiComponente",
    components: {
        MenuTags
    },
    props: {
        fila: Object
    },
    data() {
        return {
            isVisible: false
        }
    }
} 
</script>