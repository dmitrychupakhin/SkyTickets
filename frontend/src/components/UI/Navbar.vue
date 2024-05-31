<template>
    <nav class="navbar d-flex flex-column sticky-top navbar-expand-xl navbar-light bg-white mb-0 pb-0 custom-border-color px-1 px-md-5 custom-light-background-color">
        <div class="container-fluid px-5 px-md-4 border-bottom">
            <router-link :to="{name: 'home'}"  class="navbar-brand nav-link mx-2 active fw-light custom-color-title" href="#" aria-current="page">
                <div class="d-flex gap-3">
                    <div class="d-flex justify-content-center align-items-center">
                        <i class="bi bi-app-indicator fs-2"></i>
                    </div>
                    <div class="fs-5 fw-normal">
                        <div>Крутецкий</div>
                        <div>Сайт</div>    
                    </div>
                </div>
            </router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown"
                aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
    
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav ms-auto gap-3 gap-xl-0 my-3 my-xl-0 ">
                    <li class="nav-item">
                        <router-link :to="{name: 'home'}" class="custom-nav-link mx-3 fw-light" href="#" aria-current="page">Главная страница</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{name: 'home'}" class="custom-nav-link mx-3 fw-light" href="#" aria-current="page">Контент</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{name: 'home'}" class="custom-nav-link mx-3 fw-light" href="#" aria-current="page">Контент</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="custom-nav-link mx-3 fw-light" href="#">Контент</a>
                    </li>
                    
                </ul>
                <ul v-if="token" class="navbar-nav ms-auto col-12 col-xl-auto d-inline-flex">
                    <li class="nav-item mx-0">
                        <router-link class="custom-nav-link d-flex justify-content-center align-items-center flex-column" :to="{name: 'home'}">
                            <i class="bi bi-person-circle fs-5"></i>
                            <span class="d-block fs-6 fw-normal">Профиль</span>
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
import {computed} from 'vue'
import {useAuthStore} from '@/store/auth'
import { useRouter } from 'vue-router';

const authStore = useAuthStore()

const token = computed(() => authStore.userInfo.token);

</script>

<style scoped>
    .custom-nav-link{
    color: var(--custom-description-color) !important;
    text-decoration: none;
    }
    .custom-nav-link:hover{
        color:  var(--custom-dark-text-color) !important;
    }
</style>
  