import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
/* import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ResetPasswordView from '../views/ResetPasswordView.vue'
import ContentPageView from '../views/ContentPageView.vue'
import ProfileEditView from '../views/ProfileEditPage.vue'
import ContentPageView2 from '../views/ContentPageView2.vue' */
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
  /* {
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
    path: '/content/',
    name: 'content1',
    component: ContentPageView,
    meta: {
      auth: true
    }
  },
  {
    path: '/content2/',
    name: 'content2',
    component: ContentPageView2,
    meta: {
      auth: true
    }
  }, */
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
    return savedPosition;
    } else {
    return { top: 0 };
    }
}
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const token = computed(() => authStore.userInfo.token);

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