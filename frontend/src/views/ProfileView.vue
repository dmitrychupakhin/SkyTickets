<template>
<div>
    <Navbar></Navbar>
    <div class="row mx-0 px-1 px-md-5 mb-4 mt-4 ">
        <div class="col-12 mx-0 px-0">
            <div v-if="isLoading" class="d-flex justify-content-center align-items-center" style="min-height: 100vh;">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Загрузка...</span>
                </div>
            </div>
            <div v-else>
                <div class="row px-0 mx-0 position-relative justify-content-center">
                    <div class="col-12 d-flex justify-content-center">
                        <div class="col-5 col-md-2">
                            <div class="profile-image ratio ratio-1x1 mb-2" style="border-radius: 50%;" :style="{ 'background-image': `url(${profileImage})` }"></div>
                        </div>
                    </div>
                    <div class="col-12 fs-2 fw-light z-3 d-flex text-nowrap w-auto mb-2">
                        <div>
                            {{ fullName }}
                        </div>
                        <button @click="goToPage" class="d-flex justify-content-center gap-2 align-items-center z-4 fs-5" style="height: 100%; aspect-ratio: 1; background: transparent; border: none;">
                            <div class="bi bi-pencil fs-4"></div>
                        </button>
                    </div>
                    <div class="col-12 text-center fs-5 fw-light mb-3">@{{ username }}</div>
                    <div class="col-12 z-3 w-auto fw-light flex-column flex-md-row d-flex gap-4 mb-2">
                        <div class="d-flex gap-2 mb-1 z-3 w-auto text-nowrap">
                            <div><i class="bi bi-telephone"></i></div>
                            <div>{{ phone }}</div>
                        </div>
                        <div class="d-flex gap-2 mb-2 z-3 w-auto text-nowrap">
                            <div><i class="bi bi-envelope"></i></div>
                            <div>{{ email }}</div>
                        </div>
                        <div class="d-flex gap-2 mb-2 z-3 w-auto text-nowrap">
                            <div><i class="bi bi-calendar"></i></div>
                            <div>{{ birthdate }}</div>
                        </div>
                        <div class="d-flex gap-2 mb-2 z-3 w-auto text-nowrap">
                            <div><i class="bi bi-geo-alt"></i></div>
                            <div>{{ location }}</div>
                        </div>
                    </div>
                    <router-link :to="{name: 'edit-password'}" class="col-12 fw-lighter text-center custom-dark-text-color text-decoration-none">
                        Поменять пароль?
                    </router-link>
                    <div class="col-12 p-4">
                        <div class="position-relative h-100 d-flex flex-column justify-content-center">
                            <div class="d-flex align-items-end justify-content-center">
                                <ButtonOne @click="logout" class="d-flex gap-2 align-items-center z-4 px-4 py-2 fs-5 rounded-pill">
                                    <i class="bi bi-box-arrow-left fs-4"></i>
                                    <div class="d-flex fs-5">
                                        Выйти
                                    </div>
                                </ButtonOne>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-1 px-md-5 my-5">
        <div class="col-12 mb-5 border custom-border-color p-4">
            <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Сохраненные места</div>
            <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                Места которые вы сохранили
            </div>
            <div class="col-12 fs-6 text-center mb-5">
                <div class="row justify-content-center">
                    <div class="col-8 fw-light">
                        Вам приглянулись какие-то места, но вы не можете себе позволить посетить их в данный момент.
                        Создайте свой список мечты для будущих поездок.
                    </div>
                </div>
            </div>
            <PlaceElementList :elements="places"></PlaceElementList>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import PlaceElementList from "@/components/PlaceElementList";
import { ref, onMounted } from 'vue';
import axiosApiInstanceAuth from '@/api';
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';

export default {
    components: {
        PlaceElementList
    },
    data() {
        return {
            places: [],
            profileImage: '',
            profileTitle: '',
            fullName: '',
            username: '',
            about: '',
            phone: '',
            email: '',
            birthdate: '',
            location: '',
            isLoading: true,
        };
    },
    computed: {
        authStore() {
            return useAuthStore();
        },
        router() {
            return useRouter();
        }
    },
    mounted() {
        this.fetchUserData();
    },
    methods: {
        async fetchUserData() {
            try {
                const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/users/${this.authStore.userInfo.userId}/`);
                const userData = response.data;
                console.log(userData);
                this.profileImage = userData.photo;
                this.profileTitle = userData.profileTitle || 'Пользователь';
                this.fullName = `${userData.first_name} ${userData.last_name}`;
                this.username = userData.username;
                this.about = userData.about;
                this.phone = userData.phone_number;
                this.email = userData.email;
                this.birthdate = userData.date_birth;
                this.location = userData.location;
            } catch (error) {
                console.error('Error fetching user data:', error);
            } finally {
                this.isLoading = false;
            }
            try {
                const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/users/${this.authStore.userInfo.userId}/favorites/`);
                const cityData = response.data;
                console.log(cityData);
                this.places = cityData.map((place) => ({
                    id: place.id,
                    title: place.title,
                    photo: place.photo,
                    description: place.description,
                    isFavorite: place.saved
                }));
            } catch (error) {
                console.error('Error fetching places data:', error);
            }
        },
        goToPage() {
            this.$router.push({ name: 'profile-edit' });
        },
        logout() {
            this.authStore.logout();
            localStorage.removeItem('userTokens');
            this.$router.push({ name: 'sign-in' });
        },
    },
};
</script>

<style scoped>
.profile-image {
    background-size: cover;
    background-position: center;
}
</style>
