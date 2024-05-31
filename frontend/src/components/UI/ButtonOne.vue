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
    .button{
        color: var(--custom-light-text-color);
        border: none;
        background: var(--custom-dark-background-color);
    }
    .button:hover{
        background: var(--custom-dark-background-color-hover);
    }
    .button:active{
        background: var(--custom-dark-background-color-active);
    }
</style>
