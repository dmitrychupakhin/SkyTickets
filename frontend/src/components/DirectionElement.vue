<template>
<div class="row mx-0 px-0" :data-aos="isReverse ? 'fade-left' : 'fade-right'">
    <div :class="['col-6', isReverse ? 'order-2' : 'order-1']">
        <div class="d-flex flex-column h-100">
            <div class="col-12 fs-1 mb-2">
                Москва
            </div>
            <div class="col-12 fs-6 fw-light">
                Вы не можете уложиться в бюджет? Или просто не хотите продумывать всё до мелочей.
                Данный сервис сделает это за вас, используя математические алгоритмы.
            </div>
            <div class="col-12 mt-auto">
                <ButtonTwo class="d-flex gap-2 px-4 py-2 fs-5 rounded-pill" @click="goToPage">
                    <div>Перейти</div>
                    <i class="bi bi-arrow-right"></i>
                </ButtonTwo>
            </div>
        </div>
    </div>
    <div :class="['col-6', isReverse ? 'order-1' : 'order-2']">
        <img :src="require('@/assets/image 7.png')" class="img-fluid" alt="">
    </div>
</div>
</template>

<script>
export default {
    name: "DirectionElement",
    props: {
        element: {
            type: Object,
            required: true,
        },
        isReverse: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        goToPage() {
            this.$router.push({ name: 'direction' }); 
        }
    }
};
</script>

<style scoped>
            
    </style>
