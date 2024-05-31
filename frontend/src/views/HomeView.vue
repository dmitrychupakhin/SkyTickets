<template>
<div>
    <Navbar></Navbar>
    <div class="row mx-0 px-5 my-5">
        <div class="col-12 fs-title fw-light text-center mb-4 custom-title-color">
            Расчет стоимости авиабилета
        </div>
        <div class="col-12 fs-5 text-center fw-light">
            Сервис поможет подобрать вам удобный маршут, исходя из ваших предпочтений,<br /> с учётом ваших финансовых возможностей.
        </div>
        <div class="position-relative d-flex justify-content-center">
            <ButtonOne class="px-4 py-2 fs-5 rounded-pill position-absolute z-2 mt-4">Расчитать</ButtonOne>
        </div>
        <div class="col-12 position-relative video-container mx-0 px-0" data-aos="fade-up">
            <img class="position-absolute video-overlay" :src="require('@/assets/home-video-head.svg')" alt="Overlay">
            <div class="hero-glass-windows">
                <div class="hero-glass-col opacity-0"></div>
                <div class="hero-glass-col d-none d-md-flex"></div>
                <div class="hero-glass-col d-none d-md-flex"></div>
                <div class="hero-glass-col d-none d-lg-flex"></div>
                <div class="hero-glass-col"></div>
                <div class="hero-glass-col"></div>
                <div class="hero-glass-col opacity-0"></div>
            </div>
            <video autoplay muted loop class="video">
                <source :src="require('@/assets/home-video.mp4')" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
    <div class="row mx-0 px-5 my-5" data-aos="fade-up">
        <div class="col-12 border custom-border-color">
            <div class="row m-0 p-4">
                <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Расчет стоимости</div>
                <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                    Современно. Быстро. Точно.
                </div>
                <div class="col-12 fs-6 text-center">
                    <div class="row justify-content-center">
                        <div class="col-8">
                            ВЫ не можете уложиться в бюджет? Или просто не хотите продумывать всё до мелочей.
                            Данный сервис сделает это за вас, используя математические алгоритмы. 
                        </div>
                    </div>
                </div>
                <div class="col-12" style="height: 40vh;">

                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-5 my-5" data-aos="fade-up">
        <div class="col-12 px-0">
            <div class="row m-0">
                <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Популярные места</div>
                <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                    Популярные места для этого направления
                </div>
                <div class="col-12 fs-6 text-center mb-5">
                    <div class="row justify-content-center">
                        <div class="col-8">
                            Выберите направление, и наш сервис предоставит вам список значимых и интересных мест для отдыха.  
                        </div>
                    </div>
                </div>
                <div class="mx-0 px-0">
                    <DirectionElementList></DirectionElementList>
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-5 py-5 custom-purple-background-color custom-light-text-color">
        <div class="col-12 fs-5 px-0 mb-5 text-center">
            Не знаете куда полететь?
        </div>
        <div class="col-12">
            <div class="row justify-content-center">
                <div class="col-10 border custom-border-color py-5 px-5">
                    <div class="row">
                        <div class="col-6 fs-1">
                            Топ популярных<br/>
                            мест для <br/>
                            путешествия
                        </div>
                        <div class="col-6">
                            <div class="row h-100">
                                <div class="col-12 fs-5 mb-3 d-flex align-self-end fw-light">
                                    Места избраные людьми
                                </div>
                                <div class="col-12">
                                    <ButtonOne class="px-4 py-2 fs-5 rounded-pill">Узнать больше</ButtonOne>
                                </div>
                            </div>
                        </div>
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
.hero-glass-col {
    background: var(--custom-light-background-color) !important;
    width: 34px;
    height: 100%;
}
.hero-glass-windows {
    justify-content: space-between;
    display: flex;
    position: absolute;
    top: 0%;
    bottom: 0%;
    left: 0%;
    right: 0%;
}
.video-container {
    width: 100%;
    overflow: hidden;
}

.video {
    width: 100%;
    height: auto;
}

.video-overlay {
    top: 0;
    left: -10px;
    width: calc(100% + 20px);
    height: auto;
}
</style>
