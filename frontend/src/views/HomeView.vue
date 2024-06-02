<template>
<div>
    <Announcement></Announcement>
    <Navbar></Navbar>
    <div class="row mx-0 px-1 px-md-5 my-5">
        <div class="col-12 fs-title fw-light text-center mb-4 custom-title-color">
            Расчет стоимости авиабилета
        </div>
        <div class="col-12 fs-5 text-center fw-light">
            Сервис поможет подобрать вам удобный маршут, исходя из ваших предпочтений,<br /> с учётом ваших финансовых возможностей.
        </div>
        <div class="position-relative d-flex justify-content-center">
            <ButtonOne class="px-4 py-2 fs-5 rounded-pill position-absolute z-2 mt-4" @click="scrollToSection">Рассчитать</ButtonOne>
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
    <div ref="targetSection" class="row mx-0 px-1 px-md-5 my-5" data-aos="fade-up">
        <div class="col-12 border custom-border-color">
            <div class="row m-0 p-1 p-md-4">
                <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Какая будет стоимость?</div>
                <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                    Современно. Быстро. Точно.
                </div>
                <div class="col-12 fs-6 text-center">
                    <div class="row justify-content-center">
                        <div class="col-12 col-md-8 fw-light">
                            Вы не можете уложиться в бюджет? Или просто не хотите продумывать всё до мелочей.
                            Данный сервис сделает это за вас, используя математические алгоритмы.
                        </div>
                    </div>
                </div>
                <div class="col-12 col-md-6 p-4 rounded-3">
                    <div class="mb-3">
                        <label for="from" class="form-label">От</label>
                        <select v-model="selectedFrom" id="from" class="form-select red-background">
                            <option v-for="city in cities" :key="city.id" :value="city">
                                {{ city.city }}
                            </option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label for="to" class="form-label">Куда</label>
                        <select v-model="selectedTo" id="to" class="form-select red-background">
                            <option v-for="city in cities" :key="city.id" :value="city">
                                {{ city.city }}
                            </option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label for="date" class="form-label">Дата</label>
                        <div class="d-flex gap-2">
                            <select v-model="selectedMonth" id="month" class="form-select red-background">
                                <option v-for="(month, index) in months" :key="index" :value="index + 1">
                                    {{ month }}
                                </option>
                            </select>
                            <select v-model="selectedDay" id="day" class="form-select red-background">
                                <option v-for="day in daysInMonth" :key="day" :value="day">
                                    {{ day }}
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label for="time" class="form-label">Время</label>
                        <input type="time" v-model="selectedTime" id="time" class="form-control red-background" />
                    </div>

                    <div class="mb-3">
                        <label for="ticketType" class="form-label">Тип билета</label>
                        <select v-model="selectedType" id="ticketType" class="form-select red-background">
                            <option v-for="(tType, index) in ticketType" :key="index" :value="index + 1">
                                {{ tType }}
                            </option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="flightTime" class="form-label">Время на полет</label>
                        <input type="time" v-model="selectedFlightTime" id="flightTime" class="form-control red-background" />
                    </div>
                    <div class="mb-4">
                        <label for="numTransfers" class="form-label">Количество пересадок</label>
                        <select v-model="selectedNumTransfers" id="numTransfers" class="form-select red-background">
                            <option v-for="(tType, index) in numTransfers" :key="index" :value="index + 1">
                                {{ tType }}
                            </option>
                        </select>
                    </div>
                    <div class="d-flex">
                        <ButtonOne class="px-4 py-2 fs-5 rounded-pill" @click="calc">Рассчитать</ButtonOne>
                    </div>
                </div>
                <div v-if="isCalcLoading"  class="col-12 col-md-6 p-4 rounded-3 pt-5">
                    <div class="row justify-content-center mx-0 mb-4">
                        <div class="spinner-border" style="color: var(--custom-purple-color);" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                <div v-else-if="!isCalcLoading && isCalced" class="col-12 col-md-6 p-4 rounded-3 pt-5">
                    <div class="row mb-3">
                        <div class="col-12 text-center fs-5 fw-light">
                            Нейросеть 🤖 определила наиболее вероятную цену
                        </div>
                    </div>
                    <div class="row" v-if="calcResults.length > 0">
                        <div class="col-12" v-for="calcResult in calcResults" :key="calcResult.id">
                            <div class="row fw-light mb-3 fs-5">
                                <div class="col-12 d-flex gap-2 mb-2">
                                    <div class="fs-4 d-flex align-items-center gap-2">
                                        <img style="width: 30px;" :src="require('@/assets/company.svg')">
                                        <div>{{ calcResult.title }}</div>
                                    </div>
                                </div>
                                <div class="col-12 d-flex gap-2">
                                    <div>Цена: </div>
                                    <div class="fw-normal">{{ calcResult.price }} ₽</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else class="fw-light text-center">
                        Данный перелет не возможен ):
                    </div>
                </div>
                <div v-else class="col-12 col-md-6 p-4 rounded-3 pt-5">
                    
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-1 px-md-5 my-5" data-aos="fade-up">
        <div class="col-12 px-0">
            <div class="row m-0">
                <div class="col-12 text-center fs-5 fw-light custom-purple-text-color mb-3">Куда можно сходить?</div>
                <div class="col-12 text-center fs-2 fw-light custom-title-color mb-3">
                    Популярные места для этого направления
                </div>
                <div class="col-12 fs-6 text-center mb-5">
                    <div class="row justify-content-center">
                        <div class="col-12 col-md-8 fw-light">
                            Выберите направление, и наш сервис предоставит вам список значимых и интересных мест для отдыха.
                        </div>
                    </div>
                </div>
                <div class="mx-0 px-0">
                    <PlaceElementList :elements="places"></PlaceElementList>
                    <div class="col-12 d-flex justify-content-center">
                        <ButtonOne class="px-4 py-2 fs-5 rounded-pill">Показать еще</ButtonOne>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row mx-0 px-1 px-md-5 py-5 custom-purple-background-color custom-light-text-color">
        <div class="col-12 fs-5 px-0 mb-5 text-center">
            Не знаете куда полететь?
        </div>
        <div class="col-12">
            <div class="row justify-content-center">
                <div class="col-10 border custom-border-color py-3 py-md-5 px-3 px-md-5">
                    <div class="row">
                        <div class="col-12 col-md-6 fs-1">
                            Топ популярных<br />
                            мест для <br />
                            путешествия
                        </div>
                        <div class="col-12 col-md-6">
                            <div class="row h-100">
                                <div class="col-12 fs-5 mb-3 d-flex align-self-end fw-light">
                                    Места избранные людьми
                                </div>
                                <div class="col-12">
                                    <ButtonOne class="px-4 py-2 fs-5 rounded-pill text-nowrap" @click="goToPage">Узнать больше</ButtonOne>
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
import axiosApiInstanceAuth from '../api';
import PlaceElementList from "@/components/PlaceElementList";

export default {
    components: {
        PlaceElementList
    },
    data() {
        return {
            isCalced: false,
            isCalcLoading: false,
            places: [],
            cities: [],
            numTransfers: [1, 2, 3],
            ticketType: ['economy', 'business'],
            selectedFrom: null,
            selectedTo: null,
            selectedMonth: 1, // значение по умолчанию: Январь
            selectedType: 1, // значение по умолчанию: economy
            selectedDay: 1, // значение по умолчанию: 1-й день
            selectedTime: '00:00', // значение по умолчанию: полночь
            selectedFlightTime: '01:00', // значение по умолчанию: 1 час
            selectedNumTransfers: 1, // значение по умолчанию: 1 пересадка
            calcResults: [],
            months: [
                'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
            ]
        };
    },
    methods: {
        scrollToSection() {
            this.$refs.targetSection.scrollIntoView({ behavior: 'smooth' });
        },
        async calc() {
            this.isCalcLoading = true;
            console.log(this.selectedTo);
            try {
                const flightTimeParts = this.selectedFlightTime.split(':');
                const formattedFlightTime = `${flightTimeParts[0]}h ${flightTimeParts[1]}m`;
                const response = await axiosApiInstanceAuth.post(`http://127.0.0.1:8000/api/directions/price/`, {
                    from: this.selectedFrom.id,
                    to: this.selectedTo.id,
                    date: this.selectedMonth.toString().padStart(2, '0') + '-' + this.selectedDay.toString().padStart(2, '0'),
                    dep_time: this.selectedTime,
                    clas: this.selectedType,
                    stop: this.selectedNumTransfers,
                    time_taken: formattedFlightTime
                });

                const responseData = response.data;
                console.log(responseData);

                if (responseData && responseData.result && Array.isArray(responseData.result)) {
                    this.calcResults = responseData.result.map((place) => ({
                        title: place[0],
                        price: parseFloat(place[1]).toFixed(2)
                    }));
                    this.isCalcLoading = false;
                    this.isCalced = true;
                } else {
                    console.error('Invalid response format');
                }
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
            try {
                const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/directions/${this.selectedTo.id}/places/`);
                const cityData = response.data;
                console.log(cityData);
                this.places = response.data.map((place) => ({
                    id: place.id,
                    title: place.title,
                    photo: place.photo,
                    description: place.description
                }));
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        },
        goToPage(id) {
            this.$router.push({ name: 'popular' });
        },
        async fetchCities() {
            try {
                const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/directions/list/`);
                const cityData = response.data;
                console.log(cityData);
                this.cities = response.data.map((city) => ({
                    id: city.id,
                    city: city.city
                }));

                // Устанавливаем значения по умолчанию после загрузки списка городов
                if (this.cities.length > 0) {
                    this.selectedFrom = this.cities[0];
                    this.selectedTo = this.cities[1] || this.cities[0];
                }
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        }
    },
    created() {
        this.fetchCities();
    },
    computed: {
        daysInMonth() {
            if (this.selectedMonth === null) {
                return [];
            }
            const days = new Date(2024, this.selectedMonth, 0).getDate(); // 2024 - високосный год для корректного определения февраля
            return Array.from({ length: days }, (_, i) => i + 1);
        },
        formattedDate() {
            if (this.selectedMonth && this.selectedDay) {
                return `${String(this.selectedDay).padStart(2, '0')}-${String(this.selectedMonth).padStart(2, '0')}`;
            }
            return '';
        }
    }
};
</script>

<style scoped>
.form-label,
.form-select {}

.form-select.red-background,
.form-control.red-background {
    background-color: var(--custom-light-background-color) !important;
}

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
