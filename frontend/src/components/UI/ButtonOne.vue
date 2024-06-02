<template>
<button class="button rounded">
    <slot></slot>
</button>
</template>

<script>
export default {
    name: "ButtonOne",
};
</script>

<style scoped>
.button {
    color: var(--custom-light-text-color);
    border: 1px solid var(--custom-dark-background-color);
    background: var(--custom-dark-background-color);
}

.button:hover {
    border: 1px solid var(--custom-purple-color);
    background: var(--custom-purple-color);
    color: var(--custom-light-text-color) !important;
}

.button:hover ::v-deep .router-link {
    color: var(--custom-light-text-color) !important;
}

.button:active {
    background: var(--custom-purple-color-active);
}
</style>
