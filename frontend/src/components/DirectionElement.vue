<template>
<div class="row mx-0 px-0" :data-aos="isReverse ? 'fade-left' : 'fade-right'">
    <div :class="['col-12 col-md-6', isReverse ? 'order-2 order-md-2' : 'order-2 order-md-1']">
        <div class="row w-100 h-100 m-0 p-0 justify-content-center align-items-center">
            <div class="col-10">
                <div class="d-flex flex-column h-100">
                    <div class="col-12 fs-1 mb-2">
                        {{ element.title }}
                    </div>
                    <div class="col-12 fs-6 fw-light mb-4">
                        {{ element.description }}
                    </div>
                    <div class="col-12 mt-auto mb-3 mb-md-0">
                        <ButtonTwo class="d-flex gap-2 px-4 py-2 fs-5 rounded-pill" @click="goToPage(element.id)">
                            <div>Перейти</div>
                            <i class="bi bi-arrow-right"></i>
                        </ButtonTwo>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="d-flex justify-content-center justify-content-md-start col-12 col-md-6 mb-3 mb-md-0" :class="['col-6', isReverse ? 'order-1 order-md-1' : 'order-1 order-md-2']">
        <div class="row w-100 h-100 m-0 p-0 justify-content-center align-items-center">
            <div class="col-10">
                <img :src="element.photo" class="img-fluid h-100 w-100" alt="">
            </div>
        </div>
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
        goToPage(id) {
            this.$router.push({ name: 'direction', params: { id } });
        }
    }
};
</script>
    
    
<style scoped>
</style>
