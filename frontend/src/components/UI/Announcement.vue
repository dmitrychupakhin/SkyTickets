<template>
    <div v-if="!token" class="fw-lighter text-center py-1 fs-6 custom-dark-background-color custom-light-text-color">
        <div>Хотите получить больше возможностей? <router-link class="custom-light-text-color" :to="{name: 'sign-in'}">Войти</router-link></div>
    </div>
</template>
<script>
export default {
name: "Announcement",
components: {},
};
</script>

<script setup>
import {computed} from 'vue'
import {useAuthStore} from '@/store/auth'
import { useRouter } from 'vue-router';

const authStore = useAuthStore()
const router = useRouter()

const token = computed(() => authStore.userInfo.token);

const checkUser = () => {
  const tokens = JSON.parse(localStorage.getItem('userTokens'));
  if (tokens) {
    authStore.userInfo.token = tokens.token
    authStore.userInfo.refreshToken = tokens.refreshToken
  }
}

const logout = () => {
  authStore.logout()
  localStorage.removeItem('userTokens')
  router.push('/signin')
}

checkUser()
</script>

<style scoped>

</style>