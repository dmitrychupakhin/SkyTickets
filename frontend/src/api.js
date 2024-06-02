import axios from 'axios'
import {useAuthStore} from './store/auth'
import router from './router'

const axiosApiInstanceAuth = axios.create()

axiosApiInstanceAuth.interceptors.request.use((config) => {
  const url = config.url
  console.log(url);
  if (!url.includes('token') && !url.includes('register')) {
    const authStore = useAuthStore()
    config.headers = {
      ...config.headers,
      'Content-Type': 'multipart/form-data',
      'Authorization': `JWT ${authStore.userInfo.token}`
    };
  }
  return config
})

axiosApiInstanceAuth.interceptors.response.use((response) => {
  return response
}, async function (error) {
  const authStore = useAuthStore()
  const originalRequest = error.config
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;
    try {
      const newTokens = await axios.post(
        `http://127.0.0.1:8000/api/users/token/refresh/`, {
          refresh: JSON.parse(localStorage.getItem('userTokens')).refreshToken
        }
      )
      console.log('refresh');
      console.log(newTokens);
      authStore.userInfo.token = newTokens.data.access
      authStore.userInfo.refreshToken = newTokens.data.refresh
      authStore.userInfo.userId = newTokens.data.user_id
      localStorage.setItem('userTokens', JSON.stringify({
        token: newTokens.data.access,
        refreshToken: newTokens.data.refresh,
        userId: newTokens.data.user_id
      }))
      return axiosApiInstanceAuth(originalRequest);
    } catch (err) {
      console.log("123");
      localStorage.removeItem('userTokens')
      router.push('/signin')
      authStore.userInfo.token = ''
      authStore.userInfo.refreshToken = ''
    }
  }
  return Promise.reject(error);
})

export default axiosApiInstanceAuth