<template>
    <button class="button rounded">
        <slot></slot>
    </button>
    </template>
    
    <script>
    export default {
    name: "ButtonTree",
    };
    </script>
    
    <style scoped>
        .button{
            color: var(--custom-light-text-color);
            border: 1px solid var(--custom-light-background-color);
            background: transparent;
        }
        .button:hover{
            border: 1px solid var(--custom-purple-color);
            background: var(--custom-purple-color);
            color: var(--custom-light-text-color);
        }
        .button:active{
            background: var(--custom-purple-color-active);
        }
    </style>
    