<template>
<div>
    <Announcement></Announcement>
    <Navbar></Navbar>
    <div class="row mx-0 px-1 px-md-5 mb-4 mt-4">
        <div class="col-12 mb-5 px-1 px-md-4">
            <div class="row">
                <div class="col-12 text-center fs-title fw-normal custom-title-color mb-3">
                    {{ cityName }}
                </div>
                <div class="col-12 fs-6 text-center fw-light mb-5">
                    <div class="row justify-content-center">
                        <div class="col-12 col-md-8">
                            {{ cityDescription }}
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <div class="row justify-content-center">
                        <img class="col-10 col-md-5" :src="cityImage" alt="Overlay">
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-1 px-md-5 mb-4" data-aos="fade-up">
        <div class="col-12 px-0">
            <div class="row m-0">
                <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Что там интересного?</div>
                <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                    Факты & Нейросеть
                </div>
                <div class="col-12 fs-6 text-center mb-5">
                    <div class="row justify-content-center">
                        <div class="col-12 col-md-8 fw-light">
                            Здесь вы найдете уникальные и интересные факты о нашем городе,
                            которые были сгенерированы с помощью передовой нейросетевой технологии.
                            Наша нейросеть анализирует огромные объемы данных,
                            чтобы предложить вам самые захватывающие и удивительные сведения, которые вы, возможно,
                            еще не знали..
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-if="isFactsLoading" class="row justify-content-center mx-0 mb-4">
        <div class="spinner-border" style="color: var(--custom-purple-color);" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>
    <div v-else class="row mx-0 px-1 px-md-5 mb-4" data-aos="fade-up">
        <div class="col-12 mx-0 px-0">
            <div class="row px-0 px-md-0 mx-md-0">
                <div class="col-12 col-md-6 pb-2 p-md-3" v-for="(fact, index) in facts" :key="fact.title" :class="{ 'ps-md-0': index % 2 === 0, 'pe-md-0': index % 2 !== 0 }">
                    <div class="row w-100 h-100 mx-0 border custom-border-color p-4 p-md-5">
                        <div class="col-12 text-center fs-4 mb-2">{{ fact.title }}</div>
                        <div class="col-12 d-flex justify-content-center mb-3">
                            <div class="pb-2 border-bottom custom-border-color" style="width: 60px;"></div>
                        </div>
                        <div class="col-12 text-center fs-6 fw-light">{{ fact.description }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-1 px-md-5 mb-2" data-aos="fade-up">
        <div class="col-12 px-0">
            <div class="row m-0 py-5 border custom-border-color">
                <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Куда здесь можно сходить?</div>
                <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                    Интересные места города {{ cityName }}
                </div>
                <div class="col-12 fs-6 text-center">
                    <div class="row justify-content-center">
                        <div class="col-8 fw-light">
                            Откройте для себя самые захватывающие и примечательные места нашего города!
                            Наш раздел "Интересные места города" предлагает подборку мест, которые стоит посетить.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-1 px-md-5 my-5" data-aos="fade-up">
        <div class="col-12 px-0">
            <div class="row m-0">
                <div class="mx-0 px-0">
                    <PlaceElementList :elements="places"></PlaceElementList>
                    <!-- <div class="col-12 d-flex justify-content-center">
                        <ButtonOne class="px-4 py-2 fs-5 rounded-pill" @click="fetchFactsData">Показать еще</ButtonOne>
                    </div> -->
                </div>
            </div>
        </div>
    </div>
    <Footer></Footer>
</div>
</template>

<script>
import axiosApiInstanceAuth from '../api';
import axios from 'axios';
import PlaceElementList from "@/components/PlaceElementList"
import { useAuthStore } from '@/store/auth';
import { computed } from 'vue';

export default {
    components: {
        PlaceElementList
    },
    data() {
        return {
            places: [],
            cityName: '',
            cityDescription: '',
            cityImage: '',
            facts: [],
            isFactsLoading: true
        };
    },
    methods: {
        async fetchData() {
            const id = this.$route.params.id;
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/directions/${id}/`);
                const cityData = response.data;
                this.cityName = cityData.city,
                    this.cityDescription = cityData.description,
                    this.cityImage = cityData.photo
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
            try {
                const id = this.$route.params.id;
                const authStore = useAuthStore();
                if (!(computed(() => authStore.userInfo.token).value)) {
                    const response = await axios.get(`http://127.0.0.1:8000/api/directions/${id}/places`);
                    const cityData = response.data;
                    console.log(cityData);
                    this.places = cityData.map((place) => ({
                        id: place.id,
                        title: place.title,
                        photo: place.photo,
                        description: place.description,
                    }));
                }
                else{
                    const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/directions/${id}/places`);
                    const cityData = response.data;
                    console.log(cityData);
                    this.places = cityData.map((place) => ({
                        id: place.id,
                        title: place.title,
                        photo: place.photo,
                        description: place.description,
                        isFavorite: place.saved
                    }));
                }
            } catch (error) {
                console.error('Error fetching places data:', error);
            }
        },
        async fetchFactsData() {
            const id = this.$route.params.id;
            try {
                const response = await axios.post(`http://127.0.0.1:8000/api/directions/facts/`, {
                    direction: id
                });
                const cityData = response.data;
                console.log(cityData);
                const factsArray = Object.entries(response.data).map(([key, value]) => ({ title: key, description: value }));
                this.facts = factsArray;
                this.isFactsLoading = false;
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        },
    },
    created() {
        this.fetchData();
        this.fetchFactsData();
    }
};
</script>

<style scoped>
/* Ваши стили */
</style>
