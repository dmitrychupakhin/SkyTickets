<template>
    <div>
        <div class="col-12" style="overflow-x: hidden;">
            <PlaceElement class="mb-5 pb-3" v-for="(element, index) in elements" :key="element.id" :element="element" :isReverse="isOdd(index)" />
        </div>
    </div>
    </template>
    
    <script>
    import PlaceElement from "@/components/PlaceElement"
    export default {
        name: "PlaceElementList",
        components: {
            PlaceElement
        },
        props: {
            elements: {
                type: Array,
                required: true,
            },
        },
        methods: {
            isOdd(index) {
                return index % 2 !== 0; // Возвращает true, если индекс нечетный
            }
        }
    };
    </script>
    
    <style scoped>
    /* Дополнительные стили (если нужны) */
    </style>
    