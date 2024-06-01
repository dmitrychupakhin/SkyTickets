<template>
<div>
    <div class="col-12" style="overflow-x: hidden;">
        <DirectionElement class="mb-5 pb-3" v-for="(element, index) in elements" :key="element.id" :element="element" :isReverse="isOdd(index)" />
    </div>
</div>
</template>

  
  
<script>
import DirectionElement from "@/components/DirectionElement"
export default {
    name: "DirectionElementList",
    components: {
        DirectionElement
    },
    data() {
        return {
            elements: [
                { id: 1, name: "Element 1" },
                { id: 2, name: "Element 2" },
                { id: 3, name: "Element 3" },
            ]
        };
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
