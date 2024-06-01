<template>
<div>
    <Navbar></Navbar>
    <div class="row mx-1 mx-md-5 justify-content-center mb-5 mt-2" style="min-height: 100vh;">
        <div class="col-9">
            <div v-if="isLoading" class="d-flex justify-content-center align-items-center" style="min-height: 100vh;">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Загрузка...</span>
                </div>
            </div>
            <div v-else>
                <div class="row position-relative border-bottom py-4">
                    <div class="col-4">
                        <div class="profile-image ratio ratio-1x1" :style="{ 'background-image': `url(${profileImage})` }"></div>
                    </div>
                    <div class="col-8">
                        <div class="ps-4 position-relative h-100 d-flex">
                            <div class="w-100">
                                <div class="col-12 fw-light mb-2 fst-italic">{{ profileTitle }}</div>
                                <div class="col-12 fs-1 fw-bold z-3 w-auto">{{ fullName }}</div>
                                <div class="col-12 fs-6 fw-light mb-2 fw-normal">@{{ username }}</div>
                                <div class="col-12 mb-3 fw-light z-3 w-auto">{{ about }}</div>
                                <div class="col-12 z-3 w-auto">
                                    <div class="d-flex gap-2 mb-1 z-3 w-auto">
                                        <div><i class="bi bi-telephone"></i></div>
                                        <div>{{ phone }}</div>
                                    </div>
                                    <div class="d-flex gap-2 mb-2 z-3 w-auto">
                                        <div><i class="bi bi-envelope"></i></div>
                                        <div>{{ email }}</div>
                                    </div>
                                    <div class="d-flex gap-2 mb-2 z-3 w-auto">
                                        <div><i class="bi bi-calendar"></i></div>
                                        <div>{{ birthdate }}</div>
                                    </div>
                                    <div class="d-flex gap-2 mb-2 z-3 w-auto">
                                        <div><i class="bi bi-geo-alt"></i></div>
                                        <div>{{ location }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="d-flex flex-column align-items-end justify-content-between">
                                <router-link :to="{ name: 'profile-edit' }" class="bi bi-pencil fs-4 custom-dark-text-color z-2" style="background: transparent; border: none;"></router-link>
                                <button @click="logout" class="d-flex gap-2 align-items-center z-4" style="background: transparent; border: none;">
                                    <i class="bi bi-box-arrow-left fs-4"></i>
                                    <div class="d-flex fs-5">
                                        Выйти
                                    </div>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row pt-2">
                    <div class="col-12 text-center fs-2">
                        Контент в зависимости от содержимого сайта
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import axiosApiInstanceAuth from '@/api';
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

const profileImage = ref('');
const profileTitle = ref('');
const fullName = ref('');
const username = ref('');
const about = ref('');
const phone = ref('');
const email = ref('');
const birthdate = ref('');
const location = ref('');
const isLoading = ref(true);

const fetchUserData = async () => {
    try {
        const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/users/${authStore.userInfo.userId}/`);
        const userData = response.data;
        console.log(userData);
        profileImage.value = userData.photo;
        profileTitle.value = userData.profileTitle || 'Пользователь';
        fullName.value = `${userData.first_name} ${userData.last_name}`;
        username.value = userData.username;
        about.value = userData.about;
        phone.value = userData.phone_number;
        email.value = userData.email;
        birthdate.value = userData.date_birth;
        location.value = userData.location;
    } catch (error) {
        console.error('Error fetching user data:', error);
    } finally {
        isLoading.value = false;
    }
};

onMounted(fetchUserData);

const logout = () => {
    authStore.logout();
    localStorage.removeItem('userTokens');
    router.push({ name: 'sign-in' });
};
</script>
  
  
<style scoped>
.profile-image {
    background-size: cover;
    background-position: center;
}
</style>
