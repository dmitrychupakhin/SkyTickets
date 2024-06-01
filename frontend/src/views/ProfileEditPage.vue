<template>
  <div>
      <Navbar></Navbar>
      <div class="row mx-1 mx-md-5 justify-content-center mb-5 mt-2" style="min-height: 100vh;">
          <div class="col-8 py-4">
              <div class="row position-relative shadow rounded py-4 px-3 mb-4">
                  <div class="col-12 fw-medium fs-4 mb-4">
                      Личная информация
                  </div>
                  <div class="col-6 d-flex justify-content-center mb-2 px-5" style="height: min-content;">
                      <div class="ratio ratio-1x1 position-relative rounded" style="width: 100%; max-height: 100%;">
                          <img :src="userImage" @click="triggerFileInput" alt="User Image" class="userImage shadow" style="object-fit: cover; width: 100%; height: 100%; cursor: pointer;" />
                      </div>
                      <input type="file" ref="fileInput" @change="onFileSelected" style="display: none;" />
                  </div>
                  <div class="col-6 mb-2">
                      <div class="row m-0 p-0">
                          <div class="col-12">
                              <label for="username" class="inp mb-2 w-100">
                                  <input v-model="username" type="text" id="username" placeholder="&nbsp;">
                                  <span class="label">Имя пользователя</span>
                                  <span class="focus-bg"></span>
                              </label>
                          </div>
                          <div class="col-12">
                              <label for="firstName" class="inp mb-2 w-100">
                                  <input v-model="firstName" type="text" id="firstName" placeholder="&nbsp;">
                                  <span class="label">Имя</span>
                                  <span class="focus-bg"></span>
                              </label>
                          </div>
                          <div class="col-12">
                              <label for="lastName" class="inp mb-2 w-100">
                                  <input v-model="lastName" type="text" id="lastName" placeholder="&nbsp;">
                                  <span class="label">Фамилия</span>
                                  <span class="focus-bg"></span>
                              </label>
                          </div>
                          <div class="col-12">
                              <label for="about" class="inp w-100">
                                  <textarea v-model="about" id="about" placeholder="&nbsp;"></textarea>
                                  <span class="label">О себе</span>
                                  <span class="focus-bg"></span>
                              </label>
                          </div>
                      </div>
                  </div>
                  <div class="col-6">
                      <label for="birthdate" class="inp mb-2 w-100">
                          <input v-model="birthdate" type="date" id="birthdate" placeholder="&nbsp;">
                          <span class="label">Дата рождения</span>
                          <span class="focus-bg"></span>
                      </label>
                  </div>
                  <div class="col-6">
                      <label for="location" class="inp mb-2 w-100">
                          <input v-model="location" type="text" id="location" placeholder="&nbsp;">
                          <span class="label">Местоположение</span>
                          <span class="focus-bg"></span>
                      </label>
                  </div>
              </div>
              <div class="row position-relative shadow rounded py-4 px-3 mb-4">
                  <div class="col-12 fw-medium fs-4 mb-2">
                      Контакты
                  </div>
                  <div class="row m-0 p-0">
                      <div class="col-6">
                          <label for="phone" class="inp mb-2 w-100">
                              <input v-model="phone" type="tel" id="phone" placeholder="&nbsp;">
                              <span class="label">Номер телефона</span>
                              <span class="focus-bg"></span>
                          </label>
                      </div>
                  </div>
                  <div class="row m-0 p-0">
                      <div class="col-6">
                          <label for="email" class="inp mb-2 w-100">
                              <input v-model="email" type="email" id="email" placeholder="&nbsp;">
                              <span class="label">Почта</span>
                              <span class="focus-bg"></span>
                          </label>
                      </div>
                  </div>
              </div>
              <div class="row shadow rounded py-3 px-3 d-flex justify-content-end">
                  <ButtonOne class="d-flex w-auto py-2 fs-5 px-4" @click="saveAll">Сохранить</ButtonOne>
              </div>
          </div>
      </div>
  </div>
</template>
<script>
import { useAuthStore } from '@/store/auth';
import axiosApiInstanceAuth from '../api';

export default {
    data() {
        return {
            userImage: '',
            imageFile: null,  // добавляем для хранения выбранного файла
            username: '',
            firstName: '',
            lastName: '',
            about: '',
            birthdate: '',
            location: '',
            phone: '',
            email: '',
            profileTitle: '',
            fullName: '',
            isLoading: true
        };
    },
    setup() {
        const authStore = useAuthStore();
        return { authStore };
    },
    methods: {
        async fetchUserData() {
            try {
                const response = await axiosApiInstanceAuth.get(`http://127.0.0.1:8000/api/users/${this.authStore.userInfo.userId}/`);
                const userData = response.data;
                this.profileTitle = userData.profileTitle || 'Пользователь';
                this.firstName = userData.first_name;
                this.lastName = userData.last_name;
                this.username = userData.username;
                this.about = userData.about;
                this.phone = userData.phone_number;
                this.email = userData.email;
                this.birthdate = userData.date_birth;
                this.location = userData.location;
                this.userImage = userData.photo;
            } catch (error) {
                console.error('Error fetching user data:', error);
            } finally {
                this.isLoading = false;
            }
        },
        triggerFileInput() {
            this.$refs.fileInput.click();
        },
        onFileSelected(event) {
            const file = event.target.files[0];
            if (file) {
                this.imageFile = file;
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.userImage = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        },
        async saveAll() {
            const formData = new FormData();
            if (this.imageFile) {
                formData.append('photo', this.imageFile);
            }
            formData.append('username', this.username);
            formData.append('first_name', this.firstName);
            formData.append('last_name', this.lastName);
            formData.append('about', this.about);
            formData.append('date_birth', this.birthdate);
            formData.append('location', this.location);
            formData.append('phone_number', this.phone);
            formData.append('email', this.email);
            try {
                const response = await axiosApiInstanceAuth.put(`http://127.0.0.1:8000/api/users/${this.authStore.userInfo.userId}/edit/`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                if (response.status !== 200) {
                    throw new Error('Network response was not ok');
                }
            } catch (error) {
                console.error('Error saving user data:', error);
            }
        }
    },
    mounted() {
        this.fetchUserData();
    }
};
</script>

<style scoped>
.userImage:hover {
    filter: brightness(1.2);
}

.image-container {
    position: relative;
    width: 100%;
    padding-top: 100%;
    /* Соотношение 1:1 для квадратного div */
    background-color: #f0f0f0;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.image-container img {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: translate(-50%, -50%);
}

* {
    box-sizing: border-box;
}

.inp {
    position: relative;
    margin: auto;
    width: 100%;
    border-radius: 3px;
    overflow: hidden;
}

.inp .label {
    position: absolute;
    top: 20px;
    left: 12px;
    font-size: 16px;
    color: rgba(0, 0, 0, 0.5);
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

.inp input,
.inp textarea {
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
    box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.3);
    color: #000;
    transition: all .15s ease;
}

.inp input:hover,
.inp textarea:hover {
    background: rgba(0, 0, 0, 0.04);
    box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.5);
}

.inp input:not(:placeholder-shown)+.label {
    color: rgba(0, 0, 0, 0.5);
    transform: translate3d(0, -12px, 0) scale(0.75);
}

.inp textarea:not(:placeholder-shown)+.label {
    color: rgba(0, 0, 0, 0.5);
    transform: translate3d(0, -20px, 0) scale(0.75);
}

.inp input:focus,
.inp textarea:focus {
    background: rgba(60, 60, 60, 0.01);
    outline: none;
    box-shadow: inset 0 -2px 0 var(--custom-blue-color);
}

.inp input:focus+.label {
    color: var(--custom-blue-color);
    transform: translate3d(0, -12px, 0) scale(0.75);
}

.inp textarea:focus+.label {
    color: var(--custom-blue-color);
    transform: translate3d(0, -20px, 0) scale(0.75);
}

.inp textarea:focus+.label {
    color: var(--custom-blue-color);
    transform: translate3d(0, -20px, 0) scale(0.75);
}

.inp input:focus+.label+.focus-bg,
.inp textarea:focus+.label+.focus-bg {
    transform: scaleX(1);
    transition: all .1s ease;
}
</style>
