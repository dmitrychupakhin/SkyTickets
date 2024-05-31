<template>
<nav class="navbar d-flex flex-column sticky-top navbar-expand-xl mb-0 pb-0 px-1 px-md-5" style="-webkit-backdrop-filter: saturate(180%) blur(20px) !important;
        backdrop-filter: saturate(180%) blur(20px) !important; background-color: rgba(253, 252,255,0.8) !important;">
    <div class="container-fluid px-5 px-md-4 border-bottom custom-border-color">
        <router-link :to="{name: 'home'}" class="navbar-brand nav-link mx-2 active fw-light custom-color-title" href="#" aria-current="page">
            <div class="d-flex gap-3 align-items-center">
                <img class="d-flex justify-content-center align-items-center" style="width: 70px;" :src="require('@/assets/logo.svg')">
                <div class="fs-3 fw-normal">
                    <div class="gradient-text fw-semibold">AirTickets</div>
                </div>
            </div>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav d-flex align-items-center ms-auto gap-3 gap-xl-0 my-3 my-xl-0 ">
                <li class="nav-item">
                    <router-link :to="{name: 'home'}" class="custom-nav-link mx-3 fw-normal" href="#" aria-current="page">Главная страница</router-link>
                </li>
                <li class="nav-item me-4">
                    <router-link :to="{name: 'home'}" class="custom-nav-link mx-3 fw-normal" href="#" aria-current="page">Популярные направления</router-link>
                </li>
                <ul v-if="token" class="navbar-nav ms-auto col-12 col-xl-auto d-inline-flex">
                    <li class="nav-item mx-0">
                        <router-link class="custom-nav-link d-flex justify-content-center align-items-center flex-column" :to="{name: 'home'}">
                            <ButtonTwo class="d-block fs-6 fw-normal px-4 py-2 rounded-pill">Профиль</ButtonTwo>
                        </router-link>
                    </li>
                </ul>
                <ul v-if="!token" class="navbar-nav ms-auto col-12 col-xl-auto d-inline-flex">
                    <li class="nav-item mx-0">
                        <router-link class="custom-nav-link d-flex justify-content-center align-items-center gap-2" :to="{name: 'home'}">
                            <span class="d-block fs-6 fw-normal">Войти</span>
                            <i class="bi bi-arrow-up-right fs-6"></i>
                        </router-link>
                    </li>
                </ul>
            </ul>
        </div>
    </div>
</nav>
</template>

<script>
export default {
    name: "Navbar",
    components: {},
};
</script>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/store/auth'
import { useRouter } from 'vue-router';

const authStore = useAuthStore()

const token = computed(() => authStore.userInfo.token);
</script>

<style scoped>
.gradient-text {
    background: linear-gradient(90deg, rgb(230, 135, 239), #61ced5);
    -webkit-background-clip: text;
    color: transparent;
}

.custom-nav-link {
    color: var(--custom-dark-text-color) !important;
    text-decoration: none;
}

.custom-nav-link:hover {
    color: var(--custom-purple-color) !important;
}
</style>
