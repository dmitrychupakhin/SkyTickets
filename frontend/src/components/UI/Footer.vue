<template>
<div class="row m-0 px-5 py-5 custom-light-text-color custom-dark-background-color">
    <div class="col-12 fs-4 py-5">
        Будь первым, за кого всё уже Решено.
    </div>
    <div class="col-12 fs-6 mb-5 pb-2 border-bottom custom-border-color">
        <div class="d-flex justify-content-between">
            <div class="py-3">Клиент: “не заставляйте меня думать...”</div>
            <div class="d-flex gap-2 align-items-center">
                <label for="inp_email" class="inp mb-2 w-100">
                    <input v-model="username" type="text" id="inp_email" placeholder="&nbsp;">
                    <span class="label">Почта</span>
                    <span class="focus-bg"></span>
                </label>
                <ButtonTree class="px-4 py-2 fs-6 rounded-pill" style="height:min-content; width: min-content;">Подписаться</ButtonTree>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="row justify-content-center">
            <div class="col-4 d-flex justify-content-center align-items-center gap-3">
                <img class="d-flex justify-content-center align-items-center" :src="require('@/assets/logo.svg')">
                <div class="fs-title fw-normal">
                    <div class="gradient-text fw-semibold">AirTickets</div>
                </div>
            </div>  
        </div>  
    </div>
    <div class="col-12 mt-5 mb-2 text-end align-items-end fw-lighter">
        <div>© 2024 by 2 Пальчиковые батарейки и велосипедные очки</div>
    </div>
</div>
</template>

<script>
export default {
    name: "Footer",
    components: {},
};
</script>

<style scoped>
.gradient-text {
    background: linear-gradient(90deg, rgb(230, 135, 239), #61ced5);
    -webkit-background-clip: text;
    color: transparent;
}
* {
    box-sizing: border-box;
}

.inp {
    position: relative;
    margin: auto;
    width: 100%;
    max-width: 280px;
    border-radius: 3px;
    overflow: hidden;
}

.inp .label {
    position: absolute;
    top: 20px;
    left: 12px;
    font-size: 16px;
    color: var(--custom-light-text-color);
    font-weight: 500;
    transform-origin: 0 0;
    transform: translate3d(0, 0, 0);
    transition: all .2s ease;
    pointer-events: none;
}

.inp .focus-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.05);
    z-index: -1;
    transform: scaleX(0);
    transform-origin: left;
}

.inp input {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    border: 0;
    font-family: inherit;
    padding: 16px 12px 0 12px;
    height: 56px;
    font-size: 16px;
    font-weight: 400;
    background: rgba(0, 0, 0, 0);
    box-shadow: inset 0 -1px 0 var(--custom-light-text-color);
    color: var(--custom-light-text-color);
    transition: all .15s ease;
}

.inp input:hover {
    background: rgba(0, 0, 0, 0);
    box-shadow: inset 0 -1px 0 var(--custom-light-text-color);
}

.inp input:not(:placeholder-shown)+.label {
    color: var(--custom-light-text-color);
    transform: translate3d(0, -12px, 0) scale(0.75);
}

.inp input:focus {
    background: rgba(60, 60, 60, 0);
    outline: none;
    box-shadow: inset 0 -2px 0 var(--custom-light-text-color);
}

.inp input:focus+.label {
    color: var(--custom-light-text-color);
    transform: translate3d(0, -12px, 0) scale(0.75);
}

.inp input:focus+.label+.focus-bg {
    transform: scaleX(1);
    transition: all .1s ease;
}
</style>
