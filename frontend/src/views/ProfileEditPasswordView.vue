<template>
    <div>
      <Navbar></Navbar>
      <div class="row justify-content-center align-items-center mx-1 mx-md-5" style="min-height: 90vh;">
        <div class="d-flex flex-column shadow rounded p-4 text-center align-items-center my-3" style="width: min-content;">
          <div class="d-flex justify-content-center align-items-center mb-2 mt-5" style="width: 300px;">
            <img class="d-flex justify-content-center align-items-center" style="width: 70px;" :src="require('@/assets/logo.svg')">
          </div>
          <div class="fs-4 text-nowrap mb-3">Изменение пароля</div>
          <div v-if="error.general.length > 0" class="error-message custom-error-text-color mb-2">
            <div v-for="(errorMessage, index) in error.general" :key="index">
              {{ errorMessage }}
            </div>
          </div>
          <label for="inp_old_password" class="inp mb-2 w-100">
            <input v-model="oldPassword" type="password" id="inp_old_password" placeholder="&nbsp;">
            <span class="label">Старый пароль</span>
            <span class="focus-bg"></span>
          </label>
          <div v-if="error.oldPassword.length > 0" class="error-message custom-error-text-color mb-2">
            <div v-for="(errorMessage, index) in error.oldPassword" :key="index">
              {{ errorMessage }}
            </div>
          </div>
          <label for="inp_new_password" class="inp mb-2 w-100">
            <input v-model="newPassword" type="password" id="inp_new_password" placeholder="&nbsp;">
            <span class="label">Новый пароль</span>
            <span class="focus-bg"></span>
          </label>
          <div v-if="error.newPassword.length > 0" class="error-message custom-error-text-color mb-2">
            <div v-for="(errorMessage, index) in error.newPassword" :key="index">
              {{ errorMessage }}
            </div>
          </div>
          <label for="inp_confirm_new_password" class="inp mb-2 w-100">
            <input v-model="confirmNewPassword" type="password" id="inp_confirm_new_password" placeholder="&nbsp;">
            <span class="label">Подтверждение нового пароля</span>
            <span class="focus-bg"></span>
          </label>
          <div v-if="error.confirmNewPassword.length > 0" class="error-message custom-error-text-color mb-2">
            <div v-for="(errorMessage, index) in error.confirmNewPassword" :key="index">
              {{ errorMessage }}
            </div>
          </div>
          <ButtonOne @click="changePassword" class="py-2 fs-5 mb-5 px-2 mt-5" style="min-width: 50%;">Изменить</ButtonOne>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </template>
  
  <script>
  import axiosApiInstanceAuth from '../api';
  import { ref, reactive } from 'vue';
  import { useAuthStore } from '../store/auth';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'ChangePassword',
    setup() {
      const oldPassword = ref('');
      const newPassword = ref('');
      const confirmNewPassword = ref('');
      const error = reactive({
        general: [],
        oldPassword: [],
        newPassword: [],
        confirmNewPassword: []
      });
      const authStore = useAuthStore();
      const router = useRouter();
  
      const changePassword = async () => {
        try {
          const response = await axiosApiInstanceAuth.post('http://127.0.0.1:8000/api/users/password_change/', {
            old_password: oldPassword.value,
            new_password: newPassword.value,
            confirmation: confirmNewPassword.value
          });
          router.push({ name: 'profile' });
        } catch (err) {
          if (err.response && err.response.data) {
            const errors = err.response.data;
            error.general = [];
            error.oldPassword = [];
            error.newPassword = [];
            error.confirmNewPassword = [];
  
            for (const key in errors) {
              if (errors.hasOwnProperty(key)) {
                if (key === 'old_password') {
                  error.oldPassword.push(...errors[key]);
                } else if (key === 'new_password') {
                  error.newPassword.push(...errors[key]);
                } else if (key === 'confirmation') {
                  error.confirmNewPassword.push(...errors[key]);
                } else {
                  error.general.push(errors['error']);
                }
              }
            }
          } else {
            console.error('Error changing password:', err);
          }
        }
      };
  
      return {
        oldPassword,
        newPassword,
        confirmNewPassword,
        changePassword,
        error,
        authStore
      };
    }
  };
  </script>
  
  <style scoped>
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
      box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.3);
      color: #000;
      transition: all .15s ease;
  }
  
  .inp input:hover {
      background: rgba(0, 0, 0, 0.04);
      box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.5);
  }
  
  .inp input:not(:placeholder-shown)+.label {
      color: rgba(0, 0, 0, 0.5);
      transform: translate3d(0, -12px, 0) scale(0.75);
  }
  
  .inp input:focus {
      background: rgba(60, 60, 60, 0.01);
      outline: none;
      box-shadow: inset 0 -2px 0 var(--custom-blue-color);
  }
  
  .inp input:focus+.label {
      color: var(--custom-blue-color);
      transform: translate3d(0, -12px, 0) scale(0.75);
  }
  
  .inp input:focus+.label+.focus-bg {
      transform: scaleX(1);
      transition: all .1s ease;
  }
  </style>
  