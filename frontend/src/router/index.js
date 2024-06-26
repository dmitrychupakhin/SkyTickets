import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PopularContentView from '../views/PopularContentView.vue'
import DirectionView from '../views/DirectionView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ResetPasswordView from '../views/ResetPasswordView.vue'
import ResetPasswordTokenView from '../views/ResetPasswordTokenView.vue'
import ProfileEditView from '../views/ProfileEditPage.vue'
import ProfileEditPasswordView from '../views/ProfileEditPasswordView.vue'
import { useAuthStore } from '../store/auth'
import { computed, nextTick } from 'vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      auth: false
    }
  },
  {
    path: '/polular/',
    name: 'popular',
    component: PopularContentView,
    meta: {
      auth: false
    }
  },
  {
    path: '/direction/:id',
    name: 'direction',
    component: DirectionView,
    meta: {
      auth: false
    }
  },
  {
    path: '/profile-edit',
    name: 'profile-edit',
    component: ProfileEditView,
    meta: {
      auth: true
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: {
      auth: true
    }
  },
  {
    path: '/sign-in',
    name: 'sign-in',
    component: LoginView,
    meta: {
      auth: false
    }
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: RegisterView,
    meta: {
      auth: false
    }
  },
  {
    path: '/reset-password',
    name: 'reset-password',
    component: ResetPasswordView,
    meta: {
      auth: false
    }
  },
  {
    path: '/reset-password-token',
    name: 'reset-password-token',
    component: ResetPasswordTokenView,
    meta: {
      auth: false
    }
  },
  {
    path: '/edit-password',
    name: 'edit-password',
    component: ProfileEditPasswordView,
    meta:{
      auth: false
    }
  },
  { 
    path: '/:catchAll(.*)',
    redirect: '/'
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return { ...savedPosition, behavior: 'auto' }; // Исправлено здесь
    } else {
      return { top: 0, behavior: 'auto' };
    }
}
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const token = computed(() => authStore.userInfo.token);
  document.title = 'SkyTickets';
  const checkUser = () => {
    const tokens = JSON.parse(localStorage.getItem('userTokens'));
    console.log(tokens);
    if (tokens) {
      authStore.userInfo.token = tokens.token;
      authStore.userInfo.refreshToken = tokens.refreshToken;
      authStore.userInfo.userId = tokens.userId;
    }
  };

  checkUser();

  nextTick(() => {
    if (to.meta.auth && !authStore.userInfo.token) {
      next({ name: 'sign-in' });
    } else {
      next();
    }
  });
});

export default router
