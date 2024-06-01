<template>
  <div>
    <Navbar></Navbar>
    <div class="row justify-content-center align-items-center mx-1 mx-md-5" style="min-height: 90vh;">
        <div class="d-flex flex-column shadow rounded p-4 text-center align-items-center my-3" style="width: min-content;">
            <div class="d-flex justify-content-center align-items-center mb-2 mt-5" style="width: 300px;">
              <img class="d-flex justify-content-center align-items-center" style="width: 70px;" :src="require('@/assets/logo.svg')">
            </div>
            <div class="fs-4 text-nowrap mb-3">Добро пожаловать!</div>
            <div v-if="authStore.error.general" class="error-message custom-error-text-color mb-2">
              <div v-for="(errorMessage, key) in authStore.error.general" :key="key">
                <div v-for="(error) in errorMessage">
                  {{ error }}
                </div>
              </div>
            </div>
            <label for="inp" class="inp mb-2 w-100">
                <input v-model="email" type="text" id="inp" placeholder="&nbsp;">
                <span class="label">Почта</span>
                <span class="focus-bg"></span>
            </label>
            <div v-if="authStore.error.email" class="error-message custom-error-text-color mb-2">
              <div v-for="(errorMessage, key) in authStore.error.email" :key="key">
                <div v-for="(error) in errorMessage">
                  {{ error }}
                </div>
              </div>
            </div>
            <label for="inp2" class="inp mb-2 w-100">
                <input v-model="username" type="text" id="inp2" placeholder="&nbsp;">
                <span class="label">Логин</span>
                <span class="focus-bg"></span>
            </label>
            <div v-if="authStore.error.username" class="error-message custom-error-text-color mb-2">
              <div v-for="(errorMessage, key) in authStore.error.username" :key="key">
                <div v-for="(error) in errorMessage">
                  {{ error }}
                </div>
              </div>
            </div>
            <label for="inp3" class="inp mb-2 w-100">
                <input v-model="password" type="password" id="inp3" placeholder="&nbsp;">
                <span class="label">Пароль</span>
                <span class="focus-bg"></span>
            </label>
            <div v-if="authStore.error.password" class="error-message custom-error-text-color mb-2">
              <div v-for="(errorMessage, key) in authStore.error.password" :key="key">
                <div v-for="(error) in errorMessage">
                  {{ error }}
                </div>
              </div>
            </div>
            <label for="inp3" class="inp mb-2 w-100">
                <input v-model="confirmation" type="password" id="inp3" placeholder="&nbsp;">
                <span class="label">Подтвердите пароль</span>
                <span class="focus-bg"></span>
            </label>
            <div v-if="authStore.error.confirmation" class="error-message custom-error-text-color mb-2">
              <div v-for="(errorMessage, key) in authStore.error.confirmation" :key="key">
                <div v-for="(error) in errorMessage">
                  {{ error }}
                </div>
              </div>
            </div>
            <ButtonOne @click="signup" class="py-2 fs-5 mb-5 px-4 mt-5" style="min-width: 50%;">Зарегистрироваться</ButtonOne>
            <div class="fs-6 mb-5">Есть аккаунт?
                <router-link :to="{name: 'sign-in'}" class="fs-6 custom-dark-text-color">Войти</router-link>
            </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';
import {useAuthStore} from '../store/auth';
import {useRouter} from 'vue-router'

const authStore = useAuthStore();
const router = useRouter();

const email = ref('');
const password = ref('');
const confirmation = ref('');
const username = ref('');

authStore.error = {}

const signup = async () => {
  await authStore.auth({email: email.value, username: username.value, password: password.value, confirmation: confirmation.value}, 'signup')
  if (!authStore.error) {
    router.push({ name: 'sign-in' });
  }
}

</script>
<style scoped>
* {
  box-sizing: border-box; }

.inp {
  position: relative;
  margin: auto;
  width: 100%;
  max-width: 280px;
  border-radius: 3px;
  overflow: hidden; }
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
    pointer-events: none; }
  .inp .focus-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.05);
    z-index: -1;
    transform: scaleX(0);
    transform-origin: left; }
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
    transition: all .15s ease; }
    .inp input:hover {
      background: rgba(0, 0, 0, 0.04);
      box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.5); }
    .inp input:not(:placeholder-shown) + .label {
      color: rgba(0, 0, 0, 0.5);
      transform: translate3d(0, -12px, 0) scale(0.75); }
    .inp input:focus {
      background: rgba(60, 60, 60, 0.01);
      outline: none;
      box-shadow: inset 0 -2px 0 var(--custom-blue-color); }
      .inp input:focus + .label {
        color: var(--custom-blue-color);
        transform: translate3d(0, -12px, 0) scale(0.75); }
        .inp input:focus + .label + .focus-bg {
          transform: scaleX(1);
          transition: all .1s ease; }
</style>