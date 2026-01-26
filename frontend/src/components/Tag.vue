<template>
    <div class="tag">
        <span class="tag-text">{{ text }}</span>
    </div>
</template>

<script>
export default {
    name: "Tag",
    props: {
        text: String
    }
}
</script>