<template>
    <div>
        <Announcement></Announcement>
        <Navbar></Navbar>
        <div class="row mx-0 px-1 px-md-5 my-5">
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
                        <DirectionElementList :elements="cities"></DirectionElementList>
                        <div v-if="count != page" class="col-12 d-flex justify-content-center">
                            <ButtonOne class="px-4 py-2 fs-5 rounded-pill" @click="loadMoreCities">Показать еще</ButtonOne>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer></Footer>
    </div>
    </template>
    
    <script>
    import axios from 'axios';
    import DirectionElementList from "@/components/DirectionElementList"
    import ButtonOne from "@/components/UI/ButtonOne"
    
    export default {
        components: {
            DirectionElementList,
            ButtonOne
        },
        data(){
            return {
                cities: [],
                page: 1,
                count: 0
            }
        },
        methods: {
            async fetchCities() {
                try {
                    const response = await axios.get(`http://127.0.0.1:8000/api/directions/popular/?page=${this.page}&page_size=1`);
                    const cityData = response.data;
                    console.log(cityData);
                    this.count = response.data.count;
                    const newCities = cityData.results.map((city) => ({
                        id: city.id,
                        title: city.city,
                        photo: city.photo,
                        description: city.description
                    }));
                    // Append new cities to the existing list
                    this.cities = [...this.cities, ...newCities];
                } catch (error) {
                    console.error('Error fetching city data:', error);
                }
            },
            loadMoreCities() {
                this.page += 1;
                this.fetchCities();
            }
        },
        created() {
            this.fetchCities();
        }
    };
    </script>

<style scoped>
    </style>
