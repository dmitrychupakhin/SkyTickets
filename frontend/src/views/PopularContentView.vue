<template>
<div>
    <Announcement></Announcement>
    <Navbar></Navbar>
    <div class="row mx-0 px-5 my-5">
        <div class="col-12 mb-5">
            <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">А куда же мне полететь?</div>
            <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                Топ популярных направлений для путешествия
            </div>
            <div class="col-12 fs-6 text-center mb-5">
                <div class="row justify-content-center">
                    <div class="col-8 fw-light">
                        Откройте для себя лучшие места для вашего следующего приключения!
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12">
            <div class="row">
                <div class="mx-0 px-0">
                    <DirectionElementList></DirectionElementList>
                    <div class="col-12 d-flex justify-content-center">
                        <ButtonOne class="px-4 py-2 fs-5 rounded-pill">Показать еще</ButtonOne>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import DirectionElementList from "@/components/DirectionElementList"
export default {
    components: {
        DirectionElementList
    },
};
</script>

<style scoped>
    </style>
