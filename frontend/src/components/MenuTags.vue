<template>
    <div id="app">
        <h1>Menú de Tags</h1>
        <p>Tags para el elemento: {{ fila.id }}</p>
    </div>
</template>

<script>
export default {
    name: "MenuTags",

    props: {
        fila: Object
    }
}
</script>