<template>
<button class="button rounded">
    <slot></slot>
</button>
</template>

<script>
export default {
name: "ButtonTwo",
};
</script>

<style scoped>
.button {
    color: var(--custom-dark-text-color);
    border: 1px solid var(--custom-dark-background-color);
    background: transparent;
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
