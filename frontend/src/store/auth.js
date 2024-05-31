import { ref } from 'vue'
import { defineStore } from 'pinia'
import axiosApiInstanceAuth from '../api'

export const useAuthStore = defineStore('auth', () => {
    const userInfo = ref({
      token: '',
      email: '',
      userId: '',
      refreshToken: ''
    });
    const error = ref('');
    const loader = ref(false);
  
    const auth = async (payload, type) => {
      console.log( payload);
      const stringUrl = type === 'signup' ? 'users/register/' : 'users/token/';
      error.value = '';
      loader.value = true;
      try {
        const response = await axiosApiInstanceAuth.post(`http://localhost:8000/api/${stringUrl}`, payload);
        userInfo.value = {
            token: response.data.access,
            userId: response.data.user_id,
            refreshToken: response.data.refresh,
        };
        localStorage.setItem('userTokens', JSON.stringify({
            token: userInfo.value.token,
            userId: userInfo.value.userId,
            refreshToken: userInfo.value.refreshToken
        }));
      } catch (err) {
        const parsedErrors = JSON.parse(err.request.responseText);
        const errorMessage = {};
        for (const key in parsedErrors) {
          console.log(key);
          console.log(parsedErrors[key]);
          if(key == 'username' || key == 'password' || key == 'email' || key == 'confirmation'){
            if (!errorMessage[key]) {
              errorMessage[key] = [];
            }
            errorMessage[key].push(parsedErrors[key]);
          }
          else{
            if (!errorMessage['general']) {
              errorMessage['general'] = [];
            }
            errorMessage['general'].push(parsedErrors[key]);
          }
        }
        error.value = errorMessage;
      } finally {
        loader.value = false;
      }
    };
  
    const logout = () => {
      userInfo.value = {
        token: '',
        email: '',
        userId: '',
        refreshToken: ''
      };
      localStorage.removeItem('userTokens');
    };
  
    return { auth, userInfo, error, loader, logout };
  });